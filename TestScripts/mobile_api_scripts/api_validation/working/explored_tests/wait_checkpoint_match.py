# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            : Shameena HA
# Date              :   30-01-2019
# Script Version    : 1.0
# Modification details:
# APIs covered      :   "WaitCheckpointMatch"
# Test Scenario:
#              "Valid parameter, OCR checkpoint"
#              "Valid parameter, Multi line OCR checkpoint"
#               "Valid parameter, IC checkpoint, pixel"
#              "Valid parameter, IC checkpoint, rmse"
#              "Valid parameter, already on checkpoint screen"
#              "Valid parameter, Max wait equal to WD timeout"
#              "Valid parameter, Negative values for timeToWait and waitGap",
#              "Valid parameter, timeToWait < waitGap"
#               "Checkpoint does not exist"
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
    apis = ('WaitCheckpointMatch',)
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        test_result = True
        params = self.config.wait_chkpt_match_params

        try:
            for param in params.keys():
                self.logger.Log("--- Scenario: {} --- ".format(params[param][0]))

                if param == 7:
                    if not self.lib.tap_element(self.config.account_icon):
                        self.logger.Error("Failed to tap account icon")
                        test_result = False
                        continue

                self.chkpt.init(params[param][2])
                start_time = self.lib.gettimestamp()
                matched = self.dut.validator.WaitCheckPointMatch(self.chkpt, params[param][-2], params[param][-1])
                end_time = self.lib.gettimestamp()
                if matched == params[param][1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False

                self.lib.report_api_status(start_time, end_time, "WaitCheckPointMatch", status, ss_required=True)
                self.lib.report("WaitCheckPointMatch: {}".format(params[param][0]), status, ss_required=False)

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
