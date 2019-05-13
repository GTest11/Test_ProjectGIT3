# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :   Rohith P V
# Date              :   05-10-2018
# Script Version    :   1.1
# Modification details: Fixed review comments, date 17/10/2018
# APIs covered      :   "IsElementPresent",
#                       "TapElement", "SendAndroidKeyCode",
#                       "TapElement(ElementType, String, Int32)", "TapPercent"
# Test Scenario     :   Launches youtube application -> Display ADB and device details ->  Validate ADB and device details
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os
import sys
import time

sys.path.append('../')
import library.common_functions as lib
import mobile_config.test_params as params

# dut = lib.dut
# msl = lib.msl


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
apis_in_the_script = ("IsElementPresent",
                      "TapElement", "SendAndroidKeyCode",
                      "TapElement(ElementType, String, Int32)", "TapPercent"
                      )
config = lib.set_config()

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# @Function Name	: test_api()
# @Description		: Tests the IsElementPresent, TapElement, SendAndroidKeyCode,
#                     TapElement(with index), TapPercent APIs and logs its response (status, duration)
# @Input arguments	: Null
# @Output values	: Bool
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def test_api():
    api_test_status = False
    try:
        if(lib.dut.ReadProperty(3) == "Android"):
            status = "FAILED"
            ret_val = False
            start_time = lib.gettimestamp()
            if lib.dut.IsElementPresent(lib.fe_mob_lib.Constants.ElementType.XPath, config.ACCOUNT_BUTTON):
                end_time = lib.gettimestamp()
                status = "PASSED"
                ret_val = True
            else:
                end_time = lib.gettimestamp()
            lib.report_elapsed_time(start_time, end_time, "IsElementPresent")
            lib.report("API: IsElementPresent API", status, image_required=True)

            time.sleep(5)
            # if ret_val:
            #     status = "PASSED"
            # else:
            #     status = "FAILED"
            #     api_test_status = False
            #
            # lib.report("API: Time taken by IsElementPresent API {}".format(time_taken),
            #     status, image_required=True
            # )
            # lib.report("API: IsElementPresent API", status, image_required=True)

            # if not ret_val:
            #     return False

            if ret_val:
                status = "FAILED"
                start_time = lib.gettimestamp()
                if lib.dut.TapElement(lib.fe_mob_lib.Constants.ElementType.XPath, config.ACCOUNT_BUTTON):
                    end_time = lib.gettimestamp()
                    status = "PASSED"
                else:
                    end_time = lib.gettimestamp()
                lib.report_elapsed_time(start_time, end_time, "TapElement")
                lib.report("API: TapElement API", status, image_required=True)
            else:
                lib.log_info("Element {} is unavailable in the current screen, hence Tap cannot be done ".format(config.ACCOUNT_BUTTON))

        # if ret_val:
        #     status = "PASSED"
        # else:
        #     status = "FAILED"
        #     api_test_status = False
        # lib.report("API: Time taken by TapElement API {}".format(
        #                        str(lib.getAPIduration(start_time, end_time))),
        #                         status, image_required=True
        #                     )
        # lib.report("API: TapElement API", status)

            time.sleep(5)
            status = "FAILED"
            start_time = lib.gettimestamp()
            if lib.dut.SendAndroidKeyCode("Keycode_BACK"):
                end_time = lib.gettimestamp()
                status = "PASSED"
            else:
                end_time = lib.gettimestamp()
            lib.report_elapsed_time(start_time, end_time, "SendAndroidKeyCode")
            lib.report("API: SendAndroidKeyCode API", status, image_required=True)

        # if sent:
        #    status = "PASSED"
        # else:
        #     status = "FAILED"
        #     api_test_status = False
        #
        # lib.report_elapsed_time(start_time, end_time, "SendAndroidKeyCode", status)
        # lib.report("API: SendAndroidKeyCode API", status, image_required=True)
            time.sleep(5)
            if lib.dut.IsElementPresent(lib.fe_mob_lib.Constants.ElementType.XPath, config.X_CLICK_INDEX):
                status = "FAILED"
                start_time = lib.gettimestamp()
                if lib.dut.TapElement(lib.fe_mob_lib.Constants.ElementType.ClassName, config.ELEMENT_CLASSNAME_CLICK_INDEX,
                                        config.search_button_index
                                        ):
                    end_time = lib.gettimestamp()
                    status = "PASSED"
                else:
                    end_time = lib.gettimestamp()
                lib.report_elapsed_time(start_time, end_time, "TapElement with index", status)
                lib.report("API: TapElement with index", status, image_required=True)
            else:
                lib.log_info("Element {} is unavailable in the current screen, hence Tap with index cannot be done ".format(config.ELEMENT_CLASSNAME_CLICK_INDEX))
        #
        #     if tapped:
        #         status = "PASSED"
        #     else:
        #         status = "FAILED"
        #         api_test_status = False
        #
        #     lib.report_elapsed_time(start_time, end_time, "TapElement with index", status)
        #     lib.report("API: TapElement with index", status, image_required=True)
        # else:
        #     lib.report("Element not available", "FAILED", image_required=True)
        #     api_test_status = False
            #if lib.dut.SendAndroidKeyCode("Keycode_BACK"):
            time.sleep(5)
            if not lib.dut.SendAndroidKeyCode("Keycode_BACK"):
                lib.report("Failed to navigate back", "FAILED", image_required=True)
                return False

            status = "FAILED"
            time.sleep(10)
            start_time = lib.gettimestamp()
            if lib.dut.TapPercent(lib.constants.TAP_X_PERCENT, lib.constants.TAP_Y_PERCENT):
                end_time = lib.gettimestamp()
                time.sleep(2)
                if lib.dut.validator.DetectMotion(*params.det_motion_param):
                    status = "PASSED"
                    api_test_status = True
                else:
                    status = "FAILED"
            else:
                end_time = lib.gettimestamp()
            lib.report_elapsed_time(start_time, end_time, "TapPercent", status)
            lib.report("API: TapPercent", status, image_required=True)
#            else:
#                lib.log_info("SendAndroidKeyCode API failed")

            # if tapped:
            #     status = "PASSED"
            # else:
            #     status = "FAILED"
            #     api_test_status = False
            #
            # lib.report_elapsed_time(start_time, end_time, "TapPercent", status)
            # time.sleep(2)
            # if lib.dut.validator.DetectMotion(*params.det_motion_param):
            #     status = "PASSED"
            # else:
            #     status = "FAILED"
            #     api_test_status = False
            #
            # lib.report("API: TapPercent API", status, image_required=True)


    except Exception as e:
        lib.log_error("Exception raised in test_api function : " + str(e))
        api_test_status = False
    finally:
        return api_test_status


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

        'launching application'
        if lib.start_run(home=config.app_home):
            driver = True
            script_status = test_api()
        else:
            lib.report("Script Status", "FAILED", image_required=True)

    except Exception as e:
        lib.log_error("Exception raised in main function : " + str(e))
        script_status = False

    finally:
        if driver:
            lib.stop_run()
        lib.CommitScriptResult(script_status)
        lib.log_info("-- Execution End --")


if __name__ == "__main__":
    main()
