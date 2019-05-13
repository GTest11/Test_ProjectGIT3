# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            : Shameena HA
# Date              :   11-12-2018
# Script Version    : 1.0
# APIs covered      : 'CommitStepResult', 'CommitTestResult',
# Test Scenario:    Parameter boundary value checking
#                   Empty string/Invalid status
# Note: This test is designed in such a way that, this will PASS always,
#       if there is no exception.
#       This test requires a manual validation to decice on whether
#       the test is a PASS or FAIL
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
    apis = ('CommitStepResult', 'CommitTestResult',)
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        test_result = True
        report_params = {
           'commit_step': self.config.commit_step_params,
           'commit_test':  self.config.commit_test_params,
        }
        status = "PASSED"
        start_time = end_time = 0
        try:
            for report_param in report_params.keys():
                self.logger.Log("--- API: {} --- ".format(report_param))
                test_param = report_params[report_param]
                for param in test_param:
                    self.logger.Log("--- Scenario: {} - {} --- ".format(report_param, test_param[param][0]))
                    if report_param == 'commit_step':
                        start_time = self.lib.gettimestamp()
                        self.dut.CommitStepResult(*test_param[param][-1])
                        end_time = self.lib.gettimestamp()

                    if report_param == 'commit_test':
                        start_time = self.lib.gettimestamp()
                        self.dut.CommitTestResult(test_param[param][-1])
                        end_time = self.lib.gettimestamp()
                    self.lib.report_api_status(start_time, end_time, report_param, status, ss_required=True)
                    self.lib.report(report_param + ": {}".format(test_param[param][0]), status, ss_required=False)

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
