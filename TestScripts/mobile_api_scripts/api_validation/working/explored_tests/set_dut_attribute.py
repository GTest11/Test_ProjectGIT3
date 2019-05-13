# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            : Shameena HA
# Date              :   29-11-2018
# Script Version    : 1.0
# Modification details:
# APIs covered      :   "SetDUTAttribute"
# Test Scenario: "Valid attribute",
#                 "Empty attribute value",
#                 "Long attribute value",
#                 "Attribute value with special characters",
#                 "Attribute value with numbers alone",
#                 "Attribute value with combination of spl chars, numbers",
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
    apis = ('SetDUTAttribute',)
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        test_result = True
        params = self.config.set_dut_attr_params
        try:
            for param in params.keys():
                self.logger.Log("--- Scenario: {} ---".format(params[param][0]))
                start_time = self.lib.gettimestamp()
                set = self.dut.SetDUTAttribute(*params[param][-1])
                end_time = self.lib.gettimestamp()
                if set == params[param][1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False

                self.lib.report_api_status(start_time, end_time, "SetDUTAttribute", status, ss_required=True)
                self.lib.report("SetDUTAttribute: {}".format(params[param][0]), status)
                time.sleep(5) # wait between next scenario test

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
