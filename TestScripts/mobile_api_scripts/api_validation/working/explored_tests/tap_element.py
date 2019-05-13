# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :   Lincy Robert
# Date              :   01-02-2019
# Script Version    :   1.0
# APIs covered      :   "TapElement"
# Test Scenarios    :   "Element does not exist on the Page",
#                       "For a visible element",
#                       "For an element with 'visible' False",
#                       "Tap on Non-clickable element"
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import os
import sys
import time
import json
sys.path.append('../')

from library.api_test_base import apiTestBase


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class api_test(apiTestBase):

    # the class which handles the script intention.
    # this overrides base class run_api_test()

    apis = ("TapElement", )
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        '''
        Executes the test script
        :return:
        '''

        api_test_status = True

        try:
            test_params = self.config.tap_element_params
            for scenario in test_params.keys():
                self.logger.Log("----- Scenario: {} -----".format(test_params[scenario][0]))

                elm_type, type = self.lib.choose_elm_type(test_params[scenario][-1])
                if not type:
                    self.logger.Error("Invalid element type")
                    api_test_status = False
                    continue

                start_time = self.lib.gettimestamp()
                tapped = self.dut.TapElement(elm_type, test_params[scenario][-1][type])
                end_time = self.lib.gettimestamp()

                if scenario == 2:
                    self.dut.TapPercent(*self.config.back_icon_percent)
                    time.sleep(3)

                if tapped == test_params[scenario][1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    api_test_status = False

                self.lib.report_api_status(start_time, end_time, "TapElement", status, ss_required=True)
                self.lib.report("TapElement: {}".format(test_params[scenario][0]), status)

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
