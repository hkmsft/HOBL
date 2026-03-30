# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging

def run(scenario):
    logging.debug('Executing code block: code_12MYEMV.py')
    if scenario.platform.lower() == "w365":
        scenario._run_with_inputinject('powershell Move-Item -Path "~\Downloads\MSTeams*" -Destination "' + scenario.dut_data_path + '\MSTeamsLogs"')
    elif scenario.platform.lower() == "windows":
        scenario._call(["powershell.exe", 'Move-Item -Path "~\Downloads\MSTeams*" -Destination "' + scenario.dut_data_path + '\MSTeamsLogs"'])
    else:
        raise AssertionError("Not Implimented")