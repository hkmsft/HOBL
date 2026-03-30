# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging

def run(scenario):
    logging.debug('Executing code block: code_11W5TMU.py')
    try:
        scenario._kill("Resolve.exe")
    except:
        pass
    try:
        scenario._kill("CrashReporter.exe")
    except:
        pass