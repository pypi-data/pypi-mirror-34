#
# Copyright (c) 2016 BlueData Software, Inc.
#

from __future__ import print_function
import os



def autogenExecute(autogenCmd, outputLines, autogenDict, entryDict):
    """
    Handle any pattern replacements requested by the user.
    """
    if not autogenDict.has_key('execute'):
        return

    for roles, script in autogenDict['execute']:
        scriptPath = script if os.path.isabs(script) else os.path.join("${CONFIG_BASE_DIR}", script)

        with autogenCmd.getRoleIfContext(roles, outputLines) as ric:
            outputLines.append("%sbash %s || exit 2\n" %(ric.spaces, scriptPath))

        outputLines.append("\n")

    return
