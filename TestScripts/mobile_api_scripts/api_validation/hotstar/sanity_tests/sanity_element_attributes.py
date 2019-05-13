# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :
# Script Version    :
# APIs covered      :   "GetAllAttributeValues", "GetAllChildAttributeValues",
#                       "GetAttribute" and GetLocation
# Test Scenario     :
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import os
import sys
import time
from collections import OrderedDict
sys.path.append('../')

from library.api_test_base import ApiTestBase


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class api_test(ApiTestBase):

    # the class which handles the script intention.
    # this overrides base class run_api_test()

    apis = ("GetAttribute", "GetLocation", "GetAllAttributeValues", "GetAllChildAttributeValues", )

    script_name = os.path.basename(__file__)


    def run_api_test(self):
        '''
        Executes the test script

        :return:
        '''

        api_test_status = True
        try:
            time.sleep(5)
            attr_list = self.config.attr_list
            test_attribute = "enabled"
            api_list = [
                ("GetAttribute", self.dut.GetAttribute),
                ("GetLocation", self.dut.GetLocation),
                ("GetAllAttributeValues", self.dut.GetAllAttributeValues),
                ("GetAllChildAttributeValues", self.dut.GetAllChildAttributeValues)
            ]

            api_call = OrderedDict(api_list)
            elm_type, type = self.lib.choose_elm_type(self.config.search_icon)
            loc_elm_type, loc_type = self.lib.choose_elm_type(self.config.search_icon)
            if not (type or loc_type):
                self.logger.Error("Failed to find the element type")
                api_test_status = False
                return

            api_params = {
                "GetAllAttributeValues": (
                    elm_type,
                    self.config.search_icon[type],
                    attr_list
                ),
                "GetAllChildAttributeValues": (
                    elm_type,
                    self.config.search_icon[type],
                    attr_list
                ),
                "GetAttribute": (elm_type, self.config.search_icon[type], test_attribute),
                "GetLocation": (loc_elm_type, self.config.search_icon[loc_type])
            }

            attr_present = False
            for api, api_val in api_list:
                if api:
                    # self.logger.Log("**api_params[api] {}".format(api))
                    if api == "GetAllChildAttributeValues":
                        present = self.lib.is_present(self.config.search_icon)
                        if not present:
                            self.lib.report("GetAllChildAttributeValues: Element not available", "FAILED",
                                            ss_required=True)
                            continue
                    start_time = self.lib.get_time_stamp()
                    api_result = api_call[api](*api_params[api])
                    end_time = self.lib.get_time_stamp()
                # this else part is not required for the script right now, if a function does not take any parameter
                # apis_params will have a empty tuple () for that function and the else part call will work for that function.
                else:
                    start_time = self.lib.get_time_stamp()
                    api_result = api_call[api]()
                    end_time = self.lib.get_time_stamp()

                time.sleep(3)
                # if (api != "GetAttribute") and (api != "GetLocation"):
                if (api == "GetAllAttributeValues") and (api == "GetAllChildAttributeValues"):
                    # validate_result returns true if any of the attribute is true, but there can be some
                    # element without any attribute so not using this function, currently used element can be validated using this function
                    # attr_present = validate_result(ret_val)
                    if len(api_result) > 0:
                        attr_present = True
                else:
                    attr_present = api_result

                if attr_present:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    api_test_status = False

                self.logger.Log("API: {} returned - ".format(api) + str(api_result))
                self.lib.report_api_status(start_time, end_time, api, status, ss_required=True)

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
