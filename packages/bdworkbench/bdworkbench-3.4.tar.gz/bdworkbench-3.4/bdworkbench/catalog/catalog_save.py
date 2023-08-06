#
# Copyright (c) 2016 BlueData Software, Inc.
#

from __future__ import print_function
from __future__ import with_statement

from .. import SubCommand
from ..constants import *
from ..inmem_store import ENTRY_DICT, DELIVERABLE_DICT
from ..utils.config import KEY_STAGEDIR, SECTION_WB
from ..utils.misc import isVersionDebug, generateNewVersion,  getMaxDebugVersion

import os, json, traceback

class CatalogSave(SubCommand):
    """

    """
    def __init__(self, config, inmemStore, cmdObj):
        SubCommand.__init__(self, config, inmemStore, cmdObj, 'save')

    def getSubcmdDescripton(self):
        return 'Saves the current in-memory state of the catalog entry to a file.'

    def populateParserArgs(self, subparser):
        subparser.add_argument('-f', '--filepath', metavar='FILE_PATH', type=str,
                               dest='file', default=None,
                               help='File path to save the catalog entry json. '
                                    'If this is not specified, the json file '
                                    'is saved in the \'staging_dir\' defined '
                                    'in bench.conf')
        subparser.add_argument('--force', action='store_true',
                               dest='force', default=False,
                               help='Overwrite the catalog entry json file if '
                                    'it already exists.')

    def run(self, pargs):
        if (pargs.file is not None) and (not pargs.file.endswith('.json')):
            print("ERROR: Filepath must end in .json", )
            return False

        entryDict = self.inmemStore.getDict(ENTRY_DICT)
        delivDict = self.inmemStore.getDict(DELIVERABLE_DICT)
        if not entryDict.has_key(DISTROID_STR):
            print("ERROR: 'catalog load|new <args>' must be executed before saving.")
            return False

        currentVersion = entryDict[VERSION_STR]
        if isVersionDebug(currentVersion):
            distro = entryDict[DISTROID_STR]

            # start with newVersion being currentVersion, then update it if needed
            newVersion = currentVersion
            storedVersion = self.config.get(distro, VERSION_STR)

            if storedVersion is not None:
                # found prior state for this distro id
                if getMaxDebugVersion(currentVersion, storedVersion) == storedVersion:
                    # bump it up
                    newVersion = generateNewVersion(storedVersion)

            self.config.addOrUpdate(distro, VERSION_STR, newVersion)
            entryDict[VERSION_STR] = newVersion

        if pargs.file == None:
            stagingDir = self.config.get(SECTION_WB, KEY_STAGEDIR)
            filepath = os.path.join(stagingDir, entryDict[DISTROID_STR] + '.json')
            force = True
        else:
            filepath = pargs.file
            force = pargs.force

        try:
            if (not os.path.exists(filepath)) or (force == True):
                dirname = os.path.dirname(filepath)
                if (dirname is not '') and (not os.path.exists(dirname)):
                    os.makedirs(dirname)

                jsonData = json.dumps(entryDict, indent=4)
                with open(filepath, 'w') as f:
                    f.write(jsonData)

                delivDict[ENTRY_STR] = filepath
                return True
            else:
                print("ERROR: '%s' already exists. Use --force to overwrite." % filepath)
                return False

        except Exception as e:
            print("Failed to save catalog entry at '%s':" % filepath, e)
            traceback.print_exc()
            return False

    def complete(self, text, argsList):
        return []
