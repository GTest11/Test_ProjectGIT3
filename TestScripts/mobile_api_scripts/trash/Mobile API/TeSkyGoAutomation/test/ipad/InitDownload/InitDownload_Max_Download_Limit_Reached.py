# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: DL3
# TestCase Name: InitDownload_Max_Download_Limit_Reached
#
# GIVEN that I have already signed in
# AND I have already downloaded the same asset twice in the past
# WHEN I book the same asset to download on third time
# THEN I should get the download limit reached message"
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, time

sys.path.append("../../../")

# *********************************Importing required Files*********************
from ios_core.app import IOSBase
from ios_core.common import TestResult, navigate, tap_if_present, clear_downloads, \
                      init_movie_download, is_max_dl_limit, wait_for_download_complete
from ios_core.config import IOSConfig


def delete_and_download(dut, logger, MobileScriptingLibrary):
    tapped = tap_if_present(
        dut, MobileScriptingLibrary.Constants.ElementType.Name,
        IOSConfig.PGM_DETAILS_MORE_ACTION_BTN,
        IOSConfig.PGM_DETAILS_MORE_ACTION_BTN, logger
    )
    if not tapped:
        logger.Log("Tap unsuccessful")
        return False

    tapped = tap_if_present(
        dut, MobileScriptingLibrary.Constants.ElementType.Name,
        IOSConfig.DELETE_DOWNLOAD_BTN,
        IOSConfig.DELETE_DOWNLOAD_BTN, logger
    )
    if not tapped:
        logger.Log("Tap unsuccessful")
        return False

    time.sleep(IOSConfig.DEFAULT_WAIT_TIME)
    tapped = tap_if_present(
        dut, MobileScriptingLibrary.Constants.ElementType.Name,
        IOSConfig.PGM_DETAILS_MORE_ACTION_BTN,
        IOSConfig.PGM_DETAILS_MORE_ACTION_BTN, logger
    )
    if not tapped:
        logger.Log("Tap unsuccessful")
        return False

    tapped = tap_if_present(
        dut, MobileScriptingLibrary.Constants.ElementType.Name,
        IOSConfig.ASSET_DOWNLOAD_BTN,
        IOSConfig.ASSET_DOWNLOAD_BTN, logger
    )
    if not tapped:
        logger.Log("Tap unsuccessful")
        return False
    return True

class TC_DL3(IOSBase):
    description = "Download Limit Reached Message displays on downloading an asset more than two times"

    # ******************** Implementation of the functionality ********************
    def run_preconditions(self, dut, logger, MobileScriptingLibrary):
        status = super(TC_DL3,self).run_preconditions(dut, logger, MobileScriptingLibrary)
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
                    IOSConfig.SKYCINEMA_NEW_PREMIERES, IOSConfig.SKYCINEMA_NEW_PREMIERES,
                    None, None, None
                ),
            )

            is_navigated = navigate(dut, navigate_list, logger=logger)
            if not is_navigated:
                self.report("Failed to navigate to " + IOSConfig.SKYCINEMA_MOST_POPULAR, TestResult.FAILED)
                return
            self.report("Navigated to " + IOSConfig.SKYCINEMA_MOST_POPULAR, TestResult.PASSED)

            time.sleep(IOSConfig.DEFAULT_WAIT_TIME)
            dl_started, download_movie = init_movie_download(dut, logger, True, True)
            if not dl_started :
                self.report(
                    "Failed to start downloading an asset",
                    TestResult.FAILED
                )
                return
            self.report(
                "Started downloading the asset",
                TestResult.PASSED
            )

            download_limit = 0
            download_limit_reached = False
            while not download_limit_reached:
                if is_max_dl_limit(dut) and download_limit != 2:
                    tapped = tap_if_present(
                        dut, MobileScriptingLibrary.Constants.ElementType.Name,
                        IOSConfig.HOME_ICON, IOSConfig.HOME_ICON, logger)
                    navigate_list = (
                        (
                            MobileScriptingLibrary.Constants.ElementType.Name,
                            IOSConfig.HOMESCREEN_SKY_CINEMA, IOSConfig.HOMESCREEN_SKY_CINEMA,
                            MobileScriptingLibrary.Constants.ElementType.Name,
                            IOSConfig.MAIN_NAV_TITLE, IOSConfig.HOMESCREEN_SKY_CINEMA
                        ),
                        (
                            MobileScriptingLibrary.Constants.ElementType.Name,
                            IOSConfig.SKYCINEMA_NEW_PREMIERES, IOSConfig.SKYCINEMA_NEW_PREMIERES,
                            None, None, None
                        ),
                    )

                    is_navigated = navigate(dut, navigate_list, logger=logger)
                    if not is_navigated:
                        self.report(
                            "Failed to navigate to {} again since the previous download attempt failed". format(IOSConfig.SKYCINEMA_MOST_POPULAR),
                            TestResult.FAILED)
                        return
                    self.report(
                        "Navigated to {} again since the previous download attempt failed". format(IOSConfig.SKYCINEMA_MOST_POPULAR),
                        TestResult.PASSED
                    )

                    dl_started = init_movie_download(dut, logger, True, True)
                    if not dl_started :
                        logger.Log("Failed to start downloading an asset")
                        return
                    download_limit = 0
                    i = 0
                elif is_max_dl_limit(dut) and download_limit==2:
                    download_limit_reached = True
                    break
                else:
                    download_asset = wait_for_download_complete(dut, logger)
                    if not download_asset:
                        self.report(
                            "Failed to download asset",
                            TestResult.FAILED
                        )
                        return
                    else:
                        download_limit += 1
                        start_download = delete_and_download(dut, logger, MobileScriptingLibrary)
                        if not start_download:
                            dut.CommitStepResult(
                                "Step-7: Failed to start download",
                                TestResult.FAILED
                            )
                            logger.Log("Failed to start download")
                            return

            if not download_limit_reached :
                self.report(
                    "Failed to display message screen on download limit reaches",
                    TestResult.FAILED
                )
                return

            self.report(
                "Asset has downloaded 2 times, So displayed the download limit reached message",
                TestResult.PASSED
            )
            self.test_result = TestResult.PASSED

        except Exception as e:
            self.logger.Log("Exception from run_script(): " + str(e))

# ******************************************************************************

if __name__ == "__main__":
    test_script = TC_DL3()
    test_script.run()

# ******************************************************************************
# Author: Tata Elxsi
# Date: 05 Mar 2018
# Box Type: iPad Mini
# Version: 6.2.9
# Reviewer: <Reviewer>
# ******************************************************************************
