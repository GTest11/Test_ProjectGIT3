# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author                :   Lincy Robert
# Date                  :   30-11-2018
# Script Version        :   1.0
# Modification details  :
# APIs covered          :   "UploadScreenshot"
# Test Scenario         :   "Valid parameters, 
#                           InValid parameters: Invalid Screenshot, 
#                           Invalid parameters: Lengthy image name, 
#                           InValid parameters: Non base64ImageString as Screenshot"
# '''''''''''''''''''''''''''TEST CASE DETAILS' - END '''''''''''''''''''''''''''''''''

import os
import sys
sys.path.append('../')

from library.api_test_base import apiTestBase


class api_test(apiTestBase):
    # the class which handles the script intention.
    # this overrides base class run_api_test()

    # class variables
    apis = ('UploadScreenshot',)
    script_name = os.path.basename(__file__)

    def run_api_test(self):
        test_result = True
        try:
            test_params = self.config.upload_screenshot_params
            for scenario in test_params.keys():
                self.logger.Log("Scenario: {}".format(test_params[scenario][0]))
                param_1 = test_params[scenario][2][0]
                param_2 = test_params[scenario][2][-1]
                expected_status = test_params[scenario][1]

                if param_2 == "obtained_screenshot":
                    param_2 = self.dut.GetScreenshot()
                elif param_2 == "captured_image":
                    capture_params = self.config.capture_image_params
                    param_2 = self.dut.validator.CaptureImage(*capture_params[1][2])

                start_time = self.lib.gettimestamp()
                captured_image_name = self.dut.validator.UploadScreenshot(param_1, param_2)
                end_time = self.lib.gettimestamp()

                if captured_image_name is None or captured_image_name == '':
                    api_status = False
                else:
                    api_status = True
                status = "PASSED"
                if api_status != expected_status:
                    test_result = False
                    status = "FAILED"
                    
                self.lib.report_api_status(start_time, end_time, "UploadScreenshot", status, ss_required=True)
                self.lib.report("UploadScreenshot: {}".format(test_params[scenario][0]), status)
                
        except Exception as e:
            self.logger.Error("Error in run_api_test() " + str(e))
            test_result = False
        finally:
            self.test_result = test_result


def main():
    testobj = api_test()
    testobj.run_test(testobj.script_name, testobj.apis)


if __name__ == '__main__':
    main()
