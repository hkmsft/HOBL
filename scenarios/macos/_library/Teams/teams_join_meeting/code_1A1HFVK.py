# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging

def run(scenario):
    logging.debug('Executing code block: code_1A1HFVK.py')
    logging.error("Teams Security Pop Up Detected. Go to Mac Settings -> Privacy & Security -> Screen & System Audio Recording and allow Microsoft Teams")
    scenario.fail("Teams Security Pop Up Detected. Go to Mac Settings -> Privacy & Security -> Screen & System Audio Recording and allow Microsoft Teams")