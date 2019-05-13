# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :   Lincy Robert
# Date              :   31-01-2019
# Script Version    :   1.0
# Modification details:
# APIs covered      :   Reboot
# Test Scenario     :   "Reboot while media playback"
#                       "Reboot after reboot"
#                       "Reboot during locked state"
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import os
import sys
import time
sys.path.append('../')

from library.api_test_base import apiTestBase
from library.common_functions import device_config


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class api_test(apiTestBase):

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

        api_test_status = True

        self.logger.Log("*** FOR ANDROID DEVICES, SET THE SCREEN LOCK TYPE TO 'None' BEFORE RUNNING THIS TEST ***")
        self.logger.Log("*** FOR iOS DEVICES, REMOVE PASS CODE BEFORE RUNNING THIS TEST ***")

        try:
            pre_condition = {0: self.lib.play_back_from_search_result,
                             1: self.dut.Reboot,
                             2: self.dut.Lock,
                             }
            test_params = self.config.reboot_params
            
            device_platform = self.lib.get_dut_platform()
            if device_platform == "iOS":
                rebooted = self.dut.Reboot()
                if not rebooted:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    api_test_status = False
                self.lib.report("API: Reboot", status, ss_required=True)
            else:
                self.logger.Log("*** Reboot API is applicable only for Android devices! ***")
                for scenario in test_params.keys():
                    self.logger.Log("----- Scenario: {} -----".format(test_params[scenario][0]))
                    pre_condition_result = pre_condition[scenario]()
                    if scenario != 2 and not pre_condition_result:
                        self.logger.Log("Failed to execute the pre-condition. Hence, skipping the test scenario")
                        continue
                    start_time = self.lib.gettimestamp()
                    rebooted = self.dut.Reboot()
                    end_time = self.lib.gettimestamp()
                    if rebooted or (scenario == 1):
                        time.sleep(95)
                    if rebooted == test_params[scenario][1]:
                        status = "PASSED"
                    else:
                        status = "FAILED"
                        api_test_status = False

                    self.lib.report_api_status(start_time, end_time, "Reboot", status, ss_required=True)
                    self.lib.report("Reboot: {}".format(test_params[scenario][0]), status)
                    if rebooted:
                        self.handle_pop_up_for_applicable_device()

        except Exception as e:
            self.logger.Error("Error in run_api_test() " + str(e))
            api_test_status = False

        finally:
            self.test_result = api_test_status

    def handle_pop_up_for_applicable_device(self):
        """Invokes InitApp and sends a 'Keycode_BACK' key if the selected device is 'MiA1712'
        This can be used when the 'No SIM Card inserted' popup is obtained'"""

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
