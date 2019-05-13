# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: DL4
# TestCase Name: InitDownload_Playback_Downloaded_Video
#
# "GIVEN I have a downloaded item
# AND I am connected to a Wifi
# WHEN I watch the downloaded item
# THEN I can watch the programme"

import sys, time

sys.path.append("../../../")

# *********************************Importing required Files*********************
from ios_core.app import IOSBase
from ios_core.common import TestResult, navigate, tap_if_present, \
                is_present, tap_popup_init_dl_playback, sleep_for_max_time, \
                init_movie_download, wait_for_download_complete, goto_downloads
from ios_core.config import IOSConfig
from ios_core.utils import detect_motion

class TC_DL4(IOSBase):
    description="Verify Playback of downloaded video after fast-forward"

    def back_to_home_from_sky_cinema(self, dut, MSL, logger):
        return tap_if_present(
            dut, MSL.Constants.ElementType.Name,
            IOSConfig.HOME_ICON, IOSConfig.HOME_ICON, logger
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
                logger.Log("No downloaded assets available. So, going to download a Movie from Sky Cinema")
                if not tap_if_present(
                        dut,
                        MSL.Constants.ElementType.Name,
                        IOSConfig.BACK_BTN_ON_DOWNLOADS,
                        "Back Button",
                        logger
                ):
                    self.report("Failed to go back to Home Page", TestResult.FAILED)
                    return
                self.report("Home Page is displayed back", TestResult.FAILED)

                #Navigating to Sky Cinema
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

                #Going to download the movie
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

                download_successful = wait_for_download_complete(dut,logger)
                if not download_successful:
                    logger.Log("Failed to complete download")
                    return

                if not self.back_to_home_from_sky_cinema(dut, MSL, logger):
                    logger.Log("Failed to go back to Home")
                    return

                if not goto_downloads(dut, logger):
                    logger.Log("Failed to go to Downloads")
                    return
                logger.Log("Navigated to Downloads")

                #Verifying the downloaded content
                download_available = is_present(
                    dut, MSL.Constants.ElementType.Name,
                    IOSConfig.CONTENT_DOWNLOADED,
                    IOSConfig.CONTENT_DOWNLOADED, logger
                )
                if not download_available:
                    self.report(
                        "Failed to find the downloaded content in Downloads",
                        TestResult.FAILED
                    )
                    return
                self.report(
                    "Downloaded Content available in Downloads",
                    TestResult.PASSED
                )

            tapped = tap_if_present(
                dut, MSL.Constants.ElementType.XPath,
                IOSConfig.XPATH_FIRST_DOWNLOAD, "Downloaded Asset",
                logger
            )
            if not tapped:
                self.report("Failed to pick up the downloaded movie",
                    TestResult.FAILED
                )
                return
            self.report("Tapped on the Downloaded Movie to start playback",
                        TestResult.PASSED
                        )

            status = tap_popup_init_dl_playback(dut, logger)
            if not status:
                return

            sleep_for_max_time(dut, 1)
            presence_playback = False

            #Verify pressence of playback and fastforward element
            for i in range (5):
                if dut.Tap(*IOSConfig.CORD_VOD_PROGRAMME):
                    if dut.IsElementPresent(
                        MSL.Constants.ElementType.Name,
                        IOSConfig.PLAYBACK_FF_BTN
                    ):
                        presence_playback =  True
                        break
                    time.sleep(IOSConfig.MIN_SLEEP_TIME)

            is_play_started = detect_motion(dut, IOSConfig.MOVIE_PLAYBACK, 2, 3, 100, logger)
            if not(is_play_started and presence_playback):
                self.report(
                        "Failed to start playback of downloaded video",
                        TestResult.FAILED
                )
                return
            else:
                self.report(
                    "Started playback of downloaded video",
                    TestResult.PASSED
                )
            self.test_result = TestResult.PASSED

        except Exception as e:
            logger.Log("Exception from run_script(): " + str(e))

# ******************************************************************************
if __name__ == "__main__":
    test_script = TC_DL4()
    test_script.run()

# ******************************************************************************
# Author: Tata Elxsi
# Date: 23 Feb 2018
# Box Type: iPad Mini
# Sky Go Version: 6.2.9
# Reviewer: <Reviewer>
# ******************************************************************************
