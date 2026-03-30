# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging
import core.app_scenario
import time
from core.parameters import Params
import sys
import shutil


class CollectLogs(core.app_scenario.Scenario):
    '''
    Collect various system logs.
    '''
    logging.info("Beginning collect logs test scenario.")
    module = __module__.split('.')[-1]

    is_prep = True

    def runTest(self):
        # cmd = "(Get-Date) - (New-TimeSpan -Day 3)"
        # self._call(["powershell.exe", "Get-WinEvent | Where-Object { $_.TimeCreated -ge " + cmd + " } | Out-File -FilePath " + self.dut_data_path + "\\event_log"])

        # Sleepstudy failes when using powershell on ARM devices.  Using CMD instead.
        # self._call(["powershell.exe", "powercfg.exe /SLEEPSTUDY /VERBOSE /DURATION 14 /OUTPUT " + self.dut_data_path + "\\sleepstudy.xml /XML"])
        # self._call(["powershell.exe", "powercfg.exe /BATTERYREPORT /DURATION 14 /OUTPUT " + self.dut_data_path + "\\batteryreport.xml /XML"])
        self._call(["cmd.exe", "/C powercfg.exe /SLEEPSTUDY /VERBOSE /DURATION 5 /OUTPUT " + self.dut_data_path + "\\sleepstudy_verbose.xml /XML"], blocking = True, fail_on_exception=False, expected_exit_code="")
        self._call(["cmd.exe", "/C powercfg.exe /BATTERYREPORT /DURATION 5 /OUTPUT " + self.dut_data_path + "\\batteryreport.xml /XML"], blocking = True, fail_on_exception=False, expected_exit_code="")
        self._call(["cmd.exe", "/C powercfg.exe /SLEEPSTUDY /VERBOSE /DURATION 5 /OUTPUT " + self.dut_data_path + "\\sleepstudy_verbose.html"], blocking = True, fail_on_exception=False, expected_exit_code="")
        self._call(["cmd.exe", "/C powercfg.exe /BATTERYREPORT /DURATION 5 /OUTPUT " + self.dut_data_path + "\\batteryreport.html"], blocking = True, fail_on_exception=False, expected_exit_code="")
        
        self._call(["cmd.exe", "/C xcopy C:\\Windows\\Minidump\\*.* " + self.dut_data_path], expected_exit_code="")
        
        self._call(["cmd.exe", "/C netsh wlan sh wlanreport duration=\"14\""], blocking = True, fail_on_exception=False, expected_exit_code="")
        self._call(["cmd.exe", "/C xcopy C:\\ProgramData\\Microsoft\\Windows\\WlanReport\\wlan-report-latest.html " + self.dut_data_path], blocking = True, fail_on_exception=False, expected_exit_code="")
        self._call(["cmd.exe", "/C netsh wlan sh i >> " + self.dut_data_path + "\\wlan_status.txt"], blocking = True, fail_on_exception=False, expected_exit_code="")
        logging.debug("Gathering system event logs")
        self._call(["cmd.exe", "/C wevtutil epl System " + self.dut_data_path + "\\System_Event_Log.evtx"], blocking = True, fail_on_exception=False, expected_exit_code="")
        self._call(["cmd.exe", "/C wevtutil epl Application " + self.dut_data_path + "\\Application_Event_Log.evtx"], blocking = True, fail_on_exception=False, expected_exit_code="")
        self._call(["cmd.exe", "/C wevtutil epl HardwareEvents " + self.dut_data_path + "\\HardwareEvents_Event_Log.evtx"], blocking = True, fail_on_exception=False, expected_exit_code="")
        self._call(["cmd.exe", "/C wevtutil epl OAlerts " + self.dut_data_path + "\\Office_Alerts_Event_Log.evtx"], blocking = True, fail_on_exception=False, expected_exit_code="")
        logging.debug("Getting system Powershell logs")
        self._call(["cmd.exe", "/C wevtutil epl \"Windows Powershell\" " + self.dut_data_path + "\\Windows_Powershell.evtx"], blocking = True, fail_on_exception=False, expected_exit_code="")
        self._call(["cmd.exe", "/C wevtutil epl \"Microsoft-Windows-WLAN-AutoConfig/Operational\" " + self.dut_data_path + "\\Microsoft-Windows-WLAN-AutoConfig-Operational.evtx"], blocking = True, fail_on_exception=False, expected_exit_code="")
        self._call(["cmd.exe", "/C wevtutil epl \"Microsoft-Windows-WWAN-CFE/Diagnostic\" " + self.dut_data_path + "\\Microsoft-Windows-WWAN-CFE-Diagnostic.evtx"], blocking = True, fail_on_exception=False, expected_exit_code="")
        self._call(["cmd.exe", "/C wevtutil epl \"Microsoft-Windows-WWAN-MM-Events/Diagnostic\" " + self.dut_data_path + "\\Microsoft-Windows-WWAN-MM-Events-Diagnostic.evtx"], blocking = True, fail_on_exception=False, expected_exit_code="")
        self._call(["cmd.exe", "/C wevtutil epl \"Microsoft-Windows-WWAN-MediaManager/Diagnostic\" " + self.dut_data_path + "\\Microsoft-Windows-WWAN-MediaManager-Diagnostic.evtx"], blocking = True, fail_on_exception=False, expected_exit_code="")
        self._call(["cmd.exe", "/C wevtutil epl \"Microsoft-Windows-WWAN-NDISUIO-EVENTS/Diagnostic\" " + self.dut_data_path + "\\Microsoft-Windows-WWAN-NDISUIO-EVENTS-Diagnostic.evtx"], blocking = True, fail_on_exception=False, expected_exit_code="")
        self._call(["cmd.exe", "/C wevtutil epl \"Microsoft-Windows-WWAN-SVC-Events/Diagnostic\" " + self.dut_data_path + "\\Microsoft-Windows-WWAN-SVC-Events-Diagnostic.evtx"], blocking = True, fail_on_exception=False, expected_exit_code="")
        self._call(["cmd.exe", "/C wevtutil epl \"Microsoft-Windows-WWAN-SVC-Events/Operational\" " + self.dut_data_path + "\\Microsoft-Windows-WWAN-SVC-Events-Operational.evtx"], blocking = True, fail_on_exception=False, expected_exit_code="")
        self._call(["cmd.exe", "/C xcopy C:\\Windows\\System32\\LogFiles\\WMI\\Wifi.etl " + self.dut_data_path], blocking = True, fail_on_exception=False, expected_exit_code="")
        self._call(["cmd.exe", "/C bcdedit >> " + self.dut_data_path + "\\bcdedit.txt"], blocking = True, fail_on_exception=False, expected_exit_code="")
        

        
        