# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            : Shameena HA
# Date              :   26-11-2018
# Script Version     : 1.0
# Modification details:
# APIs covered      :   "GetElementCount"
# Test Scenario:  "Mutliple elements", Single element of given type, No element present
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
            bstatus = False
            for scenario in test_params.keys():
                self.logger.Log("Scenario: {}".format(test_params[scenario][0]))
                elm_type, type = self.lib.choose_elm_type(test_params[scenario][-1])
                start_time = self.lib.gettimestamp()
                count = self.dut.GetElementCount(elm_type, test_params[scenario][-1][type])
                end_time = self.lib.gettimestamp()
                bstatus = False
                self.logger.Log("Scenario - {}".format(scenario))
                if scenario == 2 and count == 0:
                    bstatus = True
                elif count:
                    bstatus = True
                else:
                    bstatus = False

                self.test_result = True
                if bstatus == test_params[scenario][1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    # to set the test status
                    test_result = False

                self.lib.report("API: GetElementCount Output", count, image_required=False)
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
