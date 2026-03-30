# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

##
# Perf gate prep that will enable energy recommendations
#   
##


from core.parameters import Params
from core.app_scenario import Scenario
import core.app_scenario
import logging
import os
import time

class EnergyRecom(core.app_scenario.Scenario):
    module = __module__.split('.')[-1]
    Params.setDefault('module', 'source_path', '..\\ScenarioAssets\\ERTestApp\\')

    source_path = Params.get('module', 'source_path')
    dut_architecture = Params.get('global', 'dut_architecture')
    

    
    # Params.setOverride("global", "collection_enabled", "0")
    Params.setOverride("global", "prep_tools", "")
    is_prep = True


    def runTest(self):
        
        if self.dut_architecture == "arm64":
            logging.info("Moving ERTestApp for arm64 to DUT")
            if not self._check_remote_file_exists("ERTestApp.exe", in_exec_path=True, target_ip=None):
                self._upload(self.source_path + "\\arm64\\ERTestApp.exe", self.dut_exec_path)
        else:
            logging.info("Moving ERTestApp for arm64 to DUT")
            if not self._check_remote_file_exists("ERTestApp.exe", in_exec_path=True, target_ip=None):
                self._upload(self.source_path + "\\amd64\\ERTestApp.exe", self.dut_exec_path)
        
        time.sleep(5)

        logging.info("Enabling energy recommendation for device")
        self._call([os.path.join(self.dut_exec_path, "ERTestApp.exe"), "PowerMode,ScreenSaver,Brightness,CABC,DarkTheme,DynamicRefresh,ReduceRefreshRate"], 
        blocking=True, timeout=172800, expected_exit_code="")


    def tearDown(self):
        core.app_scenario.Scenario.tearDown(self)

       
