# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: DL9
# TestCase Name: Download VOD from Search Results Post Login
#
# GIVEN I have already signed in
# AND I search for a VOD programme using the search feature
# WHEN I click the "Download" button of the search item
# THEN the download completes successfully

import sys, time

sys.path.append("../../../")

# *********************************Importing required Files*********************
from ios_core.app import IOSBase
from ios_core.common import TestResult, navigate, tap_if_present, wait_for_download_complete, \
    WaitForElement, initiate_download, clear_downloads, init_movie_download, \
    clear_download_from_details_page, add_movie_to_dwn_queue
from ios_core.config import IOSConfig

class TC_DL9(IOSBase):
    description="Download VOD from Search Results"

    # ******************** Implementation of the functionality *****************
    def run_script(self, dut, logger, MSL):
        time.sleep(IOSConfig.MIN_SLEEP_TIME)

        cleared = clear_downloads(dut, logger)
        if not cleared:
            logger.Log("Failed to clear existing downloads")
            return

        navigate_list = (
            (
                MSL.Constants.ElementType.Name,
                IOSConfig.HOMESCREEN_SKY_CINEMA, IOSConfig.HOMESCREEN_SKY_CINEMA,
                None, None, None
            ),
            (
                MSL.Constants.ElementType.Name,
                IOSConfig.SKYCINEMA_MOST_POPULAR, IOSConfig.SKYCINEMA_MOST_POPULAR,
                None, None, None
            ),
        )
        navigated = navigate(dut, navigate_list, navigate_interval=5, logger=logger)
        if not navigated:
            return

        download_added, movie_name = init_movie_download(dut, logger)
        if not (download_added and movie_name):
            logger.Log("Failed to find a downloadable asset")
            return

        time.sleep(IOSConfig.MD_SLEEP_TIME)

        # Cancel added download
        cleared = clear_download_from_details_page(dut, logger)
        if not cleared:
            logger.Log("Failed to clear trial download")
            return

        # Go Back to Sky Cinema
        '''
        tapped = tap_if_present(dut, MSL.Constants.ElementType.Name,
            IOSConfig.BTN_BACK_TO_SKY_CINEMA, IOSConfig.BTN_BACK_TO_SKY_CINEMA,
            logger)
        '''
        tapped = tap_if_present(
            dut, MSL.Constants.ElementType.Name,
            IOSConfig.HOME_ICON, IOSConfig.HOME_ICON, logger)
        if not tapped:
            logger.Log("Failed to go back")
            return

        time.sleep(IOSConfig.MD_SLEEP_TIME)
        movie_name = movie_name + "\n"

        tapped = tap_if_present(dut, MSL.Constants.ElementType.Name,
            IOSConfig.NAME_SEARCH_ICON, "Search Icon", logger)
        if not tapped:
            return

        sent = dut.SendKeys(
                MSL.Constants.ElementType.Name, IOSConfig.NAME_SEARCH_FIELD,
                movie_name
            )
        if not sent:
            return

        time.sleep(IOSConfig.DEFAULT_WAIT_TIME)
        present = dut.IsElementPresent(MSL.Constants.ElementType.XPath,
                                       IOSConfig.X_FIRST_SEARCH_RESULT)
        if not present:
            logger.Log("Failed to fetch search results")
            return

        tapped = dut.TapElement(MSL.Constants.ElementType.XPath,
                                IOSConfig.X_FIRST_SEARCH_RESULT)
        if not tapped:
            logger.Log("Failed to tap on search results")
            return

        time.sleep(IOSConfig.DEFAULT_WAIT_TIME)

        tapped = tap_if_present(dut, MSL.Constants.ElementType.Name,
            IOSConfig.NAME_ON_DEMAND, IOSConfig.NAME_ON_DEMAND,
            logger)
        if not tapped:
            return

        added = add_movie_to_dwn_queue(dut, logger)
        if not added:
            logger.Log("Failed to add download")
            return

        logger.Log("Waiting for download to complete")
        completed = wait_for_download_complete(dut, logger)

        if not completed:
            logger.Log("Failed to complete the asset download")
            self.report(
                "Failed to complete the asset download",
                TestResult.FAILED
            )
            return

        self.test_result = True
        self.report(
            "Successfully completed the asset download",
            TestResult.PASSED
        )
        logger.Log("Successfully completed the asset download")

# ******************************************************************************
if __name__ == "__main__":
    test_script = TC_DL9()
    test_script.run()

# ******************************************************************************
# Author: Shinoy Madhavan
# Date: 26 Feb 2018
# Box Type: iPad Mini
# Sky Go Version: 6.2.9
# Reviewer: <Reviewer>
# ******************************************************************************
