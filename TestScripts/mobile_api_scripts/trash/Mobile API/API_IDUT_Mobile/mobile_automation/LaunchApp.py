#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :   M_API_03
# Author            :   Arathy P S
# Date              :   15-03-2018
# Script Version    :   1.0
# APIs covered      :   LaunchApp
# Description       :   LaunchApp API testing.
# Common Fns Used   :   update_TC_details : to update the Common details. Change the build no
#                       in Constants.py file
#
#                       update_dut_config : to configure the device based on the platform.
#                       Change the app details in Config.py file
#
#                       open_app: to start the Appium server & also initialise the driver.
#''''''''''''''''''''AUTO GENERATED CODE - DO NOT MODIFY''''''''''''''''''''
import sys
sys.path.append('../')
import library.common_functions as com_lib
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


"""
``````````````````````````````````````````````````````````````````````````
Author			    : Arathy P S
Function Name	  	: launch_app()
Description		    : Function to test the LaunchApp API
Input arguments	    : Null
Output values		: Bool
``````````````````````````````````````````````````````````````````````````
"""


def launch_app():
    try:
        close_status = com_lib.dut.CloseApp()
		com_lib.delay(3)
        if close_status:
            com_lib.dut.validator.QuickCapture("CloseAPP_imageName")
            start_time = com_lib.str_to_milli_second_time()
            if com_lib.dut.LaunchApp():
                com_lib.dut.validator.QuickCapture("LaunchAPP_imageName")
                end_time = com_lib.str_to_milli_second_time()
                tap_time = com_lib.get_duration(start_time, end_time)
                com_lib.commit_step_result("API: Time taken by LaunchApp API", str(tap_time))
                if "Android" == platform:
                    element_id = com_lib.android_conf.android_APP_HOME
                else:
                    element_id = com_lib.ios_conf.ios_APP_HOME
                if com_lib.dut.WaitForElement(com_lib.MobileScriptingLibrary.Constants.ElementType.XPath, element_id, 20):
                    com_lib.commit_step_result("API: LaunchApp", "Passed")
                    com_lib.commit_step_result("API: Reason", "App relaunched")
                    return True
                else:
                    com_lib.commit_step_result("API: LaunchApp", "Failed")
                    com_lib.commit_step_result("API: Reason", "App not relaunched")
            else:
                return False
        else:
            return False
    except Exception as e:
        com_lib.log_error("Exception raised in test_tap function : " + str(e))

"""
``````````````````````````````````````````````````````````````````````````
Author			    : Arathy P S
Function Name	  	: main()
Description		    : Function where script execution starts
Input arguments	    : Null
Output values		: Null
``````````````````````````````````````````````````````````````````````````
"""


def main():
    try:
        'this is a variable used to hold the Platform name'
        global platform
        platform = str(com_lib.dut.ReadProperty(3))

        'updating the Test Script details'
        com_lib.update_tc_details()

        'configuring the device for automation'
        com_lib.update_dut_config(platform)

        'this is a variable used to update the Test script status'
        global status
        status = False

        'launching application'
        init_app_time = com_lib.open_app()
        if init_app_time > 0:
            if "Android" == str(platform):
                element_id = com_lib.android_conf.android_APP_HOME
            else:
                element_id = com_lib.ios_conf.ios_APP_HOME
            if not com_lib.dut.WaitForElement(com_lib.MobileScriptingLibrary.Constants.ElementType.XPath, element_id, 20):
                com_lib.log_error("App not launched")
            else:
                com_lib.log_info("App Launched Successfully")
                com_lib.delay(3)
                status = launch_app()
        else:
            com_lib.log_error("Error in InitApp API")
    except Exception as e:
        com_lib.log_error("Exception raised in main function : " + str(e))
    finally:
        com_lib.close_app()
        com_lib.stop_driver()
        com_lib.CommitScriptResult(status)

if __name__ == "__main__":
    main()
