#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :   Arathy P S
# Date              :   13-03-2018
# Script Version    :   1.0
# APIs covered      :   ChangeOrientation
#                       GetOrientation
# Description       :   ChangeOrientation API testing.
# Common Fns Used   :   update_TC_details : to update the Common details. Change the build no
#                       in Constants.py file
#
#                       update_dut_config : to configure the device based on the platform.
#                       Change the app details in Config.py file
#
#                       open_app: to start the Appium server & also initialise the driver.
#''''''''''''''''''''AUTO GENERATED CODE - DO NOT MODIFY'''''''''''''''''''''
import sys
sys.path.append('../')
import library.common_functions as com_lib

"""
``````````````````````````````````````````````````````````````````````````
Author			    : Arathy P S
Function Name	  	: test_ChangeOrientation()
Description		    : Function to test the ChangeOrientation API
Input arguments	    : Null
Output values		: bool
``````````````````````````````````````````````````````````````````````````
"""


def test_change_orientation():
    try:
        global fn_return
        fn_return = False
        start_time_get = com_lib.str_to_milli_second_time()
        orientation_before_change = com_lib.dut.GetOrientation()
        end_time_get = com_lib.str_to_milli_second_time()
        get_oren_time = com_lib.get_duration(start_time_get, end_time_get)
        com_lib.commit_step_result("API: Time taken by GetOrientation API", str(get_oren_time))
        if "" != orientation_before_change:
            com_lib.commit_step_result("API: GetOrientation API", "Passed")
        else:
            com_lib.commit_step_result("API: GetOrientation API", "Failed")
        com_lib.log_info("Get orientation : " + str(orientation_before_change))
        com_lib.commit_step_result("Get orientation : ", str(orientation_before_change))
        com_lib.delay(3)
        resln_befr_change_orient = com_lib.get_image_resolution()
        com_lib.commit_step_result("Image Resolution on "
                                   + str(orientation_before_change), str(resln_befr_change_orient))

        start_time_chng = com_lib.str_to_milli_second_time()
        if com_lib.dut.ChangeOrientation():
            end_time_chng = com_lib.str_to_milli_second_time()
            chng_oren_time = com_lib.get_duration(start_time_chng, end_time_chng)
            com_lib.commit_step_result("API: Time taken by ChangeOrientation API", str(chng_oren_time))
            com_lib.delay(3)
            com_lib.commit_step_result("API: ChangeOrientation API", "Passed")
            com_lib.commit_step_result("API: Reason", "Orientation Changed")
            orientation_after_change = com_lib.dut.GetOrientation()
            com_lib.log_info("Get orientation : " + str(orientation_after_change))
            resln_after_change_orient = com_lib.get_image_resolution()
            com_lib.commit_step_result("Image Resolution on "
                                       + str(orientation_after_change), str(resln_after_change_orient))
            if resln_befr_change_orient[0] == resln_after_change_orient[1] and resln_befr_change_orient[1] == \
                    resln_after_change_orient[0]:
                fn_return = True
        else:
            com_lib.commit_step_result("API: ChangeOrientation API", "Failed")
            com_lib.commit_step_result("API: Reason", "No change in orientation after the API call")
    except Exception as e:
        com_lib.log_error("Exception raised in test_ChangeOrientation function : " + str(e))
    finally:
        return fn_return
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
                com_lib.dut.validator.QuickCapture("wait_imageName")
                com_lib.log_error("App not launched")
            else:
                com_lib.dut.validator.QuickCapture("imageName")
                status = test_change_orientation()
        else:
            com_lib.dut.validator.QuickCapture("imageName")
            com_lib.log_error("Error in InitApp API")
    except Exception as e:
        com_lib.log_error("Exception raised in main function: " + str(e))
    finally:
        if com_lib.dut.SetOrientation("Portrait"):
            com_lib.commit_step_result("API: SetOrientation API", "Passed")
            com_lib.commit_step_result("API: Reason", "Orientation Changed")
        else:
            com_lib.commit_step_result("API: SetOrientation API", "Failed")
            com_lib.commit_step_result("API: Reason", "API returns False")
        com_lib.close_app()
        com_lib.stop_driver()
        com_lib.CommitScriptResult(status)
if __name__ == "__main__":
    main()
