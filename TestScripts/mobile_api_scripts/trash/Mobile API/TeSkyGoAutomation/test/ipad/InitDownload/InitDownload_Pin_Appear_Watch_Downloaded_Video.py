# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: DL2
# TestCase Name: InitDownload_Pin_Appear_Watch_Downloaded_Video
#
# GIVEN I have signed in
# AND I download a video from a VOD program details page
# AND I have PIN turned on
# WHEN I try to watch the downloaded video
# THEN I am asked to enter my PIN
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, time

sys.path.append("../../../")

# *********************************Importing required Files*********************
from ios_core.app import IOSBase


from ios_core.common import TestResult, navigate, tap_if_present, tap_popup_init_dl_playback, \
            is_present, init_movie_download, goto_downloads, wait_for_download_complete
from ios_core.config import IOSConfig


class TC_DL2(IOSBase):
    description="Verify the PIN window does appear for a PIN enabled user when watching a download video"

    def back_to_home_from_sky_cinema(self, dut, MSL, logger):
        return tap_if_present(
            dut, MSL.Constants.ElementType.Name,
            IOSConfig.HOME_ICON, IOSConfig.HOME_ICON, logger)


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
                    IOSConfig.CONTENT_DOWNLOADED, logger)

            if not download_available:
                logger.Log("No downloaded assets available. So, going to download a Movie from Sky Cinema")
                if not tap_if_present(
                        dut,
                        MSL.Constants.ElementType.Name,
                        IOSConfig.BACK_BTN_ON_DOWNLOADS,
                        "Back Button",
                        logger
                ):
                    logger.Log("Failed to go back to Home Page")
                    return

                logger.Log("Reached back to Home Page")

                # Navigating to Sky Cinema
                navigate_list = (
                    (
                        MSL.Constants.ElementType.Name,
                        IOSConfig.HOMESCREEN_SKY_CINEMA, IOSConfig.HOMESCREEN_SKY_CINEMA,
                        MSL.Constants.ElementType.Name,
                        IOSConfig.MAIN_NAV_TITLE, IOSConfig.HOMESCREEN_SKY_CINEMA
                    ),
                    (
                        MSL.Constants.ElementType.Name,
                        IOSConfig.SKYCINEMA_MOST_POPULAR, IOSConfig.SKYCINEMA_MOST_POPULAR,
                        None, None, None
                    ),
                )

                is_navigated = navigate(dut, navigate_list, logger=logger)
                if not is_navigated:
                    self.report(
                        "Failed to navigate to {}".format(IOSConfig.SKYCINEMA_MOST_POPULAR),
                        TestResult.FAILED)
                    return
                self.report(
                    "Navigated to {}".format(IOSConfig.SKYCINEMA_MOST_POPULAR),
                    TestResult.PASSED
                )

                download_started, movie = init_movie_download(dut, logger, True, True)
                if not download_started:
                    self.report(
                        "Failed to initiate Download from Sky Cinema Page",
                        TestResult.FAILED
                    )
                    return
                self.report(
                    "Initiated the Download of '{}' from Sky Cinema Page".format(movie),
                    TestResult.PASSED
                )

                if not wait_for_download_complete(dut,logger):
                    self.report(
                        "Failed to complete the Download",
                        TestResult.FAILED
                    )
                    return
                self.report(
                    "The download completed successfully",
                    TestResult.PASSED
                )

                if not self.back_to_home_from_sky_cinema(dut, MSL, logger):
                    logger.Log("Failed to go back to Home")
                    return

                is_downloads = goto_downloads(dut, logger)
                if not is_downloads:
                    logger.Log("Failed to go to Downloads")
                    return

            logger.Log("Navigated to Downloads")
            tapped = tap_if_present(
                    dut, MSL.Constants.ElementType.XPath,
                    IOSConfig.XPATH_FIRST_DOWNLOAD, "Downloaded Asset",
                    logger)
            if not tapped:
                return

            status = tap_popup_init_dl_playback(dut, logger)
            if not status:
                return

            # Check if PIN window is available
            pin_present = is_present(
                dut, MSL.Constants.ElementType.Name, IOSConfig.PIN_WINDOW,
                "PIN Window", logger)
            if not pin_present:
                self.report(
                    "Pin Window did not appear when trying to playback the Downloaded Movie",
                    TestResult.FAILED
                )
                return
            self.report(
                "Pin Window appeared when trying to playback the Downloaded Movie",
                TestResult.PASSED
            )
            self.test_result = TestResult.PASSED

        except Exception as e:
            logger.Log("Exception from run_script(): " + str(e))

# ******************************************************************************
if __name__ == "__main__":
    test_script = TC_DL2()
    test_script.run()

# ******************************************************************************
# Author: Shinoy Madhavan
# Date: 21 Feb 2018
# Box Type: iPad Mini
# Sky Go Version: 6.2.9
# Reviewer: <Reviewer>
# ******************************************************************************
