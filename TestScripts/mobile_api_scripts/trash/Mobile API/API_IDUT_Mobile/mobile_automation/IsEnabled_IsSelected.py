# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :   M_API_15
# Author            :   Rohith P V
# Date              :   16-03-2018
# FE Version        :   5.0.9.4
# APIs covered      :   IsEnabled, IsSelected,Click with index
# Description       :   IsEnabled, IsSelected API testing.
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
Function Name	  	: test_isenabled_isselected()
Description		    : Function to test the HideKeyboard API
Input arguments	    : Null
Output values		: bool
``````````````````````````````````````````````````````````````````````````
"""


def test_isenabled_isselected():
    try:
        fn_return = False
        if str(com_lib.dut.ReadProperty(3)) == "Android":
            element_xpath_isselected = com_lib.android_conf.ELEMENT_XPATH_ISSELECTED
            element_xpath_isenabled = com_lib.android_conf.ELEMENT_XPATH_ISENABLED
        else:
            element_xpath_isselected = com_lib.ios_conf.ELEMENT_XPATH_ISSELECTED
            element_xpath_isenabled = com_lib.ios_conf.ELEMENT_XPATH_ISENABLED
        #IsSelected API
        fn_return_isselected=False
        if com_lib.dut.Click(com_lib.MobileScriptingLibrary.Constants.ElementType.XPath,element_xpath_isselected):
            com_lib.log_info("Click (with Index) Pressed")
            com_lib.delay(com_lib.constant.CLICK_ISSELECTED_DELAY)
            # To validate the click was done at the proper place
            #if(com_lib.wait_for_checkpoint(com_lib.constant.CHKPNT_CLICK_ISSELECTED,com_lib.constant.TIME_TO_WAIT_ISSELECTED ,com_lib.constant.INITIAL_DELAY_ISSELECTED)):
            if com_lib.validate_screen(com_lib.constant.CHKPNT_CLICK_ISSELECTED):
                com_lib.commit_step_result("API: Click (with Index) API", "Passed")
                com_lib.log_info("Click (with Index) Pressed")
                start_time = com_lib.str_to_milli_second_time()
                if com_lib.dut.IsSelected(com_lib.MobileScriptingLibrary.Constants.ElementType.XPath,element_xpath_isselected):
                    end_time = com_lib.str_to_milli_second_time()
                    IsSelected_time = com_lib.get_duration(start_time, end_time)
                    com_lib.commit_step_result("API: Time taken by IsSelected API ", str(IsSelected_time))           
                    if com_lib.validate_screen(com_lib.constant.CHKPNT_CLICK_ISSELECTED):
                     #if(com_lib.wait_for_checkpoint(com_lib.constant.CHKPNT_CLICK_ISSELECTED, com_lib.constant.INITIAL_DELAY_ISSELECTED, com_lib.constant.TIME_TO_WAIT_ISSELECTED )):
                        com_lib.commit_step_result("API: IsSelected API", "Passed")
                        com_lib.log_info("Given element is selected")
                        com_lib.commit_step_result("API: Reason", "Given element is selected")
                        fn_return_isselected=True
                    else:
                        com_lib.log_info("IsSelected API failed")
                        com_lib.commit_step_result("API: Reason", "Given element is not selected")
                        com_lib.commit_step_result("API: IsSelected API", "Failed")
                else:
                    end_time = com_lib.str_to_milli_second_time()
                    IsSelected_time = com_lib.get_duration(start_time, end_time)
                    com_lib.commit_step_result("API: Time taken by IsSelected API ", str(IsSelected_time))
                    if com_lib.validate_screen(com_lib.constant.CHKPNT_CLICK_ISSELECTED):
                    #if(com_lib.wait_for_checkpoint(com_lib.constant.CHKPNT_CLICK_ISSELECTED, com_lib.constant.INITIAL_DELAY_ISSELECTED, com_lib.constant.TIME_TO_WAIT_ISSELECTED )):
                        com_lib.commit_step_result("API: IsSelected API", "Failed")
                        com_lib.log_info("Given element is not selected")
                    else:
                        com_lib.log_info("Given element is selected")
                        com_lib.commit_step_result("API: IsSelected API", "Passed")
                        fn_return_isselected=True
            else:
                com_lib.log_info("Click (with Index) API Failed")
                com_lib.commit_step_result("API: Click (with Index) API", "Failed")
        else:
            com_lib.log_info("Click (with Index) API Failed")
            com_lib.commit_step_result("API: Click (with Index) API", "Failed")

        #IsEnabled API
        
        fn_return_isenabled=False
        start_time = com_lib.str_to_milli_second_time()
        if com_lib.dut.IsEnabled(com_lib.MobileScriptingLibrary.Constants.ElementType.XPath,element_xpath_isenabled):
            end_time = com_lib.str_to_milli_second_time()
            IsEnabled_time = com_lib.get_duration(start_time, end_time)
            com_lib.commit_step_result("API: Time taken by IsEnabled API ", str(IsEnabled_time))
            com_lib.dut.validator.QuickCapture("Widgetview_imageName")
            com_lib.commit_step_result("API: IsEnabled API", "Passed")
            com_lib.commit_step_result("API: Reason", "Given element is enabled")
            com_lib.log_info("Given element is enabled")
            fn_return_isenabled=True
        else:
            end_time = com_lib.str_to_milli_second_time()
            IsEnabled_time = com_lib.get_duration(start_time, end_time)
            com_lib.commit_step_result("API: Time taken by IsEnabled API ", str(IsEnabled_time))
            com_lib.dut.validator.QuickCapture("Widgetview_imageName")
            com_lib.commit_step_result("API: IsEnabled API", "Failed")
            com_lib.commit_step_result("API: Reason", "Given element is not enabled")
            com_lib.log_info("Given element is not enabled")

    except Exception as e:
        com_lib.log_error("Exception raised in test_isenabled_isselected function : " +str(e))
    finally:
        fn_return=fn_return_isselected & fn_return_isenabled
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
            if not com_lib.dut.WaitForElement(
                    com_lib.MobileScriptingLibrary.Constants.ElementType.XPath, element_id, 20):
                com_lib.log_error("App not launched")
            else:
                status = test_isenabled_isselected()
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
