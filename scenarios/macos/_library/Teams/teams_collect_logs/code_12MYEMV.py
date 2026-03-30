# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging

def run(scenario):
    logging.debug('Executing code block: code_12MYEMV.py')
    # scenario._call(["mv", "-f ~/Downloads/*MSTeams* " + scenario.dut_data_path + "/MSTeamsLogs"])
    scenario._call(["bash", "-c \"mv -f ~/Downloads/*MSTeams* '" + scenario.dut_data_path + "/MSTeamsLogs'\""])