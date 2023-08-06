#
# Copyright (c) 2018 BlueData Software, Inc.
#

"""
Subcommand to \"image\" main command for specifying registry details.
"""

from __future__ import print_function
from .. import SubCommand
from ..inmem_store import ENTRY_DICT, DELIVERABLE_DICT
from ..utils.misc import isRegistryAuthEnabled, isRegistryContentTrustEnabled

class ImageRegistry(SubCommand):
    """
    Subcommand to \"image\" main command for specifying registry details.
    """

    def __init__(self, config, inmemStore, cmdObj):
        SubCommand.__init__(self, config, inmemStore, cmdObj, 'registry')


    def getSubcmdDescripton(self):
        return 'Registry information for the '

    def populateParserArgs(self, subparser):
        subparser.add_argument('--url', dest='registryUrl', type=str,
                               action='store', required=True, default='docker.io',
                               metavar="REGISTRY_HOST[:REGISTRY_PORT]",
                               help='Registry URL and port specification.')
        subparser.add_argument('--auth-enabled', dest='authEnabled', required=False,
                               action='store_true', default=False,
                               help='Specifies that the registry is authenation '
                               'enabled. Please set the environment variables '
                               'AWB_REGISTRY_USERNAME and AWB_REGISTRY_PASSWORD '
                               'before invoking the workbench.')
        subparser.add_argument('--trust', dest="ctEnabled", required=False,
                               action="store_true", default=False,
                               help="Specified that content trust be enabled for "
                               "the docker images. Please set the environment "
                               "variables DOCKER_CONTENT_TRUST_ROOT_PASSPHRASE "
                               "and DOCKER_CONTENT_TRUST_REPOSITORY_PASSPHRASE "
                               "before invoking the workbench.")

    def run(self, pargs):
        if pargs.registryUrl and (' ' in pargs.registryUrl):
            print("ERROR: No space is allowed in the registry url.")
            return False

        if pargs.authEnabled and (not isRegistryAuthEnabled()):
            print("ERROR: The registry is authentation enabled. But the environment "
                  "varaibles AWB_REGISTRY_USERNAME and AWB_REGISTRY_PASSWORD were "
                  "not specified.")
            return False

        if pargs.ctEnabled and (not isRegistryContentTrustEnabled()):
            print("ERROR: Docker is content trust enabled. But the environment "
                  "varaibles DOCKER_CONTENT_TRUST_ROOT_PASSPHRASE and "
                  "DOCKER_CONTENT_TRUST_REPOSITORY_PASSPHRASE were not specified.")
            return False

        registryUrl = pargs.registryUrl.strip()\
                                      .replace('http://', '')\
                                      .replace('https://', '')\
                                      .lower()
        authEnabled = 'true' if pargs.authEnabled else 'false'
        ctEnabled = 'true' if pargs.ctEnabled else 'false'

        entryDict = self.inmemStore.getDict(ENTRY_DICT)
        existingRegistryUrl = None
        if entryDict.has_key("registry"):
            existingRegistry = entryDict["registry"]
            if existingRegistry.has_key("url"):
                existingRegistryUrl = existingRegistry['url']

        if (existingRegistryUrl) and (existingRegistryUrl != registryUrl):
            print("ERROR: A different registry URL was already configured.")
            return False

        # EPIC will just ignore these fields even if they exist unless the
        # catalog api version is set appropriately.
        registryDict = {"url": registryUrl,
                        "content_trust_enabled": ctEnabled,
                        "authentication_enabled": authEnabled}
        self.inmemStore.addField(ENTRY_DICT, "registry", registryDict)

        # There fields are left the same to allow the versioned 'catalog pacakge'
        # command to take care of the correct fields to populate.
        self.inmemStore.addField(DELIVERABLE_DICT, "registryUrl", registryUrl)
        self.inmemStore.addField(DELIVERABLE_DICT, "registryAuthEnabled", authEnabled)
        self.inmemStore.addField(DELIVERABLE_DICT, "contentTrustEnabled", ctEnabled)

        return True

    def complete(self, text, argsList):
        return []


__all__ = ["ImageRegistry"]
