# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: ST5
# TestCase Name: Streaming_Watch_Vod_Programme_15_minutes
#
# GIVEN that I am watching a VOD programme
# WHEN I watch for more than 15 minutes continuously
# THEN the video is smooth
# AND audio and video are in sync"
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, time

sys.path.append("../../../")

# *********************************Importing required Files*********************
from ios_core.app import IOSBase
from ios_core.common import TestResult, tap_if_present, \
    detect_motion, video_player_loaded
from ios_core.config import IOSConfig


class TC_ST5(IOSBase):
    description="User can watch VOD programme continuously"

    # ******************** Implementation of the functionality ********************
    def run_script(self, dut, logger, MobileScriptingLibrary):
        try:
            # Verifying Sky Cinema on Home screen
            if not dut.IsElementPresent(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.HOMESCREEN_SKY_CINEMA
            ):
                self.report(
                    "Failed to display 'Sky Cinema' in the Menu Listing",
                    TestResult.FAILED
                )
                return

            self.report(
                "Displayed 'Sky Cinema' in the Menu Listing",
                TestResult.PASSED
            )

            # Selecting Sky Cinema
            if not dut.TapElement(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.HOMESCREEN_SKY_CINEMA
            ):
                self.report(
                    "Failed to tap on Sky Cinema",
                    TestResult.FAILED
                )
                return

            self.report(
                "Tapped on 'Sky Cinema' on the Home Screen",
                TestResult.PASSED
            )

            # Verifying the Sky Cinema Screen
            time.sleep(IOSConfig.DEFAULT_SLEEP_TIME)

            read_text = dut.GetText(
                MobileScriptingLibrary.Constants.ElementType.Name,
                IOSConfig.MAIN_NAV_TITLE
            )

            if not (read_text == IOSConfig.HOMESCREEN_SKY_CINEMA):
                self.report(
                    "Failed to display the Sky Cinema Screen",
                    TestResult.FAILED
                )
                return

            self.report("Sky Cinema Screen displayed",TestResult.PASSED)

            time.sleep(IOSConfig.DEFAULT_SLEEP_TIME)
            # Verifying the item - New Premieres - on the Sky Cinema Screen
            tapped = tap_if_present(
                dut,
                MobileScriptingLibrary.Constants.ElementType.Name,
                IOSConfig.SKYCINEMA_NEW_PREMIERES,
                IOSConfig.SKYCINEMA_NEW_PREMIERES,
                logger
            )

            if not tapped:
                self.report("Failed to tap on {}".format(IOSConfig.SKYCINEMA_NEW_PREMIERES), TestResult.FAILED)
                return
            self.report("Tapped on {}".format(IOSConfig.SKYCINEMA_NEW_PREMIERES), TestResult.PASSED)

            # Selecting a VOD programme
            time.sleep(IOSConfig.DEFAULT_SLEEP_TIME)
            read_text = dut.GetText(
                    MobileScriptingLibrary.Constants.ElementType.XPath,
                    IOSConfig.XPATH_VOD_PROGRAMME
                    )

            if not dut.TapElement(
                MobileScriptingLibrary.Constants.ElementType.Name,
                    read_text
            ):
                self.report(
                    "Failed to select VOD programme",
                    TestResult.FAILED
                )
                return

            self.report(
                "Selected a VOD programme",
                TestResult.PASSED
            )

            time.sleep(IOSConfig.DEFAULT_SLEEP_TIME)
            if dut.IsElementPresent(
                MobileScriptingLibrary.Constants.ElementType.Name,
                IOSConfig.MORE_INFO_BUTTON
            ):
                self.report(
                    "Selected a series in VOD programme",
                    TestResult.PASSED
                )
            else:
                if not dut.TapElement(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    read_text
                ):
                        self.report(
                            "Failed to select an item from the Series Page",
                            TestResult.FAILED
                        )
                        return

                self.report(
                    "Selected an item from the Series Page",
                    TestResult.PASSED
                )

                if not dut.IsElementPresent(
                        MobileScriptingLibrary.Constants.ElementType.Name,
                        IOSConfig.MORE_INFO_BUTTON
                ):
                    self.report(
                        "Failed to find the More Info Button",
                        TestResult.FAILED
                    )
                    return

                self.report(
                    "More Info Button is present on the Screen",
                    TestResult.PASSED
                )

            time.sleep(IOSConfig.DEFAULT_SLEEP_TIME)
            #tapping the asset to start playback
            if not dut.TapElement(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.ASSET_DETAILS_PLAYBACK_BTN
            ):
                self.report(
                    "Failed to tap on the asset - " + IOSConfig.ASSET_DETAILS_PLAYBACK_BTN,
                    TestResult.FAILED
                )
                return

            self.report(
                "Tapped on -" + IOSConfig.ASSET_DETAILS_PLAYBACK_BTN ,
                TestResult.PASSED
            )

            #Checking the VOD playback
            time.sleep(IOSConfig.MX_SLEEP_TIME)

            if not video_player_loaded(dut, logger):
                self.report("Failed to load Video Player", TestResult.FAILED)
                return
            self.report("Video Player loaded", TestResult.PASSED)

            is_play_started = detect_motion(dut,IOSConfig.MOVIE_PLAYBACK, 2, 3, 95, logger)
            if not is_play_started:
                self.report(
                    "Failed to playback the VOD asset",
                    TestResult.FAILED
                )
                return

            self.report(
                "Started playback VOD programme",
                TestResult.PASSED
            )

            #wait for 15 min
            time.sleep(IOSConfig.WAIT_SLEEP_TIME)

            # Checking the VOD playback after 15 minutes
            is_play = detect_motion(dut, IOSConfig.MOVIE_PLAYBACK, 2, 3, 95, logger)
            if is_play:
                self.report(
                    "Video is playing after 15 minutes",
                    TestResult.PASSED
                )
                self.test_result = True
            else:
                self.report(
                    "Video is not playing after 15 minutes",
                    TestResult.FAILED
                )

        except Exception as e:
            logger.Log("Exception from run_script(): " + str(e))

# ******************************************************************************

if __name__ == "__main__":
    test_script = TC_ST5()
    test_script.run()

# ******************************************************************************
# Author: Tata Elxsi
# Date: 15 Feb 2018
# Box Type: iPad Mini
# Version: 6.2.9
# Reviewer: <Reviewer>
# ******************************************************************************
