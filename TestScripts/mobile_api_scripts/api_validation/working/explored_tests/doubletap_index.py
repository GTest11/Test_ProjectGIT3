# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :   Shameena HA
# Date              :   30-01-2019
# Script Version    :   1.0
# APIs covered      :   DoubleTapElement with Index
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

    apis = ("DoubleTapElement with Index",
        )
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        '''
        Executes the test script
        :return: True or False
        '''

        test_status = True

        try:

           params = self.config.doubletap_idx_params

           for param in params:
                self.logger.Log(" ----  Scenario:  {}  ----".format(params[param][0]))
                element = params[param][-1]

                if param == 0:
                    # tapping on search icon
                    if not self.lib.element_ops(self.config.search_icon, action="tap"):
                        self.lib.report("Failed to find an element with visible false", "FAILED", False)
                        test_status = False
                        continue

                elm_type, type = self.lib.choose_elm_type(element[0])
                if not type:
                    self.logger.Error("Invalid element type")
                    return False

                start_time = self.lib.gettimestamp()
                tapped = self.dut.DoubleTapElement(elm_type, element[0][type], element[1])
                end_time = self.lib.gettimestamp()
                if tapped == params[param][1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_status = False
                self.lib.report_api_status(start_time, end_time, "DoubleTap Index", status, ss_required=True)


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
