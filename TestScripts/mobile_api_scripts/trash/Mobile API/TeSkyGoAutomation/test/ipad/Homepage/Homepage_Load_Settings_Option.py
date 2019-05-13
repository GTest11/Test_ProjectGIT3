# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: HP1
# TestCase Name: Homepage_Load_Settings_Option
#
# GIVEN I launch Sky Go
# WHEN I load the home page
# THEN I should see the Settings Category
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import sys, time

sys.path.append("../../../")

# *********************************Importing required Files*********************
from ios_core.app import IOSBase
from ios_core.common import TestResult
from ios_core.config import IOSConfig


class TC_HP1(IOSBase):
    description = "Verify 'Settings' on Home page"

    # ***************** Implementation of the functionality ********************
    def run_script(self, dut, logger, MobileScriptingLibrary):
        try:
            # Verifying 'Settings' on the Home Screen
            if dut.IsElementPresent(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.HOMESCREEN_SETTINGS):
                self.report("Successfully displayed 'Settings' on Home Page", TestResult.PASSED)
                self.test_result = True

            else:
                self.report("Failed to display 'Settings' on Home Page",
                TestResult.FAILED)

        except Exception as e:
            self.logger.Log("Exception from run_script(): " + str(e))
# ******************************************************************************

if __name__ == "__main__":
    test_script = TC_HP1()
    test_script.run()

# ******************************************************************************
# Author: Tata Elxsi
# Date: 07 Feb 2018
# Box Type: iPad Mini
# Sky Go Version: 6.2.9
# Reviewer: <Reviewer>
# ******************************************************************************
