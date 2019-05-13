__author__ = 'arya'
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :   M_API_26
# Author            :   Arya L
# Date              :   28 June 2018
# Version           :   1.0
# APIs covered      :
# Description       :   HandleAlertMessage API testing
#                       Launch youTube --> play a video -->
#                       click on download twice to launch the pop up dialog box
#
# Common Fns Used   :   update_TC_details : to update the Common details. Change the build no
#                       in Constants.py file
#
#                       update_dut_config : to configure the device based on the platform.
#                       Change the app details in Config.py file
#
# open_app: to start the Appium server & also initialise the driver.
# Before test login to youTube
# Check the correct ness of: youTubeDownloadOptionOCR and ios_youTubeDownloadPopUpOCR
# checkpoints
# Remove the video from you tube downloaded list if it is already dowloaded
# ''''''''''''''''''''AUTO GENERATED CODE - DO NOT MODIFY''''''''''''''''''''
import sys
sys.path.append('../')
import library.common_functions as com_lib
from mobile_config.constants import PLATFORM_PROPERTY, CHKPNT_IOS_YOU_TUBE_DOWNLOAD_BUTTON, \
    CHKPNT_IOS_YOU_TUBE_DOWNLOAD_POP_UP, HANDLE_ALERT_DISMISS, HANDLE_ALERT_ACCEPT, HANDLE_ALERT_INVALID
from mobile_config.ios_config import *
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


# ``````````````````````````````````````````````````````````````````````````
# Function Name	  	: verifyHandleAlertMessage()
# Description		: Function to test the handleAlertMessage API
# Input arguments	: Null
# Output values		: bool
# ``````````````````````````````````````````````````````````````````````````
def verifyHandleAlertMessage():
    try:
        fn_return = False
        com_lib.logger.Log("Message pop up available.")
        com_lib.logger.Log(
            "Checking the API behaviour if given invalid parameter")
        start_time = com_lib.str_to_milli_second_time()
        invalid_status = com_lib.dut.HandleAlertMessage(HANDLE_ALERT_INVALID)
        end_time = com_lib.str_to_milli_second_time()
        handle_invalid_time = com_lib.get_duration(start_time, end_time)
        com_lib.dut.validator.QuickCapture("afterInvalidParameter")
        com_lib.dut.CommitStepResult(
            "HANDLE_ALERT_INVALID", str(invalid_status))
        com_lib.dut.CommitStepResult(
            "API: Duration", str(handle_invalid_time))
        com_lib.time.sleep(20)
        com_lib.logger.Log("Checking the API behaviour for parameter: Accept")
        start_time = com_lib.str_to_milli_second_time()
        accept_status = com_lib.dut.HandleAlertMessage(HANDLE_ALERT_ACCEPT)
        end_time = com_lib.str_to_milli_second_time()
        handle_accept_time = com_lib.get_duration(start_time, end_time)
        com_lib.dut.CommitStepResult("HANDLE_ALERT_ACCEPT", str(accept_status))
        com_lib.dut.CommitStepResult(
            "API: Duration", str(handle_accept_time))
        com_lib.dut.validator.QuickCapture("afterAcceptParameter")
        if not com_lib.validate_screen(
                com_lib.constant.CHKPNT_IOS_YOU_TUBE_DOWNLOAD_POP_UP):
            fn_return = True
            com_lib.logger.Log("Accepted the pop up")
        else:
            com_lib.logger.Log(
                "pop up message box available even after Accepting")

        if com_lib.dut.Click(
                com_lib.MobileScriptingLibrary.Constants.ElementType.XPath, ios_youTube_download_option):
            com_lib.dut.validator.QuickCapture("Message pop up")
            com_lib.time.sleep(3)
            com_lib.logger.Log(
                "Checking the API behaviour for parameter: Dismiss")
            start_time = com_lib.str_to_milli_second_time()
            dismiss_status = com_lib.dut.HandleAlertMessage(
                HANDLE_ALERT_DISMISS)
            end_time = com_lib.str_to_milli_second_time()
            handle_dismiss_time = com_lib.get_duration(
                start_time, end_time)
            com_lib.dut.CommitStepResult(
                "HANDLE_ALERT_DISMISS", str(dismiss_status))
            com_lib.dut.CommitStepResult(
                "API: Duration", str(handle_dismiss_time))
            com_lib.dut.validator.QuickCapture("afterDismissParameter")

        if not com_lib.validate_screen(
                com_lib.constant.CHKPNT_IOS_YOU_TUBE_DOWNLOAD_POP_UP):
            fn_return = True
            com_lib.logger.Log("Dismissed the pop up")
        else:
            fn_return = False
            com_lib.logger.Log(
                "pop up message box available even after Dismissing.")
    except Exception as e:
        com_lib.log_error(
            "Exception raised in verifyHandleAlertMessage function : " +
            str(e))
    finally:
        return fn_return


# ``````````````````````````````````````````````````````````````````````````
# Function Name	  	: test_handleAlertMessage()
# Description		: Function to test the handleAlertMessage API
# Input arguments	: Null
# Output values		: bool
# ``````````````````````````````````````````````````````````````````````````
def test_handleAlertMessage():
    try:
        fn_return = False
        if com_lib.dut.Click(
                com_lib.MobileScriptingLibrary.Constants.ElementType.XPath, ios_youTube_download_option):
            com_lib.time.sleep(3)
            com_lib.dut.validator.QuickCapture("firstClickOnDownload")
            # Checking whether download button clicked or not
            # if
            # com_lib.validate_screen(com_lib.constant.CHKPNT_IOS_YOU_TUBE_DOWNLOAD_BUTTON):
            com_lib.logger.Log(
                "Checking the API behaviour if there is no message pop up available")
            com_lib.dut.HandleAlertMessage(HANDLE_ALERT_DISMISS)
            if com_lib.dut.Click(
                    com_lib.MobileScriptingLibrary.Constants.ElementType.XPath, ios_youTube_download_option):
                # Checking whether message pop - up button clicked or not
                com_lib.time.sleep(10)
                com_lib.dut.validator.QuickCapture("firstClickOnDownload")
                if com_lib.validate_screen(
                        com_lib.constant.CHKPNT_IOS_YOU_TUBE_DOWNLOAD_POP_UP):
                    com_lib.dut.validator.QuickCapture("afterPopUp")
                    fn_return = verifyHandleAlertMessage()
                else:
                    com_lib.logger.Log(
                        "Message pop up not available in the UI..")
                # else:
                 #   com_lib.logger.Log("Download option click2 failed.")
            else:
                com_lib.logger.Log(
                    "Download option is not available in the UI..")
        else:
            com_lib.logger.Log("Download option click1 failed.")
    except Exception as e:
        com_lib.log_error(
            "Exception raised in test_handleAlertMessage function : " +
            str(e))
    finally:
        return fn_return


# ``````````````````````````````````````````````````````````````````````````
# Function Name	  	: main()
# Description		: main
# Input arguments	: Null
# Output values		: Null
# ``````````````````````````````````````````````````````````````````````````
def main():
    #'this is a variable used to hold the Platform name'
    global platform
    platform = str(com_lib.dut.ReadProperty(PLATFORM_PROPERTY))
    #'this is a variable used to update the Test script status'
    global status
    status = False
    if "iOS" == platform:
        try:
            com_lib.dut.validator.QuickCapture("InitialUI")
            com_lib.logger.Log("Testing HandleAlertMessage API...")
            'updating the Test Script details'
            com_lib.update_tc_details()
            #'configuring the device for automation'
            com_lib.update_dut_config(platform)

            #'launching application'
            init_app_time = com_lib.open_app()
            if init_app_time > 0:
                element_XPath = com_lib.ios_conf.ios_youTube_home
                if not com_lib.dut.WaitForElement(
                        com_lib.MobileScriptingLibrary.Constants.ElementType.XPath, element_XPath, 30):
                    com_lib.log_error("App not launched")
                else:
                    com_lib.dut.validator.QuickCapture("appLaunched")
                    com_lib.time.sleep(5)
                    if com_lib.dut.Tap(0, 178):
                        com_lib.time.sleep(5)
                        com_lib.dut.validator.QuickCapture("videoPlayed")
                        status = test_handleAlertMessage()
                    else:
                        com_lib.log_error("Error in InitApp API")
            else:
                com_lib.logger.Log("Tap to play video failed")

        except Exception as e:
            com_lib.log_error("Exception raised in main function : " + str(e))

        finally:
            com_lib.close_app()
            com_lib.stop_driver()
            com_lib.CommitScriptResult(status)

    else:
        com_lib.logger.Warn(
            "HandleAlertMessage API is only available for iOS devices.")
        com_lib.dut.CommitTestResult("ABORTED")
# ``````````````````````````````````````````````````````````````````````````


if __name__ == "__main__":
    main()
