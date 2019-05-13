# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: Watershed
# TestCase Name: Watershed_Pin_Asked_Before_A_Specified_Time
#
# GIVEN User is signed in
# WHEN the Parental Control PIN is set
# THEN the user is prompted to enter the PIN before a certain time

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, time
import pytz, datetime


sys.path.append("../../../")

# *********************************Importing required Files*********************
from ios_core.app import IOSBase
from ios_core.common import TestResult, WaitForElement, are_all_elements_present, \
    navigate, tap_if_present, video_player_loaded, verify_epg
from ios_core.config import IOSConfig
from ios_core.utils import detect_motion


class Watershed(IOSBase):
    description="Verify whether the user is prompted to enter their PIN before a certain time"

    # ******************** Implementation of the functionality ********************
    def run_script(self, dut, logger, MSL):
        try:

            navigate_list = (
                (
                    MSL.Constants.ElementType.Name,
                    IOSConfig.HOMESCREEN_ON_NOW, IOSConfig.HOMESCREEN_ON_NOW,
                    MSL.Constants.ElementType.Name,
                    IOSConfig.MAIN_NAV_TITLE, IOSConfig.HOMESCREEN_ON_NOW
                ),
                (
                    MSL.Constants.ElementType.Name,
                    IOSConfig.ONNOW_MOVIES, IOSConfig.ONNOW_MOVIES,
                    None, None, None
                ),
            )
            navigate_status = navigate(dut, navigate_list, logger=logger)
            if not navigate_status:
                self.report("Failed to navigate to " + IOSConfig.ONNOW_MOVIES, TestResult.FAILED)
                return
            self.report("Navigated to " + IOSConfig.ONNOW_MOVIES, TestResult.PASSED)

            epg = verify_epg(dut, logger)

            if not epg:
                self.report("Failed to display Entertainment Movie Channel Listing Screen", TestResult.FAILED)
                return
            self.report("Displayed Entertainment Movie Channel Listing Screen", TestResult.PASSED)

            tapped = tap_if_present(
                    dut, MSL.Constants.ElementType.Name,
                    IOSConfig.PIN_REQUIRED_CHANNEL,
                    IOSConfig.PIN_REQUIRED_CHANNEL, logger
                    )
            if not tapped:
                self.report(IOSConfig.PIN_REQUIRED_CHANNEL + "is not available in Entertainment Movie Channel Listings",
                            TestResult.FAILED)
                return
            self.report("Tapped on {} to start the playback".format(IOSConfig.PIN_REQUIRED_CHANNEL), TestResult.PASSED)

            pin_present = False
            for i in range(5):
                pin_present = dut.IsElementPresent(
                    MSL.Constants.ElementType.Name,
                    IOSConfig.PARENTAL_PIN_WINDOW
                )
                if pin_present:
                    break
                time.sleep(IOSConfig.MIN_SLEEP_TIME)

            playback = False
            time.sleep(IOSConfig.INITIAL_PLAYBACK_TIME)
            if not pin_present:
                playback = detect_motion(dut, IOSConfig.MOVIE_PLAYBACK,
                                     2, 3, 100, logger
                                     )
            #Gets UK time
            tz = pytz.timezone(IOSConfig.UK_TIMEZONE)
            current_time = datetime.datetime.now(tz)
            logger.Log("Current UK Time: " + str(current_time))
            
            #Watershed time - 9.00 PM
            if current_time.hour < IOSConfig.WATERSHED_TIME:
                # status = pin_present and (not playback)
                # Verifying Pin Window Presence after 9 p.m
                if not pin_present:
                    self.report("Pin Window did not appear before 9.00 PM", TestResult.FAILED)
                    return
                self.report("Pin Window displayed for the Channel before 9.00 PM", TestResult.PASSED)
                self.test_result = True
            else:
                status = (not pin_present) and playback
                if status:
                    self.report("Pin Window did not appear after 9.00 PM", TestResult.PASSED)
                    self.test_result = True
                    return
                self.report("Pin window did not appear after 9.00 PM", TestResult.FAILED)

        except Exception as e:
            self.logger.Log("Exception from run_script(): " + str(e))

# ******************************************************************************

if __name__ == "__main__":
    test_script = Watershed()
    test_script.run()

# ******************************************************************************
# Author: Tata Elxsi
# Date: 28 Feb 2018
# Box Type: iPad Mini
# Version: 6.2.9
# Reviewer: <Reviewer>
# ******************************************************************************
