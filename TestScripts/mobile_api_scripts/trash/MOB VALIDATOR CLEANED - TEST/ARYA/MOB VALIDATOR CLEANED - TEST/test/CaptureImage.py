# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :
# Date              :   04-10-2018
# FE Version        :   FE 5.1.0.3
# APIs covered      :   CaptureImage
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import os
import sys

sys.path.append('../')
import library.common_functions as lib
import mobile_config.test_params as params

dut = lib.dut
msl = lib.fe_mob_lib

#''''''''''''''''''''''''''''''END IMPORTS''''''''''''''''''''''''''''''''

# Use defined variables and functions
test_data = params.capture_image_params

apis_in_the_script = ("CaptureImage",
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
        for key, value in test_data.items():
            lib.log_info(" ----- Test Scenario - {} -----".format(value[0]))
            start_time = lib.gettimestamp()
            im_path = dut.validator.CaptureImage(*value[2])
            end_time = lib.gettimestamp()
            lib.log_error("im_path - {}".format(im_path))
            if im_path: #if image path returned by the API
                captured = True
            else:
                captured = False

            if captured == value[1]:
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


# if "Android" == platform:
#     width = 720
#     height = 1280
# else:
#     width = 768
#     height = 1024


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
