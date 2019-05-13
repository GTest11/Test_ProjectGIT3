# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: DL5
# TestCase Name: InitDownload_Download_Complete_Successful
#
# "GIVEN I have signed in
# AND I am on the ""Sky Cinema"" page
# AND I navigate to a program details page
# WHEN I click the ""Download"" button
# THEN the download should complete successfully"

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, time

sys.path.append("../../../")

# *********************************Importing required Files*********************
from ios_core.app import IOSBase
from ios_core.common import TestResult, navigate, wait_for_download_complete, \
                            init_movie_download, clear_downloads
from ios_core.config import IOSConfig



class TC_DL5(IOSBase):
    description = "Verify if the VOD asset downloads correctly after login"

    def run_preconditions(self, dut, logger, MobileScriptingLibrary):
        status = super(TC_DL5,self).run_preconditions(dut, logger, MobileScriptingLibrary)
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
                    IOSConfig.SKYCINEMA_MOST_POPULAR, IOSConfig.SKYCINEMA_MOST_POPULAR,
                    None, None, None
                ),
            )

            is_navigated = navigate(dut, navigate_list, logger=logger)
            if not is_navigated:
                self.report("Failed to navigate to " + IOSConfig.SKYCINEMA_MOST_POPULAR, TestResult.FAILED)
                return
            self.report("Navigated to " + IOSConfig.SKYCINEMA_MOST_POPULAR, TestResult.PASSED)

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

            #Checking whether download completed
            if not wait_for_download_complete(dut,logger):
                self.report(
                    "Failed to complete the download",
                    TestResult.FAILED
                )

            else:
              self.report(
                    "The download has completed successfully",
                    TestResult.PASSED
              )
              self.test_result = TestResult.PASSED

        except:
            self.logger.Log("Exception from run_script(): " + str(sys.exc_info()[1]))

# ******************************************************************************

if __name__ == "__main__":
    test_script = TC_DL5()
    test_script.run()
    test_script.cleanup()

# ******************************************************************************
# Author: Tata Elxsi
# Date: 27 Feb 2018
# Box Type: iPad Mini
# Version: 6.2.9
# Reviewer: <Reviewer>
# ******************************************************************************
