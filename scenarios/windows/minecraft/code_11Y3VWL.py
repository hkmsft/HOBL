# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging

def run(scenario):
    logging.debug('Executing code block: code_11Y3VWL.py')
    
    #try:
    #    scenario._kill("javaw.exe")
    #except:
    #    pass
        
    try:
        scenario._kill("Minecraft.exe")
    except:
        pass