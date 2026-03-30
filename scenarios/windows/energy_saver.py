# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

##
# Perf gate prep that will turn on or turn off energy saver. Default is 0. 
#   
##


from core.parameters import Params
from core.app_scenario import Scenario
import core.app_scenario
import logging
import time

class EnergySaver(core.app_scenario.Scenario):
    module = __module__.split('.')[-1]
    Params.setDefault(module, 'state', '0')


    state = Params.get(module, 'state')

    
    # Params.setOverride("global", "collection_enabled", "0")
    Params.setOverride("global", "prep_tools", "")
    is_prep = True


    def runTest(self):

        # Enable/Disable energy saver
        if self.state == "1":
            self._call(["cmd.exe", '/C reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Power /v EnergySaverState /t REG_DWORD /d 1 /f > null 2>&1'])
        if self.state == "0":
            self._call(["cmd.exe", '/C reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Power /v EnergySaverState /t REG_DWORD /d 0 /f > null 2>&1'])

        time.sleep(5)

        rebootDut(self, self)
        logging.info("energy_saver complete")

        logging.info("Delaying 5 min or reboot tasks to complete.")
        time.sleep(300)

    def tearDown(self):
        core.app_scenario.Scenario.tearDown(self)

       
def rebootDut(self, scenario):
    logging.info("Rebooting DUT")
    try:
        scenario._call(["cmd.exe",  "/C shutdown.exe /r /f /t 5"])
    except:
        pass
    time.sleep(20)
    scenario._wait_for_dut_comm()
    logging.info("Reboot complete")
    return


