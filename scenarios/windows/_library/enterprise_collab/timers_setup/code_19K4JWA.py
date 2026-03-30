# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging

def run(scenario):
    logging.debug('Executing code block: code_19K4JWA.py')
    logging.info('Uploading timers at '+scenario.dut_exec_path)
    scenario._upload("utilities\\open_source\\SimpleTimer\\windows\\bin\\SimpleTimer.exe", scenario.dut_exec_path)