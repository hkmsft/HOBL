# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging
import time

def run(scenario):
    logging.debug('Executing code block: code_12AE9PC.py')
    
    try:
        scenario._kill("java")
    except:
        pass
    time.sleep(5)
    try:
        scenario._kill("launcher")
    except:
        pass