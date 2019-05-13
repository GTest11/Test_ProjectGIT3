# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: HP3
# TestCase Name: Load_Program_Details_Page
#
#GIVEN I am viewing a row within the Homepage
#WHEN I select a specific piece of content
#THEN I am taken to the Programme / Series details page

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, time

sys.path.append("../../../")

# *********************************Importing required Files*********************
from ios_core.app import IOSBase
from ios_core.common import TestResult, WaitForElement
from ios_core.config import IOSConfig


class TC_HP3(IOSBase):
    description = "Verify the programme / Series Details page loads"

# ******************** Implementation of the functionality ********************
    def run_script(self, dut, logger, MobileScriptingLibrary):
        try:

            #Verifying the first programme in the first row of Home Page
            if not WaitForElement(dut,MobileScriptingLibrary.Constants.ElementType.XPath,
                                IOSConfig.XPATH_FIRST_ELEMENT_ON_HOME,
                                "First Asset on the First Row",
                                IOSConfig.MAX_WAIT_FOR_ELEMENT_TO_LOAD,
                                logger, interval=3
                                ):
                return

            #taking the asset name
            asset_name_from_carousel = dut.GetText(
                                        MobileScriptingLibrary.Constants.ElementType.XPath,
                                        IOSConfig.XPATH_FIRST_ELEMENT_ON_HOME
            )

            if not dut.TapElement(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    asset_name_from_carousel):
                self.report("Failed to tap on the Programme " + asset_name_from_carousel,
                TestResult.FAILED)
                return

            # If tapped on piece of content in row within Homepage
            self.report(asset_name_from_carousel + "' is selected",TestResult.PASSED)

            time.sleep(IOSConfig.DEFAULT_WAIT_TIME)
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
            self.test_result = True


        except Exception as e:
            self.logger.Log("Exception from run_script(): " + str(e))

# ******************************************************************************

if __name__ == "__main__":
    test_script = TC_HP3()
    test_script.run()

# ******************************************************************************
# Author: Tata Elxsi
# Date: 13 Feb 2018
# Box Type: iPad Mini
# Sky Go Version: 6.2.9
# Reviewer: <Reviewer>
# ******************************************************************************
