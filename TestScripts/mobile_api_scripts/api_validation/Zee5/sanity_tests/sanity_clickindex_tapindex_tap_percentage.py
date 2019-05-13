# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :   16-April-2019
# Script Version    :   1.0
# APIs covered      :   "Click(Index)",
#                         "TapElement(Index)", "TapPercent"
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

    apis = (
            "Click(Index)",
            "TapElement(Index)",
            "TapPercent",
         )
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        '''
        Executes the test script

        :return: True or False
        '''

        api_test_status = True
        status = "FAILED"
        platform = self.lib.get_dut_platform()
        try:
            # done = self.lib.element_ops(self.config.click_tap_idx, index=self.config.search_icon_index, action='clickindex')
            # if not done:
            #     api_test_status = False
            #     self.lib.report("Click(Index)", "FAILED")

            sent = False
            # if platform == "Android":
            #     start_time = self.lib.get_time_stamp()
            #     sent = self.dut.SendAndroidKeyCode(self.config.BACK)
            #     end_time = self.lib.get_time_stamp()
            #     if not sent:
            #         api_test_status = False
            #     else:
            #         status = "PASSED"
            #     time.sleep(1) # wait before getting screenshot after SendAndroidKeycode
            #     self.lib.report_api_status(start_time, end_time, "SendAndroidKeyCode", status, ss_required=True)
            # else:
            #     self.lib.report("SendAndroidKeyCode not available for the platform", "SKIPPED", ss_required=True)
            #
            # if not self.lib.handle_alert(action='DISMISS'):
            #     self.lib.report("Failed to handle the Alert", "FAILED", ss_required=True)

            # self.lib.tap_element(self.config.exit_from_app_no)
            # if not sent:
                # if not self.lib.element_ops(self.config.navbar_home, action='tap'):
                #     self.lib.report("Failed to go back to home, so closing the app, relaunching it", "FAILED")
                #     time.sleep(1)

                    # if not self.lib.launch_app():
                    #     self.lib.report("Failed to launch app again", "FAILED")
                    #     api_test_status = False
                    #     return False


            done = self.lib.element_ops(self.config.click_tap_idx, index=self.config.search_icon_index,
                                        action='tapindex')
            if not done:
                api_test_status = False
                self.lib.report("Tap(Index)", "FAILED", ss_required=False)

            # going back to home
            # if not self.lib.element_ops(self.config.navbar_home, action='tap'):
            #     self.lib.report("Failed to go back to home, so closing the app, relaunching it", "FAILED")
            #     time.sleep(1)

            if not self.lib.launch_app():
                self.lib.report("Failed to launch app again", "FAILED")
                api_test_status = False
                return False

            # res = self.lib.get_image_resolution()
            start_time = self.lib.get_time_stamp()
            tapped = self.dut.TapPercent(*self.config.TAP_PERCENTAGE)
            end_time = self.lib.get_time_stamp()
            if not tapped:
                api_test_status = False
                status = "FAILED"
            else:
                status = "PASSED"
            self.lib.report_api_status(start_time, end_time, "TapPercent", status, ss_required=True)

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
