# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            :   Shameena HA
# Date              :   04-02-2019
# Script Version    :   1.0
# APIs covered      :   "HorizontalSwipe"
# Test Scenario: Wrong coordinates (start and stop point)
#                 Out of boundary coordinates
#                 Swipe with max duration = WD timeout
#                 Vertical swipe on a horizontal Swipe area
#                 Swipe duration less than minimum expected duration
#
# '''''''''''''''''''''''''''TEST CASE DETAILS' - END '''''''''''''''''''''''''''''''''

import os
import sys
import time
sys.path.append('../')

from library.api_test_base import apiTestBase

class api_test(apiTestBase):
    # the class which handles the script intention.
    # this overrides base class run_api_test()

    # class variables
    apis = ('HorizontalSwipe',)
    script_name = os.path.basename(__file__)
    overwrite = 0
    jpeg_q = 90
    pre_capture = 'precapture'
    post_capture = 'postcapture'


    def swipe_screen(self, coord):
        '''
        Swipes on the screen, captures images before and after swipe, compares
        the images and returns the result

        :param coord: coordinates to swipe
        :return: True, True on swipe, images are equal
                Else False
        '''

        resolution = self.lib.get_image_resolution()
        swiped, same = False, False

        try:
            imagePath = self.dut.validator.CaptureImage(
                0, 0, resolution[0], resolution[1], self.pre_capture, self.jpeg_q,
                self.overwrite
            )
            if not imagePath:
                self.logger.Error("Failed to capture")
                swiped, same = False, False
                return swiped, same

            start_time = self.lib.gettimestamp()
            swiped = self.dut.HorizontalSwipe(*coord)
            end_time = self.lib.gettimestamp()
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
            self.lib.report_api_status(start_time, end_time, "HorizontalSwipe", status, ss_required=True)

            if not imagePath:
                self.logger.Error("Failed to capture image")
                swiped, same = False, False
                return swiped, same

            same = self.dut.validator.ImageMatch(self.pre_capture, self.post_capture, 2, "13")

        except Exception as e:
            self.logger.Log("Failed to swipe, compare images")
            swiped, same = False, False

        finally:
            return swiped, same


    def run_api_test(self):
        '''
        Overrides the base class functions
        :return: True or False
        '''

        test_result = True
        params = self.config.h_swipe_params

        try:
            # Going to History Section of Library
            reached = self.lib.element_ops(self.config.trending_nav, action='tap')
            if not reached:
                self.lib.report(
                    "Failed to go to the horizontally scrolling area of the application",
                    "FAILED",
                    ss_required=True
                )
                # self.logger.Log("--- SWIPE IS GOING TO PERFORM ON THE VERTICALLY SCROLLING AREA ---")

            for param in params.keys():
                self.logger.Log("--- Scenario: {} ---".format(params[param][0]))
                swiped, same = self.swipe_screen(params[param][-1])

                if swiped == params[param][1] and (not same):
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False

                self.lib.report("HorizontalSwipe: {}".format(params[param][0]), status)
                time.sleep(3) # wait between next scenario test

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
