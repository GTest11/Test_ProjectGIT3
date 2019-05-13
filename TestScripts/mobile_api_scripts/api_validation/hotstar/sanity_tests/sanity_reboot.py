# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :   17-April-2018
# Script Version    :   1.0
# APIs covered      :   Reboot
# Test Scenario     :   Launches the application -> Reboot API executed
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import os
import sys
import time
sys.path.append('../')

from library.api_test_base import ApiTestBase
from library.common_functions import device_config

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class api_test(ApiTestBase):

    # the class which handles the script intention.
    # this overrides base class run_api_test()

    apis = (
        "Reboot",
    )
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        '''
        Executes the test script

        :return: test status as True or False
        '''

        api_test_status = False
        self.logger.Log("*** FOR ANDROID DEVICES, SET THE SCREEN LOCK TYPE TO 'None' BEFORE RUNNING THIS TEST ***")
        self.logger.Log("*** FOR iOS DEVICES, REMOVE PASS CODE BEFORE RUNNING THIS TEST ***")

        try:
            
            w, h = self.lib.get_image_resolution()
            self.lib.report("Validating Reboot API. Screenshot before reboot >", "PASSED", ss_required=True)
            self.logger.Log("w - {}, h - {}".format(w, h))
            self.dut.CloseApp() # Closes the app for capturing the image of home screen before reboot
            time.sleep(5)

            ref_img_path = self.dut.validator.CaptureImage(0, 0, w, h, "ref_img", 90, 2)
            start_time = self.lib.get_time_stamp()
            rebooted = self.dut.Reboot()
            end_time = self.lib.get_time_stamp()
            time.sleep(110) # waiting for the device to come up

            self.handle_pop_up_for_applicable_device()
            test_img_path = self.dut.validator.CaptureImage(0, 0, w, h, "test_img", 90, 2)
            matched = self.dut.validator.ImageMatch("ref_img", "test_img", 2, "13")
            if rebooted and matched:
                status = "PASSED"
                api_test_status = True
            else:
                status = "FAILED"

            self.lib.report_api_status(start_time, end_time, "Reboot", status, ss_required=False)
            self.lib.report("API: Reboot", status, ss_required=True)

        except Exception as e:
            self.logger.Error("Error in run_api_test() " + str(e))
            api_test_status = False

        finally:
            self.test_result = api_test_status


    def handle_pop_up_for_applicable_device(self):
        """

        Invokes InitApp and sends a 'Keycode_BACK' key if the selected device is 'MiA1712'
        This can be used when the 'No SIM Card inserted' popup is obtained'

        """

        current_device = self.lib.get_dut_name()
        init_status = send_key_status = False
        if current_device == 'MiA1712':
            # needs an InitApp for SendAndroidKeyCode to work without ECONNREFUSED error
            init_status = self.dut.InitApp(device_config)
            send_key_status = self.dut.SendAndroidKeyCode("Keycode_BACK")
            time.sleep(2)
            self.dut.CloseApp()
        if not init_status or not send_key_status:
            self.lib.report("InitApp or Sending Back Key to handle popup ", "FAILED")


def main():
    testobj = api_test()
    testobj.run_test(testobj.script_name, testobj.apis)


if __name__ == '__main__':
    main()
