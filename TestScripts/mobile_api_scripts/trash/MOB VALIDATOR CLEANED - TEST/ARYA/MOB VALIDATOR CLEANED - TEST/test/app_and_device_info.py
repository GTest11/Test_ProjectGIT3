# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :
# Date              :   01-10-2018
# FE Version        :   FE 5.1.0.3
# APIs covered      :   "GetAdbAPIVersion", "GetAdbVersion",
#                       "GetApkVersion", "GetDeviceHeight", "GetDeviceWidth"
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, os
sys.path.append('../')
import library.common_functions as lib

dut = lib.dut
msl = lib.fe_mob_lib


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
apis_in_the_script = ("GetAdbAPIVersion", "GetAdbVersion",
                      "GetApkVersion", "GetDeviceHeight", "GetDeviceWidth"
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
        status = "PASSED"
        apis = ("GetAdbAPIVersion", "GetAdbVersion", "GetApkVersion",
                "GetDeviceHeight", "GetDeviceWidth"
                )
        apis_call = {
            "GetAdbAPIVersion": dut.GetAdbAPIVersion(),
            "GetAdbVersion": dut.GetAdbVersion(),
            "GetApkVersion": dut.GetApkVersion(),
            "GetDeviceHeight" : dut.GetDeviceHeight(),
            "GetDeviceWidth" : dut.GetDeviceWidth()
        }

        for api in apis:
            start_time = lib.gettimestamp()
            api_result = apis_call[api]
            end_time = lib.gettimestamp()
            if not api_result:
                status = "FAILED"
                api_test_status = False
            else:
                status = "PASSED"

            lib.report("API: {} returned {}".format(api, api_result), status, image_required=True)
            lib.report_elapsed_time(start_time, end_time, api, status)
            lib.report("API: {}".format(api), status, image_required=True)

    except Exception as e:
        lib.log_error(
            "Exception raised in test_app_info function : " + str(e))
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
