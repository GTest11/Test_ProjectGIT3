# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :   07-Jan-2019
# Script Version    :   1.0
# APIs covered      :   'ImageSearch'
# Test Scenario     :
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import os
import sys
import time
sys.path.append('../')

from library.api_test_base import ApiTestBase


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class api_test(ApiTestBase):

    # the class which handles the script intention.
    # this overrides base class run_api_test()

    apis = ("ImageSearch",
         )
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        '''
        Executes the test script

        :return:
        '''

        api_test_status = True

        test_data = self.lib.get_test_params(
            self.config.sanity_image_search_params,
            self.config.image_search_params
        )

        try:
            # response = fe_mob_lib.ImageComparisonService.Response()
            for key, value in test_data.items():
                param_list = value[2]
                if key == 1:
                    w, h = self.lib.get_image_resolution()
                    param_list = [w if param == "max_width" else param for param in param_list]
                    param_list = [h if param == "max_height" else param for param in param_list]
                time.sleep(10)
                self.logger.Log(" ----- Test Scenario - {} -----".format(value[0]))
                start_time = self.lib.get_time_stamp()
                response = self.dut.validator.ImageSearch(*param_list)
                end_time = self.lib.get_time_stamp()
                if response.OpStatus == value[1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    api_test_status = False

                self.lib.report_api_status(start_time, end_time, 'ImageSearch', status, ss_required=True)
                self.lib.report("ImageSearch: {}".format(value[0]), status)

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
