# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging

def run(scenario):
    logging.debug('Executing code block: code_172HC3J.py')
    #kill teams process

    scenario._call(["bash", "-c \"pkill -i Teams\""])
    