# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging
import os
from core.parameters import Params

def run(scenario):
    logging.debug('Executing code block: code_163V74Y.py')
    
    presentation_video_path = Params.get('teams', 'presentation_video_path')
    presentation_video_full_path = scenario.dut_exec_path + presentation_video_path

    scenario._call(["open", presentation_video_full_path])