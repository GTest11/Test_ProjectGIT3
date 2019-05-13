# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: DL11
# TestCase Name: InitDownload_Playback_Downloaded_Video_Pause
#
# "GIVEN I have a downloaded item
# AND I watch the downloaded item
# WHEN I seek Pause
# THEN I should have smooth streaming"

import sys, time

sys.path.append("../../../")

# *********************************Importing required Files*********************
from ios_core.app import IOSBase
from ios_core.common import TestResult, navigate, tap_if_present, \
    is_present, init_movie_download, sleep_for_max_time, \
    wait_for_download_complete, goto_downloads, tap_popup_init_dl_playback
from ios_core.config import IOSConfig
from ios_core.utils import detect_motion

class TC_DL11(IOSBase):
    description="Playback of downloaded video after Pause"

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
                return

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
                    logger.Log("Navigation unsuccessful")
                    return

                # Going to download the movie
                movie_download = init_movie_download(dut, logger, True, False)
                if not movie_download:
                    self.report(
                        "Failed to start download to iPad",
                        TestResult.FAILED
                    )
                    logger.Log("Failed to start download to iPad")
                    return
                self.report(
                    "Successfully started download to iPad",
                    TestResult.PASSED
                )
                logger.Log(" Successfully started download to iPad")
                download_successful = wait_for_download_complete(dut, logger)
                if not download_successful:
                    logger.Log("Failed to complete download")
                    return
                logger.Log("Downloaded a Movie to iPad")

                if not self.back_to_home_from_sky_cinema(dut, MSL, logger):
                    logger.Log("Failed to go back to Home")
                    return

                if not goto_downloads(dut, logger):
                    logger.Log("Failed to go to Downloads")
                    return
                logger.Log("Navigated to Downloads")

                # Verifying the downloaded content
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
                    self.logger.Log("Failed to find the downloaded content in Downloads")
                    return
                self.report(
                    "Downloaded Content available in Downloads",
                    TestResult.PASSED
                )
                self.logger.Log("Downloaded Content available in Downloads")

            tapped = tap_if_present(
                dut, MSL.Constants.ElementType.XPath,
                IOSConfig.XPATH_FIRST_DOWNLOAD, "Downloaded Asset",
                logger
            )
            if not tapped:
                return

            status = tap_popup_init_dl_playback(dut, logger)
            if not status:
                return

            sleep_for_max_time(dut, 1)
            presence_playback = False
            # Verify pressence of playback and fastforward element
            for i in range(5):
                if dut.Tap(*IOSConfig.CORD_VOD_PROGRAMME):
                    if dut.IsElementPresent(
                            MSL.Constants.ElementType.Name,
                            IOSConfig.PLAYBACK_FF_BTN
                    ):
                        presence_playback = True
                        break
                    time.sleep(IOSConfig.MIN_SLEEP_TIME)

            is_play_started = detect_motion(dut, IOSConfig.MOVIE_PLAYBACK, 2, 3, 95, logger)
            if not is_play_started:
                self.report(
                        "Failed to detect motion in video playback",
                        TestResult.FAILED
                )
                self.logger.Log("Failed to detect motion in video playback")

            if not (is_play_started and presence_playback):
                self.report(
                    "Failed to start playback of downloaded video",
                    TestResult.FAILED
                )
                self.logger.Log("Failed to start playback of downloaded video")
                return
            else:
                self.report(
                    "Started playback of downloaded video",
                    TestResult.PASSED
                )
                self.logger.Log("Successfully started playback of downloaded video")

            tapped = False
            for i in range(5):
                if dut.Tap(*IOSConfig.CORD_VOD_PROGRAMME):
                    if dut.IsElementPresent(
                            MSL.Constants.ElementType.Name,
                            IOSConfig.PLAYBACK_FF_BTN
                    ):
                        tapped = dut.TapElement(
                            MSL.Constants.ElementType.Name,
                            IOSConfig.PLAYBACK_PLAY_BTN
                        )
                        if tapped:
                            break
                    time.sleep(IOSConfig.MIN_SLEEP_TIME)

            # Tap on fast forward element
            if not tapped:
                self.report(
                    "Failed to tap on the Pause Button on video",
                    TestResult.FAILED
                )
                self.logger.Log("Failed to tap on the Pause Button on video")
                return

            self.report(
                "Tapped on the fast Pause Button on video",
                TestResult.PASSED
            )
            self.logger.Log("Tapped on the Pause Button on video")

            is_play_started = detect_motion(dut, IOSConfig.MOVIE_PLAYBACK, 2, 3, 95, logger)

            if is_play_started:
                self.report(
                    "Failed to Pause playback of downloaded video ",
                    TestResult.FAILED
                )
                self.logger.Log("Failed to pause playback of downloaded video")
                return

            self.report(
                "Successfully paused playback of downloaded video after pause",
                TestResult.PASSED
            )
            self.logger.Log("Successfully paused playback of downloaded video after pause")

            tapped = False
            for i in range(5):
                if dut.Tap(*IOSConfig.CORD_VOD_PROGRAMME):
                    if dut.IsElementPresent(
                            MSL.Constants.ElementType.Name,
                            IOSConfig.PLAYBACK_PLAY_BTN
                    ):
                        tapped = dut.TapElement(
                            MSL.Constants.ElementType.Name,
                            IOSConfig.PLAYBACK_PLAY_BTN
                        )
                        if tapped:
                            break
                    time.sleep(IOSConfig.MIN_SLEEP_TIME)

            # Tap on play element
            if not tapped:
                self.report(
                    "Failed to tap on the Play Button on video",
                    TestResult.FAILED
                )
                self.logger.Log("Failed to tap on the Play Button on video")
                return

            self.report(
                "Tapped on the Play Button on video",
                TestResult.PASSED
            )
            self.logger.Log("Tapped on the Play Button on video")

            time.sleep(IOSConfig.DEFAULT_WAIT_TIME)
            is_play_started = detect_motion(dut, IOSConfig.MOVIE_PLAYBACK, 2, 3, 95, logger)

            if not is_play_started:
                self.report(
                    "Failed to resume playback of downloaded video after pause ",
                    TestResult.FAILED
                )
                self.logger.Log("Failed to resume playback of downloaded video after pause")
                return

            self.report(
                "Successfully resumed playback of downloaded video after pause",
                TestResult.PASSED
            )
            self.logger.Log("Successfully resumed playback of downloaded video after pause")
            self.test_result = TestResult.PASSED

        except Exception as e:
            logger.Log("Exception from run_script(): " + str(e))

# ******************************************************************************
if __name__ == "__main__":
    test_script = TC_DL11()
    test_script.run()

# ******************************************************************************
# Author: Reetha Riya
# Date: 23 Feb 2018
# Box Type: iPad Mini
# Sky Go Version: 6.2.9
# Reviewer: <Reviewer>
# ******************************************************************************
