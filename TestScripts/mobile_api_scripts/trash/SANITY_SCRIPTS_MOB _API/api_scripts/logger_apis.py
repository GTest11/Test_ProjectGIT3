# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :   Rohith P V
# Date              :   05-10-2018
# Script Version    :   1.1
# Modification details: Fixed review comments, date 17/10/2018
# APIs covered      :   WaitForElement, Logger APIs, CommitStepResult, CommitTestResult, GetServerTimeStamp, ReadProperty
# Test Scenario     :   Launches youtube application -> WaitForElement API executed and validates the app launch -> Unlock API executed
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import sys, os, time
import datetime
sys.path.append('../')
import library.common_functions as lib

# dut = lib.dut
# msl = lib.msl
logger = lib.logger


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
apis_in_the_script = ("WaitForElement", "Error", "Log",
                      "Warn", "GetServerTimeStamp", "CommitStepResult",
                      "CommitTestResult", "ReadProperty"
                      )
config = lib.set_config()

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# @Function Name	: start_run()
# @Description		: Launches the app and verifies using WaitForElement API
# @Input arguments	: Null
# @Output values	: Bool
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def start_run(elm_type=lib.fe_mob_lib.Constants.ElementType.XPath, home=None):
    # com_lib.update_tc_details()
    ready = False
    # log_script_data()
    try:
        if lib.init_app():
            #logger.Log("1111")
            time.sleep(5)
            start_time = lib.gettimestamp()
            ready = lib.dut.WaitForElement(elm_type, home, 50)
            end_time = lib.gettimestamp()
            lib.report_elapsed_time(start_time, end_time, "WaitForElement", "")
            if not ready:
                lib.log_error("App not launched")
                lib.report("Initialize run", "FAILED")
            else:
                lib.log_info("App launched")
                lib.report("Initialize run", "PASSED")
            # return ready
        else:
            #logger.Log("3333")
            lib.report("Failed to initialize", "FAILED", image_required=True)
            # return ready

    except Exception as e:
        logger.Log("Exception from start_run() - {}".format(e))
        ready = False
    finally:
        return ready

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# @Function Name	: test_api()
# @Description		: Tests the Logger, CommitStepResult, CommitTestResult, GetServerTimeStamp, ReadProperty APIs
# @Input arguments	: Null
# @Output values	: Bool
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def test_api():
    api_test_status = True
    api_status = "PASSED"
    try:

        apis = ("Error", "Log",
                "Warn", "GetServerTimeStamp", "CommitTestResult",#"CommitStepResult"

              )

        apis_call = {
            "Error": logger.Error,
            "Log": logger.Log,
            "Warn": logger.Warn,
            "GetServerTimeStamp" : lib.dut.validator.GetServerTimeStamp,
            "CommitTestResult": lib.dut.CommitTestResult,
        }

        # api parameters
        api_val = {
            "Error" : ("ERROR MESSAGE"),
            "Log" : ("INFO MESSAGE"),
            "Warn" : ("WARNING MESSAGE"),
            "GetServerTimeStamp" : (),
            "CommitTestResult" : ("PASSED"),
        }

        for api in apis:
            start_time = lib.gettimestamp()
            if api_val[api]:
                apis_call[api](api_val[api])
            else:
                apis_call[api]()
            end_time = lib.gettimestamp()
            lib.report_elapsed_time(start_time, end_time, api)
        start_time = lib.gettimestamp()
        lib.dut.CommitStepResult("TEST CommitStepResult","PASSED")
        end_time = lib.gettimestamp()
        lib.report_elapsed_time(start_time, end_time, "CommitStepResult")

    except Exception as e:
        lib.log_error(
            "Exception raised in test_app function : " + str(e))
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
        lib.log_script_info(os.path.basename(__file__), apis_in_the_script)

        'launching application'
        if start_run(home=config.app_home):
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
