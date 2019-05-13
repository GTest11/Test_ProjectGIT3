#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :   Arathy P S
# Date              :   15-03-2018
# Script Version    :   1.0
# APIs covered      :   TapPercent
# Description       :   TapPercent API testing.
# Common Fns Used   :   update_TC_details : to update the Common details. Change the build no
#                       in Constants.py file
#
#                       update_dut_config : to configure the device based on the platform.
#                       Change the app details in Config.py file
#
#                       open_app: to start the Appium server & also initialise the driver.
# Config changes    :   TAP_X_PERCENT & TAP_Y_PERCENT : horizontal Percentage & vertical Percentage
#                       android_APP_HOME | ios_APP_HOME : home screen element details
#''''''''''''''''''''AUTO GENERATED CODE - DO NOT MODIFY''''''''''''''''''''
import sys
sys.path.append('../')
import library.common_functions as com_lib

"""
``````````````````````````````````````````````````````````````````````````
Author			    : Arathy P S
Function Name	  	: test_tap_percent()
Description		    : Function to test the Tap percent API
Input arguments	    : Null
Output values		: Bool
``````````````````````````````````````````````````````````````````````````
"""


def test_tap_percent():
    try:
        start_time = com_lib.str_to_milli_second_time()
        if com_lib.dut.TapPercent(com_lib.constant.TAP_X_PERCENT, com_lib.constant.TAP_Y_PERCENT):
            end_time = com_lib.str_to_milli_second_time()
            tap_time = com_lib.get_duration(start_time, end_time)
            com_lib.commit_step_result("API: Time taken by TapPercent API", str(tap_time))
            com_lib.commit_step_result("API: TapPercent API", "PASSED")
            return True
        else:
            com_lib.commit_step_result("API: TapPercent API", "FAILED")
            return False
    except Exception as e:
        com_lib.log_error("Exception raised in test_tap_percent function : " + str(e))

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
                status = test_tap_percent()
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
