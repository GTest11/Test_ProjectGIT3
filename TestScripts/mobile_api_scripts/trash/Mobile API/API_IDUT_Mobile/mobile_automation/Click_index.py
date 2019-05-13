# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :   M_API_04
# Author            :   Rohith P V
# Date              :   20-03-2018
# FE Version        :   5.0.9.4
# APIs covered      :   Click(with index), SendAndroidKeyCode, SendKeys
# Description       :   Click(with index), SendAndroidKeyCode SendKeys API testing.
# Common Fns Used   :    update_TC_details : to update the Common details. Change the build no
#                       in Constants.py file
#
#                       update_dut_config : to configure the device based on the platform.
#                       Change the app details in Config.py file
#
# open_app: to start the Appium server & also initialise the driver.

# ''''''''''''''''''''AUTO GENERATED CODE - DO NOT MODIFY''''''''''''''''''''
import sys
sys.path.append('../')
import library.common_functions as com_lib

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


"""
``````````````````````````````````````````````````````````````````````````
Author			    : Rohith P V
Function Name	  	: test_click_index()
Description		    : Function to test the Click(with index) API
Input arguments	    : ElementType,ElementID,Index
Output values		: bool
``````````````````````````````````````````````````````````````````````````
"""


def test_click_index():
    try:
        # global fn_return
        fn_return = False
        if str(com_lib.dut.ReadProperty(3)) == "Android":
            click_xpath = com_lib.android_conf.ELEMENT_XPATH_CLICK_INDEX
        else:
            click_xpath = com_lib.ios_conf.ELEMENT_XPATH_CLICK_INDEX
        start_time = com_lib.str_to_milli_second_time()
        if com_lib.dut.Click(com_lib.MobileScriptingLibrary.Constants.ElementType.XPath,
                             click_xpath, com_lib.constant.CLICK_INDEX):
            end_time = com_lib.str_to_milli_second_time()
            click_index_time = com_lib.get_duration(start_time, end_time)
            com_lib.commit_step_result("API: Time taken by Click (with Index) API",
     str(click_index_time))
            com_lib.log_info("Click (with Index) Pressed")
            com_lib.delay(com_lib.constant.CLICK_INDEX_DELAY)
            # To validate the click was done at the proper place
            if(com_lib.validate_screen(com_lib.constant.CHKPNT_CLICK_INDEX)):
                com_lib.commit_step_result("API: Click (with Index) API", "Passed")
                com_lib.commit_step_result(
                    "API: Reason", "Click Passed. Confirmed by chkpt Validation")
                com_lib.log_info("Click (with Index) on Search Pressed")
                fn_return = True
            else:
                com_lib.log_info("Click (with Index) API Failed")
                com_lib.commit_step_result("API: Click (with Index) API", "Failed")
                com_lib.commit_step_result(
                    "API: Reason", "Click Failed. Confirmed by chkpt Validation")
        else:
            com_lib.log_info("Click (with Index) API Failed")
            com_lib.commit_step_result("API: Click (with Index) API", "Failed")
            com_lib.commit_step_result("API: Reason","Click failed. API returns False")
    except Exception as e:
        com_lib.log_error("Exception raised in test_click_index function : " + str(e))
    finally:
        return fn_return
"""
``````````````````````````````````````````````````````````````````````````
Author			    : Rohith P V
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
            if not com_lib.dut.WaitForElement(com_lib.MobileScriptingLibrary.Constants.ElementType.XPath,element_id, 20):
                com_lib.log_error("App not launched")
            else:
                status = test_click_index()
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
