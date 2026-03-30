# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

# Scenario for running version report on Surface devices

import builtins
import logging
import core.app_scenario
from core.parameters import Params
import os
import json
from datetime import datetime
import shutil
import getpass

class VersionReport(core.app_scenario.Scenario):
    module = __module__.split('.')[-1]

    # Set default parameters
    Params.setOverride("global", "trace", "0")
    Params.setOverride("global", "config_check", "0")
    Params.setOverride("global", "callback_test_begin", "")
    Params.setOverride("global", "callback_test_end", "")
    Params.setOverride("global", "callback_data_ready", "")
    Params.setOverride("global", "prep_tools", "")

    local_execution = Params.get('global', 'local_execution')

    is_prep = True

    def runTest(self):
        dut_data_path = Params.getCalculated("dut_data_path")
        dut_architecture = Params.get('global', 'dut_architecture')
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
        logging.info("Date-Time: " + timestamp)
        log_path = dut_data_path + "\\versionreport_" + timestamp + ".log"

        version_report_tool = 'c:\\tools\\versionreport\\versionreport.cmd'
        # Check if c:\tools\versionreport\versionreport.cmd exists
        if self._check_remote_file_exists(version_report_tool):
            version_report_tool = "C:\\Tools\\Versionreport\\VersionReport.cmd -Logfile " + log_path
            self._call(["cmd.exe", "/C " + version_report_tool], fail_on_exception=False)   

        else:
            version_report_tool = "C:\\Tools\\VersionReport.cmd -Logfile " + log_path
            try:
                self._call(["cmd.exe", "/C " + version_report_tool], fail_on_exception=False)   
            except:
                logging.info("Version report had errors")
                        
        log_file = dut_data_path + "\\WindowsUpdateLog.log"
        logging.info("Log File Path: " + log_file)
        self._call(["powershell.exe", "Get-WindowsUpdateLog -LogPath " + log_file], expected_exit_code="", fail_on_exception=False)    
        self._call(["cmd.exe", "/c copy c:\\Windows\\INF\\setupapi.setup.log " + dut_data_path], expected_exit_code="")    
        self._call(["cmd.exe", "/c copy c:\\Windows\\INF\\setupapi.dev.log " + dut_data_path], expected_exit_code="")    
        self._call(["cmd.exe", "/c copy c:\\Windows\\INF\\setupapi.offline.log " + dut_data_path], expected_exit_code="")
        self._call(["powershell.exe", r"get-pnpdevice -presentonly | where-object {$_.Instanceid -match '^USB'} | format-table -autosize > c:\hobl_data\usb_devices.txt"], expected_exit_code="", fail_on_exception=False)    

        try:
            self._call(["cmd.exe", "/c copy c:\\tools\\ple\\TOAST\\verifyversions\\results_driver*.html " + dut_data_path], expected_exit_code="")
        except:
            pass
                
         