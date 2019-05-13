# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :   02-Jan-2019
# Script Version    :   1.0
# APIs covered      :   'GetElementCount','GetHeight', 'GetWidth'
# Test Scenario     :
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import os
import sys
from collections import OrderedDict
sys.path.append('../')

from library.api_test_base import apiTestBase


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class api_test(apiTestBase):

    # the class which handles the script intention.
    # this overrides base class run_api_test()

    apis = ('GetElementCount','GetHeight', 'GetWidth')
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        '''
        Executes the test script

        :return:
        '''

        api_test_status = True

        try:
            apis = [("GetElementCount", self.dut.GetElementCount), ("GetHeight", self.dut.GetHeight),
                    ("GetWidth", self.dut.GetWidth)]
            apis_call = OrderedDict(apis)

            elm_type, type = self.lib.choose_elm_type(self.config.elem_det)
            if not type:
                self.logger.Error("Failed to get the element type")
                api_test_status = False
                return

            apis_params = {
                "GetElementCount": (elm_type, self.config.elem_det[type]),
                "GetHeight": (elm_type, self.config.elem_det[type]),
                "GetWidth": (elm_type, self.config.elem_det[type]),
            }

            for api in apis_call:
                start_time = self.lib.gettimestamp()
                api_result = apis_call[api](*apis_params[api])
                end_time = self.lib.gettimestamp()
                # else part is removed for the script right now, since the APIs do have parameters
                # when apis_params will have a empty tuple (),  need of an else clause.
                # eg: api_result = apis_call[api]()

                if not api_result:
                    status = "FAILED"
                    api_test_status = False
                else:
                    status = "PASSED"

                self.logger.Log("API: {} ".format(api) + " returned - " + str(api_result))
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
