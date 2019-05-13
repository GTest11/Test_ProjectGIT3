# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            :   Shameena HA
# Date              :   31-01-2019
# Script Version    :   1.0
# APIs covered      :   "Click"
# Test Scenario:     1. on a clickable element
#                    2. on a non clickable element
#                    3. on an element with visible property False, but available on the screen
#                    4. Element does not exist on the Page
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
    apis = ('Click',)
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        '''
        Script part of the framework.

        :return: True or False
        '''

        test_result = True
        params = self.config.click_params

        try:
            for param in params.keys():
                self.logger.Log("--- Scenario: {} ---".format(params[param][0]))

                elm_type, type = self.lib.choose_elm_type(params[param][-1])
                if not type:
                    self.logger.Error("Invalid element type")
                    test_result = False
                    return False

                start_time = self.lib.gettimestamp()
                present = self.dut.Click(elm_type, params[param][-1][type])
                end_time = self.lib.gettimestamp()
                if present == params[param][1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False

                self.lib.report_api_status(start_time, end_time, "Click", status, ss_required=True)

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
