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


class Reboot(core.app_scenario.Scenario):

	module = __module__.split('.')[-1]

	# Set default parameters
	Params.setDefault(module, 'to_uefi', '0')
	
	# Don't run any tools with reboot, since processes running on the DUT will be killed when the reboot happens.
	Params.setOverride("global", "prep_tools", "")

	is_prep = True
	
	def runTest(self):
		# Get parameters
		self.to_uefi = Params.get(self.module, 'to_uefi')
		self._dut_reboot(to_uefi=self.to_uefi == '1')
		              