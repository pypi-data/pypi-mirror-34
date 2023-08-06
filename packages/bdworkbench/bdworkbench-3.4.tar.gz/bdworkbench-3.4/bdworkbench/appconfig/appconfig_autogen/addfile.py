# Copyright (c) 2016 BlueData Software, Inc.
#

from __future__ import print_function

import os
import shutil

def autogenAddfile(autogenCmd, outputLines, packagePath, autogenDict, entryDict):
    """
    Populate the appconfig package with any files the user added
    """
    if not autogenDict.has_key('addfile'):
        return

    for pkgFile, addfileDict in autogenDict['addfile'].iteritems():
        destFile = addfileDict['dstfile']

        if addfileDict['dstdir'] != None:
            dstDir = addfileDict['dstdir']
            containerDst = os.path.join(addfileDict['dstdir'], pkgFile)
        elif addfileDict['dstfile'] != None:
            dstfile = addfileDict['dstfile']
            dstDir = os.path.dirname(dstfile)
            containerDst = dstfile

        with autogenCmd.getRoleIfContext(addfileDict.get('onroles', None),
                                         outputLines) as ric:
            outputLines.append("%s[ ! -d '%s' ] && mkdir -vp %s\n" %
                                (ric.spaces, dstDir, dstDir))
            outputLines.append("%scp -rvf ${CONFIG_BASE_DIR}/%s %s\n" %
                                (ric.spaces, pkgFile, containerDst))

        outputLines.append("\n")

    return
