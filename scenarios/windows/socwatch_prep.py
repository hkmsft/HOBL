# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

##
# Prepare the Idle App Test
#
# Setup instructions:
##

import builtins
import os
import logging
import core.app_scenario
from core.parameters import Params

class SocwatchPrep(core.app_scenario.Scenario):
    module = __module__.split('.')[-1]
    # Set default parameters
    Params.setDefault(module, 'host_path', "c:\\socwatch")

    # Get parameters
    host_path = Params.get(module, 'host_path')

    # Override collection of config data, traces, and execution of callbacks 
    # Params.setOverride("global", "collection_enabled", "0")

    is_prep = True

    def runTest(self):
        # Copy over resource folders
        self._upload(self.host_path, self.dut_exec_path)



