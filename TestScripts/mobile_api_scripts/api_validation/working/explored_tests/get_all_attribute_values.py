# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :   Lincy Robert
# Date              :   29-01-2019
# Script Version    :   1.0
# APIs covered      :   "GetAllAttributeValues", "GetAttribute"
# Test Scenario     :
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import os
import sys
import time
import json
from collections import OrderedDict
sys.path.append('../')

from library.api_test_base import apiTestBase


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class api_test(apiTestBase):

    # the class which handles the script intention.
    # this overrides base class run_api_test()

    apis = ("GetAttribute", "GetAllAttributeValues", )
    script_name = os.path.basename(__file__)

    def run_api_test(self):
        '''
        Executes the test script

        :return:
        '''

        api_test_status = True

        try:
            api_list = [
                ("GetAttribute", self.dut.GetAttribute),
                ("GetAllAttributeValues", self.dut.GetAllAttributeValues),
            ]

            api_call = OrderedDict(api_list)

            test_params = self.config.get_all_attribute_value_params
            for api in self.apis:
                for scenario in test_params.keys():
                    attribute_param = test_params[scenario][-1]
                    if api == "GetAttribute":
                        attribute_param = attribute_param.split(',')[0]
                    self.logger.Log("Scenario: {}".format(test_params[scenario][0]))
                    elm_type, type = self.lib.choose_elm_type(test_params[scenario][-2])
                    if not type:
                        self.logger.Error("Invalid element type")
                        api_test_status = False
                        continue
                    start_time = self.lib.gettimestamp()
                    api_result = api_call[api](elm_type, test_params[scenario][-2][type], attribute_param)
                    end_time = self.lib.gettimestamp()
                    validated_result = self.validate_output(api, api_result)

                    if validated_result == test_params[scenario][1]:
                        status = "PASSED"
                    else:
                        status = "FAILED"
                        api_test_status = False

                    self.lib.report_api_status(start_time, end_time, api, status, ss_required=True)
                    self.lib.report("{}: {}".format(api, test_params[scenario][0]), status)

        except Exception as e:
            self.logger.Error("Error in run_api_test() " + str(e))
            api_test_status = False

        finally:
            self.test_result = api_test_status

    def validate_output(self, api, output):
        """Validates if the output is in required format as per the API and returns a Boolean output"""
        if api == "GetAttribute":
            result = False if output == '' else True
        else:
            try:
                result = False
                if output != '':
                    json_dict = json.loads(output)
                    for key in json_dict:
                        if 'This element does not have the' not in str(json_dict[key]) and \
                                'is unknown' not in str(json_dict[key]):
                            result = True
            except ValueError as error:
                self.logger.Error("Obtained output is not in valid JSON format")
                result = False
        return result


def main():
    testobj = api_test()
    testobj.run_test(testobj.script_name, testobj.apis)


if __name__ == '__main__':
    main()
