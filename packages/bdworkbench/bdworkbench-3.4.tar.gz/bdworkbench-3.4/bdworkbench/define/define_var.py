#
# Copyright (c) 2016 BlueData Software, Inc.
#

from __future__ import print_function
from .. import SubCommand
from ..utils import printDict
from ..inmem_store import VARIABLES_DICT

class DefineVar(SubCommand):
    """

    """
    def __init__(self, config, inmemStore, cmdObj):
        SubCommand.__init__(self, config, inmemStore, cmdObj, 'var')

    def getSubcmdDescripton(self):
        return 'Define a variable.'

    def populateParserArgs(self, subparser):
        subparser.add_argument('keyvalues', metavar="KEY=VALUE", type=str,
                                nargs='+',
                                help='Define a KEY and assign a VALUE. All '
                                'occurances of %%KEY%% in any workbench command '
                                'following will be replaced by the VALUE. '
                                'NOTE: percentage(%%), equalto(=) and spaces '
                                'are not allowed in either KEY or VALUE. ')
        return

    def run(self, pargs):
        varsDict = self.inmemStore.getDict(VARIABLES_DICT)
        for var in pargs.keyvalues:
            (key, value) = var.split('=')
            self.inmemStore.addField(VARIABLES_DICT, key, value)

        return True

    def complete(self, text, argsList):
        return []


__all__ = ["DefineVar"]
