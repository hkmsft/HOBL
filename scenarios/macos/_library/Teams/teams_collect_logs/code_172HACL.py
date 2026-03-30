# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging

def run(scenario):
    logging.debug('Executing code block: code_172HACL.py')
    # Remove Any Downloads of previous logs from download folder on mac
    # open msteams:
    # scenario._call(["rm", "-rf ~/Downloads/*MSTeams*"])
    scenario._call(["bash", "-c \"rm -rf ~/Downloads/*MSTeams*\""])
    scenario._call(["bash", "-c \"rm -rf ~/Downloads/*PROD*\""])
    scenario._call(["open", "msteams:"])