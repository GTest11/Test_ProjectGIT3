# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author                :
# Date                  :   16-April-2019
# Script Version        : 1.1
# APIs covered          :   "LaunchApp", "SendAppToBackground", "CloseApp"
#                       
#Test Scenario:
#init to Youtube
#close youtube by CloseApp
#LaunchApp again and calling SendAppToBackground
# '''''''''''''''''''''''''''TEST CASE DETAILS' - END '''''''''''''''''''''''''''''''''

# ''''''''''''''''''''''''''''''''''''''''IMPORTS''''''''''''''''''''''''''''''''''''''
#importing python modules
import sys
import os
import time

#importing user defined functions
sys.path.append('../')

from library.api_test_base import ApiTestBase


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class api_test(ApiTestBase):

    # the class which handles the script intention.
    # this overrides base class run_api_test()

    apis = ("CloseApp", "LaunchApp","SendAppToBackground")
    sendAppToBackground_duration = 10

    script_name = os.path.basename(__file__)
    

    def run_api_test(self):
        '''
        Executes the test script

        :return:
        '''

        api_test_status = True
        status = "FAILED"

        try:
            start_time = end_time = 0
            apis_call = {
                "CloseApp": self.dut.CloseApp,
                "LaunchApp": self.dut.LaunchApp,
                "SendAppToBackground": self.send_app_to_background,
            }

            for api in self.apis:
                self.logger.Log("API :- "+ str(api))
                start_time = self.lib.get_time_stamp()
                if api == "SendAppToBackground":
                    api_result = apis_call[api]()
                    end_time = self.lib.get_time_stamp()
                else:
                    # start_time = self.lib.gettimestamp()
                    api_result = apis_call[api]()
                    end_time = self.lib.get_time_stamp()
                    self.logger.Log("API: {} returned {}".format(api, api_result))

                if api_result:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    api_test_status = False
                self.lib.report_api_status(start_time, end_time, api, status, ss_required=True)

        except Exception as e:
            self.logger.Error("Error in run_api_test() " + str(e))
            api_test_status = False

        finally:
            self.test_result = api_test_status


    #''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    #@Function Name	  	: send_app_to_background()
    #@Description		: wrapper for dut.SendAppToBackground
    #@Input arguments	: None
    #@Output values		: Status of the API (Boolean) 
    #''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def send_app_to_background(self):
        api = "SendAppToBackground"
        APIResponse = self.lib.mob_lib.Models.ResponseData()
        start_time = self.lib.get_time_stamp()
        APIResponse = self.dut.SendAppToBackground(self.sendAppToBackground_duration)
        end_time = self.lib.get_time_stamp()
        
        time.sleep(self.sendAppToBackground_duration)
        self.logger.Log("API: Reason - {}".format(APIResponse.Message))
        if APIResponse.Status == 1:
            status = "PASSED"
            return_value = True
        else:
            status = "FAILED"
            return_value = False
        self.lib.report_api_status(start_time, end_time, api, status, ss_required=False)
        return return_value

def main():
    testobj = api_test()
    testobj.run_test(testobj.script_name, testobj.apis)


if __name__ == '__main__':
    main()
