# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: PN1
# TestCase Name: OfflinePin_No_Pin_Required_For_Download_Playback
#
# "GIVEN I am in offline mode
# AND I have Parental Control disabled
# WHEN I choose to watch downloaded content
# THEN I must not be prompted for a PIN"

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, time

sys.path.append("../../../")

# *********************************Importing required Files*********************
from ios_core.app import IOSBase

from ios_core.common import TestResult, navigate, tap_if_present, tap_popup_init_dl_playback, \
            is_present, detect_motion

from ios_core.config import IOSConfig


class TC_PN1(IOSBase):
    description="PIN window does not appear for a PIN disabled user when watching a downloaded video in Offline Mode"

    def back_to_home_from_sky_cinema(self, dut, MSL, logger):
        back_to_home = [IOSConfig.BACK_BTN_ON_SKYCINEMA, IOSConfig.BACK_TO_HOME]
        for button in back_to_home:
            tapped = dut.TapElement(
                MSL.Constants.ElementType.Name,
                button
            )
            if not tapped:
                logger.Log("Failed to tap on "+ button)
                return tapped

        return dut.IsElementPresent(
            dut,
            MSL.Constants.ElementType.Name,
            IOSConfig.APP_HOME
        )

    # ******************** Implementation of the functionality ********************
    def run_script(self, dut, logger, MSL):
        try:
            navigate_list = (
                (
                    MSL.Constants.ElementType.Name,
                    IOSConfig.HOMESCREEN_DOWNLOADS, IOSConfig.HOMESCREEN_DOWNLOADS,
                    MSL.Constants.ElementType.Name,
                    IOSConfig.MAIN_NAV_TITLE, IOSConfig.HOMESCREEN_DOWNLOADS
                ),
            )
            navigate_status = navigate(dut, navigate_list, logger=logger)
            if not navigate_status:
                self.report("Failed to navigate to " + IOSConfig.HOMESCREEN_DOWNLOADS, TestResult.FAILED)
                return
            self.report("Navigated to " + IOSConfig.HOMESCREEN_DOWNLOADS, TestResult.PASSED)

            time.sleep(IOSConfig.DEFAULT_WAIT_TIME)
            download_available = is_present(
                    dut, MSL.Constants.ElementType.Name,
                    IOSConfig.CONTENT_DOWNLOADED,
                    IOSConfig.CONTENT_DOWNLOADED, logger
                    )

            if not download_available:
                self.report("No item in Downloads", TestResult.FAILED)
                return

            logger.Log("Navigated to Downloads")
            tapped = tap_if_present(
                    dut, MSL.Constants.ElementType.XPath,
                    IOSConfig.XPATH_FIRST_DOWNLOAD, "Downloaded Asset",
                    logger)
            if not tapped:
                self.report("Failed to get the First Movie from the Downloaded list", TestResult.FAILED)
                return
            self.report("Downloaded Movie is available", TestResult.PASSED)

            if not tap_popup_init_dl_playback(dut, logger):
                return

            # Check if PIN window is available
            pin_present = dut.IsElementPresent(
                MSL.Constants.ElementType.Name, IOSConfig.PIN_WINDOW)

            if pin_present:
                self.report("Pin window appeared while trying to playback", TestResult.FAILED)
                return
            self.report("Pin window did not appear while trying to playback", TestResult.PASSED)

            time.sleep(IOSConfig.AVG_WAIT_FOR_ELEMENT_TO_LOAD)

            ffbtn_present = False
            for i in range(5):
                if dut.Tap(*IOSConfig.CORD_VOD_PROGRAMME):
                    if dut.IsElementPresent(
                            MSL.Constants.ElementType.Name,
                            IOSConfig.PLAYBACK_FF_BTN
                    ):
                        ffbtn_present = True
                        break

            is_play_started = detect_motion(dut, IOSConfig.MOVIE_PLAYBACK, 2, 3, 100, logger)
            if is_play_started and ffbtn_present:
                self.report("Video playback started without prompting for PIN", TestResult.PASSED)
                self.test_result = TestResult.PASSED
            else:
                self.report("Failed to start playback", TestResult.FAILED)

        except Exception as e:
            logger.Log("Exception from run_script(): " + str(e))

# ******************************************************************************
if __name__ == "__main__":
    test_script = TC_PN1()
    test_script.run()

# ******************************************************************************
# Author: Shinoy Madhavan
# Date: 02 Mar 2018
# Box Type: iPad Mini
# Sky Go Version: 6.2.9
# Reviewer: <Reviewer>
# ******************************************************************************
