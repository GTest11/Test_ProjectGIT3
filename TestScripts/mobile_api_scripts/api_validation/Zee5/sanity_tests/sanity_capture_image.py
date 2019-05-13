# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :   16-April-2019
# Script Version    :   1.0
# APIs covered      :   'CaptureImage'
# Test Scenario     :   Captures image using the API with different 'overwrite action' set
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import os
import sys
import time
import uuid
sys.path.append('../')

from library.api_test_base import ApiTestBase

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class api_test(ApiTestBase):

    # the class which handles the script intention.
    # this overrides base class run_api_test()

    apis = ('CaptureImage',
         )
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        '''
        Executes the test script

        :return: True or False
        '''

        api_test_status = True
        test_data = self.lib.get_test_params(
            self.config.sanity_capture_image_params,
            self.config.capture_image_params
        )

        if not test_data:
            self.lib.report("Could not populate the test data params", "FAILED")
            api_test_status = False
            return False

        try:
            for data in test_data:
                self.logger.Log(" ----- Test Scenario - {} -----".format(test_data[data][0]))
                params_to_invoke = list(test_data[data][-1])
                if test_data[data][-1][4] == "cap_img_unique":
                    # generating unique image name so that subsequent runs of the same scenario
                    # doesn't throw error due to overwrite set to 1
                    unique_long_name = str(uuid.uuid1())
                    params_to_invoke[4] = "img_" + str(unique_long_name[:8])
                start_time = self.lib.get_time_stamp()
                im_path = self.dut.validator.CaptureImage(*params_to_invoke)
                end_time = self.lib.get_time_stamp()

                self.logger.Log("im_path - {}".format(im_path))
                if im_path:  # if image path returned by the API
                    captured = True
                else:
                    captured = False

                # we use this double comparison for including negative scenarios as well
                if captured == test_data[data][1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    api_test_status = False
                self.lib.report_api_status(start_time, end_time, 'CaptureImage', status, ss_required=True)

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
