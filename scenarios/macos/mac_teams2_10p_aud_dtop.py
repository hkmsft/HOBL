# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from core.parameters import Params
Params.setParam("teams", "duration", "300")
Params.setParam("teams", "send_video", "0")
Params.setParam("teams", "send_audio", "1")
Params.setParam("teams", "send_screen", "1")
Params.setParam("teams", "show_desktop", "1")
Params.setParam("teams", "number_of_bots", "8")
Params.setParam("teams", "bots_send_video", "0")
Params.setParam("teams", "bots_send_audio", "1")
Params.setParam("teams", "bots_share_screen", "0")
import scenarios.macos.mac_teams

class MacTeams10pAudDtop(scenarios.macos.mac_teams.MacTeams):
    '''
    Microsoft Teams audio call with 9 bot participants.
    Local camera is off and mic is on, other 9 participants are bots sending audio.
    Local user is sharing desktop.
    '''
    pass