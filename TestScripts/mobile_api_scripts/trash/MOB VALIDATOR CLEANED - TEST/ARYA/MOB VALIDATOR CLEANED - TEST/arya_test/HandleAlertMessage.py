# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :   03-10-2018
#Script Version     : 1.1
# APIs covered      :   HandleAlertMessage
#Test Scenario:
#init to Youtube
# '''''''''''''''''''''''''''TEST CASE DETAILS' - END '''''''''''''''''''''''''''''''''

# ''''''''''''''''''''''''''''''''''''''''IMPORTS''''''''''''''''''''''''''''''''''''''

#importing python modules
import sys
import os
import time

#importing user defined functions
sys.path.append('../')
try:
    # Import library file
    import library.common_functions as lib
except ImportError:
    print("Failed to import common_functions file")
    sys.exit()
# ''''''''''''''''''''''''''''''''''''''''IMPORTS - END'''''''''''''''''''''''''''''''

# ''''''''''''''''''''' ''''''''USER DEFINED VARIABLES'''''''''''''''''''''''''''''''''

apis_in_the_script = ("HandleAlertMessage")
config = lib.set_config()
# ''''''''''''''''''''' ''''''''USER DEFINED VARIABLES' - END '''''''''''''''''''''''''

# ''''''''''''''''''''''''''''USER DEFINED FUNCTIONS'''''''''''''''''''''''''''''''''''

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
        status = lib.dut.HandleAlertMessage(config.HANDLE_ALERT_INVALID)
        end_time = lib.gettimestamp()
        lib.dut.validator.QuickCapture("afterInvalidParameter")
        lib.report_elapsed_time(start_time, end_time, "HANDLE_ALERT_INVALID", str(status))

        time.sleep(20)
        lib.log_info("Checking the API behaviour for parameter: Accept")
        start_time = lib.gettimestamp()
        status = lib.dut.HandleAlertMessage(config.HANDLE_ALERT_ACCEPT)
        end_time = lib.gettimestamp()
        lib.report_elapsed_time(start_time, end_time, "HANDLE_ALERT_ACCEPT", str(status))

        lib.dut.validator.QuickCapture("afterAcceptParameter")
        if not lib.validate_screen(
                lib.constants.CHKPNT_YOU_TUBE_DOWNLOAD_POP_UP):
            api_test_status = True
            lib.log_info("Accepted the pop up")
        else:
            lib.log_warn("pop up message box available even after Accepting")

        if lib.dut.Click(lib.fe_mob_lib.Constants.ElementType.XPath,
                     config.youTube_download_option
                     ):
            lib.dut.validator.QuickCapture("Message pop up")
            time.sleep(3)
            lib.log_info("Checking the API behaviour for parameter: Dismiss")
            start_time = lib.gettimestamp()
            dismiss_status = lib.dut.HandleAlertMessage(config.HANDLE_ALERT_DISMISS)
            end_time = lib.gettimestamp()
            lib.report_elapsed_time(start_time, end_time, "HANDLE_ALERT_DISMISS", str(status))

            lib.dut.validator.QuickCapture("afterDismissParameter")

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
        if lib.dut.Click(lib.fe_mob_lib.Constants.ElementType.XPath, config.youTube_download_option):
            time.sleep(3)
            lib.dut.validator.QuickCapture("firstClickOnDownload")
            # Checking whether download button clicked or not
            # if
            # com_lib.validate_screen(com_lib.constant.CHKPNT_IOS_YOU_TUBE_DOWNLOAD_BUTTON):
            lib.log_info(
                "Checking the API behaviour if there is no message pop up available")
            lib.dut.HandleAlertMessage(config.HANDLE_ALERT_DISMISS)
            if lib.dut.Click(
                    lib.fe_mob_lib.Constants.ElementType.XPath, config.youTube_download_option):
                # Checking whether message pop - up button clicked or not
                time.sleep(10)
                lib.dut.validator.QuickCapture("firstClickOnDownload")
                if lib.validate_screen(
                        lib.constants.CHKPNT_YOU_TUBE_DOWNLOAD_POP_UP):
                    lib.dut.validator.QuickCapture("afterPopUp")
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

# ''''''''''''''''''''''''''''USER DEFINED FUNCTIONS - END '''''''''''''''''''''''''''


# ''''''''''''''''''''''''''''MAIN ''''''''''''''''''''''''''''''''''''''''''''''''''''
# ``````````````````````````````````````````````````````````````````````````
# Function Name	  	: main()
# Description		: main
# Input arguments	: Null
# Output values		: Null
# ``````````````````````````````````````````````````````````````````````````
def main():
    driver = False
    script_status = False
    platform = lib.get_dut_platform()
    if "iOS" == platform:
        try:
            if not config:
                lib.report("Invalid Config", "FAILED")
                return False

            lib.log_info("*** THIS API SUPPORTS ONLY iOS ***")

            'updating the Test Script details'
            lib.update_tc_details()
            lib.log_script_info(os.path.basename(__file__), apis_in_the_script)

            'launching application'
            if lib.start_run(home=config.app_home):
                driver = True
                # dut.Tap(0, 178)
                script_status = test_api()
            else:
                lib.report("Script Status", "FAILED", image_required=True)

        except Exception as e:
            script_status = False
            lib.log_error("Exception raised in main function : " + str(e))
        finally:
            if driver:
                lib.stop_run()
            lib.CommitScriptResult(script_status)
            lib.log_info("-- Execution End --")
    else:
        lib.logger.Warn("HandleAlertMessage API is only available for iOS devices.")
        lib.dut.CommitTestResult("ABORTED")

# ''''''''''''''''''''''''''''MAIN - END'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if __name__ == "__main__":
    main()

#''''''''''''''''''''''''''''' END OF SCRIPT ''''''''''''''''''''''''''''''''''''''''''''''''''''