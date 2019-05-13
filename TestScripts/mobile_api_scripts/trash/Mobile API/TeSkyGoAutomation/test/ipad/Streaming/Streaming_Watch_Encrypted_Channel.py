# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: ST2
# TestCase Name: Streaming_Watch_Encrypted_Channel
#
# GIVEN that I have signed in to the application
# WHEN I select a Encrypted channel to watch
# THEN the programme begins
# AND the video is smooth
# AND audio and video are in sync
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, time

sys.path.append("../../../")

# *********************************Importing required Files*********************
from ios_core.app import IOSBase
from ios_core.common import TestResult, are_all_elements_present, \
    tap_if_present, video_player_loaded, verify_epg
from ios_core.config import IOSConfig
from ios_core.utils import detect_motion


class TC_ST2(IOSBase):
    description="User can watch Encrypted Channels"

    # ******************** Implementation of the functionality ********************
    def run_script(self, dut, logger, MobileScriptingLibrary):
        try:
            if not dut.IsElementPresent(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.HOMESCREEN_ON_NOW):
                self.report(
                    "Failed to display 'On Now' in the Menu Listing",
                    TestResult.FAILED)
                return

            self.report(
                "Displayed 'On Now' in the Menu Listing",
                TestResult.PASSED)
            logger.Log("Displayed 'On Now' in the Menu Listing")

            if not dut.TapElement(
                MobileScriptingLibrary.Constants.ElementType.Name,
                IOSConfig.HOMESCREEN_ON_NOW):
                self.report(
                    "Failed to tap on On Now",
                    TestResult.FAILED)
                return

            self.report(
                "Tapped on 'On Now' on the Home Screen",
                TestResult.PASSED)
            logger.Log("Successfully tapped on 'On Now' on the Home Screen")

            #Waiting to load the On Now Screen
            read_text = dut.GetText(
                MobileScriptingLibrary.Constants.ElementType.Name,
                IOSConfig.MAIN_NAV_TITLE
            )

            if not (read_text == IOSConfig.HOMESCREEN_ON_NOW):
                self.report(
                    "Failed to display the On Now Screen",
                    TestResult.FAILED)
                return

            self.report("On Now Screen displayed", TestResult.PASSED)

            # Verifying the item - Movies - on the On Now Screen
            if not dut.IsElementPresent(
                MobileScriptingLibrary.Constants.ElementType.Name,
                IOSConfig.ONNOW_MOVIES):
                self.report(
                    "Failed to display " + IOSConfig.ONNOW_MOVIES + " in the On Now Listing",
                    TestResult.FAILED
                )
                logger.Log("Failed to display " + IOSConfig.ONNOW_MOVIES + " in the On Now Listing")
                return

            self.report(
                "Displayed " + IOSConfig.ONNOW_MOVIES + " in the On Now Listing",
                TestResult.PASSED)
            logger.Log("Displayed " + IOSConfig.ONNOW_MOVIES + " in the On Now Listing")

            if not dut.TapElement(
                MobileScriptingLibrary.Constants.ElementType.Name,
                IOSConfig.ONNOW_MOVIES):
                self.report(
                    "Failed to tap on " + IOSConfig.ONNOW_MOVIES + " in the On Now Listing",
                    TestResult.FAILED
                )
                return

            self.report(
                "Tapped on " + IOSConfig.ONNOW_MOVIES + " in the On Now Listing",
                TestResult.PASSED)

            #Verifying the EPG Details Screen
            time.sleep(IOSConfig.DEFAULT_WAIT_TIME)

            # Verifying, 'Today' string on the details screen
            epg = verify_epg(dut, logger)

            if not epg:
                self.report(
                    "Failed to display Encrypted Channel Listing Screen",
                    TestResult.FAILED)
                return

            self.report("Displayed Encrypted Channel Listing Screen",
                TestResult.PASSED)

            tapped = tap_if_present(
                    dut, MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.PIN_REQUIRED_CHANNEL,
                    IOSConfig.PIN_REQUIRED_CHANNEL, logger)
            if not tapped:
                self.report(
                    "Failed to tap on {} channel".format(IOSConfig.PIN_REQUIRED_CHANNEL),
                    TestResult.FAILED)
                return
            self.report(
                "Tapped on {} channel".format(IOSConfig.PIN_REQUIRED_CHANNEL),
                TestResult.PASSED)

            #Verifying the player
            if not video_player_loaded(dut, logger):
                self.report("Failed to load Video Player", TestResult.FAILED)
                return
            self.report("Video Player loaded", TestResult.PASSED)

            time.sleep(IOSConfig.INITIAL_PLAYBACK_TIME)
            is_play_started = detect_motion(dut,IOSConfig.MOVIE_PLAYBACK, 2, 3, 100, logger)

            if is_play_started:
                self.report(
                    "Started playback on Encrypted Channel",
                    TestResult.PASSED
                )
                self.test_result = True
            else:
                self.report(
                    "Failed to start playback on Encrypted Channel",
                    TestResult.FAILED)

        except Exception as e:
            logger.Log("Exception from run_script(): " + str(e))

# ******************************************************************************

if __name__ == "__main__":
    test_script = TC_ST2()
    test_script.run()

# ******************************************************************************
# Author: Tata Elxsi
# Date: 20 Feb 2018
# Box Type: iPad Mini
# Version: 6.2.9
# Reviewer: <Reviewer>
# ******************************************************************************
