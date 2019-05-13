# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            :   Shameena HA
# Date              :   05-02-2019
# Script Version    :   1.0
# APIs covered      :   "PressAndMove"
# Test Scenario:    Wrong coordinates (start and stop point)
#                   Out of boundary coordinates
#                   Destination distance is less
#                   Both locations are same
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
    apis = ('PressAndMove',
            )
    script_name = os.path.basename(__file__)
    overwrite = 0
    jpeg_q = 90
    pre_capture = 'precapture'
    post_capture = 'postcapture'

    def press_and_move(self, coord):
        '''
        Swipes on the screen, captures images before and after swipe, compares
        the images and returns the result

        :param coord: coordinates to swipe
        :return: True, True on swipe, images are equal
                Else False
        '''

        resolution = self.lib.get_image_resolution()
        moved, same = False, False

        try:
            image_path = self.dut.validator.CaptureImage(
                0, 0, resolution[0], resolution[1], self.pre_capture, self.jpeg_q,
                self.overwrite
            )
            if not image_path:
                self.logger.Error("Failed to capture")
                moved, same = False, False
                return moved, same

            start_time = self.lib.gettimestamp()
            moved = self.dut.PressAndMove(*coord)
            end_time = self.lib.gettimestamp()
            image_path = self.dut.validator.CaptureImage(
                0, 0, resolution[0], resolution[1], self.post_capture, self.jpeg_q,
                self.overwrite
            )
            if moved:
                status = "PASSED"
            else:
                status = "FAILED"
            self.lib.report_api_status(start_time, end_time, "PressAndMove", status, ss_required=True)

            if not image_path:
                self.logger.Error("Failed to capture image")
                moved, same = False, False
                return moved, same

            same = self.dut.validator.ImageMatch(self.pre_capture, self.post_capture, 2, "13")

        except Exception as e:
            self.logger.Log("Failed to press and move, compare images")
            moved, same = False, False

        finally:
            return moved, same


    def run_api_test(self):
        test_result = True
        params = self.config.press_and_move_params
        moved, same = False, False

        try:
            for param in params.keys():
                self.logger.Log("--- Scenario: {} ---".format(params[param][0]))

                moved, same = self.press_and_move(params[param][-1])
                if moved == params[param][1] and (not same):
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False

                self.lib.report("PressAndMove: {}".format(params[param][0]), status)
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
