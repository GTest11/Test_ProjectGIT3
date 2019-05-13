# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :   Shameena HA
# Date              :   22-April-2019
# Script Version    :   1.0
# APIs covered      :   PressAndMove
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

    apis = (
        "PressAndMove",
    )
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        '''
        Executes the test script

        :return: test status as True or False
        '''

        api_test_status = False
        status = "FAILED"

        try:
            w, h = self.lib.get_image_resolution()
            start_time = 0
            end_time = 0
            
            # closed = self.dut.CloseApp()
            # time.sleep(3)
            # if not closed:
            #     self.lib.report("CloseApp API", "FAILED", ss_required=True)
            #     api_test_status = False

            if not w and not h:
                self.lib.report("Getting Image Resolution", "FAILED", ss_required=True)
                api_test_status = False
            else:
                time.sleep(3)
                self.logger.Log("w - {}, h - {}".format(w, h))
                # tapped = self.dut.Tap(*self.config.C_TAP_PLAYBACK)
                done = self.lib.play_back_from_search_result()
                if not done:
                    self.lib.report("Tap Failed", "FAILED", ss_required=False)
                    api_test_status = False
                    return False

                ref_img_path = self.dut.validator.CaptureImage(0, 0, w, h, "ref_img", 90, 2)
                self.logger.Log("-----------------------")
                time.sleep(30)
                self.dut.Tap(3, 300)    # to show the player controls..
                # not getting the status of the tap as the controls remain only for a few seconds
                start_time = self.lib.get_time_stamp()
                moved = self.dut.PressAndMove(*self.config.c_press_move)
                end_time = self.lib.get_time_stamp()
                time.sleep(3)
                # if not self.dut.HandleAlertMessage(self.config.ALERT_DISMISS):
                #     self.lib.report("Failed to Handle Alert Message", "FAILED", ss_required=False)
                #     api_test_status = False

                test_img_path = self.dut.validator.CaptureImage(0, 0, w, h, "test_img", 90, 2)

                matched = self.dut.validator.ImageMatch("ref_img", "test_img", 2, "23")

                if (not matched) and moved:
                    status = "PASSED"
                    api_test_status = True
                else:
                    status = "FAILED"

            self.lib.report_api_status(start_time, end_time, "PressAndMove", status, ss_required=False)
            self.lib.report("API: PressAndMove", status, ss_required=True)

        except Exception as e:
            self.logger.Error("Error in run_api_test() " + str(e))
            api_test_status = False

        finally:
            self.test_result = api_test_status
            self.dut.SendAndroidKeyCode("Keycode_BACK")


def main():
    testobj = api_test()
    testobj.run_test(testobj.script_name, testobj.apis)


if __name__ == '__main__':
    main()
