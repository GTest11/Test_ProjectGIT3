# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :   04-Jan-2019
# Script Version    :   1.0
# APIs covered      :   'DynamicImageCompare'
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

    apis = ('DynamicImageCompare',
         )
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        '''
        Executes the test script

        :return:
        '''

        test_data = self.lib.get_test_params(
            self.config.sanity_dynamic_image_compare_params,
            self.config.dynamic_image_compare_params
        )

        api_test_status = True

        try:
            captured_path = self.dut.validator.CaptureImage(*self.config.c_capture_image_for_dyn_im)
            if not captured_path:
                self.lib.report("Failed to capture", "FAILED", image_required=True)
                api_test_status = False
                return False

            if not self.dut.validator.CacheImageFromUrl(
                    captured_path,
                    self.config.dyn_img
            ):
                self.lib.report("CacheImageFromUrl", "FAILED", image_required=True)
                api_test_status = False
                return False

            for key, value in test_data.items():
                time.sleep(5)
                self.logger.Log(" ----- Test Scenario - {} -----".format(value[0]))
                start_time = self.lib.get_time_stamp()
                compared = self.dut.validator.DynamicImageCompare(*value[2])
                end_time = self.lib.get_time_stamp()

                if compared == value[1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    api_test_status = False

                self.lib.report_api_status(start_time, end_time, "DynamicImageCompare", status, ss_required=False)
                self.lib.report("DynamicImageCompare - {}".format(value[0]), status)

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
