#
# Copyright (c) 2016 BlueData Software, Inc.
#

from __future__ import print_function
from .. import SubCommand
from ..constants import OS_CLASS_DICT, DEFAULT_IMAGE_ROLES
from ..utils.misc import downloadFile
from ..inmem_store import ENTRY_DICT

class ImageDownload(SubCommand):
    """

    """
    def __init__(self, config, inmemStore, cmdObj):
        SubCommand.__init__(self, config, inmemStore, cmdObj, 'download')

    def getSubcmdDescripton(self):
        return 'Download an image file from a HTTP url and add it to the '    \
               'catalog entry.'

    def populateParserArgs(self, subparser):
        subparser.add_argument('-u', '--url', metavar='IMAGE_URL', type=str,
                               required=True, dest='imageurl',
                               help='HTTP URL for downloading the image. The '
                               'file is downloaded to the staging directory.')
        subparser.add_argument('--md5sum', metavar='MD5SUM', type=str,
                               required=True,
                               help='MD5 checksum of the image: used to verify '
                               'the checksum immediatly after downloading.')
        subparser.add_argument('--os', metavar="OS", dest="os", required=True,
                               choices=OS_CLASS_DICT.keys(), action='store',
                               help="The OS distribution of the container image.")
        subparser.add_argument('--roles', metavar="ROLE(S)", dest="roles",  nargs='+',
                                 required=False, default=DEFAULT_IMAGE_ROLES,
                                 help="Assign the image to a specific ROLE or ROLES. "
                                 "If specified the image is used for the roles "
                                 "when deploying a cluster on EPIC.")

    def run(self, pargs):
        localfile = downloadFile(pargs.imageurl, pargs.md5sum, self.config)
        if localfile == None:
            return False

        return self.workbench.onecmd("image load --filepath %s --md5sum %s --os %s %s" %
                                            (localfile, pargs.md5sum, pargs.os,
                                             self.command.stringify_roles(pargs.roles)))

    def complete(self, text, argsList):
        return []
