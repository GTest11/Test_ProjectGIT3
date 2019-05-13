#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :   M_API_03
# Author            :   Arathy P S
# Date              :   13-03-2018
# Script Version    :   1.0
# APIs covered      :   SetOrientation
#                       GetOrientation
# Description       :   SetOrientation API testing.
# Common Fns Used   :   update_TC_details : to update the Common details. Change the build no
#                       in Constants.py file
#
#                       update_dut_config : to configure the device based on the platform.
#                       Change the app details in Config.py file
#
#                       open_app: to start the Appium server & also initialise the driver.
# Config changes    :   android_APP_HOME | ios_APP_HOME : home screen element details
#''''''''''''''''''''AUTO GENERATED CODE - DO NOT MODIFY''''''''''''''''''''
import sys
sys.path.append('../')
import library.common_functions as com_lib

"""
``````````````````````````````````````````````````````````````````````````
Author			    : Arathy P S
Function Name	  	: test_set_orientation()
Description		    : Function to test the SetOrientation API
Input arguments	    : Null
Output values		: bool
``````````````````````````````````````````````````````````````````````````
"""


def test_set_orientation():
    try:
        start_time_get = com_lib.str_to_milli_second_time()
        orientation_before_change = com_lib.dut.GetOrientation()
        end_time_get = com_lib.str_to_milli_second_time()
        get_oren_time = com_lib.get_duration(start_time_get, end_time_get)
        com_lib.commit_step_result("API: Time taken by GetOrientation API", str(get_oren_time))
        com_lib.log_info("Get orientation : " + str(orientation_before_change))
        if orientation_before_change == "Landscape":
            orientation = "Portrait"
        else:
            orientation = "Landscape"
        com_lib.delay(3)
        resln_before_change_orientation = com_lib.get_image_resolution()
        com_lib.commit_step_result("Image Resolution on" + str(orientation_before_change),
                                   str(resln_before_change_orientation))
        start_time_set = com_lib.str_to_milli_second_time()
        if com_lib.dut.SetOrientation(orientation):
            end_time_set = com_lib.str_to_milli_second_time()
            set_oren_time = com_lib.get_duration(start_time_set, end_time_set)
            com_lib.commit_step_result("API: Time taken by SetOrientation API",
                                       str(set_oren_time))
            com_lib.commit_step_result("API: SetOrientation", "Passed")
            com_lib.delay(3)
            orientation_after_change = com_lib.dut.GetOrientation()
            resln_after_change_orientation = com_lib.get_image_resolution()
            com_lib.commit_step_result("Image Resolution on" + str(orientation_after_change),
                                       str(resln_after_change_orientation))
            return True
        else:
            com_lib.commit_step_result("API: SetOrientation", "Failed")
            return False
    except Exception as e:
        com_lib.log_error("Exception raised in test_SetOrientation function : " + str(e))

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
                status = test_set_orientation()
        else:
            com_lib.log_error("Error in InitApp API")
    except Exception as e:
        com_lib.log_error("Exception raised in main function : " + str(e))
    finally:
        com_lib.dut.SetOrientation("Portrait")
        com_lib.close_app()
        com_lib.stop_driver()
        com_lib.CommitScriptResult(status)
if __name__ == "__main__":
    main()
