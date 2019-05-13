# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :
# Date              :   03-10-2018
# FE Version        :   FE 5.1.0.3
# APIs covered      :   HandleAlertMessage
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, os, time
sys.path.append('../')
import library.common_functions as lib

dut = lib.dut
msl = lib.msl


apis_in_the_script = ("HandleAlertMessage"
                      )
config = lib.set_config()


def log_script_info():
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    lib.log_info("Script Name: {}".format(os.path.basename(__file__)))
    lib.log_info("Validating APIs - {}".format(apis_in_the_script))
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


# ``````````````````````````````````````````````````````````````````````````
# Function Name	  	: handle_aler_message()
# Description		: Function to test the handleAlertMessage API
# Input arguments	: Null
# Output values		: bool
# ``````````````````````````````````````````````````````````````````````````
def handle_alert_message():
    api_test_status = False
    try:

        lib.log_info("Message pop up available.")
        lib.log_info(
            "Checking the API behaviour if given invalid parameter")
        start_time = lib.gettimestamp()
        status = dut.HandleAlertMessage(config.HANDLE_ALERT_INVALID)
        end_time = lib.gettimestamp()
        dut.validator.QuickCapture("afterInvalidParameter")
        lib.report_elapsed_time(start_time, end_time, "HANDLE_ALERT_INVALID", str(status))

        time.sleep(20)
        lib.log_info("Checking the API behaviour for parameter: Accept")
        start_time = lib.gettimestamp()
        status = dut.HandleAlertMessage(config.HANDLE_ALERT_ACCEPT)
        end_time = lib.gettimestamp()
        lib.report_elapsed_time(start_time, end_time, "HANDLE_ALERT_ACCEPT", str(status))

        dut.validator.QuickCapture("afterAcceptParameter")
        if not lib.validate_screen(
                lib.constants.CHKPNT_YOU_TUBE_DOWNLOAD_POP_UP):
            api_test_status = True
            lib.log_info("Accepted the pop up")
        else:
            lib.log_warn("pop up message box available even after Accepting")

        if dut.Click(msl.Constants.ElementType.XPath,
                     config.youTube_download_option
                     ):
            dut.validator.QuickCapture("Message pop up")
            time.sleep(3)
            lib.log_info("Checking the API behaviour for parameter: Dismiss")
            start_time = lib.gettimestamp()
            dismiss_status = dut.HandleAlertMessage(config.HANDLE_ALERT_DISMISS)
            end_time = lib.gettimestamp()
            lib.report_elapsed_time(start_time, end_time, "HANDLE_ALERT_DISMISS", str(status))

            dut.validator.QuickCapture("afterDismissParameter")

        if not lib.validate_screen(
                lib.constants.CHKPNT_YOU_TUBE_DOWNLOAD_POP_UP):
            api_test_status = True
            lib.log_info("Dismissed the pop up")
        else:
            api_test_status = False
            lib.log_info("pop up message box available even after Dismissing.")

    except Exception as e:
        lib.log_error("Exception raised in handle_aler_message() function : " + str(e))
        api_test_status = False
    finally:
        return api_test_status


# ``````````````````````````````````````````````````````````````````````````
# Function Name	  	: test_handleAlertMessage()
# Description		: Function to test the handleAlertMessage API
# Input arguments	: Null
# Output values		: bool
# ``````````````````````````````````````````````````````````````````````````
def test_api():
    script_status = False
    try:
        if dut.Click(msl.Constants.ElementType.XPath, config.youTube_download_option):
            time.sleep(3)
            dut.validator.QuickCapture("firstClickOnDownload")
            # Checking whether download button clicked or not
            # if
            # com_lib.validate_screen(com_lib.constant.CHKPNT_IOS_YOU_TUBE_DOWNLOAD_BUTTON):
            lib.log_info(
                "Checking the API behaviour if there is no message pop up available")
            dut.HandleAlertMessage(config.HANDLE_ALERT_DISMISS)
            if dut.Click(
                    msl.Constants.ElementType.XPath, config.youTube_download_option):
                # Checking whether message pop - up button clicked or not
                time.sleep(10)
                dut.validator.QuickCapture("firstClickOnDownload")
                if lib.validate_screen(
                        lib.constants.CHKPNT_YOU_TUBE_DOWNLOAD_POP_UP):
                    dut.validator.QuickCapture("afterPopUp")
                    script_status = handle_alert_message()
                else:
                    lib.log_info(
                        "Message pop up not available..")
                # else:
                 #   com_lib.logger.Log("Download option click2 failed.")
            else:
                lib.log_warn("Download option is not available..")
        else:
            lib.log_warn("Download option click failed.")
    except Exception as e:
        lib.log_error("Exception raised in test_handleAlertMessage function : " + str(e))
        script_status = False
    finally:
        return script_status


# ``````````````````````````````````````````````````````````````````````````
# Function Name	  	: main()
# Description		: main
# Input arguments	: Null
# Output values		: Null
# ``````````````````````````````````````````````````````````````````````````

def main():
    script_status = False
    try:
        if not config:
            lib.report("Invalid Config", "FAILED")
            return False

        lib.log_info("*** THIS API SUPPORTS ONLY iOS ***")

        'updating the Test Script details'
        lib.update_tc_details()
        log_script_info()

        'launching application'
        if lib.start_run(home=config.app_home):
            # dut.Tap(0, 178)
            script_status = test_api()
        else:
            lib.report("Script Status", "FAILED", image_required=True)

    except Exception as e:
        lib.log_error("Exception raised in main function : " + str(e))
    finally:
        lib.stop_run()
        lib.CommitScriptResult(script_status)
        lib.log_info("-- Execution End --")

if __name__ == "__main__":
    main()
