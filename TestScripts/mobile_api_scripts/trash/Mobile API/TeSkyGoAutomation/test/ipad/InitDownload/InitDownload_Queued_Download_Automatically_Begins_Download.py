# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: DL8
# TestCase Name: InitDownload_Queued_Download_Automatically_Begins_Download
#
# GIVEN I have already signed in
# WHEN I have 2 downloading items in states:
#               downloading and waiting(Now "Queued")
# AND I cancel the downloading item 1 from downloading
# THEN the waiting(Queued) item starts downloading
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, time, clr
clr.AddReference("MobileScriptingLibrary")
import MobileScriptingLibrary

sys.path.append("../../../")

# *********************************Importing required Files*********************
from ios_core.app import IOSBase
from ios_core.common import TestResult, navigate, cancel_download, \
                             get_download_status, clear_downloads, DownloadStatus, \
                            goto_movie, init_movie_download, tap_if_present, goto_downloads
from ios_core.config import IOSConfig


class TC_DL8(IOSBase):
    description = "Queued item automatically begins download when an in progress download cancelled"

    # ******************** Implementation of the functionality ********************
    def run_preconditions(self, dut, logger, MobileScriptingLibrary):
        status = super(TC_DL8,self).run_preconditions(dut, logger, MobileScriptingLibrary)
        if not status:
            return status
        return clear_downloads(dut, logger)

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
                    IOSConfig.SKYCINEMA_DISNEY, IOSConfig.SKYCINEMA_DISNEY,
                    None, None, None
                ),
            )

            is_navigated = navigate(dut, navigate_list, logger=logger)
            if not is_navigated:
                logger.Log("Navigation unsuccessful")
                return

            dl_status_movie1, movie1 = init_movie_download(dut, logger, True, False)

            if not dl_status_movie1:
                self.report(
                    "Failed to initiate Download from Sky Cinema Page",
                    TestResult.FAILED
                )
                logger.Log("Failed to initiate Download from Sky Cinema Page")
                return
            self.report(
                "Initiated the Download of '{}' from Sky Cinema Page".format(movie1),
                TestResult.PASSED
            )
            logger.Log("Initiated the Download of '{}' from Sky Cinema Page".format(movie1))

            dl_status_movie1 = get_download_status(dut, DownloadStatus.INPROGRESS, logger)
            if not dl_status_movie1:
                return
            '''
            time.sleep(IOSConfig.DEFAULT_WAIT_TIME)
            if not tap_if_present(
                dut,
                MobileScriptingLibrary.Constants.ElementType.Name,
                IOSConfig.BACK_BTN_ON_SKYCINEMA,
                "Back to Sky Cinema",
                logger
            ):
                logger.Log("Failed to go back to Sky Cinema")
                return
            '''
            time.sleep(IOSConfig.DEFAULT_WAIT_TIME)
            if not tap_if_present(
                dut, MobileScriptingLibrary.Constants.ElementType.Name,
                IOSConfig.HOME_ICON, IOSConfig.HOME_ICON, logger
            ):
                logger.Log("Failed to go back to Home Page")
                return

            logger.Log("Back on Home Page")
            time.sleep(IOSConfig.DEFAULT_WAIT_TIME)

            navigate_list = (
                (
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.HOMESCREEN_SKY_CINEMA, IOSConfig.HOMESCREEN_SKY_CINEMA,
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.MAIN_NAV_TITLE, IOSConfig.HOMESCREEN_SKY_CINEMA
                ),
                (
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.SKYCINEMA_DISNEY, IOSConfig.SKYCINEMA_DISNEY,
                    None, None, None
                ),
            )

            is_navigated = navigate(dut, navigate_list, logger=logger)
            if not is_navigated:
                logger.Log("Navigation unsuccessful")
                return

            dl_status_movie2, movie2 = init_movie_download(dut, logger, False, False)
            if not dl_status_movie2:
                self.report(
                    "Failed to initiate Download from Sky Cinema Page",
                    TestResult.FAILED
                )
                logger.Log("Failed to initiate Download from Sky Cinema Page")
                return
            self.report(
                "Initiated the Download of '{}' from Sky Cinema Page".format(movie2),
                TestResult.PASSED
            )
            logger.Log("Initiated the Download of '{}' from Sky Cinema Page".format(movie2))

            queue_status_movie2 = get_download_status(dut, DownloadStatus.QUEUED, logger)
            if not queue_status_movie2:
                return

            if not tap_if_present(
                dut, MobileScriptingLibrary.Constants.ElementType.Name,
                IOSConfig.HOME_ICON, IOSConfig.HOME_ICON, logger
            ):
                logger.Log("Failed to go back to Home Page")
                return

            logger.Log("Back on Home Page")
            time.sleep(IOSConfig.DEFAULT_WAIT_TIME)

            if not goto_downloads(dut, logger):
                logger.Log("Failed to go to Downloads")
                return
            logger.Log("Downloads Page displayed")

            moreinfo_dl_cancelled = tap_if_present(
                dut, MobileScriptingLibrary.Constants.ElementType.Name,
                IOSConfig.MORE_INFO_BUTTON, "More Info button",logger
            )

            if not moreinfo_dl_cancelled:
                logger.Log("Failed to tap on More Info Button to Cancel the Download")
                return
            logger.Log("Tapped on More Info Button to Cancel the Download")

            cancel_dl = tap_if_present(
                dut, MobileScriptingLibrary.Constants.ElementType.Name,
                IOSConfig.CANCEL_DOWNLOAD_BTN, "Cancel Download",logger
            )
            if not cancel_dl:
                self.report(
                    "Failed to Cancel the Downloading of {}".format(movie1),
                    TestResult.FAILED
                )
                logger.Log("Failed to Cancel the Downloading of {}".format(movie1))
                return
            self.report(
                "Cancelled the Downloading of {}".format(movie1),
                TestResult.PASSED
            )
            logger.Log("Cancelled the Downloading of {}".format(movie1))

            time.sleep(IOSConfig.DEFAULT_WAIT_TIME)
            if not get_download_status(dut, DownloadStatus.INPROGRESS, logger):
                self.report(
                    "Failed to start Downloading of '{}' start after cancelling the downloading of {}".format(movie2, movie1),
                    TestResult.FAILED
                )
                logger.Log("Failed to start Downloading of '{}' start after cancelling the downloading of {}".format(movie2, movie1))
            else:
                self.report(
                    "Download of '{}' started after cancelling the downloading of {}".format(movie2, movie1),
                    TestResult.PASSED
                )
                logger.Log("Download of '{}' started after cancelling the downloading of {}".format(movie2, movie1))
                self.test_result = True

            logger.Log("*** Cleanup: Cancelling Download ***")
            cancelled = cancel_download(dut, logger)
            if not cancelled:
                logger.Log("Failed to cancel download")

        except Exception as e:
            self.logger.Log("Exception from run_script(): " + str(e))

# ******************************************************************************

if __name__ == "__main__":
    test_script = TC_DL8()
    test_script.run()

# ******************************************************************************
# Author: Tata Elxsi
# Date: 26 Feb 2018
# Box Type: iPad Mini
# Version: 6.2.9
# Reviewer: <Reviewer>
# ******************************************************************************
