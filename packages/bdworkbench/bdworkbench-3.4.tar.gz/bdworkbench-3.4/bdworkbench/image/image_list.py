#
# Copyright (c) 2016 BlueData Software, Inc.
#

from __future__ import print_function
from .. import SubCommand
from ..utils import printDict
from ..inmem_store import ENTRY_DICT
from ..constants import IMAGE_PER_ROLE_SUPPORT

class ImageList(SubCommand):
    """

    """
    def __init__(self, config, inmemStore, cmdObj):
        SubCommand.__init__(self, config, inmemStore, cmdObj, 'list')

    def getSubcmdDescripton(self):
        return 'List the configured container image.'

    def populateParserArgs(self, subparser):
        return

    def run(self, pArgs):
        entryDict = self.inmemStore.getDict(ENTRY_DICT)

        if entryDict.has_key('catalog_api_version'):
            catalogApiVersion = entryDict['catalog_api_version']

            if catalogApiVersion >= IMAGE_PER_ROLE_SUPPORT:
                if entryDict.has_key('node_roles'):
                    nodeRoles = entryDict['node_roles']
                    for role in nodeRoles:
                        if role.has_key('image'):
                            printDict(role['image'])

                        print("")
            else:
                if entryDict.has_key("image"):
                    printDict(entryDict['image'])
        else:
            print("WARNING: catalog_api_version is not yet configured.")

        return True

    def complete(self, text, argsList):
        return []
