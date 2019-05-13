# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :
# Script Version    :   1.0
# APIs covered      :
# Test Scenario     :
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import os
import sys
import time
sys.path.append('../')

from library.api_test_base import apiTestBase


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class api_test(apiTestBase):

    # the class which handles the script intention.
    # this overrides base class run_api_test()

    apis = (
         )
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        '''
        Executes the test script

        :return:
        '''

        api_test_status = True
        status = "FAILED"
        res = self.lib.get_image_resolution()

        # def is_element_present(self, elm_list):
        #     presence = {}
        #     idx = 0
        #     for elm in elm_list:
        #         presence[idx] = self.lib.is_present(elm)
        #         idx += 1
        #
        #     return presence
        #
        # def tap_element(self, elm_list, dict_elm):
        #     tap_status = {}
        #     idx = 0
        #     for key, value in dict_elm.items():
        #         if value == True:
        #             tap_status[idx] = self.lib.tap_element(elm_list[key])
        #             idx += 1
        #
        #         if not self.lib.element_ops(self.config.navbar_home):
        #             tap_status[idx] = False
        #             return tap_status
        #         time.sleep(1)  # sleep between taps
        #
        #     return tap_status

        # data = self.lib.get_test_params(self.config.sanity_capture_image_params, self.config.capture_image_params)
        # print data

        try:
            self.logger.Log(str(res))
            pass
            # self.lib.report_api_status(start_time, end_time, api, status, ss_required=False)
            # self.lib.report("ADB Info API {} is {}".format(api, status), status, ss_required=True)
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
