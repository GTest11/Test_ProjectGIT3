# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: HP1
# TestCase Name: Homepage_Carousel_Stops_Scrolling
#
# GIVEN that I am on the homepage
# WHEN I am inactive for 6 seconds
# THEN the carousel manually scrolls to the next content item
# WHEN I manually swipe to view the next item
# THEN the carousel stops auto scrolling
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, time

sys.path.append("../../../")

# *********************************Importing required Files*********************

from ios_core.app import IOSBase
from ios_core.common import TestResult
from ios_core.config import IOSConfig
from ios_core.utils import detect_motion, take_screen_shot 


class TC_HP2(IOSBase):
    description = "Verify Homepage Carousel stops scrolling after a swipe"

    # ******************** Implementation of the functionality ********************
    def run_script(self, dut, logger, MobileScriptingLibrary):
        try:
            #Initial wait to load the Carousel
            time.sleep(IOSConfig.AVG_WAIT_FOR_ELEMENT_TO_LOAD)

            # Setting a region of Interest
            carousel_coords = IOSConfig.HOME_CAROUSEL_COORDS
            #take_screen_shot(dut)
            #dm = detect_motion(
                    #dut, carousel_coords, 2,
                    #IOSConfig.HOME_CAROUSEL_DISPLAY_TIME, 95, logger)
            
            dm=dut.validator.DetectMotion(10,80,200,200,5,5,"10")
                #"statement(s)"
            #else:
                #"statement(s)"

            if dm:
                self.report("Home Page Carousel auto scrolls in Six Seconds",
                TestResult.PASSED, image=False)
            else:
                self.report("Home Page Carousel does not scroll automatically",
                TestResult.FAILED, image=False)
                return

            # Swipe the Carousel to stop suto scrolling
            if dut.Swipe(*IOSConfig.CORD_SWIPE_CAROUSEL):
                self.report("Swiped on the Home Page Carousel",
                TestResult.PASSED)
            else:
                self.report("Failed to swipe on the Home Page Carousel",
                TestResult.FAILED)
                return

            ## Detect motion again
            #dm = detect_motion(
                    #dut, carousel_coords, 2,
                    #IOSConfig.HOME_CAROUSEL_DISPLAY_TIME, 95, logger
                #)
            dtm=dut.validator.DetectMotion(10,80,200,200,5,5,"10")
            if dtm:
                self.report("Auto scrolling did not stopped in Home Page Carousel",
                TestResult.FAILED, image=False)
            else:
                self.report("Home Page Carousel stopped scrolling after swipe",
                TestResult.PASSED, image=False)
                self.test_result = True

        except Exception as e:
            self.logger.Log("Exception from run_script(): " + str(e))


# ******************************************************************************
if __name__ == "__main__":
    test_script = TC_HP2()
    test_script.run()

# ******************************************************************************
# Author: Tata Elxsi
# Date: 07 Feb 2018
# Box Type: iPad Mini
# Sky Go Version: 6.2.9
# Reviewer: <Reviewer>
# ******************************************************************************
