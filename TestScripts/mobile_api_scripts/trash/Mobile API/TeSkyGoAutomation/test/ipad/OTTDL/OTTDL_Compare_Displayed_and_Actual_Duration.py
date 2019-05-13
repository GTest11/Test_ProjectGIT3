# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: OTTDL
# TestCase Name: compare the actual duration and duration on the asset detais
# screen
#
# GIVEN I note the duration on the metadata of the asset and I am downloading it
# WHEN I watch the asset in completetion
# THEN the duration matches the duration in the metadata of the asset with a tolerance

import sys, time

sys.path.append("../../../")

# *********************************Importing required Files*********************
from ios_core.app import IOSBase
from ios_core.common import TestResult, navigate, tap_if_present, is_present, \
    video_player_loaded, tap_popup_init_dl_playback, goto_downloads,\
    wait_for_download_complete, init_movie_download
from ios_core.config import IOSConfig
from ios_core.utils import detect_motion
from datetime import datetime, timedelta

def add_time(played, remaining):
    # time_str in [-]*h:m:s format

    if "-" in remaining:
        remaining = remaining.replace("-", "")
    splitted_rem_time = remaining.split(":")
    splitted_play_time = played.split(":")
    mins = int(splitted_rem_time[-2]) if len(splitted_rem_time)>1 else 0
    hours = int(splitted_rem_time[-3]) if len(splitted_rem_time)>2 else 0
    if len(splitted_play_time) > 1:
        mins += int(splitted_play_time[-2])
        if mins >60:
            hours += 1
            mins -= 60
    if len(splitted_play_time) > 2:
        hours += int(splitted_play_time[-3])
    result = "{}m".format(mins)
    if hours:
        result = "{}h {}".format(hours, result)
    return result


def get_formatted_duration(duration):
    # Duration in 0h 0m format
    try:
        duration = duration.strip() # Remove spaces
        if not "h" in duration:
            duration = "0h {}".format(duration)
        if not "m" in duration:
            duration = "{} 0m".format(duration)
        t = datetime.strptime(duration,"%Hh %Mm")
        delta = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
        return delta
    except Exception as e:
        return False

def get_formated_played_time(played_time):
    try:
        if "-" in played_time:
            played_time = played_time.replace("-", "")
        if played_time.count(":") == 1:
            played_time = "00:{}".format(played_time)
        t = datetime.strptime(played_time,"%H:%M:%S")
        delta = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
        return delta
    except Exception as e:
        return False

MAX_DELTA = 5*60

class TC_OTTDL(IOSBase):
    description = "The actual duration matches the duration in the metadata of the asset with a tolerance"

    def back_to_home_from_sky_cinema(self, dut, MSL, logger):
        back_to_home = [IOSConfig.BACK_BTN_ON_SKYCINEMA, IOSConfig.BACK_TO_HOME]
        for button in back_to_home:
            tapped = dut.TapElement(
                MSL.Constants.ElementType.Name,
                button
            )
            if not tapped:
                logger.Log("Failed to tap on "+ button)
                return tapped

        return dut.IsElementPresent(
            dut,
            MSL.Constants.ElementType.Name,
            IOSConfig.APP_HOME
        )

    # ******************** Implementation of the functionality *****************
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
                    self.report("Failed to start download to iPad",
                    TestResult.FAILED)
                    return
                self.report("Successfully started download to iPad",
                TestResult.PASSED)
                download_successful = wait_for_download_complete(dut, logger)
                if not download_successful:
                    logger.Log("Failed to complete download")
                    return
                logger.Log("Downloaded a Movie to iPad")

                if not tap_if_present(
                    dut, MSL.Constants.ElementType.Name,
                    IOSConfig.HOME_ICON, IOSConfig.HOME_ICON, logger):
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
                    self.report("Failed to find the downloaded content in Downloads",
                    TestResult.FAILED)
                    return

            self.report("Downloaded Content available in Downloads",
            TestResult.PASSED)

            # Read duration from details info
            details_duration = dut.GetText(MSL.Constants.ElementType.XPath,
               IOSConfig.X_DWN_FIRST_ITEM_DURATION)
            logger.Log("Duration read is "+ details_duration)
            delta_details_duration = get_formatted_duration(details_duration)
            if not delta_details_duration:
                logger.Log("Unable to format duration read")
                return
            logger.Log("Duration formatted is "+ str(delta_details_duration))

            tapped = tap_if_present(
                    dut, MSL.Constants.ElementType.XPath,
                    IOSConfig.XPATH_FIRST_DOWNLOAD, "Downloaded Asset",
                    logger)
            if not tapped:
                return

            status = tap_popup_init_dl_playback(dut, logger)
            if not status:
                return

            time.sleep(IOSConfig.AVG_WAIT_FOR_ELEMENT_TO_LOAD)

            trial = 3
            found = False
            while trial > 0:
                if video_player_loaded(dut, logger):
                    found = True
                    break
                else:
                    trial -= 1
                    continue
            if not found:
                return

            trial = 3
            found = False
            while trial > 0:
                if detect_motion(dut, IOSConfig.CORD_PLAYBACK, 2, 5, 100, logger):
                    found = True
                    break
                else:
                    trial -= 1
                    continue
            if not found:
                return

            # Pause playback
            trial = 3
            paused = False
            while trial > 0:
                tapped = dut.Tap(*IOSConfig.CORD_VOD_PROGRAMME)
                if tapped:
                    paused = dut.TapElement(MSL.Constants.ElementType.Name,
                                            IOSConfig.PLAYBACK_PLAY_BTN)
                    if paused:
                        break
                    else:
                        trial -= 1
            if not paused:
                return

            # Read played time from video player
            played_time = dut.GetText(MSL.Constants.ElementType.XPath,
                IOSConfig.X_MDA_PLAYER_PLAY_TIME)
            if not played_time:
                logger.Log("Failed to read played duration")
                return

            played_time = get_formated_played_time(played_time)
            if not played_time:
                logger.Log("Unable to format played duration")
                return
            logger.Log("Played duration formatted as " + str(played_time))

            # Read remaining time from video player
            remaining_time = dut.GetText(MSL.Constants.ElementType.XPath,
                IOSConfig.X_MDA_PLAYER_REMAINING_TIME)
            if not remaining_time:
                logger.Log("Failed to read remaining duration")
                return

            remaining_time = get_formated_played_time(remaining_time)
            if not remaining_time:
                logger.Log("Unable to format remaining duration")
                return
            logger.Log("Remaining duration formatted as " + str(remaining_time))

            delta_player_duration = played_time + remaining_time
            logger.Log("Total duration from Media Player is "+ str(delta_player_duration))

            diff = abs(delta_player_duration.total_seconds() - delta_details_duration.total_seconds())

            logger.Log("Difference in durations is {}".format(
                    str(timedelta(0, diff))
                ))

            logger.Log("Tolerance is {}".format(
                    str(timedelta(0, MAX_DELTA))
                ))

            if diff < MAX_DELTA:
                self.report("Difference in metadata duration and actual duration is within Tolerance",
                TestResult.PASSED)
                self.test_result = True
            else:
                self.report("Difference in metadata duration and actual duration exceeds Tolerance",
                TestResult.FAILED)
        except Exception as e:
            logger.Log("Exception in run_script")


# ******************************************************************************
if __name__ == "__main__":
    test_script = TC_OTTDL()
    test_script.run()

# ******************************************************************************
# Author: Shinoy Madhavan
# Date: 26 Feb 2018
# Box Type: iPad Mini
# Sky Go Version: 6.2.9
# Reviewer: <Reviewer>
# ******************************************************************************
