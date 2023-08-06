#
# Copyright (c) 2016 BlueData Software, Inc.
#

from __future__ import print_function
from .. import SubCommand
from ..inmem_store import ENTRY_DICT
from catalog_package_v3 import CatalogPackageV3
from catalog_package_v4 import CatalogPackageV4

import os, gzip, stat, base64, shutil, hashlib, subprocess, json

class CatalogPackage(SubCommand):
    """
    A wrapper SubCommand implementation that invokes the appropriate SubCommand
    object depending on the 'catalog_api_version' defined.
    """
    def __init__(self, config, inmemStore, cmdObj):
        SubCommand.__init__(self, config, inmemStore, cmdObj, 'package')
        self.v3 = CatalogPackageV3(config, inmemStore, cmdObj)
        self.v4 = CatalogPackageV4(config, inmemStore, cmdObj)

    def getSubcmdDescripton(self):
        return 'Package all components of the catalog into a bundle (.bin file).'

    def populateParserArgs(self, subparser):
        subparser.add_argument('-v', '--verbose', action='store_true',
                               dest='verbose', default=False,
                               help='Show details of the packing process.')

    def run(self, pargs):
        entryDict = self.inmemStore.getDict(ENTRY_DICT)
        if entryDict.has_key('catalog_api_version'):
            if entryDict['catalog_api_version'] >= 4:
                return self.v4.run(pargs)
            else:
                return self.v3.run(pargs)
        else:
            # We should never get here in practice.
            print("ERROR: 'catalog_api_version' is undefined")
            return False

    def complete(self, text, argsList):
        return []
