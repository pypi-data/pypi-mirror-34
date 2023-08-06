# -*- coding: utf-8 -*-
###########################################################################
# Bioconvert is a project to facilitate the interconversion               #
# of life science data from one format to another.                        #
#                                                                         #
# Authors: see CONTRIBUTORS.rst                                           #
# Copyright © 2018  Institut Pasteur, Paris and CNRS.                     #
# See the COPYRIGHT file for details                                      #
#                                                                         #
# bioconvert is free software: you can redistribute it and/or modify      #
# it under the terms of the GNU General Public License as published by    #
# the Free Software Foundation, either version 3 of the License, or       #
# (at your option) any later version.                                     #
#                                                                         #
# bioconvert is distributed in the hope that it will be useful,           #
# but WITHOUT ANY WARRANTY; without even the implied warranty of          #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           #
# GNU General Public License for more details.                            #
#                                                                         #
# You should have received a copy of the GNU General Public License       #
# along with this program (COPYING file).                                 #
# If not, see <http://www.gnu.org/licenses/>.                             #
###########################################################################
"""Convert :term:`FASTQ` to :term:`BAM`"""
from bioconvert import ConvBase
from bioconvert.core.decorators import requires


class BAX2BAM(ConvBase):
    """Convert :term:`BAX` to :term:`BAM`

    bax2bam converts the legacy PacBio basecall format (bax.h5) into the BAM
    basecall format.
    """
    _default_method = "bax2bam"

    def __init__(self, infile, outfile, infile2=None, *args, **kwargs):
        """
        :param str infile: The path to the input FASTA file.
        :param str outfile: The path to the output file.
        """
        super().__init__(infile, outfile)

    @requires("bax2bam")
    def _method_bax2bam(self, *args, **kwargs):
        """
        """
        cmd = "bax2bam {} -o {} ".format(self.infile, self.outfile)
        self.execute(cmd)

