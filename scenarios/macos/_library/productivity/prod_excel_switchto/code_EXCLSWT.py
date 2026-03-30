# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging

def run(scenario):
    logging.debug('Executing code block: code_EXCLSWT.py - Switch to Microsoft Excel')
    
    # Use AppleScript to activate Microsoft Excel
    applescript = 'tell application "Microsoft Excel" to activate'
    scenario._call(["osascript", "-e", applescript])
