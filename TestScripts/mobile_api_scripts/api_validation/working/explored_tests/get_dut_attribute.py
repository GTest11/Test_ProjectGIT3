# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            : Shameena HA
# Date              :   29-11-2018
# Script Version    : 1.0
# Modification details:
# APIs covered      :   "GetDUTAttribute "
# Test Scenario: "Valid attribute",
#                 "Empty attribute value",
#                 "Non Existing attribute",
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
    apis = ('GetDUTAttribute',)
    script_name = os.path.basename(__file__)

    def run_api_test(self):
        test_result = True
        params = self.config.get_dut_attr_params
        try:
            for param in params.keys():
                self.logger.Log("--- Scenario: {} ---".format(params[param][0]))
                start_time = self.lib.gettimestamp()
                get_val = self.dut.GetDUTAttribute (params[param][-1])
                end_time = self.lib.gettimestamp()
                if get_val:
                    get = True
                else:
                    get = False
                if get == params[param][1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False

                self.lib.report_api_status(start_time, end_time, "GetDUTAttribute", status, ss_required=True)
                self.lib.report("GetDUTAttribute: {}".format(params[param][0]), status)
                time.sleep(1) # wait between next scenario test

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
