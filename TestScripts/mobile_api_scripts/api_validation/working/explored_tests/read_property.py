# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :   Lincy Robert
# Date              :   01-02-2019
# Script Version    :   1.0
# APIs covered      :   "ReadProperty"
# Test Scenarios    :   "Invalid property number",
#                       "Lowest boundary value of property",
#                       "Highest boundary value of property",
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

    apis = ("ReadProperty", )
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        '''
        Executes the test script
        :return:
        '''

        api_test_status = True

        try:
            test_params = self.config.read_property_params
            dut_mob_name = self.lib.get_dut_name()  # Read the name of the mobile DUT
            if dut_mob_name in self.config.dut_property_dict_map:
                property_dict = self.config.dut_property_dict_map[dut_mob_name]
                for scenario in test_params.keys():
                    self.logger.Log("-----Scenario: {}-----".format(test_params[scenario][0]))
                    try:
                        start_time = self.lib.gettimestamp()
                        property_obtained = self.dut.ReadProperty(test_params[scenario][-1])
                        end_time = self.lib.gettimestamp()
                        self.logger.Log("Output obtained for ReadProperty API is : "+str(property_obtained))
                    except Exception as api_exception:
                        api_test_status = False
                        self.logger.Log("Obtained exception while invoking API for Scenario : "
                                        + str(test_params[scenario][0]))
                        self.logger.Error(str(api_exception))
                        continue
                    property_matched = True if property_dict[test_params[scenario][-1]] == property_obtained else False
                    if property_matched == test_params[scenario][1]:
                        status = "PASSED"
                    else:
                        status = "FAILED"
                        api_test_status = False
                    self.lib.report_api_status(start_time, end_time, "ReadProperty", status, ss_required=True)
                    self.lib.report("ReadProperty: {}".format(test_params[scenario][0]), status)
            else:
                self.logger.Error("Property values of the DUT is unavailable in the config. Hence, skipping test.")
                api_test_status = False

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
