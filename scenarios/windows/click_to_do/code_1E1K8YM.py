# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging

def run(scenario):
    logging.debug('Executing code block: code_1E1K8YM.py')
    scenario._upload("scenarios\\windows\\click_to_do\\seattle_test.pdf", scenario.dut_exec_path)