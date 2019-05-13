# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :   Lincy Robert
# Date              :   31-01-2019
# Script Version    :   1.0
# Modification details:
# APIs covered      :   Lock, Unlock, Shake
# Test Scenario     :   "Lock while device is not Locked"
#                       "Lock while device is already Locked"
#                       "Unlock while device is Locked"
#                       "Unlock while device is already Unlocked"
#                       "Shake while device is not Locked"
#                       "Shake while device is already Locked"
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import os
import sys
import time
sys.path.append('../')

from library.api_test_base import apiTestBase


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class api_test(apiTestBase):

    # the class which handles the script intention.
    # this overrides base class run_api_test()

    apis = (
        "Lock", "Unlock", "Shake",
    )
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        '''
        Executes the test script
        :return: test status as True or False
        '''

        api_test_status = True

        try:
            w, h = self.lib.get_image_resolution()
            api_dict = {
                "Lock": self.dut.Lock,
                "Unlock": self.dut.Unlock,
                "Shake": self.dut.Shake,
            }
            device_platform = self.lib.get_dut_platform()
            if not self.dut.CloseApp():
                api_test_status = False
                self.logger.Error("CloseApp API failed. Hence, skipping test execution")
                self.lib.report("CloseApp API", "FAILED", ss_required=True)
            else:
                time.sleep(3)
                for api in self.apis:
                    if api == "Unlock" and device_platform == 'iOS':
                        continue
                    test_params = self.config.unlock_params if api == 'Unlock' else self.config.lock_params
                    for scenario in test_params.keys():
                        self.logger.Log("----- API :- {}: Scenario: {} -----".format(api, test_params[scenario][0]))
                        if (api == "Lock" and scenario == 1) or (api == "Unlock" and scenario == 0) or (api == "Shake"
                                                                                                        and scenario == 1):
                            self.logger.Error("Locking as Precondition!!!")
                            self.dut.Lock()
                            time.sleep(2)
                        capture_before_api = self.dut.validator.CaptureImage(0, 0, w, h, "capture_before_api", 90, 0)
                        start_time = self.lib.gettimestamp()
                        response = api_dict[api]()
                        end_time = self.lib.gettimestamp()
                        time.sleep(2)
                        capture_after_api = self.dut.validator.CaptureImage(0, 0, w, h, "capture_after_api", 90, 0)
                        
                        # post condition: Unlock the device to start with next scenario
                        if api != 'Unlock':
                            if device_platform == 'iOS':
                                time.sleep(12)  #iOS devices gets automatically unlocked after 10 seconds
                            else:
                                self.dut.Unlock() 
                                time.sleep(12)
                            validate_capture_output = True if capture_after_api == '' else False
                        else:
                            validate_capture_output = True if capture_after_api != '' else False                            
                        
                        capture_after_post_condition = self.dut.validator.CaptureImage(0, 0, w, h, "capture_after_post_condition", 90, 0)

                        matched = self.dut.validator.ImageMatch("capture_before_api", "capture_after_post_condition", 2, "38")
                        if validate_capture_output and matched:
                            status = "PASSED"
                        else:
                            status = "FAILED"
                            api_test_status = False
                        self.lib.report_api_status(start_time, end_time, api, status, ss_required=False)
                        self.lib.report(str(api)+": "+str(test_params[scenario][0]), status)

        except Exception as e:
            self.logger.Error("Error in run_api_test() " + str(e))
            api_test_status = False

        finally:
            self.test_result = api_test_status


def main():
    testobj = api_test()
    testobj.run_test(testobj.script_name, testobj.apis)


if __name__ == '__main__':
    main()
