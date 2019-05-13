# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase name     : ValidateCheckpoint.py
# Author            :
# Date              : 05-10-2018
# Script Version    : 1.1
# APIs covered      : validateCheckPoint, validateCheckpoint with base 64 image
# Test Scenario     : Launch the App, call validateCheckPoint API
#                       1. OCR checkpoint - Mobile_YouTube
#                       2. Multi line OCR - youtube_MultiOcr
#                       3. IC checkpoint, pixel - youtube_valIcPixel
#                       4. IC checkpoint, rmse - youtube_valIcRmse
# Note              : Please check the checkpoints before executing the script
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

try:
    import os
    import sys
    sys.path.append('../')
    import library.common_functions as lib
    import mobile_config.test_params as params
except Exception as e:
    print ("Exception in Import " + str(e))
    sys.exit()

#''''''''''''''''''''''''''''''END IMPORTS''''''''''''''''''''''''''''''''

# Use defined variables and functions
test_data = params.validate_chkpt_params

apis_in_the_script = "validateCheckPoint"
config = lib.set_config()
file_name = os.path.basename(__file__)

"""
``````````````````````````````````````````````````````````````````````````
Function Name	  	: test_api
Description		    : Function to test the APIs
Input arguments	    : null
Output values		: bool  :   script execution status
``````````````````````````````````````````````````````````````````````````
"""


def test_api():
    api_status = False
    try:

        for key, value in test_data.items():
            lib.log_info(" ----- Test Scenario - {} -----".format(value[0]))

            lib.chkpt.init(value[2])

            lib.delay(3)
            start_time = lib.gettimestamp()
            validated = lib.dut.validator.validateCheckPoint(lib.chkpt)
            end_time = lib.gettimestamp()
            # we use this double comparison for including negative scenarios as well
            if validated == value[1]:
                status = "PASSED"
                api_status = True
            else:
                status = "FAILED"
                api_status = False

            lib.report_elapsed_time(start_time, end_time, "validateCheckPoint", status)
            lib.report("API: validateCheckPoint API", status, image_required=True)

        #validateCheckPoint base 64
        imgstring = lib.dut.GetScreenshot()
        lib.dut.validator.UploadScreenshot("UploadScreenshot", imgstring)
        lib.chkpt.init("validate_base64")
        if lib.dut.validator.validateCheckPoint(lib.chkpt, imgstring):
            status = "PASSED"
            api_status = True
        else:
            status = "FAILED"
            api_status = False
        lib.report_elapsed_time(start_time, end_time, "validateCheckPoint_base64", status)
        lib.report("API: validateCheckPoint base64 API", status, image_required=True)

    except Exception as e:
        lib.log_info("Exception from test_api(): " + str(e))
        api_status = False

    finally:
        return api_status

"""
``````````````````````````````````````````````````````````````````````````
Function Name	  	: main
Description		    : main function
Input arguments	    : null
Output values		: null
# ``````````````````````````````````````````````````````````````````````````
"""


def main():
    script_status = False
    try:
        if not config:
            lib.report("Invalid Config", "FAILED")
            return False

        'updating the Test Script details'
        lib.update_tc_details()
        lib.log_script_info(file_name, apis_in_the_script)

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
