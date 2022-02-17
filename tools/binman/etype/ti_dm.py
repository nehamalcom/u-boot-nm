# SPDX-License-Identifier: GPL-2.0+
# Copyright (C) 2022 Texas Instruments Incorporated - https://www.ti.com/
#
# Entry type for TI Device Manager

from binman.etype.blob import Entry_blob
import os


class Entry_ti_dm(Entry_blob):
    """Entry containing a Device Manager (DM)

    Properties / Entry arguments:
        - ti-dm-path: Filename of file to read into the entry, typically dm.bin

    This entry holds the device manager responsible for resource and power management
    in K3 devices.
    """

    def __init__(self, section, etype, node):
        super().__init__(section, etype, node)
        self._filename = os.environ['DM']
