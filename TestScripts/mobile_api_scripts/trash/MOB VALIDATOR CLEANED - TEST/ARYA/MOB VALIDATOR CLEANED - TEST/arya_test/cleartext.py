# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :
#Script Version     : 1.1
# Date              :   01-10-2018, 22 Oct 2018
#Script Version     : 1.1
#Modification details: 22 Oct 2018, fixed review comments - Arya
# APIs covered      :   ("HideKeyboard", "ClearText", "SendKeys", "Click")
#Test Scenario:
#init to Youtube
#Saerch for master chef australia
#Hide the keyboard
#Clear the text in search field.
# '''''''''''''''''''''''''''TEST CASE DETAILS' - END '''''''''''''''''''''''''''''''''

# ''''''''''''''''''''''''''''''''''''''''IMPORTS''''''''''''''''''''''''''''''''''''''
#importing python modules
import sys
import os

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
apis_in_the_script = ("HideKeyboard", "ClearText", "SendKeys", "Click")
config = lib.set_config()
# ''''''''''''''''''''' ''''''''USER DEFINED VARIABLES' - END '''''''''''''''''''''''''

# ''''''''''''''''''''''''''''USER DEFINED FUNCTIONS'''''''''''''''''''''''''''''''''''
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#@Function Name	  	: hide_keyboard()
#@Description		: Positive scenario testing of  "HideKeyboard"
#@Input arguments	: None
#@Output values		: None
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def hide_keyboard():
    hidden_status = False
    try:
        start_time = lib.gettimestamp()
        hidden = lib.dut.HideKeyboard()
        end_time = lib.gettimestamp()
        if hidden:
            status = "PASSED"
            hidden_status = True
        else:
            status = "FAILED"

        lib.report_elapsed_time(start_time, end_time, "HideKeyboard", status)
        lib.report("HideKeyboard API", status, image_required=True)
    except Exception as e:
        lib.log_error("Exception from hide_keyboard() " + str(e))
        hidden_status = False
    finally:
        return hidden_status


#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#@Function Name	  	: cleartext()
#@Description		: Positive scenario testing of following APIs: "ClearText"
#@Input arguments	: None
#@Output values		: None
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def cleartext():
    cleared = False
    try:
        start_time = lib.gettimestamp()
        lib.dut.ClearText(lib.fe_mob_lib.Constants.ElementType.XPath, config.X_CLEARTEXT)
        lib.dut.validator.QuickCapture("ClearText_imageName")
        end_time = lib.gettimestamp()
        lib.time.sleep(5)
        lib.chkpt.init(lib.constants.CHKPNT_CLEARTEXT)
        if lib.dut.validator.validateCheckPoint(lib.chkpt):
            status = "PASSED"
            cleared = True
        else:
            status = "FAILED"

        lib.report_elapsed_time(start_time, end_time, "ClearText", status)
        lib.report("ClearText API", status, image_required=True)

    except Exception as e:
        lib.log_error("Exception from hide_keyboard() " + str(e))
        cleared = False
    finally:
        return cleared


#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#@Function Name	  	: test_api()
#@Description		: Positive scenario testing of following APIs:
#                     "HideKeyboard", "ClearText", "SendKeys", "Click"
#@Input arguments	: None
#@Output values		: None
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def test_api():
    script_status = False
    try:
        if not lib.search_in_youtube(config):
            lib.report("Search in Youtube", "FAILED")
            return False

        hide_keyboard_status = hide_keyboard()
        cleartext_status = cleartext()
        if hide_keyboard_status and cleartext_status:
            script_status = True
    except Exception as e:
        lib.log_error("Exception raised in test_cleartext function : " +str(e))
        script_status = False
    finally:
        return script_status
# ''''''''''''''''''''''''''''USER DEFINED FUNCTIONS - END '''''''''''''''''''''''''''


# ''''''''''''''''''''''''''''MAIN ''''''''''''''''''''''''''''''''''''''''''''''''''''
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#@Function Name	  	: main()
#@Description		: main function
#@Input arguments	: None
#@Output values		: None
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def main():
    driver = False
    script_status = False
    try:
        if not config:
            lib.report("Invalid Config", "FAILED")
            return False

        'updating the Test Script details'
        lib.update_tc_details()
        lib.log_script_info(os.path.basename(__file__), apis_in_the_script)

        if lib.start_run(home=config.app_home):
            driver = True
            script_status = test_api()
        else:
            lib.report("API Test", "FAILED")

    except Exception as e:
        script_status = False
        lib.log_error("Exception raised in main function : " + str(e))
    finally:
        if driver:
            lib.stop_run()
        lib.CommitScriptResult(script_status)
# ''''''''''''''''''''''''''''MAIN - END'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if __name__ == "__main__":
    main()

#''''''''''''''''''''''''''''' END OF SCRIPT ''''''''''''''''''''''''''''''''''''''''''''''''''''