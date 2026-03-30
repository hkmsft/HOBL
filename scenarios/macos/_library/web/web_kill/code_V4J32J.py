# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging
import time

def run(scenario):
    logging.debug('Executing code block: code_V4J32J.py')
    
    try:
        scenario._kill("Safari")
    except:
        pass
        
    time.sleep(3)

    scenario._web_replay_kill()
