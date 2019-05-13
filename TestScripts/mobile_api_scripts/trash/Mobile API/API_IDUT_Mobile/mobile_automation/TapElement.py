#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :   M_API_03
# Author            :   Arathy P S
# Date              :   16-03-2018
# Script Version    :   1.0
# APIs covered      :   TapElement
# Description       :   TapElement API testing.
# Common Fns Used   :   update_TC_details : to update the Common details. Change the build no
#                       in Constants.py file
#                       update_dut_config : to configure the device based on the platform.
#                       Change the app details in Config.py file
#                       open_app: to start the Appium server & also initialise the driver.
# Config changes    :   android_APP_TAP_ID | ios_APP_TAP_ID : element id on which TAP has to be performed
#                       android_APP_HOME | ios_APP_HOME : home screen element details
#
#''''''''''''''''''''AUTO GENERATED CODE - DO NOT MODIFY''''''''''''''''''''
import sys
sys.path.append('../')
import library.common_functions as com_lib
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


"""
``````````````````````````````````````````````````````````````````````````
Author			    : Arathy P S
Function Name	  	: test_tap_element()
Description		    : Function to test the Tap API
Input arguments	    : Null
Output values		: bool
``````````````````````````````````````````````````````````````````````````
"""


def test_tap_element():
    try:
        if str(com_lib.dut.ReadProperty(3)) == "Android":
            tap_element_id = com_lib.android_conf.android_APP_TAP_ID
        else:
            tap_element_id = com_lib.ios_conf.ios_APP_TAP_ID

        start_time = com_lib.str_to_milli_second_time()
        if com_lib.dut.TapElement(com_lib.MobileScriptingLibrary.Constants.ElementType.XPath, tap_element_id):
            end_time = com_lib.str_to_milli_second_time()
            tap_time = com_lib.get_duration(start_time, end_time)
            com_lib.commit_step_result("API: TapElement API", "PASSED")
            com_lib.commit_step_result("API: Time taken by TapElement API", str(tap_time))
            return True
        else:
            com_lib.commit_step_result("API: TapElement API", "FAILED")
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
                status = test_tap_element()
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
