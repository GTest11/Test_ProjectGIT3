# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: EP2
# TestCase Name: Epg_Channel_Listings_Menu
#
# WHEN I enter the channel listings menu
# THEN the app make the EPG requests
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, time

sys.path.append("../../../")

#**************************Importing required Files************************
from ios_core.app import IOSBase
from ios_core.common import TestResult
from ios_core.config import IOSConfig


class TC_EP2(IOSBase):
    description = "Verify EPG displays"

    # ************Implementation of the functionality**********************
    def run_script(self, dut, logger, MobileScriptingLibrary):
        try:

            if not dut.TapElement(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    "hamburger"):
                self.report("Failed to tap on 'Hamburger Menu'", TestResult.FAILED)
                return

            if not dut.TapElement(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.HOMESCREEN_ON_NOW):
                self.report("Failed to tap on 'On Now'", TestResult.FAILED)
                return

            self.report("Tapped on 'On Now'", TestResult.PASSED)

            read_text = dut.GetText(MobileScriptingLibrary.Constants.ElementType.Name, IOSConfig.MAIN_NAV_TITLE)
            if not (read_text == IOSConfig.HOMESCREEN_ON_NOW):
                self.report("Failed to launch On Now", TestResult.FAILED)
                return

            self.report("On Now Screen launched", TestResult.PASSED)

            if not dut.TapElement(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.ONNOW_ALL_CHANNELS):
                self.report("Failed to tap on All Channels Menu",TestResult.FAILED)
                return

            self.report("Tapped on All Channels Menu",TestResult.PASSED)
            
            if not dut.TapElement(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    "hamburger"):
                self.report("Failed to tap on 'Hamburger Menu'", TestResult.FAILED)
                return


            is_today_present = dut.IsElementPresent(
                MobileScriptingLibrary.Constants.ElementType.Name,
                IOSConfig.DAYPICKER_TODAY
            )

            #is_actions_present = dut.IsElementPresent(
                #MobileScriptingLibrary.Constants.ElementType.Name,
                #IOSConfig.EPG_PGM_DETAILS_ACTION_BTN
            #)

            if (is_today_present ): #and is_actions_present
                self.report("Channel Listings displayed successfully",TestResult.PASSED)
                self.test_result = True
            else:
                self.report("Failed to display Channel Listings",TestResult.FAILED)

        except:
            self.logger.Log("Exception from run_script(): " + str(sys.exc_info()[0]))


# ******************************************************************************

if __name__ == "__main__":
    test_script = TC_EP2()
    test_script.run()

# ******************************************************************************
# Author: Tata Elxsi
# Date: 09 Feb 2018
# Box Type: iPad Mini
# Sky Go Version: 6.2.9
# Reviewer: <Reviewer>
# ******************************************************************************
