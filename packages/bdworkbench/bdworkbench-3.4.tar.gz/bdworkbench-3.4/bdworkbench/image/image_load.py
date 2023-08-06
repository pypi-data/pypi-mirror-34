#
# Copyright (c) 2016 BlueData Software, Inc.
#

from __future__ import print_function
from .. import SubCommand
from ..utils.misc import calculateMD5SUM
from ..inmem_store import ENTRY_DICT, DELIVERABLE_DICT
from ..constants import OS_CLASS_DICT, DEFAULT_IMAGE_ROLES
from ..constants import IMAGE_REGISTRY_SUPPORT, IMAGE_PER_ROLE_SUPPORT

import os
import copy

class ImageLoad(SubCommand):
    """

    """
    def __init__(self, config, inmemStore, cmdObj):
        SubCommand.__init__(self, config, inmemStore, cmdObj, 'load')

    def getSubcmdDescripton(self):
        return 'Load an image '

    def populateParserArgs(self, subparser):
        subparser.add_argument('--os', metavar="OS", dest="os", required=True,
                               choices=OS_CLASS_DICT.keys(), action='store',
                               help="The OS distribution of the container image.")
        subparser.add_argument('--roles', metavar="ROLE(S)", dest="roles", nargs='+',
                                required=False, default=DEFAULT_IMAGE_ROLES,
                                help="Assign the image to a specific ROLE or ROLES. "
                                "If specified the image is used for the roles "
                                "when deploying a cluster on EPIC. Only supported"
                                "when catalog_api_version >= " + IMAGE_PER_ROLE_SUPPORT)
        subparser.add_argument('-i', '--image-repotag', metavar='IMAGE_REPOTAG',
                                type=str, dest='repotag', required=True,
                                help='Container name and tag to save in the '
                                'metadata. This is usually of the form '
                                'REGISTRY_HOST[:REGISTRY_PORT]/]REPOSITORY[:TAG]. '
                                'See \'man docker-pull\' for more details.')

        localfileGroup = subparser.add_argument_group('Options for adding a local file')
        localfileGroup.add_argument('-f', '--filepath', metavar='FILEPATH',
                                    type=str, dest='filepath', default=None,
                                    help='File path to the container image on the '
                                    'local filesystem.')
        localfileGroup.add_argument('--md5sum', metavar='MD5SUM', type=str,
                                    dest='md5sum', default=None,
                                    help='MD5 checksum of the appconfig package. If '
                                    'this is not specified, checksum for the '
                                    'file is calculated.')

    def run(self, pargs):
        entryDict = self.inmemStore.getDict(ENTRY_DICT)
        if entryDict.has_key('catalog_api_version'):
            catalog_api_version = entryDict['catalog_api_version']
            if (int(catalog_api_version) < int (IMAGE_PER_ROLE_SUPPORT)) and   \
                    (pargs.roles != DEFAULT_IMAGE_ROLES and                    \
                        DEFAULT_IMAGE_ROLES not in pargs.roles):
                print("ERROR: Image per role is not supported for catalog_api_version ",
                        catalog_api_version)
                return False
        else:
            print("ERROR: Unknown catalog_api_version. Please use either "
                  "'catalog load' or 'catalog new' to define it.")
            return False

        if entryDict.has_key('node_roles'):
            existing_roles = entryDict['node_roles']
        else:
            print("ERROR: No roles are defined yet. You may use either "
                  "'role add' or 'catalog load' commands. The later assumes "
                  "you have a fully populated entry json file.")
            return False

        if (not pargs.filepath) and (not pargs.repotag):
            print("ERROR: Either Local file or registry image must be specified.")
            return False

        if pargs.filepath:
            if not os.path.exists(pargs.filepath):
                print("ERROR: '%s' does not exist." % pargs.filepath)
                return False

            if not os.path.isfile(pargs.filepath):
                print("ERROR: '%s' is not a regular file." % pargs.filepath)
                return False

            # FIXME! Validate the following:
            #         1. The file is actually a compressed archive.
            #         2. The compressed archive has a 'repositories' directory.

            filename = os.path.basename(pargs.filepath)
            absFilename = os.path.abspath(pargs.filepath)
            checksum = pargs.md5sum if (pargs.md5sum != None) else calculateMD5SUM(absFilename)
        else:
            filename = None
            absFilename = None
            checksum = None

        imageOS = OS_CLASS_DICT[pargs.os][0]
        imageOSMajor = OS_CLASS_DICT[pargs.os][1]
        delivDict = self.inmemStore.getDict(DELIVERABLE_DICT)
        if pargs.repotag:
            registryUrl, repotag = self.command.normalizeImageName(pargs.repotag, delivDict)
            if repotag == None:
                # Something went wrong. Log message was already printed.
                return False
        else:
            repotag = None

        if int(catalog_api_version) < int(IMAGE_REGISTRY_SUPPORT):
            if delivDict.has_key('registryUrl'):
                print("ERROR: Registry import is unsupported for catalog_api_version ",
                        catalog_api_version)
                return False

        existingImages = delivDict['images']
        if len(existingImages) > 0:
            for image in existingImages:
                for role in image.get("imageRoles", []):
                    # FIXME! This check enforces one catalog bundle per WB file.
                    # We can no longer build a rhel and centos version of the
                    # same catalog entry with a single WB file.
                    if (role != DEFAULT_IMAGE_ROLES) and (role in pargs.roles):
                        print("ERROR: An image for the role (%s) already exists." % pargs.role)
                        return False

        ImageDict = {"imageOS"      : imageOS,
                     "imageOSMajor" : imageOSMajor,
                     "imageRepotag" : repotag,
                     "imageFile"    : absFilename,
                     "imageChecksum": checksum,
                     "imageRoles"   : pargs.roles
                    }
        self.inmemStore.appendValue(DELIVERABLE_DICT, "images", ImageDict)

        # Populate the entry JSON
        if int(catalog_api_version) >=  int(IMAGE_PER_ROLE_SUPPORT):
            process_role_ids = []
            if pargs.roles == DEFAULT_IMAGE_ROLES:
                for e_role in existing_roles:
                    process_role_ids.append(e_role['id'])
            else:
                process_role_ids = pargs.roles

            for e_role in existing_roles:
                for p_role_id in process_role_ids:
                    if e_role['id'] == p_role_id:
                        roleImageDict = {"source_file" : filename,
                                         "checksum"    : checksum,
                                         "imageOS"     : imageOS,
                                         "imageOSMajor": imageOSMajor,
                                         "imageRepotag": repotag
                                        }

                        e_role['image'] = roleImageDict
        else:
            self.inmemStore.addField(ENTRY_DICT, "image", {"source_file": filename,
                                                           "checksum": checksum})

        return True

    def complete(self, text, argsList):
        return []


__all__ = ['ImageAdd']
