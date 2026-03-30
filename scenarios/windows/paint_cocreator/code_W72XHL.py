# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging

def run(scenario):
    logging.debug('Executing code block: code_W72XHL.py')
    try:
        scenario._kill("mspaint.exe")
    except:
        pass