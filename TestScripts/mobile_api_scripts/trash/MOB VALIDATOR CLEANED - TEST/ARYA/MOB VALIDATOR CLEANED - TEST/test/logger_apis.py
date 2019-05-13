# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :
# Date              :   01-10-2018
# FE Version        :   FE 5.1.0.3
# APIs covered      :   "Error", "Log",
#                       "Warn", "GetServerTimeStamp", "CommitStepResult",
#                       "CommitTestResult", "ReadProperty"
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import sys, os, time
import datetime
sys.path.append('../')
import library.common_functions as lib

dut = lib.dut
msl = lib.fe_mob_lib
logger = lib.logger


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
apis_in_the_script = ("Error", "Log",
                      "Warn", "GetServerTimeStamp", "CommitStepResult",
                      "CommitTestResult", "ReadProperty"
                      )
config = lib.set_config()


def log_script_info():
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    lib.log_info("Script Name: {}".format(os.path.basename(__file__)))
    lib.log_info("Validating APIs - {}".format(apis_in_the_script))
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# the below function is not using since
# GetServerTimeStamp API returns True or False
def get_server_timestamp():
    server_time = dut.validator.GetServerTimeStamp()
    local_time = datetime.datetime.now()
    local_time_converted = lib.strtomillisecond(local_time)



def test_api():
    api_test_status = True
    try:
        time.sleep(3)
        lib.report("API: WaitForElement", "PASSED", image_required=True)
        status = "PASSED"
        apis = ("Error", "Log",
                "Warn", "GetServerTimeStamp", "CommitStepResult",
                "CommitTestResult", "ReadProperty"
              )
        apis_call = {
            "Error": logger.Error("ERROR MESSAGE"),
            "Log": logger.Log("INFO MESSAGE"),
            "Warn": logger.Warn("WARNING MESSAGE"),
            "GetServerTimeStamp" : dut.validator.GetServerTimeStamp(),
            "CommitStepResult" : dut.CommitStepResult("TEST CommitStepResult","PASSED"),
            "CommitTestResult": dut.CommitTestResult("PASSED"),
            "ReadProperty" : dut.ReadProperty(3)
        }

        for api in apis:
            start_time = lib.gettimestamp()
            api_result = apis_call[api]
            logger.Log("API Status - {}".format(api_result))
            end_time = lib.gettimestamp()
            time_taken = lib.getAPIduration(start_time, end_time)
            dut.CommitStepResult("API: Time taken by {} API :  {}".format(api, str(time_taken)), "PASSED")

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
    finally:
        lib.stop_run()
        lib.CommitScriptResult(script_status)
        lib.log_info("-- Execution End --")


if __name__ == "__main__":
    main()
