#
# Copyright (c) 2016 BlueData Software, Inc.
#

from __future__ import print_function



def autogenReplace(autogenCmd, outputLines, autogenDict, entryDict):
    """
    Handle any pattern replacements requested by the user.
    """
    if not autogenDict.has_key('replace'):
        return

    #for containerDst, replaceDict in autogenDict['replace'].iteritems():
    for pathDict in autogenDict['replace']:
        #print("DEBUG:",containerDst,replaceDict)
        #replaceDict = autogenDict['replace'][containerDst]
        pattern = pathDict['substitute']['pattern']
        containerDst = pathDict['path']
        roles = pathDict.get('onroles', None)
        macro = pathDict['substitute']['macro']

        with autogenCmd.getRoleIfContext(roles, outputLines) as ric:
            outputLines.append("%sREPLACE_PATTERN %s %s %s\n" %(ric.spaces,
                                                                pattern,
                                                                containerDst,
                                                                macro))

        outputLines.append("\n")
    return
