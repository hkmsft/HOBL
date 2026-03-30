# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging
import time

def run(scenario):
    logging.debug('Executing code block: code_X8JJAP.py')
    try:
        scenario._kill("Minecraft.Windows.exe")
    except:
        pass
        