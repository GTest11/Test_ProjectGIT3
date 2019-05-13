# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :
# Date              :   05-10-2018
# FE Version        :   FE 5.1.0.3
# APIs covered      :   Lock
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, os, time
sys.path.append('../')
import library.common_functions as lib

dut = lib.dut
msl = lib.msl

#''''''''''''''''''''''''''''''END IMPORTS''''''''''''''''''''''''''''''''

# Use defined variables and functions
# test_data = params.capture_image_params

apis_in_the_script = ("Lock", "Unlock"
                      )
config = lib.set_config()

def log_script_info():
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    lib.log_info("Script Name: {}".format(os.path.basename(__file__)))
    lib.log_info("Validating APIs - {}".format(apis_in_the_script))
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# @Function Name	  	: TestAPI()
# @Description		: Tests the CaptureImage API with diffrent parameters and
# logs its response (status, duration)
# @Input arguments	: Iteration count
# @Output values		: Null
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def test_api():
    api_status = True
    try:
        w, h = lib.get_image_resolution()
        lib.report("Validating Lock API. Screenshot >", "PASSED", image_required=True)
        lib.log_info("w - {}, h - {}".format(w, h))
        ref_img_path = dut.validator.CaptureImage(0, 0, w, h, "ref_img", 90, 0)
        start_time = lib.gettimestamp()
        dut.Lock()
        end_time = lib.gettimestamp()
        time.sleep(15)
        test_img_path = dut.validator.CaptureImage(0, 0, w, h, "test_img", 90, 0)

        matched = dut.validator.ImageMatch("ref_img", "test_img", 2, "13")
        if (config.platform_name == "iOS") and matched:
            status = "PASSED"
        elif (config.platform_name == "Android") and not matched:
            status = "PASSED"
        else:
            api_status = False
            status = "FAILED"

        lib.report_elapsed_time(start_time, end_time, "Lock", status)
        lib.report("API: Lock API", status, image_required=True)

        lib.log_info("*** UNLOCK () API DOES NOT AVAILABLE FOR iOS DEVICES ***")

        ref_img_path = dut.validator.CaptureImage(0, 0, w, h, "ref_img", 90, 0)
        start_time = lib.gettimestamp()
        dut.Unlock()
        end_time = lib.gettimestamp()
        time.sleep(15)
        test_img_path = dut.validator.CaptureImage(0, 0, w, h, "test_img", 90, 0)
        matched = dut.validator.ImageMatch("ref_img", "test_img", 2, "13")
        if not (config.platform_name == "iOS") and not matched:
            status = "PASSED"
        else:
            api_status = False
            status = "FAILED"
        lib.report_elapsed_time(start_time, end_time, "Unlock", status)
        lib.report("API: Unlock API", status, image_required=True)

    except Exception as e:
        lib.log_error("Exception thrown by python from test_api(): " + str(e))
        api_status = False
    finally:
        return api_status


def main():
    script_status = False
    try:
        if not config:
            lib.report("Invalid Config", "FAILED")
            return False

        lib.log_info("*** FOR iOS DEVICES, UNLOCKS AFTER 10 SECONDS - REMOVE PASSCODE BEFORE RUNNING THIS TEST ***")

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
