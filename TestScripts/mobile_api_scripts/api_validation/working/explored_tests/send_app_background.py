# ''''''''''''''''''''''''''' TEST CASE DETAILS '''''''''''''''''''''''''''''''''''''''''
# Author            :   Shameena HA
# Date              :   29-01-2019
# Script Version    :   1.0
# APIs covered      :   "SendAppToBackground"
# Test Scenarios    : 1. app is not open
#                     2. already backgrounded
#                     3. with duration as max timeout time of webdriver
#                     4. with 0 duration
#                     5. with duration as max WD timeout+1
#                     6. Negative value for duration
#                     7. Without InitApp call(calls CloseApp before launching the application)
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
    apis = ('SendAppToBackground',)
    script_name = os.path.basename(__file__)

    def test_send_app_bg(self, duration):
        '''
        This function tries to launch the application again, if the application is opened already

        :return:
        '''

        sent = False
        try:
            start_time = self.lib.gettimestamp()
            response = self.dut.SendAppToBackground(duration)
            end_time = self.lib.gettimestamp()
            self.logger.Log("API: SendAppToBackground Status - {}".format(response.Status))
            self.logger.Log("API: SendAppToBackground Message - {}".format(response.Message))

            if response.Status: # returns 1 for valid status
                status = "PASSED"
                sent = True
            else:
                status = "FAILED"
                sent = False
            self.lib.report_api_status(start_time, end_time, "SendAppToBackground", status, ss_required=True)

        except Exception as e:
            self.logger.Error("Exception in test_send_app_bg() " + str(e))
            sent = False

        finally:
            return sent


    def close_app(self):
        closed = False
        try:
            start_time = self.lib.gettimestamp()
            closed = self.dut.CloseApp()
            end_time = self.lib.gettimestamp()
            if closed:
                status = "PASSED"
            else:
                status = "FAILED"
            self.lib.report_api_status(start_time, end_time, "CloseApp", status, ss_required=True)
        except Exception as e:
            self.logger.Error("Error while closing the application" + str(e))
            closed = False
        finally:
            return closed


    def run_api_test(self):
        '''
        This overrides the run_api_test() in Base class

        :return: script status; True or False
        '''

        # for api status
        test_result = True
        try:
            params = self.config.send_app_bg_params
            for param in params:
                self.logger.Log(" ----  Scenario: {}  ----".format(params[param][0]))

                if param == 6:  #  app closed
                    done = self.close_app()
                    opened = self.lib.is_app_open()
                    if (not done) or opened:
                        self.logger.Error("Failed to close the application")
                        continue

                done = self.test_send_app_bg(params[param][-1])
                if done == params[param][1] :
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False
                self.lib.report("SendAppToBackground: {}".format(params[param][0]), status, True)

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
