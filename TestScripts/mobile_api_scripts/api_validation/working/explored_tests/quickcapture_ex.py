# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author                : Lincy Robert
# Date                  : 04-02-2019
# Script Version        : 1.0
# Modification details  :
# APIs covered          : "QuickCaptureEx"
# Test Scenario         : "Lengthy image name"
#                         "Invalid image format"
#                         "Case sensitivity of valid image formats"
#                         "Valid image name, valid image format"
#                         "Valid image name (containing numbers), valid image format"
#                         "Invalid image name (containing special characters), valid image format"
# '''''''''''''''''''''''''''TEST CASE DETAILS' - END '''''''''''''''''''''''''''''''''

import os
import sys
sys.path.append('../')

from library.api_test_base import apiTestBase

class api_test(apiTestBase):
    # the class which handles the script intention.
    # this overrides base class run_api_test()

    # class variables
    apis = ('QuickCaptureEx',)
    script_name = os.path.basename(__file__)

    def run_api_test(self):
        test_result = True
        try:
            test_params = self.config.quick_capture_ex_params
            for scenario in test_params.keys():
                self.logger.Log("-----Scenario: {}-----".format(test_params[scenario][0]))
                start_time = self.lib.gettimestamp()
                captured_path = self.dut.validator.QuickCaptureEx(*test_params[scenario][-1])
                end_time = self.lib.gettimestamp()
                self.logger.Log("Captured image's absolute path returned by API : "+str(captured_path))
                captured = True if captured_path != '' else False
                if captured == test_params[scenario][1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False
                self.lib.report_api_status(start_time, end_time, "QuickCaptureEx", status, ss_required=True)
                self.lib.report("QuickCaptureEx: {}".format(test_params[scenario][0]), status)

        except Exception as e:
            self.logger.Error("Error in run_api_test() " + str(e))
            test_result = False

        finally:
            # to set the test status
            self.test_result = test_result


def main():
    testobj = api_test()
    testobj.run_test(testobj.script_name, testobj.apis)


if __name__ == '__main__':
    main()
