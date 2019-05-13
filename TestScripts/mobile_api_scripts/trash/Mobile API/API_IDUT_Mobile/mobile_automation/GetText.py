#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :   M_API_03
# Author            :   Arathy P S
# Date              :   16-03-2018
# Script Version    :   1.0
# APIs covered      :   GetText
# Description       :   GetText API testing.
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
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


"""
``````````````````````````````````````````````````````````````````````````
Author			    : Arathy P S
Function Name	  	: test_get_text()
Description		    : Function to test the GetText API
Input arguments	    : Null
Output values		: get_text : string obtained from GetText API
``````````````````````````````````````````````````````````````````````````
"""


def test_get_text():
    try:
        if platform == "Android":
            get_text_element_id = com_lib.android_conf.android_APP_GETTEXT
            
        else:
            get_text_element_id = com_lib.ios_conf.ios_APP_GETTEXT
            
        com_lib.dut.validator.QuickCapture("imageName")
        start_time = com_lib.str_to_milli_second_time()
        get_text = com_lib.dut.GetText(com_lib.MobileScriptingLibrary.Constants.ElementType.XPath,get_text_element_id)
        end_time = com_lib.str_to_milli_second_time()
        com_lib.dut.validator.QuickCapture("imageName")
        get_text_time = com_lib.get_duration(start_time, end_time)
        com_lib.commit_step_result("API: Time taken by GetText API", str(get_text_time))
        com_lib.commit_step_result("Text from GetText API", str(get_text))
        return get_text
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
        status = False

        'launching application'
        init_app_time = com_lib.open_app()
        if init_app_time > 0:
            if "Android" == platform:
                element_id = com_lib.android_conf.android_APP_HOME
            else:
                element_id = com_lib.ios_conf.ios_APP_HOME
            com_lib.dut.validator.QuickCapture("imageName")
            if not com_lib.dut.WaitForElement(com_lib.MobileScriptingLibrary.Constants.ElementType.XPath, element_id, 20):
                com_lib.log_error("App not launched")
            else:
                str_get_text = test_get_text()
                if str_get_text == com_lib.constant.android_expected_str_gettext or str_get_text == com_lib.constant.ios_expected_str_gettext:
                    status = True
                    com_lib.commit_step_result("API: GetText API", "Passed")
                    com_lib.commit_step_result("API: Reason", "Expected text obtained from the API")
                else:
                    com_lib.commit_step_result("API: GetText API", "Failed")
                    com_lib.commit_step_result("API: Reason", "No text obtained")
                com_lib.dut.validator.QuickCapture("imageName")
        else:
            com_lib.dut.validator.QuickCapture("imageName")
            com_lib.log_error("Error in InitApp API")

    except Exception as e:
        com_lib.log_error("Exception raised in main function : " + str(e))
    finally:
        com_lib.close_app()
        com_lib.stop_driver()
        com_lib.CommitScriptResult(status)

if __name__ == "__main__":
    main()
