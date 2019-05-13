# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: EP1
# TestCase Name: Epg_Load_Sports_Section
#
# GIVEN I select the sports Section
# WHEN I see the section loads
# THEN I see a list of the live sports channels
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, time

sys.path.append("../../../")

# *********************************Importing required Files*********************
from ios_core.app import IOSBase
from ios_core.common import TestResult
from ios_core.config import IOSConfig


class TC_EP1(IOSBase):
    description = "Verify the list of Live Sports Channels in Sports Section"

    # ******************** Implementation of the functionality ********************
    def run_script(self, dut, logger, MobileScriptingLibrary):

        if not dut.TapElement(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    "hamburger"):
                self.report("Failed to tap on 'Hamburger Menu'", TestResult.FAILED)
                return

        if not dut.TapElement(
                MobileScriptingLibrary.Constants.ElementType.Name,
                IOSConfig.HOMESCREEN_SPORTS):
            self.report("Failed to tap on 'Sports' on Home Page",TestResult.FAILED)
            return

        # If tapped on Sports
        self.report("Successfully tapped on 'Sports' on Home Page",TestResult.PASSED)

        read_text = dut.GetText(MobileScriptingLibrary.Constants.ElementType.Name, IOSConfig.MAIN_NAV_TITLE)

        if not (read_text in IOSConfig.HOMESCREEN_SPORTS):
            self.report("Failed to display the Sports Section",TestResult.FAILED)
            return

        # If Sports Section displayed successfully
        self.report("Successfully displayed the Sports Section",TestResult.PASSED)

        # selecting 'Live Sport'
        if not dut.TapElement(
                MobileScriptingLibrary.Constants.ElementType.Name,
                IOSConfig.SPORTS_LIVE_SPORTS):
            self.report("Failed to select the 'Live Sport'",TestResult.FAILED)
            return

        self.report("'Live Sport' selected successfully",TestResult.PASSED)

        if not dut.TapElement(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    "hamburger"):
                self.report("Failed to tap on 'Hamburger Menu'", TestResult.FAILED)
                return

        is_today_present = dut.IsElementPresent(
            MobileScriptingLibrary.Constants.ElementType.Name,
            IOSConfig.SPORTS_LIVE_SPORTS
        )

        #is_actions_present = dut.IsElementPresent(
            #MobileScriptingLibrary.Constants.ElementType.Name,
            #IOSConfig.EPG_PGM_DETAILS_ACTION_BTN
        #)
        if (is_today_present ): #and is_actions_present
            # If Sports Section displayed successfully
            self.report("List of Live Sports Channels displayed successfully",TestResult.PASSED)
            self.test_result = True
        else:
            self.report("Failed to display the List of Live Sports Channels",TestResult.FAILED)


# ******************************************************************************
if __name__ == "__main__":
    test_script = TC_EP1()
    test_script.run()


# ******************************************************************************
# Author: Tata Elxsi
# Date: 09 Feb 2018
# Box Type: iPad Mini
# Sky Go Version: 6.2.9
# Reviewer: <Reviewer>
# ******************************************************************************
