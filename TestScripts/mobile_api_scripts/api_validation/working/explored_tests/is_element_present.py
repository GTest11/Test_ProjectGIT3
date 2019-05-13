# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            : Shameena HA
# Date              :   29-11-2018
# Script Version    : 1.0
# Modification details:
# APIs covered      :   "IsElementPresent"
# Test Scenario: "Element does not exist on the Page",
#                 "For a visible element",
#                 "For an element with 'visible' False"
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
    apis = ('IsElementPresent',)
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        test_result = True
        params = self.config.is_element_present_params
        try:
            for param in params.keys():
                self.logger.Log("--- Scenario: {} ---".format(params[param][0]))

                if param == 2:
                    if not self.dut.Tap(*self.config.C_TAP_PLAYBACK):
                        self.logger.Error("Tap failed, exiting the test..")
                        test_result = False
                        return False
                    time.sleep(10) # waiting for the video player to load

                elm_type, type = self.lib.choose_elm_type(params[param][-1])
                if not type:
                    self.logger.Error("Invalid element type")
                    test_result = False
                    continue

                start_time = self.lib.gettimestamp()
                present = self.dut.IsElementPresent(elm_type, params[param][-1][type])
                end_time = self.lib.gettimestamp()
                if present == params[param][1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False

                self.lib.report_api_status(start_time, end_time, "IsElementPresent", status, ss_required=True)
                self.lib.report("IsElementPresent: {}".format(params[param][0]), status)

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
