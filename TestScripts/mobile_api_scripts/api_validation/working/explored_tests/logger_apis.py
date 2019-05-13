# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            : Shameena HA
# Date              :   11-12-2018
# Script Version    : 1.0
# APIs covered      :   'Error', 'Log', 'Warn'
# Test Scenario: Parameter boundary value checking
#                 Empty string/Invalid status
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
    apis = ('Error', 'Log', 'Warn',)
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        test_result = True
        log_params = {
           'Error': self.config.logger_error_params,
           'Log':  self.config.logger_log_params,
           'Warn':  self.config.logger_warn_params
        }

        try:
            for log_param in log_params.keys():
                params = log_params[log_param]

                for param in params.keys():
                    self.logger.Log("--- Scenario: {} --- ".format(params[param][0]))
                    if log_param == 'Error':
                        self.logger.Error(params[param][-1])

                    if log_param == 'Log':
                        self.logger.Log(params[param][-1])

                    if log_param == 'Warn':
                        self.logger.Warn(params[param][-1])

                    self.lib.report("{}".format(log_param), "PASSED")

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
