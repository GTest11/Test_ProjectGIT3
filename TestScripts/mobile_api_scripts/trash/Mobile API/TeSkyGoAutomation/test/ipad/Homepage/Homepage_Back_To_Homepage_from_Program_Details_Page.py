# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: HP4
# TestCase Name: Homepage_Back_To_Homepage_from_Program_Details_Page
#
#GIVEN I have selected a specific piece of content on the HomePage
#WHEN the programme details page loads
#THEN a back icon will be present
#AND when I select back I will return to the previouly viewed page

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, time

sys.path.append("../../../")

# *********************************Importing required Files*********************
from ios_core.app import IOSBase
from ios_core.common import TestResult
from ios_core.config import IOSConfig


class TC_HP4(IOSBase):
    description = "Tapping on the 'Back' Button on Program Details Page takes back to Home Page"

# ******************** Implementation of the functionality ********************
    def run_script(self, dut, logger, MobileScriptingLibrary):
        try:
            time.sleep(IOSConfig.DEFAULT_SLEEP_TIME)

            # Verifying the first programme in the first row of Home Page
            if not dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.XPath,
                                        IOSConfig.XPATH_FIRST_ELEMENT_ON_HOME):
                self.report("Failed to find the specified programme on the Home Page",
                TestResult.FAILED)
                return

            self.report("The specified programme is present on the Home Page",
            TestResult.PASSED)

            # taking the asset name
            asset_name_from_carousel = dut.GetText(
                                        MobileScriptingLibrary.Constants.ElementType.XPath,
                                        IOSConfig.XPATH_FIRST_ELEMENT_ON_HOME
            )

            if not dut.TapElement(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    asset_name_from_carousel
            ):
                self.report("Failed to tap on the Programme " + asset_name_from_carousel,
                TestResult.FAILED)
                return

            # If tapped on piece of content in row within Homepage
            self.report(asset_name_from_carousel + " is selected",
            TestResult.PASSED)

            asset_name_from_info = dut.GetText(MobileScriptingLibrary.Constants.ElementType.Name,
                                               IOSConfig.MAIN_NAV_TITLE)

            if not (asset_name_from_carousel == asset_name_from_info):
                is_same_asset = False
            else:
                is_same_asset = True

            is_more_info_button = dut.IsElementPresent(
                MobileScriptingLibrary.Constants.ElementType.Name,
                IOSConfig.PGM_DETAILS_MORE_ACTION_BTN)
            if not (is_same_asset and is_more_info_button):
                self.report("Failed to display the Programme Information Screen for the programme - " + asset_name_from_carousel,
                TestResult.FAILED)
                return

            self.report("Displayed the Programme Information Screen for the programme - " + asset_name_from_carousel,
            TestResult.PASSED)

            # Verifying the back button on the Home Page
            if not dut.IsElementPresent(
                MobileScriptingLibrary.Constants.ElementType.Name,
                IOSConfig.BACK_BTN_ON_PGMDETAILS
            ):
                self.report("'Back' button is not displayed on the Programme Details page",
                 TestResult.FAILED)
                return

            self.report("'Back' button is displayed on the Programme Details Page",
            TestResult.PASSED)

            if not dut.TapElement(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.BACK_BTN_ON_PGMDETAILS
            ):
                self.report("Failed to tap on the 'Back' Button", TestResult.FAILED)
                return

            self.report("Tapped on the 'Back' Button",TestResult.PASSED)

            time.sleep(IOSConfig.DEFAULT_SLEEP_TIME)
            if not dut.IsElementPresent(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.APP_HOME
            ):
                self.report("Failed to go back to Home Page by tapping on the Back Button",
                TestResult.FAILED)
                return

            self.report("Tapping on the Back Button taken to the Home Page",
            TestResult.PASSED)
            self.test_result = True
        except:
            self.logger.Log("Exception from run_script(): " + str(sys.exc_info()[0]))


# ******************************************************************************

if __name__ == "__main__":
    test_script = TC_HP4()
    test_script.run()

# ******************************************************************************
# Author: Tata Elxsi
# Date: 13 Feb 2018
# Box Type: iPad Mini
# Sky Go Version: 6.2.9
# Reviewer: <Reviewer>
# ******************************************************************************
