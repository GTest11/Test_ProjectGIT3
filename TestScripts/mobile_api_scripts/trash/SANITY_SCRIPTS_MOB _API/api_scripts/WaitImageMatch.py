# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase Name     :   WaitImageMatch.py
# Author            :
# Date              :   01-10-2018
# Script Version    :   1.1
# APIs covered      :   WaitImageMatch, CaptureImage
# Test Scenario     :   Launch the app, capture an image using params in the test_params.py.
#                       Compare this image at run time using WaitImageMatch API and update the status
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


# Use defined variables and functions
test_data = params.wait_image_match_params

apis_in_the_script = ("WaitImageMatch", "CaptureImage")
config = lib.set_config()
file_name = os.path.basename(__file__)

"""
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Function Name       : test_api()
Description         : Tests the WaitImageMatch API
Input arguments     : Null
Output values		: bool  :   API status
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""


def test_api():
    api_status = False
    try:
        if not lib.dut.validator.CaptureImage(params.Capt_x, params.Capt_y, params.Capt_width, params.Capt_height,
                                              params.img_wait_im_match, params.CAP_IMG_DEFAULT_QUALITY, 1):
            lib.report("CaptureImage", "FAILED", image_required=True)
            return False

        for key, value in test_data.items():
            lib.log_info(" ----- Test Scenario - {} -----".format(value[0]))
            start_time = lib.gettimestamp()
            match_found = lib.dut.validator.WaitImageMatch(*value[2])
            end_time = lib.gettimestamp()
            lib.log_info("Match detected - {}".format(match_found))

            if match_found == value[1]:
                status = "PASSED"
                api_status = True
            else:
                api_status = False
                status = "FAILED"

            lib.report_elapsed_time(start_time, end_time, "WaitImageMatch")
            lib.report("API: WaitImageMatch API", status, image_required=True)

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
``````````````````````````````````````````````````````````````````````````
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
