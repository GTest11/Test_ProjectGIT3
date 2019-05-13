# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :   Rohith P V
# Date              :   05-10-2018
# Script Version    :   1.1
# Modification details: Fixed review comments, date 17/10/2018
# APIs covered      :   "GetAdbAPIVersion", "GetAdbVersion",
#                       "GetApkVersion", "GetDeviceHeight", "GetDeviceWidth"
# Test Scenario     :   Launches youtube application -> Display ADB and device details ->  Validate ADB and device details
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, os
sys.path.append('../')
import library.common_functions as lib

#dut = lib.dut
#msl = lib.msl


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
apis_in_the_script = ("GetAdbAPIVersion", "GetAdbVersion",
                      "GetApkVersion", "GetDeviceHeight", "GetDeviceWidth"
                      )
config = lib.set_config()

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# @Function Name	: test_api()
# @Description		: Tests the ADB and device details APIs and logs its response (status, duration)
# @Input arguments	: Null
# @Output values	: Bool
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def test_api():
    api_test_status = False
    # dict_out_android = {}
    # dict_out_ios = {}
    dict_out = {}
    dut_mob_name = lib.get_dut_name() # Read the name of the mobile DUT
    status = "FAILED"

    try:
        apis_android = ("GetAdbAPIVersion", "GetAdbVersion", "GetApkVersion",
                "GetDeviceHeight", "GetDeviceWidth"
                )
        apis_ios = ("GetDeviceHeight", "GetDeviceWidth"
                )

        apis_call = {
            "GetAdbAPIVersion": lib.dut.GetAdbAPIVersion,
            "GetAdbVersion": lib.dut.GetAdbVersion,
            "GetApkVersion": lib.dut.GetApkVersion,
            "GetDeviceHeight" : lib.dut.GetDeviceHeight,
            "GetDeviceWidth" : lib.dut.GetDeviceWidth
        }
        if (config.platform_name == "iOS"):
            for api in apis_ios:
                start_time = lib.gettimestamp()
                api_result = apis_call[api]()
                end_time = lib.gettimestamp()
                lib.log_info("API: {} returned {}".format(api, api_result))
                lib.report_elapsed_time(start_time, end_time, api)
                dict_out.update({api:str(api_result)}) # Update the dictionary "dict_out" with the values obtained from API calls
                print dict_out
        else:
            for api in apis_android:
                start_time = lib.gettimestamp()
                api_result = apis_call[api]()
                end_time = lib.gettimestamp()
                lib.log_info("API: {} returned {}".format(api, api_result))
                lib.report_elapsed_time(start_time, end_time, api)
                dict_out.update({api:str(api_result)}) # Update the dictionary with the values obtained from APIs
                #print dict_out

        if dut_mob_name in lib.constants.dict_dut_name:
            dict_mob = lib.constants.dict_dut_name[dut_mob_name]

        # for dut_mob in lib.constants.dict_dut_name:
        #     dict_mob = lib.constants.dict_dut_name[dut_mob]


        if dict_out == dict_mob : # Comparison with original dict of values obtained from constants file
            status = "PASSED"
            api_test_status = True
        else:
            status = "FAILED"
        lib.report("ADB Info APIs " + status, status, image_required=True)
    except Exception as e:
        lib.log_error(
            "Exception raised in test_api function : " + str(e))
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
        lib.log_info("*** ADB APIs are available only for Android devices ***")

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
