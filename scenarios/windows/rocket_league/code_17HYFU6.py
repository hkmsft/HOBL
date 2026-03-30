# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging

def run(scenario):
    logging.debug('Executing code block: code_17HYFU6.py')

    try:
        scenario._kill("RocketLeague.exe")
    except:
        pass

    scenario._sleep_to_now()
