# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            :   Shameena HA
# Date              :   31-01-2019
# Script Version    :   1.0
# APIs covered      :   "Tap"
# Test Scenario:     1. Tap on anywhere on an element
#                    2. invalid coordinates
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
    apis = ('Tap',)
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        '''
        Script part of the framework.
        :return: True or False
        '''

        test_result = True
        params = self.config.tap_params

        try:
            for param in params.keys():
                self.logger.Log("--- Scenario: {} ---".format(params[param][0]))

                start_time = self.lib.gettimestamp()
                tapped = self.dut.Tap(*params[param][-1])
                end_time = self.lib.gettimestamp()
                if tapped and param == 1:
                    if self.dut.validator.DetectMotion(*self.config.detect_motion_check):
                        self.lib.report("Motion detected", "PASSED", ss_required=True)
                    else:
                        self.lib.report("Motion not detected, check the coordinates", "FAILED", ss_required=True)

                if tapped == params[param][1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False

                self.lib.report_api_status(start_time, end_time, "Tap", status, ss_required=True)
                self.lib.report("Tap: {}".format(params[param][0]), status, ss_required=False)

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
