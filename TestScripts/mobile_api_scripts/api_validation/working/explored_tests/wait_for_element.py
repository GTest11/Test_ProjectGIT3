# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            : Shameena HA
# Date              :   04-12-2018
# Script Version    : 1.0
# Modification details:
# APIs covered      :   "WaitForElement"
# Test Scenario: Invalid Parameters: TimeToWait=0, element available
#                 Valid Parameters: Wait till WD timeout time, element not available
#                 Valid Parameters: Min wait time, element not available
#                 Valid Parameters: Min wait time, element available
#                 Valid Parameters: Element already available
#                 Invalid Parameters: Negative TimeToWait
#                 Valid Parameters: Wait till WD timeout time, element available
#                 Invalid Params: Element which does not exist
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
    apis = ('WaitForElement',)
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        test_result = True
        params = self.config.wait_for_element_params

        try:
            for param in params.keys():
                self.logger.Log("--- Scenario: {} --- ".format(params[param][0]))
                if param == 6:
                    tapped = self.lib.element_ops(self.config.search_icon, action='tap')
                    if not tapped:
                        self.logger.Error("Failed to tap on Search Icon")
                        test_result = False
                        return False

                args = params[param][-1]
                element = self.lib.wait_for_element(args[0], args[1])
                if element == params[param][1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False

                self.lib.report("WaitForElement {}".format(params[param][0]), status)

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
