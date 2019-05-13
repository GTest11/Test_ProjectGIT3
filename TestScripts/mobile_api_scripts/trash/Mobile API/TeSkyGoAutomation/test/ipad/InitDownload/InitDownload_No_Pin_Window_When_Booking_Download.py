# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: DL1
# TestCase Name: InitDownload_No_Pin_Window_When_Booking_Download
#
# "GIVEN I have signed in
# AND I navigate to a VOD program details page
# WHEN I click the ""Download"" button
# AND I have PIN turned on
# THEN I am not asked to enter my PIN
# AND the download has initialised
# THEN the download limit increases by 1
# AND the download should complete successfully"
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, time

sys.path.append("../../../")

# *********************************Importing required Files*********************
from ios_core.app import IOSBase
from ios_core.common import TestResult, navigate, tap_if_present, \
    are_all_elements_present, is_present, WaitForElement, init_movie_download, \
    clear_downloads, wait_for_download_complete
from ios_core.config import IOSConfig
from ios_core.utils import detect_motion


class TC_DL1(IOSBase):
    description = "Pin Window does not appear on booking a Download, if Parental Pin is enabled"

    def run_preconditions(self, dut, logger, MSL):
        status = super(TC_DL1, self).run_preconditions(dut, logger, MSL)
        if not status:
            return status
        return clear_downloads(dut, logger)

    # ******************** Implementation of the functionality ********************
    def run_script(self, dut, logger, MobileScriptingLibrary):
        try:
            # Navigate to Sky Cinema -> New Premieres
            navigate_list = (
                (
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.HOMESCREEN_SKY_CINEMA, IOSConfig.HOMESCREEN_SKY_CINEMA,
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.MAIN_NAV_TITLE, IOSConfig.HOMESCREEN_SKY_CINEMA
                ),
                (
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.SKYCINEMA_MOST_POPULAR, IOSConfig.SKYCINEMA_MOST_POPULAR,
                    None, None, None
                ),
            )

            is_navigated = navigate(dut, navigate_list, logger=logger)
            if not is_navigated:
                self.report("Failed to navigate to " + IOSConfig.SKYCINEMA_MOST_POPULAR, TestResult.FAILED)
                return
            self.report("Navigated to " + IOSConfig.SKYCINEMA_MOST_POPULAR, TestResult.PASSED)

            # Add movie to download
            download_added = init_movie_download(dut, logger)
            if not download_added:
                self.report(
                    "Failed to add Movie download",
                    TestResult.FAILED
                )
                return
            self.report(
                "Successfully added Movie download",
                TestResult.FAILED
            )

            #Waiting for the Pin Window
            trial = IOSConfig.DEFAULT_TRIAL
            pin_present = False
            while trial:
                pin_present = dut.IsElementPresent(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.PIN_WINDOW,
                    )
                if pin_present:
                    break
                else:
                    time.sleep(IOSConfig.MIN_SLEEP_TIME)
                    trial -= 1
            if pin_present:
                self.report(
                    "PIN Window appeared while booking download",
                    TestResult.FAILED
                )
                return

            self.report(
                "PIN Window did not appear while booking Download",
                TestResult.PASSED
            )

            #Waiting for download to complete
            completed = wait_for_download_complete(dut, logger)
            if not completed:
                self.report(
                    "Failed to complete the asset download",
                    TestResult.FAILED
                )
                return

            self.report(
                "Successfully completed the asset download",
                TestResult.PASSED
            )
            self.test_result = TestResult.PASSED
        except Exception as e:
            self.logger.Log("Exception from run_script(): " + str(e))

# ******************************************************************************

if __name__ == "__main__":
    test_script = TC_DL1()
    test_script.run()

# ******************************************************************************
# Author: Tata Elxsi
# Date: 22 Feb 2018
# Box Type: iPad Mini
# Version: 6.2.9
# Reviewer: <Reviewer>
# ******************************************************************************
