# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author                :   Shameena HA
# Date                  :   30-01-2019
# Script Version        :   1.0
# APIs covered          :   "SetCustomDUTAttribute", "GetDUTAttribute", 'ReadCustomProperty'
# Test Scenario         :   Valid parameters
#                           Invalid parameters: Empty attribute, 
#                           Invalid parameters: Long name, 
#                           Invalid parameters: Name with special characters"
#                           Invalid: Value with digits alone
#                           Invalid: Value with combination of splchar, numbers, alphabets
#
# '''''''''''''''''''''''''''TEST CASE DETAILS' - END '''''''''''''''''''''''''''''''''

import os
import sys
import datetime
import time
sys.path.append('../')

from library.api_test_base import apiTestBase


class api_test(apiTestBase):
    # the class which handles the script intention.
    # this overrides base class run_api_test()

    # class variables
    apis = ('SetCustomDUTAttribute', 'GetDUTAttribute', 'ReadCustomProperty')
    script_name = os.path.basename(__file__)


    def set_dut_attr(self, attr, attr_value, exp=None):
        '''
        :param attr:
        :param attr_value:
        :param exp:
        :return:
        '''

        test_result = False
        try:
            start_time = self.lib.gettimestamp()
            set = self.dut.SetCustomDUTAttribute(attr, attr_value)
            end_time = self.lib.gettimestamp()
            if set == exp:
                status = "PASSED"
                test_result = True
            else:
                status = "FAILED"

            self.lib.report_api_status(start_time, end_time, "SetCustomDUTAttribute", status, ss_required=True)
        except Exception as e:
            self.logger.Error("Exception from set_dut_attr() " + str(e) )
            test_result = False

        return test_result


    def run_api_test(self):
        test_result = True
        try:
            test_params = self.config.set_custom_dut_attribute_params
            test_scenario = ["ordinary_attribute", "long_attribute", "attrubte_name_with_specialchar"]

            for scenario in test_scenario:
                self.logger.Log("**************  Start Scenario {}  ****************".format(scenario))

                if scenario == "ordinary_attribute":
                    self.attr_name = self.config.attr_name.format(datetime.datetime.now().strftime("%H_%M_%S"))
                if scenario == "long_attribute":
                    self.attr_name = self.config.long_val_attr
                if scenario == "attrubte_name_with_specialchar":
                    self.attr_name = self.config.comb_attr_val
                added = self.lib.add_custom_attribute(self.attr_name)
                if not added:
                    self.lib.report("Failed to add attrubute {}, attribute may be available".format(self.attr_name), "FAILED", ss_required=True)
                    self.logger.Log("Attribute may be added already, hence proceeding with the execution")
                    # continue
                else:
                    self.lib.report("Attribute - {} - added".format(scenario),
                                    "PASSED", ss_required=True)
                time.sleep(1)

                for param in test_params:
                    self.logger.Log(" -------  Scenario: {}  -------".format(test_params[param][0]))
#                    set = self.set_dut_attr(self.attr_name, test_params[param][-1], test_params[param][1])
#                    if not set:
#                        test_result = False

                    start_time = self.lib.gettimestamp()
                    get = self.dut.GetCustomDUTAttribute(self.attr_name)
                    end_time = self.lib.gettimestamp()
                    self.logger.Log("-------------- get - {}".format(get))
                    if get == test_params[param][-1] or ( param==2 and get == ''):
                        status = "PASSED"
                    else:
                        status = "FAILED"
                        test_result = False
                    self.lib.report_api_status(start_time, end_time, "GetCustomDUTAttribute", status, ss_required=False)
                    self.lib.report(
                        "GetCustomDUTAttribute: {} - {}".format(scenario, test_params[param][0]),
                        status, ss_required=False
                    )

                    start_time = self.lib.gettimestamp()
                    read = self.dut.ReadCustomProperty(self.attr_name)
                    end_time = self.lib.gettimestamp()
                    self.logger.Log("-------------- read - {}".format(read))
                    if read == test_params[param][-1] or ( param==2 and read == ''):
                        status = "PASSED"
                    else:
                        status = "FAILED"
                        test_result = False
                    self.lib.report_api_status(start_time, end_time, "ReadCustomProperty", status, ss_required=False)
                    self.lib.report(
                        "ReadCustomProperty: {} - {}".format(scenario, test_params[param][0]),
                        status,ss_required=False
                    )
                    time.sleep(1)
                self.logger.Log("**************  End Scenario {}  ****************".format(scenario))

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
