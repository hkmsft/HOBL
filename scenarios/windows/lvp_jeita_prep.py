# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

##
# Invoke lvp_prep scenario with video_file set to JB2_0.mp4
##

from core.parameters import Params
Params.setOverride("lvp_prep", "video_file", "JB3_0-MOVIE.mp4")
Params.setOverride("lvp_prep", "video_url", "https://home.jeita.or.jp/page_file/JB3_0-MOVIE.mp4")
import scenarios.windows.lvp_prep

Params.setAssociatedSections("lvp_jeita_prep", ["lvp_prep"])

class LvpJeitaPrep(scenarios.windows.lvp_prep.LvpPrep):
    is_prep = True
    pass

