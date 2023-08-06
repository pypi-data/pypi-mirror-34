#
# Copyright (c) 2018 BlueData Software, Inc.
#
"""Module for packaging a docker image into the catalog bundle.
"""
from __future__ import print_function
import os
import sys
import shutil
import atexit

from .. import SubCommand
from ..constants import *
from ..inmem_store import DELIVERABLE_DICT
from ..utils import executeShellCmd as executeShellCmd
from ..utils.misc import getOrgname, doSkipImageRebuild, getBaseOSMajorVersion
from ..utils.config import KEY_STAGEDIR, SECTION_WB

class ImagePull(SubCommand):
    """
    Subcommand for building docker image for the catalog
    """
    def __init__(self, config, inmemStore, cmdObj):
        SubCommand.__init__(self, config, inmemStore, cmdObj, 'pull')

    def getSubcmdDescripton(self):
        return 'Pull an image from the registry.'

    def populateParserArgs(self, subparser):
        subparser.add_argument('-i', '--image-repotag', metavar='IMAGE_REPOTAG',
                               type=str, dest='repotag', required=True,
                               help='Container name and tag for the newly built image.'
                               'This is usually of the form '
                               'REGISTRY_HOST[:REGISTRY_PORT]/]REPOSITORY[:TAG]. See'
                               '\'man docker-build\' for more details.')
        subparser.add_argument('-t', '--retag', metavar='NEW_REPOTAG',
                                type=str, dest='retag', default=None,
                                help="Retag the image after pull it from remote "
                                "registry.")

        self.command.addAuthAndCTArgs(subparser)


    def run(self, pargs):
        delivDict = self.inmemStore.getDict(DELIVERABLE_DICT)

        # Check if the repotag includes the registry url
        registryUrl, repotag = self.command.normalizeImageName(pargs.repotag, delivDict)
        if repotag == None:
            return False

        with self.command.getDockerLoginContext(delivDict["built_on_docker"],
                                                registryUrl, pargs):
            print("Pulling", repotag)
            dockerPullCmd = 'docker pull %s' % repotag
            if executeShellCmd(dockerPullCmd):
                if pargs.retag != None:
                    dockerTagCmd = 'docker tag %s %s' %(pargs.repotag, pargs.retag)
                    if not executeShellCmd(dockerTagCmd):
                        print("ERROR: Retagging %s failed" % (pargs.repotag))
                        return False
            else:
                print("ERROR: Failed to pull %s from registry %s" %(pargs.repotag, registryUrl))
                return False

        return True

    def complete(self, text, argsList):
        return []

__all__ = ['ImagePull']
