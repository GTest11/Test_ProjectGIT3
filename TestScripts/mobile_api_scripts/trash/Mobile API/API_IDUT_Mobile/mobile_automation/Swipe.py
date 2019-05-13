# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :   M_API_15
# Author            :   Rohith P V
# Date              :   16-03-2018
# FE Version        :   5.0.9.4
# APIs covered      :   Swipe, Click (with index), SendKeys, SendAndroidKeyCode, Tap
# Description       :   Swipe API testing.
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
Function Name	  	: test_swipe()
Description		    : Function to test the Swipe API
Input arguments	    : Null
Output values		: bool
``````````````````````````````````````````````````````````````````````````
"""


def test_swipe():
    try:
        fn_return = False
        if str(com_lib.dut.ReadProperty(3)) == "Android":
            X1=com_lib.coordinate.X1_SWIPE_ANDROID
            Y1=com_lib.coordinate.Y1_SWIPE_ANDROID
            X2=com_lib.coordinate.X2_SWIPE_ANDROID
            Y2=com_lib.coordinate.Y2_SWIPE_ANDROID
        else:
            X1=com_lib.coordinate.X1_SWIPE_IOS
            Y1=com_lib.coordinate.Y1_SWIPE_IOS
            X2=com_lib.coordinate.X2_SWIPE_IOS
            Y2=com_lib.coordinate.Y2_SWIPE_IOS
        if com_lib.youtube_launch_video():
            com_lib.delay(com_lib.constant.DELAY_BEFORE_SWIPE)
            start_time = com_lib.str_to_milli_second_time()
            if com_lib.dut.Swipe(X1,Y1,X2,Y2):
                end_time = com_lib.str_to_milli_second_time()
                Swipe_time = com_lib.get_duration(start_time, end_time)
                com_lib.commit_step_result("API: Time taken by Swipe API ", str(Swipe_time))
                com_lib.delay(com_lib.constant.DELAY_AFTER_SWIPE)
                if com_lib.validate_screen(com_lib.constant.CHKPNT_SWIPE):
                    com_lib.logger.Log("Swiping done ")
                    com_lib.commit_step_result("API: Swipe", "Passed")
                    com_lib.commit_step_result("API: Reason" , "Swiping done, confirmed by chkpt validation")
                    fn_return=True
                else:
                    com_lib.commit_step_result("API: Swipe","Failed")
                    com_lib.log_info("Swipe API Failed")
                    com_lib.commit_step_result("API: Reason" , "Swiping not done, confirmed by chkpt validation")
            else:
                com_lib.logger.Log("Swipe failed")
                com_lib.commit_step_result("API: Swipe API", "Failed")
                com_lib.commit_step_result("API: Reason" , "API returned False")
        else:
            com_lib.log_info("youtube_launch_video function failed")
            com_lib.commit_step_result("youtube_launch_video function", "Failed")
    except Exception as e:
        com_lib.log_error("Exception raised in test_swipe function : " +str(e))
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
            if not com_lib.dut.WaitForElement(
                    com_lib.MobileScriptingLibrary.Constants.ElementType.XPath, element_id, 20):
                com_lib.log_error("App not launched")
            else:
                status = test_swipe()
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
