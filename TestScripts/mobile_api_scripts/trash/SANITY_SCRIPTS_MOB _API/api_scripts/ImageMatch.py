# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase Name     :   ImageMatch.py
# Author            :
# Date              :   04-10-2018
# Script Version    :   1.1
# APIs covered      :   "CaptureImage", "ImageMatch"
# Test Scenario     :   Launch the app, capture ref image and test image using CaptureImage API.
#                       Compare the images using ImageMatch and update the script status.
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
test_data = params.image_match_params

apis_in_the_script = ("ImageMatch", "CaptureImage")
config = lib.set_config()
file_name = os.path.basename(__file__)
"""
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Function Name       : test_api()
Description         : Tests the ImageMatch API
Input arguments     : Null
Output values		: bool  :   API status
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""


def test_api():
    api_status = False
    try:

        for key, value in test_data.items():
            ref_img_path = lib.dut.validator.CaptureImage(*params.ref_image_param)
            lib.delay(1)
            test_img_path = lib.dut.validator.CaptureImage(*params.test_image_param)

            if not (ref_img_path and test_img_path):
                lib.report("Capture test image and reference image", "FAILED", image_required=True)
                return False

            lib.log_info(" ----- Test Scenario - {} -----".format(value[0]))
            start_time = lib.gettimestamp()
            match_found = lib.dut.validator.ImageMatch(*value[2])
            end_time = lib.gettimestamp()
            lib.log_error("match_found - {}".format(match_found))

            if match_found == value[1]:
                status = "PASSED"
                api_status = True
            else:
                status = "FAILED"

            lib.report_elapsed_time(start_time, end_time, "ImageMatch")
            lib.report("API: ImageMatch API", status, image_required=True)

    except Exception as e:
        lib.log_error("Exception thrown by python from test_api(): " + str(e))
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
