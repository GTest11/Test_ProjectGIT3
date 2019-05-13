# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :
# Date              :   01-10-2018
# FE Version        :   FE 5.1.0.3
# APIs covered      :   "LaunchApp", "SendAppToBackground",
#                       "CloseApp",
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import sys, os, time
sys.path.append('../')
import library.common_functions as lib

dut = lib.dut
msl = lib.fe_mob_lib


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
apis_in_the_script = ("LaunchApp", "SendAppToBackground",
                      "CloseApp",
                      )

config = lib.set_config()


def log_script_info():
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    lib.log_info("Script Name: {}".format(os.path.basename(__file__)))
    lib.log_info("Validating APIs - {}".format(apis_in_the_script))
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def send_app_to_background():
    APIResponse = msl.Models.ResponseData()
    start_time = lib.gettimestamp()
    APIResponse = dut.SendAppToBackground(10)
    end_time = lib.gettimestamp()
    time_taken = lib.getAPIduration(start_time, end_time)
    time.sleep(60)
    lib.log_info("API: Reason - {}".format(APIResponse.Message))
    if APIResponse.Status == 1:
        return True, time_taken
    else:
        return False, time_taken


def test_api():
    api_test_status = True
    try:
        apis = ("CloseApp", "LaunchApp",
                "SendAppToBackground",
              )

        apis_call = {
            "CloseApp": dut.CloseApp(),
            "LaunchApp": dut.LaunchApp(),
            "SendAppToBackground": send_app_to_background(),
        }

        for api in apis:
            lib.log_info("****  API  TEST **** {} ****".format(api))
            if api == "SendAppToBackground":
                api_result, time_taken = apis_call[api]
            else:
                start_time = lib.gettimestamp()
                api_result = apis_call[api]
                end_time = lib.gettimestamp()
                time_taken = lib.getAPIduration(start_time, end_time)
            if not api_result:
                status = "FAILED"
                api_test_status = False
            else:
                status = "PASSED"

            dut.CommitStepResult("API: Time taken by {} :  {}".format(api, str(time_taken)), status)
            time.sleep(2)

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
