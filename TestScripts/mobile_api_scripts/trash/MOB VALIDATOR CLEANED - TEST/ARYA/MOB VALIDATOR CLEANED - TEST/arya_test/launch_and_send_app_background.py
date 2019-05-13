# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :   01-10-2018, 17-10-2018
#Script Version     : 1.1
#Modification details: 17 Oct 2018, fixed review comments - Arya
# APIs covered      :   "LaunchApp", "SendAppToBackground",
#                       "CloseApp"
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
try:
    # Import library file
    import library.common_functions as lib
except ImportError:
    print("Failed to import common_functions file")
    sys.exit()
# ''''''''''''''''''''''''''''''''''''''''IMPORTS - END'''''''''''''''''''''''''''''''

# ''''''''''''''''''''' ''''''''USER DEFINED VARIABLES'''''''''''''''''''''''''''''''''

#Variables
sendAppToBackground_duration = 10
config = lib.set_config()

apis_in_the_script = ("CloseApp", "LaunchApp","SendAppToBackground")
# ''''''''''''''''''''' ''''''''USER DEFINED VARIABLES' - END '''''''''''''''''''''''''

# ''''''''''''''''''''''''''''USER DEFINED FUNCTIONS'''''''''''''''''''''''''''''''''''

#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#@Function Name	  	: log_script_info()
#@Description		: logs file name and APIs covered
#@Input arguments	: None
#@Output values		: None
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def log_script_info():
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    lib.log_info("Script Name: {}".format(os.path.basename(__file__)))
    lib.log_info("Validating APIs - {}".format(apis_in_the_script))
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#@Function Name	  	: send_app_to_background()
#@Description		: wrapper for dut.SendAppToBackground
#@Input arguments	: None
#@Output values		: None
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def send_app_to_background():
    APIResponse = lib.fe_mob_lib.Models.ResponseData()
    start_time = lib.gettimestamp()
    APIResponse = lib.dut.SendAppToBackground(sendAppToBackground_duration)
    end_time = lib.gettimestamp()
    lib.report_elapsed_time(start_time, end_time, "SendAppToBackground")
    time.sleep(sendAppToBackground_duration)
    lib.log_info("API: Reason - {}".format(APIResponse.Message))
    if APIResponse.Status == 1:
        return True
    else:
        return False


#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#@Function Name	  	: test_api()
#@Description		: Positive scenario testing of following APIs:
#                     "CloseApp", "LaunchApp","SendAppToBackground"
#@Input arguments	: None
#@Output values		: None
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def test_api():
    api_test_status = True
    try:
        apis_call = {
            "CloseApp": lib.dut.CloseApp,
            "LaunchApp": lib.dut.LaunchApp,
            "SendAppToBackground": send_app_to_background,
        }

        for api in apis_in_the_script:
            lib.log_info("****  API  TEST **** {} ****".format(api))
            if api == "SendAppToBackground":
                api_result = apis_call[api]()
            else:
                start_time = lib.gettimestamp()
                api_result = apis_call[api]()
                end_time = lib.gettimestamp()
                lib.report_elapsed_time(start_time, end_time, api)
            if not api_result:
                status = "FAILED"
                api_test_status = False
            else:
                status = "PASSED"

            lib.report(api, status, image_required=True)
            time.sleep(2)

    except Exception as e:
        lib.log_error(
            "Exception raised in test_app_info function : " + str(e))
        api_test_status = False
    finally:
        return api_test_status
# ''''''''''''''''''''''''''''USER DEFINED FUNCTIONS - END '''''''''''''''''''''''''''


# ''''''''''''''''''''''''''''MAIN ''''''''''''''''''''''''''''''''''''''''''''''''''''
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#@Function Name	  	: main()
#@Description		: main function
#@Input arguments	: None
#@Output values		: None
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def main():
    driver = False
    script_status = False
    try:
        if not config:
            lib.report("Invalid Config", "FAILED")
            return False

        'updating the Test Script details'
        lib.update_tc_details()
        log_script_info()

        'launching application'
        if lib.start_run(home=config.app_home):
            driver = True
            script_status = test_api()
        else:
            lib.report("Script Status", "FAILED", image_required=True)

    except Exception as e:
        lib.log_error("Exception raised in main function : " + str(e))
        script_status = False

    finally:
        if driver:
            lib.stop_run()
        lib.CommitScriptResult(script_status)
        lib.log_info("-- Execution End --")
# ''''''''''''''''''''''''''''MAIN - END'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if __name__ == "__main__":
    main()

#''''''''''''''''''''''''''''' END OF SCRIPT ''''''''''''''''''''''''''''''''''''''''''''''''''''
