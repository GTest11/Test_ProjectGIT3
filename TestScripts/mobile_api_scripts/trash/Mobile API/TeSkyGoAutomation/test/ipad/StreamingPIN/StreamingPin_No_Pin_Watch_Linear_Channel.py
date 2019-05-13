# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: ST6
# TestCase Name: Streaming_Watch_Live_Channel
#
# GIVEN that I have the parental control is disabled on my account
# WHEN I choose to watch a linear channel
# THEN I am not prompted for any PIN
# AND playback starts seamlessly

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, time

sys.path.append("../../../")

# *********************************Importing required Files*********************
from ios_core.app import IOSBase
from ios_core.common import TestResult, WaitForElement, tap_if_present, \
    video_player_loaded, navigate
from ios_core.utils import detect_motion
from ios_core.config import IOSConfig


class TC_ST6(IOSBase):
    description="No PIN Prompt appears on watching Linear Channels when Parental Control disabled"

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
                    IOSConfig.ONNOW_NEWS, IOSConfig.ONNOW_NEWS,
                    None, None, None
                ),
            )
            navigate_status = navigate(dut, navigate_list, logger=logger)
            if not navigate_status:
                self.report("Failed to navigate to " + IOSConfig.ONNOW_NEWS, TestResult.FAILED)
                return
            self.report("Navigated to " + IOSConfig.ONNOW_NEWS, TestResult.PASSED)

            time.sleep(IOSConfig.MD_SLEEP_TIME)

            is_today_present = dut.IsElementPresent(
                MSL.Constants.ElementType.Name,
                IOSConfig.DAYPICKER_TODAY
            )

            if not is_today_present:
                self.report("Failed to display News Programmes Listing", TestResult.FAILED)
                return
            self.report("Displayed News Programmes Listing", TestResult.PASSED)

            # tapping on the first programme in the listing
            tapped = tap_if_present(
                    dut, MSL.Constants.ElementType.Name,
                    IOSConfig.ST_NEWS_CHANNEL,
                    IOSConfig.ST_NEWS_CHANNEL, logger
                    )
            if not tapped:
                self.report(IOSConfig.ST_NEWS_CHANNEL + "is not available in Entertainment Movie Channel Listings",
                            TestResult.FAILED)
                return
            self.report("Tapped on {} to start the playback".format(IOSConfig.ST_NEWS_CHANNEL), TestResult.PASSED)

            # Verifying Pin Window
            pin_window = WaitForElement(
                dut, MSL.Constants.ElementType.Name, IOSConfig.PARENTAL_PIN_WINDOW,
                IOSConfig.PARENTAL_PIN_WINDOW, IOSConfig.DEFAULT_WAIT_TIME,
                logger, interval=3
            )
            if pin_window:
                self.report("Pin Window appeared before starting to stream on the channel",
                            TestResult.FAILED)
                return
            self.report("Pin Window did not appear before starting to stream on the channel",
                        TestResult.PASSED)

            if not video_player_loaded(dut, logger):
                self.report("Failed to load Media Player", TestResult.FAILED)
                return

            time.sleep(IOSConfig.INITIAL_PLAYBACK_TIME)

            #Verifying playback
            play_started = detect_motion(dut, IOSConfig.CORD_PLAYBACK, 2, 3, 100, logger)
            if play_started:
                self.report("Started playback in Linear Channel without prompting for PIN",
                            TestResult.PASSED)
                self.test_result = True
            else:
                self.report("Failed to start the playback", TestResult.FAILED)

        except:
            self.logger.Log("Exception from run_script(): " + str(sys.exc_info()[1]))

# ******************************************************************************

if __name__ == "__main__":
    test_script = TC_ST6()
    test_script.run()

# ******************************************************************************
# Author: Tata Elxsi
# Date: 14 Feb 2018
# Box Type: iPad Mini
# Version: 6.2.9
# Reviewer: <Reviewer>
# ******************************************************************************
