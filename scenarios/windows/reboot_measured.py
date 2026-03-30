# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

##
# Reboot DUT
##

import builtins
import os
import unittest
import logging
import core.app_scenario
import time
from core.parameters import Params


class RebootMeasured(core.app_scenario.Scenario):
	# Don't run any tools with reboot, since processes running on the DUT will be killed when the reboot happens.
	Params.setOverride("global", "prep_tools", "")
	
	# Get parameters
	def runTest(self):              
		logging.info("Rebooting DUT")        
		self._call(["shutdown.exe", "/r /f /t 5"])
		time.sleep(15)
		self._wait_for_dut_comm()
		# Wait for 120s after reboot completes for the scheduled task to minimize windows to run.
		# time.sleep(120)


