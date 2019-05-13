# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            : Shameena HA
# Date              :   28-11-2018
# Script Version    : 1.0
# Modification details:
# APIs covered      :   "WaitForCheckpoint"
# Test Scenario: "Valid parameters, DUT already on checkpoint screen",
#                 "Valid parameters, No screen transition to the checkpoint screen",
#                 "Valid parameters, screen transition to the checkpoint screen",
#                 "Valid parameters, very small time to wait, 2 sec",
#                 "InValid parameters, non existing checkpoint name",
#                 "InValid parameters, negative time to wait, -20 sec",
#                 "InValid parameters, negative initial delay, -2 sec",
#                 "InValid parameters, Initial delay greater than TimeToWait",
#                 "Valid parameters, Maximum TimeToWait = WD Timeout",
#
# '''''''''''''''''''''''''''TEST CASE DETAILS' - END '''''''''''''''''''''''''''''''''

import os
import sys
import time
sys.path.append('../')

from library.api_test_base import apiTestBase

class api_test(apiTestBase):
    # the class which handles the script intention.
    # this overrides base class run_api_test()

    # class variables
    apis = ('WaitForCheckpoint',)
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        test_result = True
        params = self.config.wait_for_chkpt_params        

        try:
            for param in params.keys():
                self.logger.Log("--- Scenario: {} --- ".format(params[param][0]))
                if param == 3:
                    if not self.dut.Tap(*self.config.C_TAP_PLAYBACK):
                        self.logger.Error("Failed to tap on the video")
                        test_result = False
                        continue
                    time.sleep(2)

                if param == 8:
                    if not self.lib.element_ops(elm_name=self.config.navbar_home, action='tap'):
                        self.logger.Error("Failed to tap on Home Button on the Navigation Bar")
                        test_result = False
                        continue
                    time.sleep(3)

                if not self.dut.validator.StartCaptureZapFrames(self.config.captureZapTime):
                    self.logger.Error("Failed to start capture frames")
                    test_result = False
                    return False

                start_time = self.lib.gettimestamp()
                chkpt_available = self.dut.validator.WaitForCheckpoint(*params[param][-1])
                end_time = self.lib.gettimestamp()
                if not self.dut.validator.StopCaptureZapFrames():
                    self.logger.Error("Failed to Stop capturing frames")

                if chkpt_available >= 0:
                    chkpt_available = 1
                if chkpt_available and chkpt_available == params[param][1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False

                self.lib.report_api_status(start_time, end_time, "WaitForCheckpoint", status, ss_required=True)
                self.lib.report("WaitForCheckpoint: {}".format(params[param][0]), status)

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
