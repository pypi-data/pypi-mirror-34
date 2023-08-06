#
# Copyright (c) 2016 BlueData Software, Inc.
#

from __future__ import print_function
from .. import SubCommand
from ..constants import *
from ..utils import executeShellCmd
from ..utils.misc import calculateMD5SUM
from ..inmem_store import ENTRY_DICT, DELIVERABLE_DICT

import os
import subprocess

DOCKER_LOGIN_CMD_FMT = "docker login -u '%(username)s' -p '%(password)s' %(email)s %(registryurl)s"

class ImagePush(SubCommand):
    """

    """
    def __init__(self, config, inmemStore, cmdObj):
        SubCommand.__init__(self, config, inmemStore, cmdObj, 'push')

    def getSubcmdDescripton(self):
        return 'Push a docker image to a registry and refer to it in the catalog entry metadata.'


    def populateParserArgs(self, subparser):
        subparser.add_argument('-i', '--image-repotag', metavar='IMAGE_REPOTAG',
                               type=str, dest='repotag', required=True,
                               help='Container name and tag to be pushed to the '
                               'registry. This is usually of the form '
                               'REGISTRY_HOST[:REGISTRY_PORT]/]REPOSITORY[:TAG]. See'
                               '\'man docker-push\' for more details.')
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
        deliveryDict = self.inmemStore.getDict(DELIVERABLE_DICT)

        registryUrl, newRepoTag = self.command.normalizeImageName(pargs.repotag,
                                                                  deliveryDict)
        with self.command.getDockerLoginContext(deliveryDict["built_on_docker"],
                                                 registryUrl, pargs) as dlc:
            # It is possible these were specified on the command line. So make
            # sure the environment is updated before we run the docker push cmd
            if dlc.ctRoot != None:
                os.environ[DOCKER_CONTENT_TRUST_ROOT_PASSPHRASE] = dlc.ctRoot

            if dlc.ctRegistry != None:
                os.environ[DOCKER_CONTENT_TRUST_REPOSITORY_PASSPHRASE] = dlc.ctRegistry

            if dlc.ctRoot:
                contentTrustOption = "--trust"
            else:
                contentTrustOption = ""

            pushCmd = "docker push %s %s" %(contentTrustOption, pargs.repotag)
            if not executeShellCmd(pushCmd):
                print("ERROR: Failed to push container image to registry.")
                return False

        self.workbench.onecmd("image load --os %s --image-repotag %s %s"
                                %(pargs.os, newRepoTag,
                                  self.command.stringify_roles(pargs.roles)))

        return True

    def complete(self, text, argsList):
        return []


__all__ = ['ImagePush']
