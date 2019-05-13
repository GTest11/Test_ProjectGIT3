# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author                : Shameena HA
# Date                  : 26-11-2018
#Script Version         : 1.0
#Modification details   :
# APIs covered          : "QuickCapture"
#Test Scenario          : "Valid Scenario: QuickCapture from current active source"
#                         "Valid Scenario: QuickCapture from changed active source"
#                         "Invalid Scenario: QuickCapture with lengthy name"
#                         "Invalid Scenario: QuickCapture with name containing special characters"
#                         "Valid Scenario: QuickCapture with name containing numbers"
# '''''''''''''''''''''''''''TEST CASE DETAILS' - END '''''''''''''''''''''''''''''''''

import os
import sys
sys.path.append('../')

from library.api_test_base import apiTestBase


class api_test(apiTestBase):
    # the class which handles the script intention.
    # this overrides base class run_api_test()

    # class variables
    apis = ('QuickCapture',)
    script_name = os.path.basename(__file__)

    def run_api_test(self):
        test_result = True
        try:
            # Scenario: 1
            self.logger.Log("--- Valid Scenario: QuickCapture from current active source ---")
            captured = self.test_quick_capture(self.config.IMG_NAME)
            if captured:
                status = "PASSED"
            else:
                test_result = False
                status = "FAILED"
            self.lib.report("QuickCapture: QuickCapture from current active source", status)

            # Scenario: 2
            self.logger.Log("--- Valid Scenario: QuickCapture from changed active source ---")
            if not self.dut.validator.SetActiveFrameSource(self.config.available_video_source):
                self.logger.Error("Failed to change source")
                test_result = False
                return False

            captured = self.test_quick_capture(self.config.IMG_NAME)
            if captured:
                status = "PASSED"
            else:
                test_result = False
                status = "FAILED"
            self.lib.report("QuickCapture: QuickCapture from changed active source", status)

            # Scenario: 3
            self.logger.Log("--- Invalid Scenario: QuickCapture with lengthy name ---")
            captured = self.test_quick_capture(self.config.LONG_IMG_NAME)
            if not captured:
                status = "PASSED"
            else:
                test_result = False
                status = "FAILED"
            self.lib.report("QuickCapture: QuickCapture with lengthy image name", status)

            # Scenario: 4
            self.logger.Log("--- Invalid Scenario: QuickCapture with name containing special characters ---")
            captured = self.test_quick_capture(self.config.IMG_NAME_SPL)
            if not captured:
                status = "PASSED"
            else:
                test_result = False
                status = "FAILED"
            self.lib.report("QuickCapture: QuickCapture with name containing special characters", status)

            # Scenario: 5
            self.logger.Log("--- Valid Scenario: QuickCapture with name containing numbers ---")
            captured = self.test_quick_capture(self.config.IMAGE_NAME_NUMBER)
            if captured:
                status = "PASSED"
            else:
                test_result = False
                status = "FAILED"
            self.lib.report("QuickCapture: Valid Scenario: QuickCapture with name containing numbers", status)

        except Exception as e:
            self.logger.Error("Error in run_api_test() " + str(e))
            test_result = False

        finally:
            self.test_result = test_result

    def test_quick_capture(self, image_name="test_img"):
        start_time = self.lib.gettimestamp()
        captured = self.dut.validator.QuickCapture(image_name)
        end_time = self.lib.gettimestamp()
        if captured:
            capture_result = True
            status = "PASSED"
        else:
            capture_result = False
            status = "FAILED"
        self.lib.report_api_status(start_time, end_time, "QuickCapture", status, ss_required=True)
        return capture_result


def main():
    testobj = api_test()
    testobj.run_test(testobj.script_name, testobj.apis)


if __name__ == '__main__':
    main()
