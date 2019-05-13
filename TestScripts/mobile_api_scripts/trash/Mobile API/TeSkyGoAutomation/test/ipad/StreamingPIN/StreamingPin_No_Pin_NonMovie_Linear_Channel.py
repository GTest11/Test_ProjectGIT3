# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: ST8
# TestCase Name: StreamingPin_No_Pin_NonMovie_Linear_Channel
#
# GIVEN that I have the parental control enabled
# WHEN I press the Entertainment channels
# THEN I am not prompted with the PIN window
# AND I am watching the Entertainment channels
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, time

sys.path.append("../../../")

# *********************************Importing required Files*********************
from ios_core.app import IOSBase
from ios_core.common import TestResult, WaitForElement, verify_epg, \
    navigate, tap_if_present, video_player_loaded
from ios_core.config import IOSConfig
from ios_core.utils import detect_motion


class TC_ST8(IOSBase):
    description="No Pin appears for non-Movie channel if Parental Pin is set"

    # ******************** Implementation of the functionality ********************
    def run_script(self, dut, logger, MSL):
        try:

            navigate_list = (
                (
                    MSL.Constants.ElementType.Name,
                    IOSConfig.HOMESCREEN_ON_NOW, IOSConfig.HOMESCREEN_ON_NOW,
                    MSL.Constants.ElementType.Name,
                    IOSConfig.MAIN_NAV_TITLE, IOSConfig.HOMESCREEN_ON_NOW
                ),
                (
                    MSL.Constants.ElementType.Name,
                    IOSConfig.ONNOW_ENTERTAINMENT, IOSConfig.ONNOW_ENTERTAINMENT,
                    None, None, None
                ),
            )
            navigate_status = navigate(dut, navigate_list, logger=logger)
            if not navigate_status:
                self.report("Failed to navigate to " + IOSConfig.ONNOW_ENTERTAINMENT, TestResult.FAILED)
                return
            self.report("Navigated to " + IOSConfig.ONNOW_ENTERTAINMENT, TestResult.PASSED)

            time.sleep(IOSConfig.MD_SLEEP_TIME)

            #Verifying the EPG Details Screen
            epg = verify_epg(dut, logger)
            if not epg:
                self.report("Failed to display Entertainment Movie Channel Listing Screen", TestResult.FAILED)
                return
            self.report("Displayed Entertainment Movie Channel Listing Screen", TestResult.PASSED)

            tapped = tap_if_present(
                    dut, MSL.Constants.ElementType.Name,
                    IOSConfig.ST_ENTRTNMNT_CHANNEL,
                    IOSConfig.ST_ENTRTNMNT_CHANNEL, logger
                    )
            if not tapped:
                self.report(IOSConfig.ST_ENTRTNMNT_CHANNEL + "is not available in Entertainment Movie Channel Listings",
                            TestResult.FAILED)
                return
            self.report("Tapped on {} to start the playback".format(IOSConfig.ST_ENTRTNMNT_CHANNEL), TestResult.PASSED)

            # Verifying Pin Window Presence
            pin_present = WaitForElement(
                dut, MSL.Constants.ElementType.Name, IOSConfig.PARENTAL_PIN_WINDOW,
                IOSConfig.PARENTAL_PIN_WINDOW, IOSConfig.PLAYBACK_WAIT_TIME,
                logger
            )
            if pin_present:
                self.report("Pin Window appeared before starting to stream on the channel",
                            TestResult.FAILED)
                return
            self.report("Pin Window did not appear before starting to stream on the channel",
                        TestResult.PASSED)

            # Verifies playback
            if not video_player_loaded(dut, logger):
                self.report("Failed to load Media Player", TestResult.FAILED)
                return

            time.sleep(IOSConfig.INITIAL_PLAYBACK_TIME)
            play_started = detect_motion(dut, IOSConfig.CORD_PLAYBACK, 2, 5, 100, logger)
            if play_started:
                self.report("Started playback in Linear Channel without prompting for PIN",
                            TestResult.PASSED)
                self.test_result = True
            else:
                self.report("Failed to start the playback", TestResult.FAILED)
        except Exception as e:
            self.logger.Log("Exception from run_script(): " + str(e))

# ******************************************************************************

if __name__ == "__main__":
    test_script = TC_ST8()
    test_script.run()

# ******************************************************************************
# Author: Tata Elxsi
# Date: 21 Feb 2018
# Box Type: iPad Mini
# Version: 6.2.9
# Reviewer: <Reviewer>
# ******************************************************************************
