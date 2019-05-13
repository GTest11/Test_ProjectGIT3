# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: EP3
# TestCase Name: Epg_Programme_Listings_Till_Midnight
#
# GIVEN I am on the channel listings menu
# WHEN I enter a channel to view the programme listings till midnight
# THEN the app requests EPG programme listings for the channel till midnight
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, time

sys.path.append("../../../")

# **************************Importing required Files************************
from ios_core.app import IOSBase
from ios_core.common import TestResult, verify_epg
from ios_core.config import IOSConfig


class TC_EP3(IOSBase):
    description = "Verify EPG programme listings till midnight"

    # ************Implementation of the functionality**********************
    def run_script(self, dut, logger, MobileScriptingLibrary):

        # Verifying the presence of On Now on Home Page
        if not dut.IsElementPresent(
                MobileScriptingLibrary.Constants.ElementType.Name,
                IOSConfig.HOMESCREEN_ON_NOW):
            self.report("Failed to find 'On Now'", TestResult.FAILED)
            return

        self.report("On Now' is present on the Home Page", TestResult.PASSED)

        if not dut.TapElement(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    "hamburger"):
                self.report("Failed to tap on 'Hamburger Menu'", TestResult.FAILED)
                return

        # Tapping on 'On Now'
        if not dut.TapElement(
                MobileScriptingLibrary.Constants.ElementType.Name, IOSConfig.HOMESCREEN_ON_NOW):
            self.report("Failed to tap on 'On Now'", TestResult.FAILED)
            return

        self.report("Successfully tapped on 'On Now'",TestResult.PASSED)
        read_text = dut.GetText(MobileScriptingLibrary.Constants.ElementType.Name, IOSConfig.MAIN_NAV_TITLE)

        if not (read_text in IOSConfig.HOMESCREEN_ON_NOW):
            self.report("Failed to display the On Now Screen", TestResult.FAILED)
            return

        # If On Now Section displayed successfully
        self.report("Successfully displayed the On Now Screen", TestResult.PASSED)

        # Verifying the presence of All Channels on On Now Screen
        if not dut.IsElementPresent(
                MobileScriptingLibrary.Constants.ElementType.Name,
                IOSConfig.ONNOW_ALL_CHANNELS):
            self.report("Failed to find 'All Channels'", TestResult.FAILED)
            return

        self.report("'All Channels' is present on the Home Page", TestResult.PASSED)

        # tapping on 'All Channels'
        if not dut.TapElement(
                MobileScriptingLibrary.Constants.ElementType.Name, IOSConfig.ONNOW_ALL_CHANNELS):
            self.report("Failed to tap on All Channels Menu", TestResult.FAILED)
            return

        self.report("Successfully tapped on 'All Channels' Menu", TestResult.PASSED)

        if not dut.TapElement(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    "hamburger"):
                self.report("Failed to tap on 'Hamburger Menu'", TestResult.FAILED)
                return

        # Verifying EPG
        is_epg_present = verify_epg(dut, logger)

        # Verifying the string 'Today' and the title on the EPG Listings screen
        if not is_epg_present:
            return

        self.report("Channel Listings displayed successfully", TestResult.PASSED)

        # Coordinates to swipe on the EPG Listings
        EPG_SWIPE_CORD = IOSConfig.CORD_SWIPE_EPG
        is_midnight = False
        for i in range(20):
            dut.Swipe(EPG_SWIPE_CORD[0], EPG_SWIPE_CORD[1], EPG_SWIPE_CORD[2], EPG_SWIPE_CORD[3])
            time.sleep(IOSConfig.DEFAULT_SLEEP_TIME)
            if dut.IsElementPresent(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.TIME_MID_NIGHT
            ):
                is_midnight = True
                break

        if is_midnight:
            self.report("Successfully displayed Programme Listings till midnight", TestResult.PASSED)
            self.test_result = True

        else:
            self.report("Failed to display Programme Listings till midnight", TestResult.FAILED)

# ******************************************************************************

if __name__ == "__main__":
    test_script = TC_EP3()
    test_script.run()

# ******************************************************************************
# Author: Tata Elxsi
# Date: 13 Feb 2018
# Box Type: iPad Mini
# Sky Go Version: 6.2.9
# Reviewer: <Reviewer>
# ******************************************************************************
