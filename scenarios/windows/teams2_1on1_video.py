# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from core.parameters import Params
Params.setParam("teams", "duration", "300")
Params.setParam("teams", "send_video", "1")
Params.setParam("teams", "send_audio", "1")
Params.setParam("teams", "number_of_bots", "1")
Params.setParam("teams", "bots_send_video", "1")
Params.setParam("teams", "bots_send_audio", "1")
Params.setParam("teams", "bots_share_screen", "0")

import scenarios.windows.teams

class Teams1on1Video(scenarios.windows.teams.Teams):
    '''
    Microsoft Teams video call with 1 bot participant.
    Local camera and mic are on, other participant is a bot sending video and audio.
    '''
    pass