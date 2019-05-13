# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: DL6
# TestCase Name: InitDownload_Relaunch_App_Not_Affects_The_Download
#
# GIVEN I have a download in progress
# WHEN I close and re-launch Sky Go
# THEN the download should resume as expected
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, time

sys.path.append("../../../")

# *********************************Importing required Files*********************
from ios_core.app import IOSBase
from ios_core.common import TestResult, navigate, tap_if_present, \
                            verify_movie_details_reached, is_present, \
                            are_all_elements_present, init_movie_download, \
                            WaitForElement, get_download_status, clear_downloads
from ios_core.config import IOSConfig


class TC_DL6(IOSBase):
    description = "Download in progress resume if the application is closed and relaunched"

    # ******************** Implementation of the functionality ********************
    def run_preconditions(self, dut, logger, MobileScriptingLibrary):
        status = super(TC_DL6,self).run_preconditions(dut, logger, MobileScriptingLibrary)
        if not status:
            return status
        cleared = clear_downloads(dut, logger)
        if not cleared:
            return False
        return True

    # ******************** Implementation of the functionality ********************
    def run_script(self, dut, logger, MobileScriptingLibrary):
        try:
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
                logger.Log("Navigation unsuccessful")
                return

            time.sleep(IOSConfig.DEFAULT_WAIT_TIME)
            download_movie, movie_name = init_movie_download(dut, logger, True, True)
            if not download_movie :
                self.report(
                    "Failed to start downloading an asset",
                    TestResult.FAILED
                )
                logger.Log("Failed to start downloading an asset")
                return
            self.report(
                "Started downloading the asset",
                TestResult.PASSED
            )
            logger.Log("Successfully started downloading the asset")

            #Closing and relaunching application
            dut.Stop()
            logger.Log("The application is closed")
            time.sleep(IOSConfig.DEFAULT_WAIT_TIME)
            self.init_app()

            navigate_list = (
                (
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.HOMESCREEN_DOWNLOADS, IOSConfig.HOMESCREEN_DOWNLOADS,
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.MAIN_NAV_TITLE, IOSConfig.HOMESCREEN_DOWNLOADS
                ),
            )

            is_navigated = navigate(dut, navigate_list, logger=logger)
            if not is_navigated:
                logger.Log("Navigation unsuccessful")
                return

            movie_present= is_present(
                    dut, MobileScriptingLibrary.Constants.ElementType.Name,
                    movie_name,"the Movie in Sky Cinema", logger
            )
            if not movie_present:
                self.report(
                    "Failed to find Movie in downloads",
                    TestResult.FAILED
                )
                logger.Log("Failed to find Movie in downloads")
                return

            self.report(
                "'{}' movie is available in downloads".format(movie_name),
                TestResult.PASSED
            )
            logger.Log("'{}' movie is successfully available in downloads".format(movie_name))

            tapped = tap_if_present(
                dut, MobileScriptingLibrary.Constants.ElementType.Name,
                IOSConfig.MORE_INFO_BUTTON,
                IOSConfig.MORE_INFO_BUTTON, logger
            )
            if not tapped:
                logger.Log("Tap unsuccessful")
                return

            downloading_present = is_present(
                dut, MobileScriptingLibrary.Constants.ElementType.Name,
                IOSConfig.ASSET_DOWNLOAD_CANCEL_BTN,
                IOSConfig.ASSET_DOWNLOAD_CANCEL_BTN, logger
            )
            if not downloading_present:
                self.report(
                    "Failed to download after closing and relaunching app",
                    TestResult.FAILED
                )
                logger.Log("Failed to download after closing and relaunching app")
                return

            self.report(
                "Downloading continues after closing and relaunching app",
                TestResult.PASSED
            )
            logger.Log("Downloading continues after closing and relaunching app")
            self.test_result = TestResult.PASSED

        except:
            self.logger.Log("Exception from run_script(): " + str(sys.exc_info()[1]))

# ******************************************************************************

if __name__ == "__main__":
    test_script = TC_DL6()
    test_script.run()

# ******************************************************************************
# Author: Tata Elxsi
# Date: 23 Feb 2018
# Box Type: iPad Mini
# Version: 6.2.9
# Reviewer: <Reviewer>
# ******************************************************************************
