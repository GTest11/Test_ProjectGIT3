# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: NV2
# TestCase Name: Navigation_Categories_have_subcategory_catchup
#
# GIVEN I select Catch Up
# AND I locate a category in the feed which has subcategories
# WHEN I tap on that category
# THEN I will see the list of the subcategories
# AND they are shown in the same order as in the feed
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, time

sys.path.append("../../../")

# *********************************Importing required Files*********************
from ios_core.app import IOSBase
from ios_core.common import TestResult
from ios_core.config import IOSConfig


class TC_NV2(IOSBase):
    description = "Verify Catch Up category can have subcategories"

    # ******************** Implementation of the functionality ********************
    def run_script(self, dut, logger, MobileScriptingLibrary):
        try:
            # Catch Up > Channel 5 > Featured, Most Popular, By Day
            if not dut.IsElementPresent(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.CATCHUP_CATEGORY['category_level1']):
                self.report("Failed to display " + IOSConfig.CATCHUP_CATEGORY['category_level1'],
                TestResult.FAILED)
                return

            self.report(IOSConfig.CATCHUP_CATEGORY['category_level1'] + " is available in the Menu Listing",
            TestResult.PASSED)


            # Selecting the Catch up menu
            if not dut.TapElement(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.CATCHUP_CATEGORY['category_level1']):
                self.report("Failed to tap on " + IOSConfig.CATCHUP_CATEGORY['category_level1'],
                TestResult.FAILED)
                return

            self.report("Tapped on " + IOSConfig.CATCHUP_CATEGORY['category_level1'] + " on the Home Screen",
            TestResult.PASSED)

            time.sleep(IOSConfig.AVG_WAIT_FOR_ELEMENT_TO_LOAD)
            # Verifying the Catch Up TV Screen
            read_text = dut.GetText(MobileScriptingLibrary.Constants.ElementType.Name, IOSConfig.MAIN_NAV_TITLE)
            if not (read_text == IOSConfig.CATCHUPSCREEN_MAIN_NAV_TITLE):
                self.report("Failed to launch " + IOSConfig.CATCHUP_CATEGORY['category_level1'] + "Screen",
                TestResult.FAILED)
                return

            self.report("Successfully launched" + IOSConfig.CATCHUP_CATEGORY['category_level1'] + " Screen launched",
            TestResult.PASSED)

            # inside Catch up
            if not dut.IsElementPresent(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.CATCHUP_CATEGORY['category_level2']):
                self.report("Failed to display " + IOSConfig.CATCHUP_CATEGORY['category_level2'],
                TestResult.FAILED)
                return

            self.report("Successfully displayed"+IOSConfig.CATCHUP_CATEGORY['category_level2'] + " is available in the Menu Listing",
            TestResult.PASSED)

            # Selecting the Catch up menu
            if not dut.TapElement(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.CATCHUP_CATEGORY['category_level2']):
                self.report("Failed to tap on " + IOSConfig.CATCHUP_CATEGORY['category_level2'],
                TestResult.FAILED)
                return

            self.report("Tapped on " + IOSConfig.CATCHUP_CATEGORY['category_level2'] + " on the Home Screen",
            TestResult.PASSED)

            # Verifying the Catch Up TV Screen
            read_text = dut.GetText(MobileScriptingLibrary.Constants.ElementType.Name, IOSConfig.MAIN_NAV_TITLE)
            if not (read_text == IOSConfig.CATCHUP_CATEGORY['category_level2']):
                self.report("Failed to launch " + IOSConfig.CATCHUP_CATEGORY['category_level2'] + "Screen",
                TestResult.FAILED)
                return

            self.report("Successfully launched"+IOSConfig.CATCHUP_CATEGORY['category_level2'] + "Screen launched",
            TestResult.PASSED)
            # Under Channel 5
            list_of_category = IOSConfig.CATCHUP_CATEGORY['category_level3']
            category_1 = dut.IsElementPresent(
                MobileScriptingLibrary.Constants.ElementType.Name,
                list_of_category[0])

            category_2 = dut.IsElementPresent(
                MobileScriptingLibrary.Constants.ElementType.Name,
                list_of_category[1])

            category_3 = dut.IsElementPresent(
                MobileScriptingLibrary.Constants.ElementType.Name,
                list_of_category[2])

            # Verifying the sub categories
            if not (category_1 and category_2 and category_3):
                self.report("Failed to find the subcategories under the category " +
                IOSConfig.CATCHUP_CATEGORY['category_level2'],
                TestResult.FAILED)
                self.logger.Log("Failed to find the subcategories - "
                                + list_of_category[0] + ", "
                                + list_of_category[1] + ", "
                                + list_of_category[2]
                                )
                return

            self.report("Subcategories are available under " +
            IOSConfig.CATCHUP_CATEGORY['category_level2'],
            TestResult.PASSED)
            self.logger.Log(
                "Subcategories are available -  "
                + list_of_category[0] + ", "
                + list_of_category[1] + ", "
                + list_of_category[2]
            )
            self.test_result = True

        except Exception as e:
            self.logger.Log("Exception from run_script(): " + str(e))

# ******************************************************************************

if __name__ == "__main__":
    test_script = TC_NV2()
    test_script.run()

# ******************************************************************************
# Author: Tata Elxsi
# Date: 08 Feb 2018
# Box Type: iPad Mini
# Version: 6.2.9
# Reviewer: <Reviewer>
# ******************************************************************************
