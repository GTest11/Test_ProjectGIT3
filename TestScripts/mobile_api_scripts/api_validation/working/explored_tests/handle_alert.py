# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :   Shameena HA
# Date              :   30-01-2019
# Script Version    :   1.0
# APIs covered      :   "HandleAlertMessage",
# Test Scenario     :    "Invalid: Alert not present"
#                         "Invalid: During media playback"
#                         "Invalid: Popup present, Empty action"
#                         "Invalid: Popup present, Wrong action"
#                         "Valid: Action - ACCEPT - uppercase",
#                         "Valid: Action - accept - lowercase",
#                         "Valid: Action - Accept - Camel case",
#                         "Valid: Action - DISMISS - uppercase",
#                         "Valid: Action - dismiss - lowercase",
#                         "Valid: Action - Dismiss - Camel case"
#
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
        "HandleAlertMessage",

    )
    script_name = os.path.basename(__file__)


    def doubletap(self):
        tapped = False
        dload_elmts = [
                    self.config.download_opt,
                    self.config.downloaded,
                    # self.config.downloading,
           ]
        for elm in dload_elmts:
            elm_type, type = self.lib.choose_elm_type(elm)
            if not type:
                self.logger.Error("Invalid element type")
                return False

            if self.dut.IsElementPresent(elm_type, elm[type]):
                tapped = self.dut.DoubleTapElement(elm_type, elm[type])
                if tapped:
                    break
        return tapped


    def prepare_env_handle_alert(self):
        '''
        Starts a playback and taps on the download button twice (doubletap)
        :return: True or False
        '''

        prepared = True
        try:
            if not self.dut.CloseApp():
                self.lib.report("Failed to close the applicaion", "FAILED", ss_required=True)
                prepared = False
                return False

            if not self.dut.LaunchApp():
                self.lib.report("Failed to close the applicaion", "FAILED", ss_required=True)
                prepared = False
                return False

            time.sleep(3)  # wait for the app to launch home
            if not self.dut.Tap(*self.config.C_TAP_PLAYBACK):
                self.lib.report("Failed to tap on video", "FAILED", ss_required=True)
                prepared = False
                return False

            time.sleep(5)  # to start the playback
            done = self.doubletap()
            if not done:
                self.lib.report("Failed to perform DoubleTap", "FAILED", ss_required=True)
                prepared = False
            return prepared

        except Exception as e:
            self.logger.Log("Exception - " + str(e))
            prepared = False

        finally:
            return prepared


    def run_api_test(self):
        '''
        Executes the test script

        :return: test status as True or False
        '''

        test_status = True
        params = self.config.handle_alert_params

        try:
            for param in params:
                self.logger.Log("---------- Scenario {} ---------".format(params[param][0]))

                if param is 1 or 2:
                    if not self.dut.Tap(*self.config.C_TAP_PLAYBACK):
                        self.lib.report("Failed to tap on video", "FAILED", ss_required=True)
                        test_status = False
                        return False
                    time.sleep(3)  # to start the playback

                    if param == 2:
                        done = self.doubletap()
                        if not done:
                            self.lib.report("Failed to perform DoubleTap", "FAILED", ss_required=True)
                            test_status = False

                if param >= 4:
                    prepared = self.prepare_env_handle_alert()
                    if not prepared:
                        self.lib.report("Failed to configure for API", "FAILED", ss_required=True)
                        test_status = False
                        continue

                start_time = self.lib.gettimestamp()
                hidden = self.dut.HandleAlertMessage(params[param][-1])
                end_time = self.lib.gettimestamp()
                if hidden == params[param][1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_status = False
                self.lib.report_api_status(start_time, end_time, "HandleAlertMessage", status, ss_required=True)
                self.lib.report("HandleAlertMessage: {}".format(params[param][0]), status, ss_required=False)

        except Exception as e:
            self.logger.Error("Error in run_api_test() " + str(e))
            test_status = False

        finally:
            self.test_result = test_status


def main():
    testobj = api_test()
    testobj.run_test(testobj.script_name, testobj.apis)


if __name__ == '__main__':
    main()
