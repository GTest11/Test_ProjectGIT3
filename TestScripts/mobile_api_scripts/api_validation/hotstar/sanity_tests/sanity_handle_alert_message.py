# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :   02-Jan-2019
# Script Version    :   1.0
# APIs covered      :   "HandleAlertMessage"
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
        "DoubleTapElement",
        "HandleAlertMessage",
    )
    script_name = os.path.basename(__file__)

    def handle_alert(self, tap_param, alert_type, api):
        '''

        :param tap_param: action to be given to element_ops()
        :param alert_type: whether accept/dismiss alert
        :return: True or False
        '''
        api_test = False
        if not self.dut.Tap(*self.config.C_TAP_PLAYBACK):
            self.lib.report("Tap on the video to start playback", "FAILED", ss_required=True)
            return api_test

        time.sleep(3)
        if tap_param == "doubletap":
            done = self.lib.element_ops(self.config.download_opt, index=0, action=tap_param)
        else:
            done = self.lib.element_ops(self.config.click_tap_idx, index=11, action=tap_param)

        if not done:
            self.lib.report("DoubleTap failed, so skipping 'HandleAlertMessage' API", "FAILED", ss_required=True)
            return api_test

        time.sleep(3)  # waits for the popup
        start_time = self.lib.gettimestamp()
        handled = self.dut.HandleAlertMessage(alert_type)
        end_time = self.lib.gettimestamp()
        if handled:
            status = "PASSED"
            api_test = True
        else:
            status = "FAILED"

        self.lib.report_api_status(start_time, end_time, api, status, ss_required=True)
        return api_test


    def run_api_test(self):
        '''
        Executes the test script

        :return:
        '''

        api_test_status = True
        status = "FAILED"

        try:
            dismissed = self.handle_alert("doubletap", self.config.dismiss_alert, "HandleAlertMessage - Dismiss")

            self.logger.Log("Relaunching app ***")

            if not self.lib.launch_app():
                self.lib.report("Failed to launch app", "FAILED", ss_required = True)
                api_test_status = False
                return False

            time.sleep(3)

            home = self.lib.wait_for_element(self.config.home, self.config.T_WAIT_FOR_HOME)
            if not home:
                self.lib.report("Failed to wait for home", "FAILED", ss_required=True)
                api_test_status = False
                return False

            accepted = self.handle_alert("doubletapindex", self.config.accept_alert, "HandleAlertMessage - Accept")
            api_test_status = dismissed and accepted

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
