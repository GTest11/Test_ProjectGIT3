# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: CR1
# TestCase Name: CarouselOnHomepage_Load_Carousel
#
# GIVEN that I am on the homepage
# WHEN I render the carousel content
# THEN I can see the Asset Title, the associated channel
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import sys, time

sys.path.append("../../../")

# *********************************Importing required Files*********************
from ios_core.app import IOSBase
from ios_core.common import TestResult, WaitForElement
from ios_core.config import IOSConfig


class TC_CR1(IOSBase):
    description = "Asset Title and associated Channel are present on the Carousel"

    # ******************** Implementation of the functionality ********************
    def run_script(self, dut, logger, MobileScriptingLibrary):
        try:
            # Asset Name
            if not WaitForElement(
                dut,
                MobileScriptingLibrary.Constants.ElementType.XPath,
                IOSConfig.XPATH_ASSETNAME_CAROUSEL,
                "Movie Name",
                IOSConfig.MAX_WAIT_FOR_ELEMENT_TO_LOAD,
                logger,interval=3):
                self.report("Failed to display Movie Name", TestResult.FAILED)
                return
            self.report("Movie Name is present on the screen", TestResult.PASSED)
            asset_name = dut.GetText(
                MobileScriptingLibrary.Constants.ElementType.XPath,
                IOSConfig.XPATH_ASSETNAME_CAROUSEL)
            if asset_name == None:
                self.report("Failed to read the Asset Name from Carousel",TestResult.FAILED )
                return

            self.report("Asset Name - {} -  is available on the Carousel".format(asset_name),TestResult.PASSED )

            # Channel Info
            if not WaitForElement(
                dut,
                MobileScriptingLibrary.Constants.ElementType.XPath,
                IOSConfig.XPATH_CHANNEL_CAROUSEL,
                "Channel Logo",
                IOSConfig.MAX_WAIT_FOR_ELEMENT_TO_LOAD,
                logger, interval=3 ):
                self.report("Failed to display Channel Logo", TestResult.FAILED)
                return
            self.report("Channel Logo is present on the screen", TestResult.PASSED)
            self.test_result = True

        except:
            self.logger.Log("Exception from run_script(): " + str(sys.exc_info()[1]))

# ******************************************************************************

if __name__ == "__main__":
    test_script = TC_CR1()
    test_script.run()

# ******************************************************************************
# Author: Tata Elxsi
# Date: 07 Feb 2018
# Box Type: iPad Mini
# Sky Go Version: 6.2.9
# Reviewer: <Reviewer>
# ******************************************************************************
