# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :
# Date              :   01-10-2018
# FE Version        :   FE 5.1.0.3
# APIs covered      :   "IsElementPresent",
#                       "TapElement", "SendAndroidKeyCode",
#                       "TapElement(ElementType, String, Int32)", "TapPercent"
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os
import sys
import time

sys.path.append('../')
import library.common_functions as lib
import mobile_config.test_params as params

dut = lib.dut
msl = lib.fe_mob_lib


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
apis_in_the_script = ("IsElementPresent",
                      "TapElement", "SendAndroidKeyCode",
                      "TapElement(ElementType, String, Int32)", "TapPercent"
                      )
config = lib.set_config()


def log_script_info():
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    lib.log_info("Script Name: {}".format(os.path.basename(__file__)))
    lib.log_info("Validating APIs - {}".format(apis_in_the_script))
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def test_api():
    api_test_status = True
    try:
        start_time = lib.gettimestamp()
        ret_val = dut.IsElementPresent(msl.Constants.ElementType.XPath, config.ACCOUNT_BUTTON)
        end_time = lib.gettimestamp()
        lib.log_info("API: IsElementPresent API returned - "+ str(ret_val))
        time_taken = lib.getAPIduration(start_time, end_time)
        time.sleep(5)
        if ret_val:
            status = "PASSED"
        else:
            status = "FAILED"
            api_test_status = False

        lib.report("API: Time taken by IsElementPresent API {}".format(time_taken),
            status, image_required=True
        )
        lib.report("API: IsElementPresent API", status, image_required=True)

        if not ret_val:
            return False

        start_time = lib.gettimestamp()
        ret_val = dut.TapElement(msl.Constants.ElementType.XPath, config.ACCOUNT_BUTTON)
        end_time = lib.gettimestamp()
        if ret_val:
            status = "PASSED"
        else:
            status = "FAILED"
            api_test_status = False
        lib.report("API: Time taken by TapElement API {}".format(
                               str(lib.getAPIduration(start_time, end_time))),
                                status, image_required=True
                            )
        lib.report("API: TapElement API", status)

        time.sleep(5)
        start_time = lib.gettimestamp()
        sent = dut.SendAndroidKeyCode("Keycode_BACK")
        end_time = lib.gettimestamp()

        if sent:
           status = "PASSED"
        else:
            status = "FAILED"
            api_test_status = False

        lib.report_elapsed_time(start_time, end_time, "SendAndroidKeyCode", status)
        lib.report("API: SendAndroidKeyCode API", status, image_required=True)

        if dut.IsElementPresent(msl.Constants.ElementType.XPath, config.X_CLICK_INDEX):
            start_time = lib.gettimestamp()
            tapped = dut.TapElement(msl.Constants.ElementType.ClassName, config.ELEMENT_CLASSNAME_CLICK_INDEX,
                                    config.search_button_index
                                    )
            end_time = lib.gettimestamp()

            if tapped:
                status = "PASSED"
            else:
                status = "FAILED"
                api_test_status = False

            lib.report_elapsed_time(start_time, end_time, "TapElement with index", status)
            lib.report("API: TapElement with index", status, image_required=True)
        else:
            lib.report("Element not available", "FAILED", image_required=True)
            api_test_status = False

        if not dut.SendAndroidKeyCode("Keycode_BACK"):
            lib.report("Failed to navigate back", "FAILED", image_required=True)
            return False

        start_time = lib.gettimestamp()
        tapped = dut.TapPercent(30,20)
        end_time = lib.gettimestamp()

        if tapped:
            status = "PASSED"
        else:
            status = "FAILED"
            api_test_status = False

        lib.report_elapsed_time(start_time, end_time, "TapPercent", status)
        time.sleep(2)
        if dut.validator.DetectMotion(*params.det_motion_param):
            status = "PASSED"
        else:
            status = "FAILED"
            api_test_status = False

        lib.report("API: TapPercent API", status, image_required=True)


    except Exception as e:
        lib.log_error("Exception raised in test_api function : " + str(e))
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
        script_status = False

    finally:
        lib.stop_run()
        lib.CommitScriptResult(script_status)
        lib.log_info("-- Execution End --")


if __name__ == "__main__":
    main()
