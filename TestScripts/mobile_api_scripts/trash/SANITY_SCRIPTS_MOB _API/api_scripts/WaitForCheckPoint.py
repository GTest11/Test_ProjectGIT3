# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :   Shameena HA
# Date              :   04-10-2018
# Script Version    :   1.1
# APIs covered      :   "init", "WaitForCheckpoint",
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
test_data = params.wait_for_chkpt_params

apis_in_the_script = ("init", "WaitForCheckpoint",
                      )
config = lib.set_config()


#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# @Function Name          : test_api()
# @Description        : to test - "init", "WaitForCheckpoint" APIs
# @Input arguments    : None
# @Output values        : True or False
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def test_api():
    api_status = True
    try:

        iter = 0
        for key, value in test_data.items():
            lib.log_info(" ----- Test Scenario - {} -----".format(value[0]))
            time.sleep(1)

            if iter == 1:
                dut.Tap(*config.c_tap_for_yt_playback)
                time.sleep(1) # default wait before starting playback
            # else:
            #     lib.log_info("****11")
            #     if not lib.tapelement_if_present(lib.fe_mob_lib.Constants.ElementType.XPath, config.x_back_to_home,
            #                                  "Home Nav Button"):
            #         lib.report("Failed to tap on Home", "FAILED")
            #         return False

            match_found = False
            start_time = 0
            end_time = 0
            if (dut.validator.StartCaptureZapFrames(params.captureZapTime)):
                start_time = lib.gettimestamp()
                match_found = dut.validator.WaitForCheckpoint(*value[2])
                end_time = lib.gettimestamp()
                dut.validator.StopCaptureZapFrames()
            else:
                lib.report("StartCaptureZapFrames failed", "FAILED", image_required=True)

            if match_found == value[1]:
                status = "PASSED"
            else:
                status = "FAILED"
                api_status = False

            lib.report("API: Init", status, image_required=False)
            lib.report_elapsed_time(start_time, end_time, "WaitForCheckpoint")
            lib.report("API: WaitForCheckpoint API", status, image_required=True)

            time.sleep(1)

            iter += 1

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
