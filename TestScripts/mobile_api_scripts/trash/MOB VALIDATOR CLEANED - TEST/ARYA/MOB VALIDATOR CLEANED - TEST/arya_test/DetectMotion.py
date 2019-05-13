# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :   01-10-2018, 22 Oct 2018, 24 Oct 2018
#Script Version     : 1.1
#Modification details: 22 Oct 2018, fixed review comments - Arya
#Script Version     : 1.1
# APIs covered      :   "Tap", "DetectMotion", "VolumeUp", "VolumeDown"
#Test Scenario:
#init to Youtube
# '''''''''''''''''''''''''''TEST CASE DETAILS' - END '''''''''''''''''''''''''''''''''

# ''''''''''''''''''''''''''''''''''''''''IMPORTS''''''''''''''''''''''''''''''''''''''
#importing python modules
import sys
import os
import time

#importing user defined functions
sys.path.append('../')
try:
    # Import library file
    import library.common_functions as lib
except ImportError:
    print("Failed to import common_functions file")
    sys.exit()

try:
    # Import library file
    import mobile_config.test_params as params
except ImportError:
    print("Failed to import test_params file")
    sys.exit()
# ''''''''''''''''''''''''''''''''''''''''IMPORTS - END'''''''''''''''''''''''''''''''

# ''''''''''''''''''''' ''''''''USER DEFINED VARIABLES'''''''''''''''''''''''''''''''''

# Use defined variables and functions
test_data = params.detect_motion_params

apis_in_the_script = ("Tap", "DetectMotion", "VolumeUp", "VolumeDown")
config = lib.set_config()
# ''''''''''''''''''''' ''''''''USER DEFINED VARIABLES' - END '''''''''''''''''''''''''

# ''''''''''''''''''''''''''''USER DEFINED FUNCTIONS'''''''''''''''''''''''''''''''''''
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#@Function Name	  	: test_api()
#@Description		: Positive scenario testing of following APIs:
#                     "Tap", "DetectMotion", "VolumeUp", "VolumeDown"
#@Input arguments	: None
#@Output values		: None
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def test_api():
    api_status = True
    try:
        # start playback
        start_time = lib.gettimestamp()
        tapped = lib.dut.Tap(*config.c_tap_for_yt_playback)
        end_time = lib.gettimestamp()
        if tapped:
            status = "PASSED"
        else:
            status = "FAILED"
            api_status = False

        lib.report_elapsed_time(start_time, end_time, "Tap ", status)
        lib.report("API: Tap API", status, image_required=True)

        time.sleep(10)

        for key, value in test_data.items():
            lib.log_info(" ----- Test Scenario - {} -----".format(value[0]))
            start_time = lib.gettimestamp()
            detected = lib.dut.validator.DetectMotion(*value[2])
            end_time = lib.gettimestamp()
            lib.log_error("detected - {}".format(detected))

            if detected == value[1]:
                status = "PASSED"
            else:
                status = "FAILED"
                # dut.Tap(*config.c_tap_for_yt_playback)
                api_status = False

            lib.report_elapsed_time(start_time, end_time, "DetectMotion", status)
            lib.report("API: DetectMotion API", status, image_required=True)

            if detected:
                up = lib.dut.VolumeUp(5)
                if up:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    api_status = False
                lib.report_elapsed_time(start_time, end_time, "VolumeUp", status)
                lib.report("API: VolumeUp API", status, image_required=True)

                down = lib.dut.VolumeDown(5)
                if down:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    api_status = False
                lib.report_elapsed_time(start_time, end_time, "VolumeDown", status)
                lib.report("API: VolumeDown API", status, image_required=True)
    except Exception as e:
        lib.log_error("Exception thrown by python from test_api(): " + str(e))
        api_status = False
    finally:
        return api_status
# ''''''''''''''''''''''''''''USER DEFINED FUNCTIONS - END '''''''''''''''''''''''''''


# ''''''''''''''''''''''''''''MAIN ''''''''''''''''''''''''''''''''''''''''''''''''''''
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#@Function Name	  	: main()
#@Description		: main function
#@Input arguments	: None
#@Output values		: None
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def main():
    driver = False
    script_status = False
    try:
        if not config:
            lib.report("Invalid Config", "FAILED")
            return False

        'updating the Test Script details'
        lib.update_tc_details()
        lib.log_script_info(os.path.basename(__file__), apis_in_the_script)

        'launching application'
        if lib.start_run(home=config.app_home):
            driver = True
            script_status = test_api()
        else:
            lib.report("Script Status", "FAILED", image_required=True)

    except Exception as e:
        lib.log_error("Exception raised in main function : " + str(e))
        script_status = False
    finally:
        if driver:
            lib.stop_run()
        lib.CommitScriptResult(script_status)
        lib.log_info("-- Execution End --")
# ''''''''''''''''''''''''''''MAIN - END'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if __name__ == "__main__":
    main()

#''''''''''''''''''''''''''''' END OF SCRIPT ''''''''''''''''''''''''''''''''''''''''''''''''''''
