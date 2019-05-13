# ''''''''''''''''''''''''''' TEST CASE DETAILS '''''''''''''''''''''''''''''''''''''''''
# Author            : Shameena HA
# Date              :   26-11-2018
# Script Version    : 1.0
# APIs covered      :   "LaunchApp"
# Test Scenarios    : app is already open
#                      app is backgrounded
#                      Without InitApp call (calls CloseApp before launching the application)
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
    apis = ('LaunchApp',)
    script_name = os.path.basename(__file__)

    def test_launch_app(self):
        '''
        This function tries to launch the application again, if the application is opened already

        :return:
        '''

        done = False
        try:
            self.logger.Log("Scenario: Application is open already")
            start_time = self.lib.gettimestamp()
            done = self.dut.LaunchApp()
            end_time = self.lib.gettimestamp()
            if done:
                status = "PASSED"
            else:
                status = "FAILED"
            self.lib.report_api_status(start_time, end_time, "LaunchApp", status, ss_required=True)

        except Exception as e:
            self.logger.Error("Failed to call API LaunchApp " + str(e))
        finally:
            return done


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


    def background_app(self):
        backgrounded = False
        try:
            start_time = self.lib.gettimestamp()
            backgrounded = self.dut.SendAppToBackground(60)
            end_time = self.lib.gettimestamp()
            if backgrounded:
                status = "PASSED"
            else:
                status = "FAILED"
            self.lib.report_api_status(start_time, end_time, "SendAppToBackground", status, ss_required=True)
        except Exception as e:
            self.logger.Error("Error while sending the application to background" + str(e))
            backgrounded = False
        finally:
            return backgrounded


    def is_app_open(self):
        '''
        Verifies an element presence in the application.
        If element present, returns True.
        Else returns False

        :return: True if found,
                Else returns False
        '''

        opened = False
        try:
            opened = self.lib.is_present(elm_name=self.config.home)
        except Exception as e:
            self.logger.Error("Failed to verify the Application open status " + str(e))
            opened = False
        finally:
            return opened


    def run_api_test(self):
        '''
        This overrides the run_api_test() in Base class

        :return: script status; True or False
        '''


        # for api status
        test_result = True
        try:
            params = self.config.launch_app_params
            for param in params:
                self.logger.Log(" ----  Scenario: {}  ----".format(params[param][0]))
                if param == 0:
                    done = self.close_app()
                    opened = self.is_app_open()
                    if (not done) or opened:
                        self.logger.Error("Failed to close the application")
                        continue
                if param == 2:
                    done = self.background_app()
                    if not done:
                        self.logger.Error("Failed to background the application")
                        continue

                done = self.test_launch_app()
                if done == params[param][1] :
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False
                self.lib.report("LaunchApp: {}".format(params[param][0]), status, True)

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
