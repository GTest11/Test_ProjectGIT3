#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :   M_API_03
# Author            :   Arathy P S
# Date              :   13-03-2018
# Script Version    :   1.0
# APIs covered      :   GetScreenshot
#                       UploadScreenshot
# Description       :   GetScreenshot & UploadScreenshot API testing.
# Common Fns Used   :   update_TC_details : to update the Common details. Change the build no
#                       in Constants.py file
#
#                       update_dut_config : to configure the device based on the platform.
#                       Change the app details in Config.py file
#
#                       open_app : to start the Appium server & also initialise the driver.
#''''''''''''''''''''AUTO GENERATED CODE - DO NOT MODIFY''''''''''''''''''''
import sys
sys.path.append('../')
import library.common_functions as com_lib


"""
``````````````````````````````````````````````````````````````````````````
Author			    : Arathy P S
Function Name	  	: test_screen_shot()
Description		    : Function to test the GetScreenshot & UploadScreenshot APIs
Input arguments	    : Null
Output values		: Null
``````````````````````````````````````````````````````````````````````````
"""


def test_screen_shot():
    try:
        com_lib.log_info("Getting screen shot from the DUT")
        com_lib.delay(3)
        get_srn_time_list = []
        up_srn_time_list = []

        for i in range(3):
            get_start_time = com_lib.str_to_milli_second_time()
            screen_shot_string = com_lib.dut.GetScreenshot()
            get_end_time = com_lib.str_to_milli_second_time()
            get_srn_time = com_lib.get_duration(get_start_time, get_end_time)
            get_srn_time_list.append(get_srn_time)
            com_lib.commit_step_result("API: Time Taken by GetScreenshotAPI iteration " +
                                       str(i), str(get_srn_time_list.count(i)))

            up_start_time = com_lib.str_to_milli_second_time()
            com_lib.dut.validator.UploadScreenshot("UploadScreenshot", screen_shot_string)
            up_end_time = com_lib.str_to_milli_second_time()
            up_scrn_time = com_lib.get_duration(up_start_time, up_end_time)
            up_srn_time_list.append(up_scrn_time)
            com_lib.commit_step_result("API: Time Taken by UploadScreenshot iteration "
                                       + str(i), str(up_srn_time_list.count(i)))
    except Exception as e:
        com_lib.log_error("Exception raised in test_screen_shot function : " + str(e))

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

        'this is a variable used to update the Test script status'
        global status
        status = False

        'updating the Test Script details'
        com_lib.update_tc_details()

        'configuring the device for automation'
        com_lib.update_dut_config(platform)

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
                test_screen_shot()
                status = True
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
