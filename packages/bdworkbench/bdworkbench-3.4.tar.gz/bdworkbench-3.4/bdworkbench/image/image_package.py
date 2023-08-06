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

class ImagePackage(SubCommand):
    """
    Subcommand for building docker image for the catalog
    """
    def __init__(self, config, inmemStore, cmdObj):
        SubCommand.__init__(self, config, inmemStore, cmdObj, 'package')

    def getSubcmdDescripton(self):
        return 'Package an image in the local registry into catalog bundle as a file.'

    def populateParserArgs(self, subparser):
        subparser.add_argument('-i', '--image-repotag', metavar='IMAGE_REPOTAG',
                               type=str, dest='repotag', required=True,
                               help='Container name and tag for the newly built image.'
                               'This is usually of the form '
                               'REGISTRY_HOST[:REGISTRY_PORT]/]REPOSITORY[:TAG]. See'
                               '\'man docker-build\' for more details.')
        subparser.add_argument('--os', metavar="OS", dest="os", required=True,
                                 choices=OS_CLASS_DICT.keys(), action='store',
                                 help="The OS distribution of the container image.")
        subparser.add_argument('--roles', metavar="ROLE(S)", dest="roles",  nargs='+',
                                 required=False, default=DEFAULT_IMAGE_ROLES,
                                 help="Assign the image to a specific ROLE or ROLES. "
                                 "If specified the image is used for the roles "
                                 "when deploying a cluster on EPIC.")

        self.command.addAuthAndCTArgs(subparser)


    def run(self, pargs):
        delivDict = self.inmemStore.getDict(DELIVERABLE_DICT)

        # Check if the repotag includes the registry url
        registryUrl, repotag = self.command.normalizeImageName(pargs.repotag, delivDict)
        if repotag == None:
            return False

        stagindDir = self.config.get(SECTION_WB, KEY_STAGEDIR)
        tarfileName = repotag.replace(':', '-').replace('/', '-') +  \
                                                    '.tar'
        zipFilename = tarfileName + '.gz'
        destTarFile = os.path.join(stagindDir, tarfileName)
        zippedDestFile = os.path.join(stagindDir, zipFilename)

        if not doSkipImageRebuild(zippedDestFile):
            # This means we were asked to not rebuild the image and so the
            # assumption is that the compressed image file also exists.
            dockerSaveCmd = 'docker save -o %s %s' % (destTarFile, repotag)
            zipCmd = 'gzip -f %s' % (destTarFile)

            print("Saving the docker image: %s" % (tarfileName))
            if not executeShellCmd(dockerSaveCmd):
                print ("ERROR: Failed to save the docker image.")
                return False

            print("Compressing the saved image: %s." %(zipFilename))
            if not executeShellCmd(zipCmd):
                print("ERROR: Failed to compress the docker iamge file.")
                return False

        self.workbench.onecmd("image load --filepath %s --os %s --image-repotag %s %s"
                                %(zippedDestFile, pargs.os, pargs.repotag,
                                  self.command.stringify_roles(pargs.roles)))

        return True

    def complete(self, text, argsList):
        return []

__all__ = ['ImagePackage']
