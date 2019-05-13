# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: ST3
# TestCase Name: Streaming_Watch_Unencrypted_Channel
#
# GIVEN that I have signed in to the application
# WHEN I select a Unencrypted channel to watch
# THEN the programme begins
# AND the video is smooth
# AND audio and video are in sync
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, time

sys.path.append("../../../")

# *********************************Importing required Files*********************
from ios_core.app import IOSBase
from ios_core.common import TestResult,  are_all_elements_present, \
    tap_if_present, video_player_loaded, wait_for_detect_motion, verify_epg
from ios_core.config import IOSConfig
from ios_core.utils import detect_motion


class TC_ST3(IOSBase):
    description="User can watch Unencrypted Channels"

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

            #Waiting to load the On Now Screen
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

            # Verifying the item - Documentaries - on the On Now Screen
            if not dut.IsElementPresent(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.ONNOW_DOCUMENTARIES
            ):
                self.report(
                    "Failed to display " + IOSConfig.ONNOW_DOCUMENTARIES + " in the On Now Listing",
                    TestResult.FAILED
                )
                return

            self.report(
                "Displayed " + IOSConfig.ONNOW_DOCUMENTARIES + " in the On Now Listing",
                TestResult.PASSED
            )

            if not dut.TapElement(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.ONNOW_DOCUMENTARIES
            ):
                self.report(
                    "Failed to tap on " + IOSConfig.ONNOW_DOCUMENTARIES + " in the On Now Listing",
                    TestResult.FAILED
                )
                return

            self.report(
                "Tapped on " + IOSConfig.ONNOW_DOCUMENTARIES + " in the On Now Listing",
                TestResult.PASSED
            )

            #Verifying the EPG Details Screen
            time.sleep(IOSConfig.DEFAULT_WAIT_TIME)

            # Verifying, 'Today' string, action button, and playback button on the details screen
            epg = verify_epg(dut, logger)

            if not epg:
                self.report(
                    "Failed to display Unencrypted Channel Listing Screen",
                    TestResult.FAILED
                )
                return

            self.report(
                "Displayed Unencrypted Channel Listing Screen",
                TestResult.PASSED
            )

            tapped = tap_if_present(
                    dut, MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.ST_DOC_CHANNEL,
                    IOSConfig.ST_DOC_CHANNEL, logger)
            if not tapped:
                self.report(
                    "Failed to tap on {} channel".format(IOSConfig.ST_DOC_CHANNEL),
                    TestResult.FAILED)
                return
            self.report(
                "Tapped on {} channel".format(IOSConfig.ST_DOC_CHANNEL),
                TestResult.PASSED)

            if not video_player_loaded(dut, logger):
                self.report("Failed to load Video Player", TestResult.FAILED)
                return
            self.report("Video Player loaded", TestResult.PASSED)

            time.sleep(IOSConfig.INITIAL_PLAYBACK_TIME)
            is_play_started = wait_for_detect_motion(dut, IOSConfig.CORD_PLAYBACK, 2, 2, 100, logger, 5)
            if is_play_started:
                self.report(
                    "Started playback on Unencrypted Channel",
                    TestResult.PASSED
                )
                self.test_result = True
            else:
                self.report(
                    "Failed to start playback on Unencrypted Channel",
                    TestResult.FAILED
                )

        except Exception as e:
            logger.Log("Exception from run_script(): " + str(e))

# ******************************************************************************

if __name__ == "__main__":
    test_script = TC_ST3()
    test_script.run()

# ******************************************************************************
# Author: Tata Elxsi
# Date: 20 Feb 2018
# Box Type: iPad Mini
# Version: 6.2.9
# Reviewer: <Reviewer>
# ******************************************************************************
