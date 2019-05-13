# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :
# Date              :   01-10-2018
# FE Version        :   FE 5.1.0.3
# APIs covered      :   WaitImageMatch
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os
import sys
import time

sys.path.append('../')
import library.common_functions as lib
import mobile_config.test_params as params

dut = lib.dut
msl = lib.msl

# Use defined variables and functions
test_data = params.wait_image_match_params

apis_in_the_script = ("WaitImageMatch",
                      )
config = lib.set_config()

def log_script_info():
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    lib.log_info("Script Name: {}".format(os.path.basename(__file__)))
    lib.log_info("Validating APIs - {}".format(apis_in_the_script))
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def test_api():
    api_status = True
    try:
        # start playback
        dut.Tap(500, 500)
        time.sleep(20)

        if not dut.validator.CacheImageFromUrl(params.CACHE_VALID_URL, params.img_wait_im_match):
            lib.report("CacheImageFromUrl", "FAILED", image_required=True)
            return False

        for key, value in test_data.items():
            time.sleep(10)
            lib.log_info(" ----- Test Scenario - {} -----".format(value[0]))
            start_time = lib.gettimestamp()
            match_found = dut.validator.WaitImageMatch(*value[2])
            end_time = lib.gettimestamp()
            lib.log_info("detected - {}".format(match_found))

            if match_found == value[1]:
                status = "PASSED"
                # cur_status = True
            else:
                status = "FAILED"
                api_status = False

            lib.report_elapsed_time(start_time, end_time, "CaptureImage", status)
            lib.report("API: CaptureImage API", status, image_required=True)

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
