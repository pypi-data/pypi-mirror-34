#!/bin/env python
#
# Copyright (c) 2016 BlueData Software, Inc.

from __future__ import print_function
from .. import Command
from ..constants import *
from ..inmem_store import DELIVERABLE_DICT

from .define_var import DefineVar

import os

class Define(Command):
    """

    """

    def __init__(self, wb, config, inmemStore):
        Command.__init__(self, wb, config, inmemStore, 'define',
                         'Define variables and/or constants')

        DefineVar(config, inmemStore, self)

Command.register(Define)
__all__ = ['Define']
