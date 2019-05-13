# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            : Shameena HA
# Date              :   29-11-2018
# Script Version    : 1.0
# Modification details:
# APIs covered      :   "Init "
# Test Scenario: "Non Existing checkpoint",
#                 "Checkpoint with lengthy name",
#                 "Checkpoint which is not created for the target device"
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
    apis = ('Init',)
    script_name = os.path.basename(__file__)

    def run_api_test(self):
        test_result = True
        params = self.config.init_params
        try:
            for param, param_value in params.items():
                self.logger.Log("--- Scenario: {} ---".format(param_value[0]))
                start_time = self.lib.gettimestamp()
                done = self.chkpt.init(param_value[-2])
                end_time = self.lib.gettimestamp()
                timetowait = param_value[-1][0]
                waitgap = param_value[-1][1]

                matched = False
                try:
                    matched = self.dut.validator.WaitCheckPointMatch(self.chkpt, timetowait, waitgap)
                except Exception as e:
                    self.logger.Log("Could not find a match - {}".format(e))
                    matched = False

                if matched == param_value[1] and not done:
                # validated = self.dut.validator.validateCheckPoint(self.chkpt)
                # self.logger.Log("validated - {}".format(validated))

                # if done == param_value[1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False

                self.lib.report_api_status(start_time, end_time, "Init", status, ss_required=True)
                self.lib.report("Init: {}".format(param_value[0]), status)
                time.sleep(3) # wait between next scenario test

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
