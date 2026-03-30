# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging

def run(scenario):
    logging.debug('Executing code block: code_11RY088.py')

    scenario._call(["cmd.exe", '/C "C:\Program Files\Blackmagic Design\DaVinci Resolve\Resolve.exe"'], blocking=False)