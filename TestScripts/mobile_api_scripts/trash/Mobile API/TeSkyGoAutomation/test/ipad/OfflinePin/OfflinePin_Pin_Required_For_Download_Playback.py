# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: PN2
# TestCase Name: OfflinePin_Pin_Required_For_Download_Playback
#
# "GIVEN I have Parental Control enabled
# AND I launch the app in offline mode
# WHEN I choose to watch downloaded content
# THEN I am prompted to enter a PIN
# WHEN I enter my PIN correctly
# THEN I can watch the downloaded content"
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, time

sys.path.append("../../../")

# *********************************Importing required Files*********************
from ios_core.app import IOSBase

from ios_core.common import TestResult, navigate, tap_if_present, tap_popup_init_dl_playback, \
            is_present, init_movie_download, goto_downloads, \
            wait_for_download_complete, sendpin, detect_motion

from ios_core.config import IOSConfig


class TC_PN2(IOSBase):
    description="PIN window appears for a PIN enabled user when watching a downloaded video in Offline Mode"

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
            navigate_status, step = navigate(dut, navigate_list, logger=logger)
            if not navigate_status:
                self.report("Failed to display {} ".format(HOMESCREEN_DOWNLOADS),
                 TestResult.FAILED)
                return

            self.report("{} displayed".format(HOMESCREEN_DOWNLOADS),
                    TestResult.PASSED)
            time.sleep(IOSConfig.DEFAULT_WAIT_TIME)
            download_available = is_present(
                    dut, MSL.Constants.ElementType.Name,
                    IOSConfig.CONTENT_DOWNLOADED,
                    IOSConfig.CONTENT_DOWNLOADED, logger, step
                    )

            if not download_available:
                self.report("No item in Downloads",TestResult.FAILED)
                return

            logger.Log("Navigated to Downloads")
            tapped = tap_if_present(
                    dut, MSL.Constants.ElementType.XPath,
                    IOSConfig.XPATH_FIRST_DOWNLOAD, "Downloaded Asset",
                    logger)
            if not tapped:
                return

            if not tap_popup_init_dl_playback(dut, logger):
                return

            # Check if PIN window is available
            pin_present = is_present(
                dut, MSL.Constants.ElementType.Name, IOSConfig.PIN_WINDOW,
                "PIN Window", logger)
            if not pin_present:
                logger.Log("Pin Window did not appear")
                return

            if not sendpin(dut, IOSConfig.PC_PIN, logger):
                self.report("Failed to enter Parental Control PIN to the Pin window",
                TestResult.FAILED)
                return
            self.report("Parental Control PIN entered to the Pin window",
            TestResult.PASSED)

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
                self.report("Video playback started after entering the PIN",
                TestResult.PASSED)
                self.test_result = TestResult.PASSED
            else:
                self.report("Failed to start playback",
                TestResult.FAILED)
        except Exception as e:
            logger.Log("Exception from run_script(): " + str(e))

# ******************************************************************************
if __name__ == "__main__":
    test_script = TC_PN2()
    test_script.run()

# ******************************************************************************
# Author: Shinoy Madhavan
# Date: 02 Mar 2018
# Box Type: iPad Mini
# Sky Go Version: 6.2.9
# Reviewer: <Reviewer>
# ******************************************************************************
