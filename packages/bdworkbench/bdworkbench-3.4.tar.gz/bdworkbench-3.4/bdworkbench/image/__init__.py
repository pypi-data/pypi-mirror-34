#!/bin/env python
#
# Copyright (c) 2016 BlueData Software, Inc.

from __future__ import print_function
from .. import Command
from ..constants import *
from ..inmem_store import ENTRY_DICT, DELIVERABLE_DICT
from ..utils import executeShellCmd
from ..utils.misc import constructDistroId
from ..utils.misc import isRegistryAuthEnabled, isRegistryContentTrustEnabled

from .image_load import ImageLoad
from .image_list import ImageList
from .image_pull import ImagePull
from .image_push import ImagePush
from .image_build import ImageBuild
from .image_package import ImagePackage
from .image_download import ImageDownload
from .image_registry import ImageRegistry

import os

DOCKER_LOGIN_CMD_FMT = "docker login -u '%(username)s' -p '%(password)s' %(email)s %(registryurl)s"

class Image(Command):
    """

    """

    class DockerLoginContext(object):
        """

        """

        def __init__(self, builtOnDocker, registryUrl, pargs):
            self.registryUrl = '' if registryUrl in ['docker.io', 'default'] else registryUrl
            self.emailString = "-e 'default@default.com'" if (builtOnDocker == "1.7") else ''

            self.username = pargs.username if pargs.username else              \
                                os.getenv(AWB_REGISTRY_USERNAME, None)
            self.password = pargs.password if pargs.password else              \
                                os.getenv(AWB_REGISTRY_PASSWORD, None)
            self.authEnabled = (self.username and self.password)

            self.ctRoot = pargs.ctroot if pargs.ctroot else                         \
                                os.getenv(DOCKER_CONTENT_TRUST_ROOT_PASSPHRASE, None)
            self.ctRegistry = pargs.ctregistry if pargs.ctregistry  else            \
                                os.getenv(DOCKER_CONTENT_TRUST_REPOSITORY_PASSPHRASE, None)
            self.contentTrustEnabled = (self.ctRoot and self.ctRegistry)

        def __enter__(self):
            if (not self.authEnabled) or (self.registryUrl == None):
                return self

            loginCmd = DOCKER_LOGIN_CMD_FMT % {'username'    : self.username,
                                               'password'    : self.password,
                                               'email'       : self.emailString,
                                               'registryurl' : self.registryUrl}
            altLoginCmd = DOCKER_LOGIN_CMD_FMT % {'username'    : self.username,
                                                  'password'    : "<<hidden>>",
                                                  'email'       : self.emailString,
                                                  'registryurl' : self.registryUrl}
            # Login
            if not executeShellCmd(loginCmd, alternateStr=altLoginCmd):
                print ("ERROR: Failed to login to registry")
                return False

            return self

        def __exit__(self, _type, _value, _traceback):
            if (not self.authEnabled) or (self.registryUrl == None):
                return

            logoutCmd = "docker logout %s" % (self.registryUrl)
            executeShellCmd(logoutCmd)

    def __init__(self, wb, config, inmemStore):
        Command.__init__(self, wb, config, inmemStore, 'image',
                         'Container image management for the catalog entry.')

        ## Initialize the subcommands.
        ImageLoad(config, inmemStore, self)
        ImageList(config, inmemStore, self)
        ImagePull(config, inmemStore, self)
        ImagePush(config, inmemStore, self)
        ImageBuild(config, inmemStore, self)
        ImagePackage(config, inmemStore, self)
        ImageDownload(config, inmemStore, self)
        ImageRegistry(config, inmemStore, self)

    def getDockerLoginContext(self, builtOnDocker, registryUrl, pargs):
        return Image.DockerLoginContext(builtOnDocker, registryUrl, pargs)

    def addAuthAndCTArgs(self, subparser):
        """
        """
        authGroup = subparser.add_argument_group('For authentication-enabled registry.')
        authGroup.add_argument('-u', '--username', metavar='USERNAME', type=str,
                                dest='username', default=None, required=False,
                                help='Specify the username for pushing the image '
                                'to an authentication-enabled registry. You may'
                                'also set the environment variable AWB_REGISTRY_USERNAME.')
        authGroup.add_argument('-p', '--password', metavar='PASSWORD', type=str,
                                dest='password', default=None, required=False,
                                help='Specify the password for pushing to an '
                                'authentication-enabled registry. You may also set '
                                'the environment variable AWB_REGISTRY_PASSWORD.')

        ctGroup = subparser.add_argument_group('For content trust enabled registry.')
        ctGroup.add_argument('-o', '--ct-root-passphrase', metavar='PASSPHRASE',
                             type=str, dest='ctroot', required=False, default=None,
                             help='Specify the content trust root passphrase if'
                             'content trust is enabled for the repository. You may'
                             'also set the environment variable DOCKER_CONTENT_TRUST_ROOT_PASSPHRASE')
        ctGroup.add_argument('-r', '--ct-registry-passphrase', metavar='PASSPHRASE',
                             type=str, dest='ctregistry', required=False, default=None,
                             help='Specify the content trust repository passphrase if'
                             'content trust is enabled for the repository. You may'
                             'also set the environment variable DOCKER_CONTENT_TRUST_REPOSITORY_PASSPHRASE')

    def stringify_roles(self, roles):
        """
        """
        return "--roles %s" %(' '.join(roles)) if roles != DEFAULT_IMAGE_ROLES else ''

    def normalizeImageName(self, inputRepoTag, delivDict):
        """""
        Ensures that the image name contains the registry info if a registry is
        configured at all. If the repository is specified in the names, this
        function extracts that info and records it in the metadata.
        """
        usableInputRepoTag = inputRepoTag.strip()\
                                         .replace('http://', '')\
                                         .replace('https://', '')\
                                         .lower()
        repotagSplits = usableInputRepoTag.split('/')
        if len(repotagSplits) > 2:
            registryUrl = repotagSplits[0]
            if delivDict.has_key('registryUrl'):
                if registryUrl != delivDict['registryUrl']:
                    print("ERROR: Registry URL specified along with the image "
                          "differs from that specified with 'image registry' command.")
                    return (None, None)
            else:
                # Assuming the appropriate environment varaibles are set. Or that
                # the 'image registry' command was already executed.
                authEnabled = isRegistryAuthEnabled() or\
                                (delivDict.has_key('registryAuthEnabled') and\
                                                delivDict['registryAuthEnabled'])
                ctEnabled = isRegistryContentTrustEnabled() or\
                                (delivDict.has_key('contentTrustEnabled') and\
                                                delivdict('contentTrustEnabled'))

                # Invoke the 'image registry' command and let it figure out where
                # these params needs to be set.
                registryCmd = "image registry --url %s" %(registryUrl)
                if authEnabled:
                    registryCmd = "%s --auth-enabled" %(registryCmd)

                if ctEnabled:
                    registryCmd = "%s --trust" %(registryCmd)

                self.workbench.onecmd(registryCmd)

            repotag = '/'.join([registryUrl, repotagSplits[1], repotagSplits[2]])
        else:
            # Even though we allow distro_id and image-repotag to be different,
            # rules for naming them are exactly the same.
            distroid = constructDistroId(self.inmemStore, self.config, inputRepoTag)
            if distroid == None:
                raise Exception("Builder's organiation name not set.")

            if delivDict.has_key("registryUrl"):
                repotag = '/'.join([delivDict["registryUrl"], distroid])
                registryUrl = delivDict["registryUrl"]
            else:
                repotag = distroid
                registryUrl = None

        return (registryUrl, repotag)

Command.register(Image)
__all__ = ['Image', 'DockerLoginContext']
