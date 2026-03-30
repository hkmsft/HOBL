# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging

def run(scenario):
    logging.debug('Executing code block: code_WORDSWT.py - Switch to Microsoft Word')
    
    # Use AppleScript to activate Microsoft Word
    applescript = 'tell application "Microsoft Word" to activate'
    scenario._call(["osascript", "-e", applescript])
