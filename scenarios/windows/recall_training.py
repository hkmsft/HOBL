# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

##
# Invoke copilot short scenario with training_mode param set
##

import builtins
from core.parameters import Params
Params.setOverride("global", "training_mode", "1")
import scenarios.ai_scenarios.recall

Params.setAssociatedSections("recall_training", ["recall"])

class RecallTraining(scenarios.ai_scenarios.recall.recall):
    is_prep = True
    pass

