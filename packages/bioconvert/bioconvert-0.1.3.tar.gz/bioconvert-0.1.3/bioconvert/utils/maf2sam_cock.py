"""Simple MIRA alignment format (MAF) to SAM format converter.

See: http://mira-assembler.sourceforge.net/docs/chap_maf_part.html
and: http://samtools.sourceforge.net/

The source code repository for this script is here:

http://github.com/peterjc/maf2sam

Copyright 2010-2013, Peter Cock, all rights reserved.
"""
import sys
import re
import hashlib

CIGAR_M = True

if len(sys.argv)==3:
    ref = sys.argv[1]
    maf = sys.argv[2]
else:
    import os
    name = os.path.basename(sys.argv[0])
    print("Usage: Takes two command line arguments, (un)padded FASTA reference")
    print("file, and matching MAF file. Output is SAM format to stdout.")
    print()
    print("python %s EX_out.unpadded.fasta EX_out.maf > EX_out.unpadded.sam" %name)
    print()
    print("or if the script is marked as executable,")
    print()
    print("./%s EX_out.unpadded.fasta EX_out.maf > EX_out.unpadded.sam" % name)
    print()
    print("Note that conventionally SAM/BAM files have used an unpadded (ungapped)")
    print("reference sequence, also can be used with a padded (gapped) reference.")
    print("This will be formallised in the upcoming SAM/BAM v1.5 specification,")
    print("along with other additions intended for (de novo) assemblies. One of")
    print("the advantages of using a padded reference is inserts are easier to")
    print("visualise.")
    print()
    print("You can now produce either style SAM file, depending on if your")
    print("reference FASTA sequence is gapped/padded or not. e.g.")
    print()
    print("python %s EX_out.padded.fasta EX_out.maf > EX_out.padded.sam" % name)
    print()
    print("NOTE - This script does not accept ACE files as input.")
    sys.exit(1)

try:
    from Bio.Seq import reverse_complement
    from Bio import SeqIO
except ImportError:
    sys.stderr.write("Requires Biopython\n")
    sys.exit(1)

def log(msg):
    sys.stderr.write("[maf2sam] %s\n" % msg.rstrip())

def seq_md5(seq):
    #TODO - Remove these asserts after testing
    assert " " not in seq
    assert seq == seq.upper()
    return hashlib.md5(seq.encode()).hexdigest()

class Read(object):
    def __init__(self, contig_name, read_name="", template_name="",
                 read_seq="", first_in_pair=True, ref_rc = False,
                 ref_pos=0, map_qual=255, insert_size = 0,
                 vect_left = 0, vect_right = 0,
                 qual_left = 0, qual_right = 0,
                 clip_left = 0, clip_right = 0,
                 read_group = None, seq_tech = "", strain = "",
                 tags=[]):
        self.contig_name = contig_name
        self.read_name = read_name
        self.template_name = template_name
        self.read_seq = read_seq
        self.first_in_pair = first_in_pair
        self.ref_rc = ref_rc
        self.ref_pos = ref_pos
        self.map_qual = map_qual
        self.cigar = ""
        self.insert_size = insert_size
        self.vect_left = vect_left
        self.vect_right = vect_right
        self.qual_left = qual_left
        self.qual_right = qual_right
        self.clip_left = clip_left
        self.clip_right = clip_right
        self.read_group = read_group
        self.seq_tech = seq_tech
        self.strain = strain
        self.tags = tags

    def __repr__(self):
        return "Read(%r, %r, %r, %r, %r, %r, %r, %r, ...)" % (
            self.contig_name,
            self.read_name,
            self.template_name,
            self.read_seq,
            self.first_in_pair,
            self.ref_rc,
            self.ref_pos,
            self.map_qual)

    def is_paired(self):
        if not self.template_name:
            assert self.read_name
            # log("%s is NOT paired (no template name)" % self.read_name)
            return False
            self.template_name = self.read_name
        elif self.template_name != self.read_name:
            # Looks like a paired end read!
            # log("%s is paired" % self.read_name)
            return True
        else:
            # log("%s is NOT paired" % self.read_name)
            return False

    def get_partner(self):
        if not self.is_paired():
            raise ValueError
        return cached_pairs[(self.template_name, not self.first_in_pair)]

    def need_partner(self):
        if not self.is_paired():
            return False
        return (self.template_name, not self.first_in_pair) not in cached_pairs

    def __str__(self):
        global cached_pairs, read_group_ids
        if self.ref_rc:
            flag = 0x10 #maps to reverse strand
            read_seq = reverse_complement(self.read_seq)
            read_qual = self.read_qual[::-1]
        else:
            flag = 0
            read_seq = self.read_seq
            read_qual = self.read_qual
        mate_ref_name = "*"
        mate_ref_pos = 0
        if not self.template_name:
            assert self.read_name
            self.template_name = self.read_name
        if self.is_paired():
            flag += 1 #paired
            if self.first_in_pair:
                flag += 0x40 #forward partner
            else:
                flag += 0x80 #reverse partner
            try:
                mate = self.get_partner()
            except KeyError:
                #Paired but no parter in ACE file
                flag += 0x08 #mate unmapped
            else:
                mate_ref_name = mate.contig_name
                mate_ref_pos = mate.ref_pos
                if mate_ref_name == self.contig_name:
                    #Since MIRA seems happy and both on same contig,
                    flag += 0x02 #properly aligned

        assert not self.tags
        read_seq_unpadded = read_seq.replace("*", "")
        read_qual_unpadded = "".join(q for (l,q) in zip(read_seq,read_qual) if l!="*")
        cigar = self.cigar
        #assert "M" not in cigar, cigar
        if "D" not in cigar:
            #Sum of lengths of the M/I/S/=/X operations should match the sequence length
            #By construction there are no M entries in our CIGAR string.
            #TODO - Improve this check to consider D in CIGAR?
            if len(read_seq_unpadded) != sum(int(x) for x in cigar.replace("I","=").replace("S","=").replace("M","X").replace("X","=").split("=") if x):
                raise ValueError("%s vs %i for %s" % (cigar, len(read_seq_unpadded), read_seq))
        assert len(read_seq_unpadded) == len(read_qual_unpadded)
        line = "%s\t%i\t%s\t%i\t%i\t%s\t%s\t%i\t%s\t%s\t%s" % \
            (self.template_name, flag, self.contig_name, self.ref_pos,
             self.map_qual, cigar,
             mate_ref_name, mate_ref_pos, self.insert_size,
             read_seq_unpadded, read_qual_unpadded)
        if self.read_group:
            #MIRA v3.9+ assigns this
            if self.read_group not in read_group_ids:
                log("Undeclared read group %r" % self.read_group)
                log(line)
                sys.exit(1)
            line += "\tRG:Z:%s" % self.read_group
        else:
            #We assign this on old MIRA
            assert self.seq_tech
            line += "\tRG:Z:%s" % read_group_ids[(self.seq_tech, self.strain)]
        for tag in self.tags:
             assert not tag.startswith("RG:"), tag
             line += "\t" + tag
        return line

print("@HD\tVN:1.4\tSO:unsorted")
print("@CO\tConverted from a MIRA Alignment Format (MAF) file")

ref_lens = {}
ref_md5 = {}
handle = open(ref)
gapped_sam = False
for rec in SeqIO.parse(handle, "fasta"):
    #Note MIRA uses * rather than - in the output padded FASTA
    #However, for padded references SAM/BAM say use * for MD5
    seq = str(rec.seq).upper().replace("-","*")
    if not gapped_sam and "*" in seq:
        log("NOTE: Producing SAM using a gapped reference sequence.")
        gapped_sam = True
    md5 = seq_md5(seq)
    ref_md5[rec.id] = md5
    ref_lens[rec.id] = len(seq)
    print("@SQ\tSN:%s\tLN:%i\tM5:%s" % (rec.id, len(seq), md5))
handle.close()
del handle
if not ref_lens:
    log("No FASTA sequences found in reference %s" % ref)
    sys.exit(1)

def clean_platform(tech):
    platform = tech.upper()
    if platform == "SANGER":
        platform = "CAPILLARY"
    elif platform == "SOLEXA":
        platform = "ILLUMINA"
    elif platform == "454":
        platform = "LS454"
    elif platform == "IONTOR":
        platform = "IONTORRENT"
    if platform == "TEXT":
        return "SYNTHETIC" # Nothing in the SAM/BAM spec is appropriate for synthetic reads
    if platform not in ["CAPILLARY", "LS454", "ILLUMINA", "SOLID", "HELICOS", "IONTORRENT", "PACBIO"]:
        raise ValueError("Sequencing technology/platform %r not supported in SAM/BAM" % tech)
    return platform

def read_groups_old(handle):
    """Scan entire (old) MAF file to determine read groups."""
    log("Starting pre-pass though the MAF file")
    seq_tech_strains = set() #will make into a list of 2-tuples
    #handle = open(maf)
    tech = ""
    strain = ""
    for line in handle:
        if line.startswith("RD"):
            assert not tech and not strain
        elif line.startswith("ST\t"):
            tech = line[3:].strip()
        elif line.startswith("SN\t"):
            strain = line[3:].strip()
        elif line.startswith("ER"):
            assert tech or strain, "Missing read group data!"
            seq_tech_strains.add((tech, strain))
            tech = ""
            strain = ""
    #handle.close()
    seq_tech_strains = sorted(list(seq_tech_strains))
    read_group_ids = dict()
    for id, (tech, strain) in enumerate(seq_tech_strains):
        platform = clean_platform(tech)
        assert len(strain.split())<=1, "Whitespace in strain %r (SN line)" % strain
        read_group_id = ("%s_%s" % (tech, strain)).strip("_")
        read_group_ids[(tech, strain)] = read_group_id
        print("@RG\tID:%s\tPL:%s\tSM:%s" % (read_group_id, platform, strain))
    del strain, tech, seq_tech_strains
    return read_group_ids

def read_groups_new(handle):
    read_groups = set()
    read_group_id = platform = name = strain = None
    while True:
        line = handle.readline()
        if not line or line.startswith("CO\t"):
            break
        elif line.startswith("@ReadGroup"):
            assert read_group_id == platform == strain == None
        elif line.startswith("@RG\tname\t"):
            name = line.split("\t")[2].strip()
        elif line.startswith("@RG\tID\t"):
            read_group_id = line.split("\t")[2].strip()
        elif line.startswith("@RG\ttechnology\t"):
            platform = clean_platform(line.split("\t")[2].strip())
        elif line.startswith("@RG\tstrainname\t"):
            strain = line.split("\t")[2].strip()
        elif line.startswith("@EndReadGroup"):
            assert read_group_id and platform and strain
            if name:
                print("@RG\tID:%s\tPL:%s\tLB:%s\tSM:%s" \
                    % (read_group_id, platform, name, strain))
            else:
                print("@RG\tID:%s\tPL:%s\tSM:%s" \
                    % (read_group_id, platform, strain))
            read_groups.add(read_group_id)
            read_group_id = platform = name = strain = None
    return read_groups


def make_ungapped_ref_cigar_m(contig, read):
    #For testing legacy code which expects CIGAR with M rather than X/=
    assert len(contig) == len(read)
    cigar = ""
    count = 0
    d_count = 0
    mode = ""
    for c,r in zip(contig, read):
        if c == "*" and r == "*":
            pass
        elif c != "*" and r != "*":
            #alignment match/mismatch
            if mode!="M":
                if count: cigar += "%i%s" % (count, mode)
                mode = "M"
                count = 1
            else:
                count+=1
        elif c == "*":
            if mode!="I":
                if count: cigar += "%i%s" % (count, mode)
                mode = "I"
                count = 1
            else:
                count+=1
        elif r == "*":
            if mode!="D":
                if count: cigar += "%i%s" % (count, mode)
                mode = "D"
                count = 1
            else:
                count+=1
            d_count+=1
        else:
            assert False
    if count: cigar += "%i%s" % (count, mode)
    if len(read.replace("*", "")) != sum(int(x) for x in cigar.replace("D","M").replace("I","M").split("M") if x) - d_count:
        raise ValueError("%s versus %i, %s" % (cigar, len(read.replace("*", "")), read))
    return cigar

def make_ungapped_ref_cigar(contig, read):
    #WARNING - This function expects contig and read to be in same case!
    assert len(contig) == len(read)
    cigar = ""
    count = 0
    d_count = 0
    mode = "" #Character codes in CIGAR string
    for c,r in zip(contig, read):
        if c == "*" and r == "*":
            pass
        elif c != "*" and r != "*":
            #alignment match/mismatch
            #CIGAR in SAM v1.2 just had M for match/mismatch
            if c==r:
                if mode!="=":
                    if count: cigar += "%i%s" % (count, mode)
                    mode = "="
                    count = 1
                else:
                    count+=1
            else:
                if mode!="X":
                    if count: cigar += "%i%s" % (count, mode)
                    mode = "X"
                    count = 1
                else:
                    count+=1
        elif c == "*":
            if mode!="I":
                if count: cigar += "%i%s" % (count, mode)
                mode = "I"
                count = 1
            else:
                count+=1
        elif r == "*":
            if mode!="D":
                if count: cigar += "%i%s" % (count, mode)
                mode = "D"
                count = 1
            else:
                count+=1
            d_count+=1
        else:
            assert False
    if count: cigar += "%i%s" % (count, mode)
    if len(read.replace("*", "")) != sum(int(x) for x in cigar.replace("D","=").replace("I","=").replace("X","=").split("=") if x) - d_count:
        raise ValueError("%s versus %i, %s" % (cigar, len(read.replace("*", "")), read))
    return cigar


assert make_ungapped_ref_cigar("ACGTA" ,"ACGTA") == "5="
assert make_ungapped_ref_cigar("ACGTA" ,"CGTAT") == "5X"
assert make_ungapped_ref_cigar("ACGTA" ,"ACTTA") == "2=1X2="
assert make_ungapped_ref_cigar("ACG*A" ,"ACT*A") == "2=1X1="
assert make_ungapped_ref_cigar("ACGTA" ,"ACT*A") == "2=1X1D1="
assert make_ungapped_ref_cigar("ACG*A" ,"ACTTA") == "2=1X1I1="

def make_gapped_ref_cigar_m(contig, read):
    #For testing legacy code which expects CIGAR with M rather than X/=
    #WARNING - This function expects contig and read to be in same case!
    assert len(contig) == len(read)
    cigar = ""
    count = 0
    d_count = 0
    mode = "" #Character codes in CIGAR string
    for c,r in zip(contig, read):
        if r == "*":
            if mode!="D":
                if count: cigar += "%i%s" % (count, mode)
                mode = "D"
                count = 1
            else:
                count+=1
        elif r != "*":
            #alignment match/mismatch
            if mode!="M":
                if count: cigar += "%i%s" % (count, mode)
                mode = "M"
                count = 1
            else:
                count+=1
    if count: cigar += "%i%s" % (count, mode)
    return cigar


def make_gapped_ref_cigar(contig, read):
    #WARNING - This function expects contig and read to be in same case!
    assert len(contig) == len(read)
    cigar = ""
    count = 0
    d_count = 0
    mode = "" #Character codes in CIGAR string
    for c,r in zip(contig, read):
        if r == "*":
            if mode!="D":
                if count: cigar += "%i%s" % (count, mode)
                mode = "D"
                count = 1
            else:
                count+=1
        elif r != "*":
            #alignment match/mismatch
            #CIGAR in SAM v1.2 just had M for match/mismatch
            if c==r:
                if mode!="=":
                    if count: cigar += "%i%s" % (count, mode)
                    mode = "="
                    count = 1
                else:
                    count+=1
            else:
                if mode!="X":
                    if count: cigar += "%i%s" % (count, mode)
                    mode = "X"
                    count = 1
                else:
                    count+=1
    if count: cigar += "%i%s" % (count, mode)
    return cigar

assert make_gapped_ref_cigar("ACGTA" ,"CGTAT") == "5X"
assert make_gapped_ref_cigar("ACGTA" ,"ACGTA") == "5="
assert make_gapped_ref_cigar("AC*TA" ,"ACGTA") == "2=1X2="
assert make_gapped_ref_cigar("AC*TA" ,"AC*TA") == "2=1D2="
assert make_gapped_ref_cigar("ACGTA" ,"AC*TA") == "2=1D2="
assert make_gapped_ref_cigar("ACGTA" ,"ACTTA") == "2=1X2="
assert make_gapped_ref_cigar("ACG*A" ,"ACT*A") == "2=1X1D1="
assert make_gapped_ref_cigar("ACGTA" ,"ACT*A") == "2=1X1D1="
assert make_gapped_ref_cigar("ACG*A" ,"ACTTA") == "2=2X1="

if gapped_sam:
    if CIGAR_M:
        make_cigar = make_gapped_ref_cigar_m
    else:
        make_cigar = make_gapped_ref_cigar
else:
    if CIGAR_M:
        make_cigar = make_ungapped_ref_cigar_m
    else:
        make_cigar = make_ungapped_ref_cigar

contig_lines_to_ignore = ['NR', #number of reads
                          'LC', #padded contig length
                          'CT', #consensus tag
                         ]
re_contig_lines_to_ignore = re.compile(r'^(%s)\t' % '|'.join(contig_lines_to_ignore))
read_lines_to_ignore = ['SV', #sequencing vector
                        'LR', #read length
                        'TF', #min estimated template length
                        'TT', #max estimated template length
                        'SF', #sequencing file
                        'AO', #align to original
                        'RT', #reads tag
                        'MT', #machine type
                        'IB', #backbone
                        'IC', #coverage equivalent
                        'IR', #rail
                        'BC', #not sure what this is yet...
                        'TS', #not sure what this is yet...
                        ]
re_read_lines_to_ignore = re.compile(r'^(%s)\t' % '|'.join(read_lines_to_ignore))
assert re_read_lines_to_ignore.match('LR\t2000\n')
assert re_read_lines_to_ignore.match('TF\t2000\n')
assert re_read_lines_to_ignore.match('TT\t5000\n')
assert not re_read_lines_to_ignore.match('LN\tFred\n')


maf_handle = open(maf)
line = maf_handle.readline()
if not line:
    log("Your MAF file is empty!")
    sys.exit(1)
elif line.startswith("CO\t"):
    log("Identified as up to MIRA v3.4 (MAF v1)")
    read_group_ids = read_groups_old(maf_handle) #dict
elif line.startswith("@Version\t2"):
    log("Identified as MIRA v3.9 or later (MAF v2)")
    log("WARNING - Support for this is *still* EXPERIMENTAL!")
    read_group_ids = read_groups_new(maf_handle) #set
else:
    log("Not a MIRA Alignment Format (MAF) file?")
    log("Starts: %r" % line)
    sys.exit(1)
log("Identified %i read groups" % len(read_group_ids))
log("Starting main pass though the MAF file")
cached_pairs = dict()
maf_handle.seek(0)  # Should be able to avoid this with MAF v2
line = maf_handle.readline()
while line.startswith("@"):
    # Skip MIRA v3.9+ style header
    line = maf_handle.readline()
assert line.startswith("CO\t"), line
bad_line_types = set()
while True:
    if not line: break
    assert line.startswith("CO\t"), line

    contig_name = line.rstrip().split("\t")[1]
    assert contig_name in ref_lens
    padded_con_seq = None
    padded_con_qual = None
    current_read = None

    # log("Contig %s" % contig_name)

    while True:
        line = maf_handle.readline()
        if line == "EC\n":
            line = maf_handle.readline()
            break
        elif line.startswith("CS\t"):
            padded_con_seq = line.rstrip().split("\t")[1].upper()
            if gapped_sam:
                assert ref_lens[contig_name] == len(padded_con_seq), \
                    "Gapped reference length mismatch for %s" % contig_name
                assert ref_md5[contig_name] == seq_md5(padded_con_seq), \
                    "Gapped reference checksum mismatch for %s" % contig_name
            else:
                assert ref_lens[contig_name] == len(padded_con_seq) - padded_con_seq.count("*"), \
                    "Ungapped reference length mismatch for %s" % contig_name
                assert ref_md5[contig_name] == seq_md5(padded_con_seq.replace("*","")), \
                    "Ungapped reference checksum mismatch for %s" % contig_name
        elif line.startswith("CQ\t"):
            assert len(padded_con_seq) == len(line.rstrip().split("\t")[1])
        elif line == "\\\\\n":
            assert padded_con_seq
            mapping = []
            index = 0
            for letter in padded_con_seq:
                mapping.append(index)
                if letter != "*":
                    index+=1
            while line != "//\n":
                current_read = Read(contig_name, first_in_pair = None)
                while True:
                    line = maf_handle.readline()
                    if line == "//\n":
                        break
                    elif line.startswith("RD\t"):
                        current_read.read_name = line.rstrip().split("\t")[1]
                        assert current_read.read_name
                    elif line.startswith("RS\t"):
                        current_read.read_seq = line.rstrip().split("\t")[1].upper()
                    elif line.startswith("RQ\t"):
                        current_read.read_qual = line.rstrip().split("\t")[1]
                        assert len(current_read.read_qual) == len(current_read.read_seq)
                    elif line.startswith("TN\t"):
                        current_read.template_name = line.rstrip().split("\t")[1]
                        #assert current_read.read_name.startswith(current_read.template_name)
                    elif line.startswith("DI\t"):
                        #MAF v1 uses DI, MAF v2 uses TS
                        if line == "DI\tF\n":
                            current_read.first_in_pair = True
                        elif line == "DI\tR\n":
                            current_read.first_in_pair = False
                        else:
                            raise ValueError(line)
                    elif line.startswith("TS\t"):
                        if line == "TS\t1\n":
                            current_read.first_in_pair = True
                        elif line == "TS\t255\n":
                            current_read.first_in_pair = False
                        else:
                            # MAF and SAM/BAM support multiple fragments,
                            # but thus far this script only does pairs.
                            raise ValueError("Unsported pairing info: %r" % line)
                    elif line.startswith("SL\t"):
                        current_read.vect_left = int(line.rstrip().split("\t")[1])
                    elif line.startswith("SR\t"):
                        current_read.vect_right = int(line.rstrip().split("\t")[1])
                    elif line.startswith("QL\t"):
                        current_read.qual_left = int(line.rstrip().split("\t")[1])
                    elif line.startswith("QR\t"):
                        current_read.qual_right = int(line.rstrip().split("\t")[1])
                    elif line.startswith("CL\t"):
                        current_read.clip_left = int(line.rstrip().split("\t")[1])
                    elif line.startswith("CR\t"):
                        current_read.clip_right = int(line.rstrip().split("\t")[1])
                    elif line.startswith("ST\t"):
                        current_read.seq_tech = line.rstrip().split("\t")[1]
                    elif line.startswith("SN\t"):
                        current_read.strain = line.rstrip().split("\t")[1]
                    elif line.startswith("RG\t"):
                        current_read.read_group = line.rstrip().split("\t")[1]
                    elif line == "ER\n":
                        #End of read - next line should be AT then //
                        pass
                    elif line.startswith("AT\t"):
                        #Assembles to
                        x1, y1, x2, y2 = [int(i) for i in line[3:-1].split()]
                        #AT Four integers: x1 y1 x2 y2
                        #The AT (Assemble_To) line defines the placement of the
                        #read in the contig and follows immediately the closing
                        #"ER" of a read so that parsers do not need to perform
                        #time consuming string lookups. Every read in a contig
                        #has exactly one AT line.
                        #The interval [x2 y2] of the read (i.e., the unclipped
                        #data, also called the 'clear range') aligns with the
                        #interval [x1 y1] of the contig. If x1 > y1 (the contig
                        #positions), then the reverse complement of the read is
                        #aligned to the contig. For the read positions, x2 is
                        #always < y2.
                        #
                        # If MIRA is used in mapping mode, the soft trimmed
                        # region can contain gaps which must be discarded
                        # for getting the CIGAR S operator count.
                        if x1 > y1:
                            current_read.ref_rc = True
                            #SAM stores these backwards:
                            cigar = make_cigar(padded_con_seq[y1-1:x1],
                                               reverse_complement(current_read.read_seq[x2-1:y2]))
                            if x2 > 1:
                                clipped = len(current_read.read_seq[:x2-1].replace("*", ""))
                                cigar += "%iS" % clipped
                            if y2 < len(current_read.read_seq):
                                clipped = len(current_read.read_seq[y2:].replace("*", ""))
                                cigar = "%iS%s" % (clipped, cigar)
                        else:
                            cigar = make_cigar(padded_con_seq[x1-1:y1],
                                               current_read.read_seq[x2-1:y2])
                            if x2 > 1:
                                clipped = len(current_read.read_seq[:x2-1].replace("*", ""))
                                cigar = "%iS%s" % (clipped, cigar)
                            if y2 < len(current_read.read_seq):
                                clipped = len(current_read.read_seq[y2:].replace("*", ""))
                                cigar += "%iS" % clipped
                        current_read.cigar = cigar
                        current_read.padded_pos = min(x1, y1)-1 #zero based
                        if gapped_sam:
                            current_read.ref_pos = current_read.padded_pos+1 #one based for SAM
                        else:
                            current_read.ref_pos = mapping[current_read.padded_pos]+1 #one based for SAM
                        break #End of this read
                    elif not line:
                        raise ValueError("EOF in read")
                    elif re_read_lines_to_ignore.match(line):
                        pass
                    elif len(line) > 3 and line[2] == "\t" and line[0:2] in bad_line_types:
                        pass
                    else:
                        sys.stderr.write("Bad line in read: %s\n" % repr(line))
                        #Continue and hope we can just ignore it!
                        if len(line) > 3 and line[2] == "\t":
                            #Ignore future occurances of this line type
                            bad_line_types.add(line[0:2])
                if line == "//\n":
                    break
                assert (current_read.template_name, current_read.first_in_pair) not in cached_pairs, \
                    "Appear to have duplicate entries for %s" % current_read.read_name
                if current_read.need_partner():
                    cached_pairs[(current_read.template_name, current_read.first_in_pair)] = current_read
                elif current_read.is_paired():
                    cached_pairs[(current_read.template_name, current_read.first_in_pair)] = current_read
                    print(current_read.get_partner())
                    print(current_read)
                    # Clear from cache
                    del cached_pairs[(current_read.template_name, current_read.first_in_pair)]
                    del cached_pairs[(current_read.template_name, not current_read.first_in_pair)]
                else:
                    log("Unpaired read %s" % current_read.read_name)
                    print(current_read)
        elif not line:
            raise ValueError("EOF in contig")
        elif re_contig_lines_to_ignore.match(line):
            pass
        else:
            sys.stderr.write("Bad line in contig: %s" % repr(line))
            #Continue and hope we can just ignore it!

if cached_pairs:
    log("Almost done, %i orphaned paired reads remain" % len(cached_pairs))
    #Special cases - paired reads where partner was not found in MAF file
    for current_read in cached_pairs.itervalues():
        print(current_read)
else:
    log("No orphaned paired reads")
log("Done")
