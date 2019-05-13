#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :   M_API_03
# Author            :   Arathy P S
# Date              :   15-03-2018
# Script Version    :   1.0
# APIs covered      :   Tap
# Description       :   Tap API testing.
# Common Fns Used   :   update_TC_details : to update the Common details. Change the build no
#                       in Constants.py file
#
#                       update_dut_config : to configure the device based on the platform.
#                       Change the app details in Config.py file
#
#                       open_app: to start the Appium server & also initialise the driver.
# Config changes    :   TAP_X & TAP_Y : X coordinate & Y coordinate
#                       android_APP_HOME | ios_APP_HOME : home screen element details
#''''''''''''''''''''AUTO GENERATED CODE - DO NOT MODIFY''''''''''''''''''''
import sys
sys.path.append('../')
import library.common_functions as com_lib


"""
``````````````````````````````````````````````````````````````````````````
Author			    : Arathy P S
Function Name	  	: test_tap()
Description		    : Function to test the Tap API
Input arguments	    : Null
Output values		: Bool
``````````````````````````````````````````````````````````````````````````
"""


def test_tap():
    try:
        if "Android" == platform:
            com_lib.youtube_search_click_type_android()
        else:
            com_lib.youtube_search_click_type_iOS()
        start_time = com_lib.str_to_milli_second_time()
        if com_lib.dut.Tap(com_lib.constant.TAP_X, com_lib.constant.TAP_Y):
            end_time = com_lib.str_to_milli_second_time()
            tap_time = com_lib.get_duration(start_time, end_time)
            com_lib.commit_step_result("API: Time taken by Tap API", str(tap_time))
            if com_lib.motion_detection():
                com_lib.commit_step_result("API: Tap", "PASSED")
                com_lib.commit_step_result("API: Reason" , "Screen changed, confirmed by Detectmotion")
                return True
            else:
                com_lib.commit_step_result("API: Tap", "FAILED")
                com_lib.commit_step_result("API: Reason" , "Tap failed, confirmed by Detectmotion")
                return False
        else:
            com_lib.commit_step_result("API: Tap", "FAILED")
            com_lib.commit_step_result("API: Reason" , "API returned False")
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
            if "Android" == platform:
                element_id = com_lib.android_conf.android_APP_HOME
            else:
                element_id = com_lib.ios_conf.ios_APP_HOME
            if not com_lib.dut.WaitForElement(com_lib.MobileScriptingLibrary.Constants.ElementType.XPath, element_id, 20):
                com_lib.log_error("App not launched")
            else:
                status = test_tap()
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
