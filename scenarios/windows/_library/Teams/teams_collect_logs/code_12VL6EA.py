# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging

def run(scenario):
    if scenario.platform.lower() == "w365":
        raise NotImplementedError("Not working on w365 yet.")
    else:
        scenario._copy_data_from_remote(scenario.result_dir + "\\MSTeamsLogs", source=scenario.dut_data_path + "\\MSTeamsLogs")