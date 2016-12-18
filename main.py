#!c:\\python27\python.exe
# -*- coding: utf-8 -*-

'''IDA PDB Loader.'''

# FIXME: fails to find non-mangled names, pdbparse bug?


import traceback

import idautils
import idaapi
import idc

import pdbparse.symlookup
idaapi.require('pdbparse.symlookup')

__author__ = 'Arthur Gerkis'
__version__ = '0.0.2'


class Plugin(object):
    '''IDA Pro Plugin'''
    def __init__(self):
        super(Plugin, self).__init__()
        self.symbol_path = ''
        self.image_base = 0
        self.PDBLookup = None

    def run(self):
        '''Public function.'''

        self.symbol_path = idc.AskFile(0, '*.pdb', 'Choose PDB file...')
        self.image_base = idaapi.get_imagebase()

        print "IPL: Loading PDB data, might take a while..."
        self.PDBLookup = pdbparse.symlookup.Lookup([(self.symbol_path, self.image_base)])

        if not self.PDBLookup:
            print "IPL: PDBLookup failed to initialize, exiting."
            return

        self._rename_functions()
        return

    def _rename_functions(self):
        '''Rename functions.'''

        print "IPL: Started to rename functions..."

        failed = 0
        total = 0
        for function in idautils.Functions():
            total += 1
            pdb_mangled_name = self.PDBLookup.lookup(function, True)
            if not pdb_mangled_name:
                failed += 1
                print "IPL: Failed to find symbol for function: 0x{:08x}".format(function)
                continue
            _, mangled_function_name = pdb_mangled_name.split('!')
            # https://www.hex-rays.com/products/ida/support/idadoc/203.shtml
            idc.MakeNameEx(function, mangled_function_name,
                           idc.SN_AUTO | idc.SN_NOCHECK)
        print "IPL: Total {} functions, {} failed to rename.".format(total, failed)


def main():
    '''Main.'''
    try:
        Plugin().run()
    except Exception:
        print traceback.format_exc()


if __name__ == '__main__':
    main()
