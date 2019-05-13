# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase Name     :   CaptureImage.py
# Author            :
# Date              :   04-10-2018
# Script Version    :   1.1
# APIs covered      :   CaptureImage
# Test Scenario     :   Launch the app, capture the image with given params. If CaptureImage
#                       API returns image path, update the script status as PASS
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

# User defined variables and functions
test_data = params.capture_image_params

apis_in_the_script = "CaptureImage"
config = lib.set_config()
file_name = os.path.basename(__file__)


"""
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Function Name       : test_api()
Description         : Tests the CaptureImage API with different parameters and
                      logs its response (status, duration)
Input arguments     : Null
Output values		: bool  :   API status
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""


def test_api():
    api_status = False
    try:
        for key, value in test_data.items():
            lib.log_info(" ----- Test Scenario - {} -----".format(value[0]))
            start_time = lib.gettimestamp()
            im_path = lib.dut.validator.CaptureImage(*value[2])
            end_time = lib.gettimestamp()
            lib.log_info("im_path - {}".format(im_path))
            if im_path:  # if image path returned by the API
                captured = True
            else:
                captured = False
            # we use this double comparison for including negative scenarios as well
            if captured == value[1]:
                status = "PASSED"
                api_status = True
            else:
                status = "FAILED"

            lib.report_elapsed_time(start_time, end_time, "CaptureImage")
            lib.report("API: CaptureImage API", status, image_required=True)

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
