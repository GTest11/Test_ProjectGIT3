# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            :   Shameena HA
# Date              :   22-April-2019
# Script Version    :   1.0
# APIs covered      :   Swipe, 'VerticalSwipe', 'HorizontalSwipe'
# Test Scenario:    Sanity - verify the functionality of the APIs
# '''''''''''''''''''''''''''TEST CASE DETAILS' - END '''''''''''''''''''''''''''''''''

import os
import sys
import time
sys.path.append('../')

from library.api_test_base import ApiTestBase

class api_test(ApiTestBase):
    # the class which handles the script intention.
    # this overrides base class run_api_test()

    # class variables
    apis = ('Swipe', 'VerticalSwipe', 'HorizontalSwipe',)
    script_name = os.path.basename(__file__)
    overwrite = 0
    jpeg_q = 90
    pre_capture = 'precapture'
    post_capture = 'postcapture'

    def run_api_test(self):
        '''
        Swipes on the screen, captures images before and after swipe, compares
        the images and returns the result

        :return:
        '''

        test_result = True
        resolution = self.lib.get_image_resolution()

        try:
            dev_name = self.lib.get_dut_name()
            api_list = {
                "Swipe": self.dut.Swipe,
                "VerticalSwipe":  self.dut.VerticalSwipe,
                "HorizontalSwipe": self.dut.HorizontalSwipe,
            }

            param_list = {
                "Swipe": self.config.c_swipe[dev_name],
                "VerticalSwipe":  self.config.c_swipe[dev_name],
                "HorizontalSwipe": self.config.c_swipe[dev_name],
            }

            self.logger.Log("12345")
            self.logger.Log(self.config.c_swipe[dev_name])
            for param in param_list:
                imagePath = self.dut.validator.CaptureImage(
                    0, 0, resolution[0], resolution[1], self.pre_capture, self.jpeg_q,
                    self.overwrite
                )
                if not imagePath:
                    self.logger.Error("Failed to capture")
                    test_result = False
                self.logger.Log("12345")
                start_time = self.lib.get_time_stamp()
                self.logger.Log("12345666")
                swiped = api_list[param](*param_list[param])
                end_time = self.lib.get_time_stamp()

                imagePath = self.dut.validator.CaptureImage(
                    0, 0, resolution[0], resolution[1],
                    self.post_capture,
                    self.jpeg_q,
                    self.overwrite
                )

                if swiped:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False
                self.lib.report_api_status(start_time, end_time, param, status, ss_required=True)

                if not imagePath:
                    self.logger.Error("Failed to capture image")
                    test_result = False
                time.sleep(2)   # sleep before next swipe

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
