# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from parameters import Params
Params.setParam("teams", "duration", "600")
Params.setParam("teams", "send_video", "1")
Params.setParam("teams", "send_audio", "1")
Params.setParam("teams", "send_screen", "0")
Params.setParam("teams", "number_of_bots", "4")
Params.setParam("teams", "bots_send_video", "1")
Params.setParam("teams", "bots_send_audio", "1")
Params.setParam("teams", "bots_share_screen", "1")
import scenarios.windows.teams

class Teams3x3VideShare(scenarios.windows.teams.Teams):
    '''
    Microsoft Teams video call with 4 bot participants.
    Local camera and mic are on, other 4 participants are bots sending video and audio.
    One of the bots is sharing a video.
    '''
    pass