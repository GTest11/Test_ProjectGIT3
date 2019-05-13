# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :
# Date              :   01-10-2018
# FE Version        :   FE 5.1.0.3
# APIs covered      :   "AddCustomDUTAttribute", "GetCustomDUTAttribute", "ReadCustomProperty"
#                       "SetCustomDUTAttribute", "SetDUTAttribute", "GetDUTAttribute",
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, os, datetime
sys.path.append('../')
import library.common_functions as lib

dut = lib.dut
msl = lib.msl


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
apis_in_the_script = ("AddCustomDUTAttribute", "GetCustomDUTAttribute", "ReadCustomProperty"
                      "SetCustomDUTAttribute", "SetDUTAttribute", "GetDUTAttribute",

                      )
config = lib.set_config()

def log_script_info():
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    lib.log_info("Script Name: {}".format(os.path.basename(__file__)))
    lib.log_info("Validating APIs - {}".format(apis_in_the_script))
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def custom_attribute():
    ret = False
    try:
        cur_time = datetime.datetime.now().strftime("%H:%M:%S")
        cur_time = cur_time.replace(":", "_")

        start_time = lib.gettimestamp()
        added = dut.AddCustomDUTAttribute("attr_" + cur_time)
        end_time = lib.gettimestamp()
        if added:
            status = "PASSED"
        else:
            status = "FAILED"
        lib.report_elapsed_time(start_time, end_time, "AddCustomDUTAttribute", status)
        lib.report("API: AddCustomDUTAttribute", status, image_required=True)
        if not added: #and cus_att == "AddCustomDUTAttribute":
            return ret

        start_time = lib.gettimestamp()
        set = dut.SetCustomDUTAttribute("attr_" + cur_time, cur_time)
        end_time = lib.gettimestamp()
        if set:
            status = "PASSED"
        else:
            status = "FAILED"
        lib.report_elapsed_time(start_time, end_time, "SetCustomDUTAttribute", status)
        # if not set:  # and cus_att == "AddCustomDUTAttribute":
        lib.report("API: SetCustomDUTAttribute", status, image_required=True)

        start_time = lib.gettimestamp()
        cust_attr = dut.GetCustomDUTAttribute("attr_"+cur_time)
        end_time = lib.gettimestamp()
        if cust_attr == cur_time:
            status = "PASSED"
        else:
            status = "FAILED"
        lib.report_elapsed_time(start_time, end_time, "GetCustomDUTAttribute", status)
        lib.report("API: GetCustomDUTAttribute", status, image_required=True)

        start_time = lib.gettimestamp()
        cust_attr = dut.ReadCustomProperty("attr_"+cur_time)
        end_time = lib.gettimestamp()
        if cust_attr == cur_time:
            status = "PASSED"
            ret = True
        else:
            status = "FAILED"
        lib.report_elapsed_time(start_time, end_time, "ReadCustomProperty", status)
        lib.report("API: ReadCustomProperty", status, image_required=True)

    except Exception as e:
        lib.log_error("Exception raised in custom_attribute() function : " + str(e))
        ret = False
    finally:
        return ret


def dut_attribute():
    start_time = lib.gettimestamp()
    set = dut.SetDUTAttribute("manufacturer", "manufacturer")
    end_time = lib.gettimestamp()
    if set:
        status = "PASSED"
    else:
        status = "FAILED"
    lib.report_elapsed_time(start_time, end_time, "SetDUTAttribute", status)
    lib.report("API: SetDUTAttribute", status, image_required=True)
    if not set:  # and cus_att == "AddCustomDUTAttribute":
        return False

    start_time = lib.gettimestamp()
    dut_attr = dut.GetDUTAttribute("manufacturer")
    end_time = lib.gettimestamp()
    if dut_attr == "manufacturer":
        status = "PASSED"
    else:
        status = "FAILED"

    lib.report_elapsed_time(start_time, end_time, "GetDUTAttribute", status)
    lib.report("API: GetDUTAttribute", status, image_required=True)
    if not set:  # and cus_att == "AddCustomDUTAttribute":
        return False
    return True

def test_api():
    api_test_status = True
    try:
        if not custom_attribute():
            lib.report("Failed to configure Custom Attributes", "FAILED", image_required=False)
            api_test_status = False

        if not dut_attribute():
            lib.report("Failed to configure DUT Attributes", "FAILED", image_required=False)
            api_test_status = False

    except Exception as e:
        lib.log_error(
            "Exception raised in test_api function : " + str(e))
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
