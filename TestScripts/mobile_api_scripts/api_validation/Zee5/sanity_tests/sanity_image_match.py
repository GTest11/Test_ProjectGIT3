# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :   04-Jan-2019
# Script Version    :   1.0
# APIs covered      :   "ImageMatch", "CaptureImage"
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

    apis = ("ImageMatch", "CaptureImage",
         )
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        '''
        Executes the test script

        :return: True or False
        '''
        
        api_test_status = True
        status = "FAILED"

        try:
            test_data = self.lib.get_test_params(
                self.config.sanity_image_match_params,
                self.config.image_match_params
            )
            cur_dut = self.lib.get_dut_name()
            if cur_dut in self.config.c_capture_image_non_playback_region:
                x,y,w,h = self.config.c_capture_image_non_playback_region[cur_dut]
                cap_img_ref_region = (x, y, w, h, self.config.ref_img_0, self.config.CAP_IMG_DEFAULT_QUALITY, self.config.overwrite_file)
                cap_img_test_region = (x, y, w, h, self.config.test_img_0, self.config.CAP_IMG_DEFAULT_QUALITY, self.config.overwrite_file)
            else:
                self.lib.report(
                    "Coordinates for capture image is not available in Config. Hence skipping the test",
                    "FAILED", ss_required=True
                    )
                return False
            for key, value in test_data.items():
                ref_img_path = self.dut.validator.CaptureImage(*cap_img_ref_region)
                time.sleep(3)
                test_img_path = self.dut.validator.CaptureImage(*cap_img_test_region)

                if not (ref_img_path and test_img_path):
                    self.lib.report("Capture test image and reference image", "FAILED", ss_required=True)
                    api_test_status = False
                    continue

                self.logger.Log(" ----- Test Scenario - {} -----".format(value[0]))
                start_time = self.lib.get_time_stamp()
                match_found = self.dut.validator.ImageMatch(*value[2])
                end_time = self.lib.get_time_stamp()

                if match_found == value[1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    api_test_status = False
                self.lib.report_api_status(start_time, end_time, 'ImageMatch', status, ss_required=False)

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
