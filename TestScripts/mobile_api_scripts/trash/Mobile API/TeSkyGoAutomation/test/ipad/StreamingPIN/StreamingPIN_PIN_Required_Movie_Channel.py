# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: ST7
# TestCase Name: StreamingPIN_PIN_Required_Movie_Channel
#
# GIVEN that I have the parental control enabled on <setting>
# WHEN I choose to watch a Sky Cinema channel programme
# THEN I am prompted for a PIN
#
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, time

sys.path.append("../../../")

# *********************************Importing required Files*********************
from ios_core.app import IOSBase
from ios_core.common import TestResult, navigate, tap_if_present, is_present, verify_epg
from ios_core.config import IOSConfig


class TC_ST7(IOSBase):
    description="When parental control is enabled, Sky cinema channel prompts for PIN"

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

            time.sleep(IOSConfig.MD_SLEEP_TIME)

            epg = verify_epg(dut, logger)
            if not epg:
                self.report("Failed to display Movie Channel Listing Screen", TestResult.FAILED)
                return
            self.report("Displayed Movie Channel Listing Screen", TestResult.PASSED)

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

            # Check if PIN window is available
            pin_present = is_present(
                dut, MSL.Constants.ElementType.Name, IOSConfig.PIN_WINDOW,
                "PIN Window", logger)
            if pin_present:
                self.report("Pin Window appeared before starting to stream on the channel",
                            TestResult.PASSED)
                self.test_result = TestResult.PASSED
                return
            self.report("Pin Window did not appear before starting to stream on the channel",
                        TestResult.FAILED)

        except Exception as e:
            logger.Log("Exception from run_script(): " + str(e))



# ******************************************************************************
if __name__ == "__main__":
    test_script = TC_ST7()
    test_script.run()

# ******************************************************************************
# Author: Shinoy Madhavan
# Date: 21 Feb 2018
# Box Type: iPad Mini
# Sky Go Version: 6.2.9
# Reviewer: <Reviewer>
# ******************************************************************************
