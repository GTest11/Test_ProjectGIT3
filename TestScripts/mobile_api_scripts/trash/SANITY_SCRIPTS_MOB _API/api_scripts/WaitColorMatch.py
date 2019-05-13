# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :
# Date              :   05-10-2018
# Script Version    :   1.1
# APIs covered      :   "StartCaptureZapFrames", "WaitColorMatch", "StopCaptureZapFrames"
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os
import sys
import time

sys.path.append('../')
import library.common_functions as lib
import mobile_config.test_params as params

dut = lib.dut
# msl = lib.msl
chkpt = lib.chkpt


# Use defined variables and functions
test_data = params.wait_color_match_params

apis_in_the_script = ("StartCaptureZapFrames", "WaitColorMatch", "StopCaptureZapFrames"
                      )
config = lib.set_config()

#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# @Function Name          : test_api()
# @Description        : validates  "StartCaptureZapFrames", "WaitColorMatch",
#                       "StopCaptureZapFrames"
# @Input arguments    : None
# @Output values        : True or False
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def test_api():
    api_status = True
    try:

        for key, value in test_data.items():
            lib.log_info(" ----- Test Scenario - {} -----".format(value[0]))

            time.sleep(3)
            if dut.validator.StartCaptureZapFrames(params.captureZapTime):
                lib.report("API: StartCaptureZapFrames", "PASSED", image_required=True)
                start_time = lib.gettimestamp()
                match_found = dut.validator.WaitColorMatch(*value[2])
                end_time = lib.gettimestamp()

                time1 = lib.gettimestamp()
                stopped = dut.validator.StopCaptureZapFrames()
                time2 = lib.gettimestamp()
                if stopped:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    api_status = False
                lib.report_elapsed_time(time1, time2, "StopCaptureZapFrames", status)
                lib.report("StopCaptureZapFrames API", status, image_required=True)

                if match_found == value[1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    api_status = False

                lib.report_elapsed_time(start_time, end_time, "WaitColorMatch", status)
                lib.report("API: WaitColorMatch API", status, image_required=True)
            else:
                lib.report("StartCaptureZapFrames failed", "FAILED", image_required=True)

    except Exception as e:
         lib.log_info("Exception from test_api(): " + str(e))
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
        lib.log_script_info(os.path.basename(__file__), apis_in_the_script)

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
