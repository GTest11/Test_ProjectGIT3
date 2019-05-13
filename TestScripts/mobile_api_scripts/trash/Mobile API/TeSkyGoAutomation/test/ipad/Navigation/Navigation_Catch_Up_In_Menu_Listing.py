# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: NV1
# TestCase Name: Navigation_Catch_Up_In_Menu_Listing
#
# WHEN I visit the menu
# THEN I can see Catch Up in the listing
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, time

sys.path.append("../../../")

# *********************************Importing required Files*********************
from ios_core.app import IOSBase
from ios_core.common import TestResult
from ios_core.config import IOSConfig


class TC_NV1(IOSBase):
    description="Verify 'Catch Up' in the Menu Listings"

    # ******************** Implementation of the functionality ********************
    def run_script(self, dut, logger, MobileScriptingLibrary):
        try:
            if not dut.IsElementPresent(
                MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.HOMESCREEN_CATCHUP_TV):
                self.report("Failed to display 'Catch Up' in the Menu Listing",
                TestResult.FAILED)
                return

            self.report("Step-1: 'Catch Up' is available in the Menu Listing",
            TestResult.PASSED)
            self.test_result = True

        except Exception as e:
            self.logger.Log("Exception from run_script(): " + str(e))

# ******************************************************************************

if __name__ == "__main__":
    test_script = TC_NV1()
    test_script.run()

# ******************************************************************************
# Author: Tata Elxsi
# Date: 08 Feb 2018
# Box Type: iPad Mini
# Version: 6.2.9
# Reviewer: <Reviewer>
# ******************************************************************************
