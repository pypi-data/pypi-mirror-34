#
# Copyright (c) 2018 BlueData Software, Inc.
#
"""Module for building docker image for the current catalog.
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

def restoreDockerFile(originalFile, bkpfile):
    if os.path.exists(bkpfile):
        shutil.move(bkpfile, originalFile)

class ImageBuild(SubCommand):
    """
    Subcommand for building docker image for the catalog
    """
    def __init__(self, config, inmemStore, cmdObj):
        SubCommand.__init__(self, config, inmemStore, cmdObj, 'build')

    def getSubcmdDescripton(self):
        return 'Build a catalog image from a Dockerfile. No additional action is taken.'

    def populateParserArgs(self, subparser):
        subparser.add_argument('-b', '--basedir', metavar='BASEDIR', type=str,
                               required=True, action="store", dest='basedir',
                               help='Directory path where the Dockerfile and '
                                    'related files are located.')
        subparser.add_argument('-i', '--image-repotag', metavar='IMAGE_REPOTAG',
                               type=str, dest='repotag', required=True,
                               help='Container name and tag for the newly built image.'
                               'This is usually of the form '
                               'REGISTRY_HOST[:REGISTRY_PORT]/]REPOSITORY[:TAG]. See'
                               '\'man docker-build\' for more details.')

    def run(self, pargs):
        absBaseDir = os.path.abspath(pargs.basedir)
        if not os.path.exists(absBaseDir):
            print("ERROR: '%s' does not exist." % absBaseDir)
            return False

        delivDict = self.inmemStore.getDict(DELIVERABLE_DICT)

        # Check if the repotag includes the registry url
        registryUrl, repotag = self.command.normalizeImageName(pargs.repotag, delivDict)
        if repotag == None:
            return False

        if doSkipImageRebuild():
            # Skip image rebuilding.
            return True

        # Replace RHEL_USERNAME and RHEL_PASSWORD variables, if any in the docker file.
        dockerfile = os.path.join(absBaseDir, 'Dockerfile')
        bkpDockerfile = dockerfile + '.orig'

        # On exit, restore the bkp file. Register this first incase we crash.
        atexit.register(restoreDockerFile, originalFile=dockerfile, bkpfile=bkpDockerfile)

        # Backup existing docker file and then replace the RHEL username/password
        # variables.
        shutil.copy2(dockerfile, bkpDockerfile)
        with open(dockerfile, 'r+') as f:
            lines = f.readlines()

            replaced = []
            for line in lines:
                replaced.append(line.replace("\${RHEL_USERNAME}", os.getenv(RHEL_USERNAME, "UNSET"))\
                                    .replace("\${RHEL_PASSWORD}", os.getenv(RHEL_PASSWORD, "UNSET"))\
                                    .replace("\$RHEL_USERNAME", os.getenv(RHEL_USERNAME, "UNSET"))\
                                    .replace("\$RHEL_PASSWORD", os.getenv(RHEL_PASSWORD, "UNSET")))

            f.truncate(0)
            f.seek(0)
            f.writelines(replaced)

        buildCmd = "docker build -t %s %s" % (repotag, absBaseDir)
        if not executeShellCmd(buildCmd):
            print("ERROR: Failed to build the image.")
            return False

        return True

    def complete(self, text, argsList):
        return []

__all__ = ['ImageBuild']
