# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :   Shameena HA
# Date              :   29-01-2019
# Script Version    :   1.0
# APIs covered      :   DoubleTapElement
# Test Scenario     :   1. Invalid element id
#                       2. on an element with visible property False, but available on the screen
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

    apis = ("DoubleTapElement",
        )
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        '''
        Executes the test script

        :return: True or False
        '''

        test_status = True

        try:

            params = self.config.doubletap_params
            # doubletap
            # tapping on search icon

            for param in params:
                self.logger.Log(" ----  Scenario:  {}  ----".format(params[param][0]))
                if param == 0:
                    if not self.lib.element_ops(self.config.search_icon, action="tap"):
                        self.lib.report("Failed to find an element with visible false", "FAILED", False)
                        test_status = False
                        continue

                elm_type, type = self.lib.choose_elm_type(params[param][-1])
                if not type:
                    self.logger.Error("Invalid element type")
                    return False

                start_time = self.lib.gettimestamp()
                tapped = self.dut.DoubleTapElement(elm_type, params[param][-1][type])
                end_time = self.lib.gettimestamp()
                if tapped == params[param][1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_status = False
                self.lib.report_api_status(start_time, end_time, "DoubleTap", status, ss_required=False)
                self.lib.report("DoubleTap - {}".format(params[param][0]), status, ss_required=False)

        except Exception as e:
            self.logger.Error("Error in run_api_test() " + str(e))
            test_status = False

        finally:
            self.test_result = test_status


def main():
    testobj = api_test()
    testobj.run_test(testobj.script_name, testobj.apis)


if __name__ == '__main__':
    main()
