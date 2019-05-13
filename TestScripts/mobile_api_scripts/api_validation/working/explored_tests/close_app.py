# ''''''''''''''''''''''''''' TEST CASE DETAILS '''''''''''''''''''''''''''''''''''''''''
# Author            : Shameena HA
# Date              : 29-01-2019
# Script Version    : 1.0
# APIs covered      :   "CloseApp"
# Test Scenarios    : 1. when launch app/initapp failed (calls CloseApp)
#                     2. App is backgrounded
#
# ''''''''''''''''''''''''''' TEST CASE DETAILS - END '''''''''''''''''''''''''''''''''

import os
import sys
sys.path.append('../')

from library.api_test_base import apiTestBase

class api_test(apiTestBase):
    '''
    The class which handles the script intention.
    this overrides base class run_api_test()

    '''

    # class variables
    apis = ('CloseApp',)
    script_name = os.path.basename(__file__)

    def test_send_app_bg(self):
        '''
        Sends the application to background and returns the API status

        :return: True or False
        '''

        sent = False
        try:
            start_time = self.lib.gettimestamp()
            response = self.dut.SendAppToBackground(self.config.send_app_bg_duration)
            end_time = self.lib.gettimestamp()
            self.logger.Log("API: SendAppToBackground Status - {}".format(response.Status))
            self.logger.Log("API: SendAppToBackground Message - {}".format(response.Message))
            if response:
                status = "PASSED"
                sent = True
            else:
                status = "FAILED"
            self.lib.report_api_status(start_time, end_time, "SendAppToBackground", status, ss_required=True)

        except Exception as e:
            self.logger.Error("Exception in test_send_app_bg() " + str(e))
            sent = False

        finally:
            return sent


    def run_api_test(self):
        '''
        This overrides the run_api_test() in Base class

        :return: script status; True or False
        '''

        # for api status
        test_result = True
        try:
            params = self.config.close_app_params
            for param in params:
                self.logger.Log(" ----  Scenario:  {}  ----".format(params[param][0]))

                if param == 0:
                    done = self.test_send_app_bg()
                    if not done:
                        test_result = False
                        return test_result
                else:
                    if not self.lib.close_app():
                        test_result = False
                        self.lib.report("Failed to close the Application", "FAILED", False)
                        return test_result

                done = self.lib.close_app()
                opened = self.lib.is_app_open()
                if (not done) or opened:
                    self.logger.Error("Failed to close the application")
                    test_result = False

                if done == params[param][1] :
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False
                self.lib.report("CloseApp: {}".format(params[param][0]), status, True)

        except Exception as e:
            self.logger.Error("Error in run_api_test() " + str(e))
            test_result = False

        finally:
            # to set the test status
            self.test_result = test_result


def main():
    testobj = api_test()
    testobj.run_test(testobj.script_name, testobj.apis)


if __name__ == '__main__':
    main()
