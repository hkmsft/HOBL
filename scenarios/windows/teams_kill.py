# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

##
# Force kill the Teams process
##

import core.app_scenario


class TeamsKill(core.app_scenario.Scenario):

    # Local parameters
    is_prep = True

    def setUp(self):
        # Intentionally not calling base method to prevent extraneous call attempts to DUT
        pass

    def runTest(self):
        self._kill("Teams.exe", force = True)  # hard kill
        self._kill("ms-teams.exe", force = True)  # hard kill

    def tearDown(self):
        # Don't call base tearDown so that we don't interact with DUT.
        pass

    def kill(self):
        # self._kill("Teams.exe", force = True)
        try:
            logging.debug("Killing Teams.exe")
            self._kill("Teams.exe", force = True)  # hard kill
            self._kill("ms-teams.exe", force = True)  # hard kill
        except:
            pass