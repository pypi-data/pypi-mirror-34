#
# Copyright (c) 2016 BlueData Software, Inc.
#
from __future__ import print_function
from .. import SubCommand
from ..constants import AWB_VERSION
import os, shutil

class WorkbenchVersion(SubCommand):
    """

    """

    def __init__(self, config, inmemStore, cmdObj):
        SubCommand.__init__(self, config, inmemStore, cmdObj, 'version')

    def getSubcmdDescripton(self):
        return 'Displays the workbench version.'

    def populateParserArgs(self, subparser):
        return

    def run(self, pargs):
        print("BlueData workbench version: ", AWB_VERSION)
        return True

    def complete(self, text, argsList):
        return []
