# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: ST5
# TestCase Name: Streaming_Watch_Live_Channel_15_Minutes
#
# "GIVEN that I am watching a linear channel
# WHEN I watch for more than 15 minutes without channel changing
# THEN the video is smooth
# AND audio and video are in sync"

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, time

sys.path.append("../../../")

# *********************************Importing required Files*********************
from ios_core.app import IOSBase
from ios_core.config import IOSConfig
from ios_core.common import TestResult, verify_epg, sleep_for_max_time,  \
    tap_if_present, video_player_loaded
from ios_core.utils import detect_motion

class TC_ST4(IOSBase):
    description="User can watch a linear channel continuously for an extended period over Wi-Fi-15 minutes"

    # ******************** Implementation of the functionality ********************
    def run_script(self, dut, logger, MobileScriptingLibrary):
        try:
            if not dut.IsElementPresent(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.HOMESCREEN_ON_NOW
            ):
                self.report(
                    "Failed to display 'On Now' in the Menu Listing",
                    TestResult.FAILED
                )
                return

            self.report(
                "Displayed 'On Now' in the Menu Listing",
                TestResult.PASSED
            )

            if not dut.TapElement(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.HOMESCREEN_ON_NOW
            ):
                self.report(
                    "Failed to tap on On Now",
                    TestResult.FAILED
                )
                return

            self.report(
                "Tapped on 'On Now' on the Home Screen",
                TestResult.PASSED
            )

            read_text = dut.GetText(
                MobileScriptingLibrary.Constants.ElementType.Name,
                IOSConfig.MAIN_NAV_TITLE
            )

            if not (read_text == IOSConfig.HOMESCREEN_ON_NOW):
                self.report(
                    "Failed to display the On Now Screen",
                    TestResult.FAILED
                )
                return

            self.report("On Now Screen displayed",TestResult.PASSED)

            # Verifying the item - News - on the On Now Screen
            if not dut.IsElementPresent(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.ONNOW_NEWS
            ):
                self.report(
                    "Failed to display 'News' in the On Now Listing",
                    TestResult.FAILED
                )
                return

            self.report(
                "Displayed 'News' in the On Now Listing",
                TestResult.PASSED
            )

         #Tap the item - News - on the On Now Screen
            if not dut.TapElement(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.ONNOW_NEWS
            ):
                self.report(
                    "Failed to tap on News",
                    TestResult.FAILED
                )
                return

            self.report(
                "Tapped on 'News' on the Home Screen",
                TestResult.PASSED
            )

            # Verifying the EPG Listings
            if not verify_epg(dut, logger):
                self.report(
                    "Failed to display News Programmes Listing",
                    TestResult.FAILED
                )
                return

            self.report(
                "Displayed News Programmes Listing",
                TestResult.PASSED
            )

            tapped = tap_if_present(
                    dut, MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.ST_NEWS_CHANNEL,
                    IOSConfig.ST_NEWS_CHANNEL, logger)
            if not tapped:
                self.report(
                    "Failed to tap on {} channel".format(IOSConfig.ST_NEWS_CHANNEL),
                    TestResult.FAILED)
                return
            self.report(
                "Tapped on {} channel".format(IOSConfig.ST_NEWS_CHANNEL),
                TestResult.PASSED)

            if not video_player_loaded(dut, logger):
                self.report("Failed to load Video Player", TestResult.FAILED)
                return
            self.report("Video Player loaded", TestResult.PASSED)

            time.sleep(IOSConfig.INITIAL_PLAYBACK_TIME)

            # Verify playback
            play_started = detect_motion(dut, IOSConfig.CORD_PLAYBACK, 2, 5, 100, logger)
            if not play_started:
                self.report(
                    "Failed to start playback in linear channel",
                    TestResult.FAILED
                )
                return
            self.report(
                "Started playback in Linear Channel",
                TestResult.PASSED
            )

            # Watching linear channel for 15 minutes
            sleep_for_max_time(dut, 15)

            #Verifying video after 15 minutes
            if detect_motion(dut, IOSConfig.CORD_PLAYBACK, 2, 5, 100, logger):
                self.report(
                "The video is playing after 15 minutes",
                TestResult.PASSED
                )
                self.test_result = True
            else:
                self.report(
                    "Failed playback in linear channel after 15 minutes",
                    TestResult.FAILED
                )

        except Exception as e:
            logger.Log("Exception from run_script(): " + str(e))

# ******************************************************************************

if __name__ == "__main__":
    test_script = TC_ST4()
    test_script.run()

# ******************************************************************************
# Author: Tata Elxsi
# Date: 14 Feb 2018
# Box Type: iPad Mini
# Version: 6.2.9
# Reviewer: <Reviewer>
# ******************************************************************************
