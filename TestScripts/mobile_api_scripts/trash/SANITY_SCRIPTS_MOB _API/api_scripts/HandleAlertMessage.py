# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :   03-10-2018, 26 Oct 2018
#Script Version     : 1.1
#Modification details:  re written the script - Arya
# APIs covered      :   HandleAlertMessage
#Test Scenario:
#init to Youtube
# play a video
# click on download twice to launch the pop up dialog box
# Call the API
# Note:
# Before running script login to youTube
# Remove the video from you tube downloaded list if it is already downloaded
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
# Function Name	  	: test_handleAlertMessage()
# Description		: Function to test the handleAlertMessage API
# Input arguments	: Null
# Output values		: bool
# ``````````````````````````````````````````````````````````````````````````
def test_api():
    api_status = False

    try:
        #Playing a video to download
        lib.dut.Tap(*config.c_tap_for_yt_playback)
        lib.time.sleep(10)
        lib.dut.validator.QuickCapture("beforeGetText")
        text_obtained = lib.dut.GetText(lib.fe_mob_lib.Constants.ElementType.XPath, config.youTube_download_option)
        lib.logger.Log("Obtained text: " + text_obtained)
        text_obtained = text_obtained.lower()
        if text_obtained in ["downloading", "downloaded", "download"]:
            click_status = False
            click_status_1 = False
            click_status_2 = False
            if "downloading" == text_obtained or " downloaded" == text_obtained:
                click_status = lib.dut.Click(lib.fe_mob_lib.Constants.ElementType.XPath, config.youTube_download_option)
                lib.time.sleep(5)
                lib.dut.validator.QuickCapture("SecondClickOnDownloadingORdownloaded")
            if "download" == text_obtained:
                click_status_1 = lib.dut.Click(lib.fe_mob_lib.Constants.ElementType.XPath, config.youTube_download_option)
                lib.time.sleep(5)
                lib.dut.validator.QuickCapture("firstClickOnDownload")
                lib.time.sleep(120)
                click_status_2 = lib.dut.Click(lib.fe_mob_lib.Constants.ElementType.XPath, config.youTube_download_option)
                lib.time.sleep(5)
                lib.dut.validator.QuickCapture("SecondClickOnDownload")

            #click_status = lib.dut.Click(lib.fe_mob_lib.Constants.ElementType.XPath, config.youTube_download_option)
            #Wait until the download completes, now assuming wait time to 120 since played video is add.
            # Different version of youtube shows different behavior on download click

            if click_status or (click_status_1 and click_status_2):
                if lib.validate_screen(lib.constants.CHKPNT_YOU_TUBE_DOWNLOAD_POP_UP):
                    lib.dut.validator.QuickCapture("afterPopUp")
                    lib.log_info("Message pop up available.")
                    lib.time.sleep(10)
                    lib.log_info("Checking the API behaviour for parameter: Accept")
                    start_time = lib.gettimestamp()
                    accept_status = lib.dut.HandleAlertMessage(lib.constants.HANDLE_ALERT_ACCEPT)
                    end_time = lib.gettimestamp()
                    if (accept_status):
                        if not lib.validate_screen(lib.constants.CHKPNT_YOU_TUBE_DOWNLOAD_POP_UP):
                            api_status = True
                            status = "PASSED"
                            lib.log_info("Accepted the pop up")
                        else:
                            status = "FAILED"
                            lib.log_warn("pop up message box available even after Accepting")
                    lib.report_elapsed_time(start_time, end_time, "HandleAlertMessage", api_status)
                    lib.report("API:HandleAlertMessage", status, image_required=True)
                else:
                    lib.log_warn("pop up message box not available")
            else:
                lib.logger.Log("Download option click failed.")
        else:
            lib.log_warn("Download option is not available..")
    except Exception as e:
        lib.log_error("Exception raised in test_handleAlertMessage function : " + str(e))
        api_status = False
    finally:
        return api_status

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
    lib.log_info("*** THIS API SUPPORTED IN ONLY iOS  DEVICES***")
    if "iOS" == platform:
        try:
            if not config:
                lib.report("Invalid Config", "FAILED")
                return False
            'updating the Test Script details'
            lib.update_tc_details()
            lib.log_script_info(os.path.basename(__file__), apis_in_the_script)

            'launching application'
            if lib.start_run(home=config.app_home):
                driver = True
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
