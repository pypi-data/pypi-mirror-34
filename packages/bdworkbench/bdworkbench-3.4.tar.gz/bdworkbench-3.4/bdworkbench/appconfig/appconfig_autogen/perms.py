#
# Copyright (c) 2016 BlueData Software, Inc.
#

from __future__ import print_function

def autogenPermission(autogenCmd, outputLines, autogenDict, entryDict):
    """
    Set permissions for files or directories as requested by the user.
    """
    if not autogenDict.has_key('perms'):
        return

    for containerDst, permsDict in autogenDict['perms'].iteritems():
        with autogenCmd.getRoleIfContext(permsDict.get('onroles', None),
                                         outputLines) as ric:
            rwx = permsDict['rwx']
            uid = permsDict['uid'] if permsDict.has_key('uid') else None
            gid = permsDict['gid'] if permsDict.has_key('gid') else None

            if rwx:
                outputLines.append("%schmod -v %s %s\n" % (ric.spaces, rwx, containerDst))

            if uid and (not gid):
                outputLines.append("%schown -v %s %s\n" %(ric.spaces, uid, containerDst))

            if uid and gid:
                outputLines.append("%schown -v %s:%s %s\n" %(ric.spaces, uid, gid, containerDst))

        outputLines.append("\n")

    return
