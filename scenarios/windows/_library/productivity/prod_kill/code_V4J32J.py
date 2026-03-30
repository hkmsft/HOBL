# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging

def run(scenario):
    logging.debug('Executing code block: code_V4J32J.py')
    
    try:
        logging.debug("Killing Outlook.exe Excel.exe Powerpnt.exe Winword.exe OneNnote.exe")
        scenario._kill("Outlook.exe Excel.exe Powerpnt.exe Winword.exe OneNote.exe")
    except:
        pass
