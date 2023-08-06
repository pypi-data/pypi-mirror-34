#
# Copyright (c) 2017 BlueData Software, Inc.
#

from __future__ import print_function
import os



def autogenSourceFile(autogenCmd, outputLines, autogenDict):
    """
    Add an line that sources the give file.
    """
    if not autogenDict.has_key('sourcefiles'):
        return

    for roles, script in autogenDict['sourcefiles']:
        scriptPath = script if os.path.isabs(script) else os.path.join("${CONFIG_BASE_DIR}", script)

        with autogenCmd.getRoleIfContext(roles, outputLines) as ric:
            outputLines.append("%ssource %s || exit 1\n" %(ric.spaces, scriptPath))

        outputLines.append("\n")
    return
