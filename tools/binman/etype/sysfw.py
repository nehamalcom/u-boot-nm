# SPDX-License-Identifier: GPL-2.0+
# Copyright (C) 2022 Texas Instruments Incorporated - https://www.ti.com/
#
# Entry type module for TI SYSFW binary blob
#

import struct
import zlib
import os
import sys

from binman.etype.blob import Entry_blob
from dtoc import fdt_util
from patman import tools


class Entry_sysfw(Entry_blob):
    """Entry containing System Firmware (SYSFW) blob

    Properties / Entry arguments:
        - sysfw-path: Filename of file to read into the entry, typically sysfw.bin

This entry contains system firmware necessary for booting of K3 architecture devices.
    """

    def __init__(self, section, etype, node):
        super().__init__(section, etype, node)

    def ReadBlobContents(self):
        k3_cert_gen_path = os.environ['srctree'] + "/tools/k3_gen_x509_cert.sh"
        self.load_addr = fdt_util.GetInt(self._node, 'load')
        args = [
            '-c', "0",
            '-b', self._filename,
            '-l', str(self.load_addr),
            '-o', os.getcwd() + "/" + "sysfwint"
        ]
        tools.run(k3_cert_gen_path, *args)
        self.SetContents(tools.read_file(os.getcwd() + "/" + "sysfwint"))
        return True

    def ProcessFdt(self, fdt):
        self._filename = os.environ['SCP']
        return super().ProcessFdt(fdt)
