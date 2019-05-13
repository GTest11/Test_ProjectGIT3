# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: DL12
# TestCase Name: InitDownload_Cancel_Download
#
#"GIVEN I have a download in progress
# WHEN I select  cancel download
# THEN I send a Cancel Download call to SPS
# AND my download is removed from the device
# AND my download count is decreased by one"

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, time

sys.path.append("../../../")

# *********************************Importing required Files*********************
from ios_core.app import IOSBase
from ios_core.common import TestResult, navigate, clear_downloads, \
                            cancel_download, init_movie_download
from ios_core.config import IOSConfig


class TC_DL12(IOSBase):
    description = "Verify the cancelling of an in progress download "

    def run_preconditions(self, dut, logger, MobileScriptingLibrary):
        status = super(TC_DL12,self).run_preconditions(dut, logger, MobileScriptingLibrary)
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
                self.report("Failed to navigate to " + IOSConfig.SKYCINEMA_NEW_PREMIERES, TestResult.FAILED)
                return
            self.report("Navigated to " + IOSConfig.SKYCINEMA_NEW_PREMIERES, TestResult.PASSED)

            #Start movie download
            movie_download = init_movie_download(dut, logger, True, False)
            if not movie_download:
                self.report(
                    "Failed to start download to iPad",
                    TestResult.FAILED
                )
                return
            self.report(
                "Successfully started download to iPad",
                TestResult.PASSED
            )

            #cancel download
            cancel_movie_download = cancel_download(dut, logger)
            if not cancel_movie_download:
               self.report(
                   "Failed to cancel download to iPad",
                   TestResult.FAILED
               )
               return
            self.report(
               "Successfully canceled download to iPad ",
               TestResult.PASSED
            )
            self.test_result = TestResult.PASSED
        except:
            self.logger.Log("Exception from run_script(): " + str(sys.exc_info()[1]))

# ******************************************************************************

if __name__ == "__main__":
    test_script = TC_DL12()
    test_script.run()

# ******************************************************************************
# Author: Tata Elxsi
# Date: 26 Feb 2018
# Box Type: iPad Mini
# Version: 6.2.9
# Reviewer: <Reviewer>
# ******************************************************************************
