# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :   Lincy Robert
# Date              :   04-02-2019
# Script Version    :   1.0
# APIs covered      :   "TapElement(with index)"
# Test Scenarios    :   "For a visible element",
#                       "Valid element which does not exist on the Page",
#                       "For an element with 'visible' False",
#                       "Tap on Non-clickable element",
#                       "Element with wrong index value"
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

    apis = ("TapElement (with index)", )
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        '''
        Executes the test script
        :return:
        '''

        api_test_status = True

        try:
            test_params = self.config.tap_element_with_index_params
            for scenario in test_params.keys():
                self.logger.Log("-----Scenario: {}-----".format(test_params[scenario][0]))
                element_params = test_params[scenario][-1]
                elm_type, type = self.lib.choose_elm_type(element_params[0])
                if not type:
                    self.logger.Error("Invalid element type")
                    test_result = False
                    continue
                else:
                    if scenario == 3:
                        self.dut.TapPercent(*self.config.back_icon_percent)
                        time.sleep(5)
                    start_time = self.lib.gettimestamp()
                    tapped = self.dut.TapElement(elm_type, element_params[0][type], element_params[1])
                    end_time = self.lib.gettimestamp()

                    if tapped == test_params[scenario][1]:
                        status = "PASSED"
                    else:
                        status = "FAILED"
                        api_test_status = False

                    self.lib.report_api_status(start_time, end_time, "TapElement (with index)", status, ss_required=True)
                    self.lib.report("TapElement (with index): {}".format(test_params[scenario][0]), status)

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
