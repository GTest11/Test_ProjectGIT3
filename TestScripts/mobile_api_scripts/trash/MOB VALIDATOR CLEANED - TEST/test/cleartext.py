# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :
# Date              :   01-10-2018
# FE Version        :   FE 5.1.0.3
# APIs covered      :   ("HideKeyboard", "ClearText", "SendKeys", "Click")
#
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, os
sys.path.append('../')
import library.common_functions as lib

dut = lib.dut
msl = lib.msl


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
apis_in_the_script = ("HideKeyboard", "ClearText", "SendKeys", "Click")
config = lib.set_config()

def log_script_info():
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    lib.log_info("Script Name: {}".format(os.path.basename(__file__)))
    lib.log_info("Validating APIs - {}".format(apis_in_the_script))
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def hide_keyboard():
    hidden_status = False
    try:
        start_time = lib.gettimestamp()
        hidden = dut.HideKeyboard()
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

def cleartext():
    cleared = False
    try:
        start_time = lib.gettimestamp()
        dut.ClearText(msl.Constants.ElementType.XPath, config.X_CLEARTEXT)
        dut.validator.QuickCapture("ClearText_imageName")
        end_time = lib.gettimestamp()
        gettime = lib.getAPIduration(start_time, end_time)
        lib.commit_step_result("API: Time taken by ClearText API ", str(gettime))
        if (lib.wait_for_checkpoint(lib.constants.CHKPNT_CLEARTEXT, lib.constants.TIME_TO_WAIT_CLEARTEXT,
                                    lib.constants.INITIAL_DELAY_CLEARTEXT)
            ):
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


def test_api():
    script_status = True
    try:
        if not lib.search_in_youtube(config):
            lib.report("Search in Youtube", "FAILED")
            return False

        script_status = hide_keyboard()
        script_status = cleartext()

    except Exception as e:
        lib.log_error("Exception raised in test_cleartext function : " +str(e))
        script_status = False
    finally:
        return script_status


def main():
    status = False
    try:
        if not config:
            lib.report("Invalid Config", "FAILED")
            return False

        'updating the Test Script details'
        lib.update_tc_details()
        log_script_info()

        if lib.start_run(home=config.app_home):
            status = test_api()
        else:
            lib.report("API Test", "FAILED")

    except Exception as e:
        lib.log_error("Exception raised in main function : " + str(e))
    finally:
        lib.stop_run()
        lib.CommitScriptResult(status)


if __name__ == "__main__":
    main()
