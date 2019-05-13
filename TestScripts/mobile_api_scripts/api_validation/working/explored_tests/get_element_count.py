# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            : Shameena HA
# Date              :   26-11-2018
# Script Version    : 1.0
# APIs covered      :   "GetElementCount"
# Test Scenario:    "Mutliple elements", Single element of given type, No element present
#
# '''''''''''''''''''''''''''TEST CASE DETAILS' - END '''''''''''''''''''''''''''''''''

import os
import sys
sys.path.append('../')

from library.api_test_base import apiTestBase


class api_test(apiTestBase):
    # the class which handles the script intention.
    # this overrides base class run_api_test()

    # class variables
    apis = ('GetElementCount',)
    script_name = os.path.basename(__file__)

    def run_api_test(self):
        test_result = True

        try:
            test_params = self.config.get_element_count_params
            for scenario in test_params.keys():
                self.logger.Log("Scenario: {}".format(test_params[scenario][0]))
                elm_type, type = self.lib.choose_elm_type(test_params[scenario][-1])
                if not type:
                    self.logger.Error("Invalid element type")
                    test_result = False
                    return False

                start_time = self.lib.gettimestamp()
                count = self.dut.GetElementCount(elm_type, test_params[scenario][-1][type])
                end_time = self.lib.gettimestamp()
                if scenario == 2 and count == 0:
                    elem_count_status = True
                elif count:
                    elem_count_status = True
                else:
                    elem_count_status = False

                if elem_count_status == test_params[scenario][1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False # to set the test status

                self.lib.report_api_status(start_time, end_time, "GetElementCount", status, ss_required=True)

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
