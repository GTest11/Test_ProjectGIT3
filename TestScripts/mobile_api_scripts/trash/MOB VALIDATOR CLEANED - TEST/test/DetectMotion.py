# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :
# Date              :   01-10-2018
# FE Version        :   FE 5.1.0.3
# APIs covered      :   "Tap", "DynamicImageCompare",
#
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os
import sys
import time

sys.path.append('../')
import library.common_functions as lib
import mobile_config.test_params as params

dut = lib.dut
msl = lib.msl

#''''''''''''''''''''''''''''''END IMPORTS''''''''''''''''''''''''''''''''

# Use defined variables and functions
test_data = params.detect_motion_params

apis_in_the_script = ("Tap", "DetectMotion", "VolumeUp", "VolumeDown"
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
        start_time = lib.gettimestamp()
        tapped = dut.Tap(*config.c_tap_for_yt_playback)
        end_time = lib.gettimestamp()
        if tapped:
            status = "PASSED"
        else:
            status = "FAILED"
            api_status = False

        lib.report_elapsed_time(start_time, end_time, "Tap ", status)
        lib.report("API: Tap API", status, image_required=True)

        time.sleep(20)

        for key, value in test_data.items():
            lib.log_info(" ----- Test Scenario - {} -----".format(value[0]))
            start_time = lib.gettimestamp()
            detected = dut.validator.DetectMotion(*value[2])
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
                up = dut.VolumeUp(5)
                if up:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    api_status = False
                lib.report_elapsed_time(start_time, end_time, "VolumeUp", status)
                lib.report("API: VolumeUp API", status, image_required=True)

                down = dut.VolumeDown(5)
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
