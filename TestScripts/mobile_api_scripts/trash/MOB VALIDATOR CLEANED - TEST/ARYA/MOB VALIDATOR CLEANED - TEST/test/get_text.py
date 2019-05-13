# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :
# Date              :   01-10-2018
# FE Version        :   FE 5.1.0.3
# APIs covered      :   "GetText", "GetTextIndex",
#
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import sys, os
sys.path.append('../')
import library.common_functions as lib

dut = lib.dut
msl = lib.fe_mob_lib


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
apis_in_the_script = ("GetText", "GetTextIndex",
                      )
config = lib.set_config()


def log_script_info():
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    lib.log_info("Script Name: {}".format(os.path.basename(__file__)))
    lib.log_info("Validating APIs - {}".format(apis_in_the_script))
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def get_text_index():
    read_text = False
    try:
        if not dut.Click(msl.Constants.ElementType.XPath, config.click_gettext):
            lib.report("Failed to click", "FAILED", image_required=True)
            return False

        start_time = lib.gettimestamp()
        get_text = dut.GetText(msl.Constants.ElementType.XPath, config.GETTEXT_XPath, config.GETTEXT_index)
        end_time = lib.gettimestamp()
        if get_text:
            status = "PASSED"
            read_text = True
        else:
            status = "FAILED"
        lib.report_elapsed_time(start_time, end_time, "GetText with Index", status)
        lib.report("GetText with Index", status, image_required=True)

    except Exception as e:
        lib.log_error("Exception from get_text_index() " + str(e))
        read_text = False
    finally:
        return read_text

def test_api():
    api_test_status = True
    try:
        start_time = lib.gettimestamp()
        get_text = dut.GetText(msl.Constants.ElementType.XPath, config.APP_GETTEXT)
        end_time = lib.gettimestamp()
        if get_text:
            status = "PASSED"
        else:
            status = "FAILED"
            api_test_status = False

        lib.report_elapsed_time(start_time, end_time, "GetText", status)
        lib.report("GetText API", status, image_required=True)

        api_test_status = get_text_index()

    except Exception as e:
        lib.log_error("Exception raised in test_app_info function : " + str(e))
        api_test_status = False
    finally:
        return api_test_status


def main():
    script_status = False
    try:
        if not config:
            lib.report("Invalid Config", "FAILED")
            return False

        'updating the Test Script details'
        lib.update_tc_details()
        log_script_info()

        'launching application'
        if lib.start_run(home=config.app_home):
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
