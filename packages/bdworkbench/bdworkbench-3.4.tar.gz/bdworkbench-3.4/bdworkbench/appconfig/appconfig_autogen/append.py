#
# Copyright (c) 2016 BlueData Software, Inc.
#

from __future__ import print_function



def autogenAppend(autogenCmd, outputLines, autogenDict, entryDict):
    """
    Handle any pattern replacements requested by the user.
    """
    if not autogenDict.has_key('append'):
        return

    #for containerDst, replaceDict in autogenDict['replace'].iteritems():
    appendDict = autogenDict['append']
    for key, valueDict in appendDict.iteritems():
        with autogenCmd.getRoleIfContext(valueDict.get('onroles', None),
                                         outputLines) as ric:
            outputLines.append("%sAPPEND_FILE %s %s \n" %(ric.spaces, key, appendDict[key]))

        outputLines.append("\n")

    return
