# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author                :   Lincy Robert
# Date                  :   30-11-2018
# Script Version        :   1.0
# Modification details  :
# APIs covered          :   "AddCustomDUTAttribute"
# Test Scenario         :   "Valid parameters, 
#                           Invalid parameters: Empty attribute, 
#                           Invalid parameters: Long name, 
#                           Invalid parameters: Name with special characters"
# '''''''''''''''''''''''''''TEST CASE DETAILS' - END '''''''''''''''''''''''''''''''''

import os
import sys
import re
import datetime
sys.path.append('../')

from library.api_test_base import apiTestBase


class api_test(apiTestBase):
    # the class which handles the script intention.
    # this overrides base class run_api_test()

    # class variables
    apis = ('AddCustomDUTAttribute',)
    script_name = os.path.basename(__file__)

    def run_api_test(self):
        test_result = True

        try:
            test_params = self.config.add_custom_dut_attribute_params
            for scenario in test_params.keys():
                self.logger.Log("--- Scenario: {} ---".format(test_params[scenario][0]))
                expected_status = test_params[scenario][1]
                param = test_params[scenario][2]

                if test_params[scenario][2] == "unique_attr" or scenario == 3 :
                    param = test_params[scenario][2]+ datetime.datetime.now().strftime("%H_%M_%S")

                start_time = self.lib.gettimestamp()
                attribute_added = self.dut.AddCustomDUTAttribute(param)
                end_time = self.lib.gettimestamp()
                self.logger.Log("attribute added >>> {}".format(attribute_added))

                if attribute_added == test_params[scenario][1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False

                # if api_status is not expected_status:
                #     test_result = False
                    
                self.lib.report_api_status(start_time, end_time, "AddCustomDUTAttribute", status, ss_required=True)
                self.lib.report("AddCustomDUTAttribute: {}".format(test_params[scenario][0]), status,
                                ss_required=False
                                )

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
