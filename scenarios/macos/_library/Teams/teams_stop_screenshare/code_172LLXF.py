# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging

def run(scenario):
    logging.debug('Executing code block: code_172LLXF.py')
    scenario._call(["killall", '"QuickTime Player"'], expected_exit_code="", timeout=10)