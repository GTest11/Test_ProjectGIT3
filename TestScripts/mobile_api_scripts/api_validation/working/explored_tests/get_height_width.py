# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            : Lincy Robert
# Date              : 29-01-2019
# Script Version     : 1.0
# Modification details:
# APIs covered      :   "GetElementHeight, GetElementWidth, GetLocation"
# Test Scenario:  "1.for a unique element, 2.more than one element present
#
# '''''''''''''''''''''''''''TEST CASE DETAILS' - END '''''''''''''''''''''''''''''''''


import os
import sys
sys.path.append('../')

from library.api_test_base import apiTestBase


class api_test(apiTestBase):
    # the class which handles the script intention.
    # this overrides base class run_api_test()

    # class variables
    apis = ('GetHeight', 'GetWidth', 'GetLocation',)
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        test_result = True
        try:
            
            api_dict = {
                "GetHeight": self.dut.GetHeight,
                "GetWidth": self.dut.GetWidth,
                "GetLocation": self.dut.GetLocation,
            }

            test_params = self.config.get_height_width_params
            for api in self.apis:
                for scenario in test_params.keys():
                    self.logger.Log("Scenario: {}".format(test_params[scenario][0]))
                    elm_type, type = self.lib.choose_elm_type(test_params[scenario][-1])
                    if not type:
                        self.logger.Error("Invalid element type")
                        test_result = False
                        continue
                    start_time = self.lib.gettimestamp()
                    api_result = api_dict[api](elm_type, test_params[scenario][-1][type])
                    end_time = self.lib.gettimestamp()
                    value_obtained = False
                    if api_result:
                        value_obtained = True
                        if api == "GetLocation":
                            value_obtained = self.validate_location_format(api_result)

                    if value_obtained == test_params[scenario][1]:
                        status = "PASSED"
                    else:
                        status = "FAILED"
                        # to set the test status
                        test_result = False

                    self.lib.report_api_status(start_time, end_time, api, status, ss_required=True)
                    self.lib.report("{}: {}".format(api, test_params[scenario][0]), status)

        except Exception as e:
            self.logger.Error("Error in run_api_test() " + str(e))
            test_result = False
        finally:
            self.test_result = test_result

    def validate_location_format(self, result):
        """Validates if the obtained result is of Location type and returns a Boolean output"""
        try:
            if (type(result.X).__name__ == "int") and (type(result.Y).__name__ == "int"):
                value_obtained = True
            else:
                value_obtained = False
        except Exception as e:
            value_obtained = False
        return value_obtained

def main():
    testobj = api_test()
    testobj.run_test(testobj.script_name, testobj.apis)


if __name__ == '__main__':
    main()
