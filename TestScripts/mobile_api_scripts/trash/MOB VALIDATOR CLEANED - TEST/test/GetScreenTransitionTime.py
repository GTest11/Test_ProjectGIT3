# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :
# Date              :   05-10-2018
# FE Version        :   FE 5.1.0.3
# APIs covered      :   "GetScreenTransitionTime", "Click(ElementType, String, Int32)"
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os
import sys

sys.path.append('../')
import library.common_functions as lib
import mobile_config.test_params as params

dut = lib.dut
msl = lib.msl

#''''''''''''''''''''''''''''''END IMPORTS''''''''''''''''''''''''''''''''

# Use defined variables and functions
test_data = params.get_screen_transition_time_params

apis_in_the_script = ("GetScreenTransitionTime", "Click(ElementType, String, Int32)"
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
        scenarios = ("chkpt_screen", "not_on_chkpt_screen", "move_out_chkpt_screen" )
        for scenario in scenarios:

            if scenario == "not_on_chkpt_screen":
                start_time = lib.gettimestamp()
                clicked = dut.Click(msl.Constants.ElementType.ClassName, config.ELEMENT_CLASSNAME_CLICK_INDEX, config.search_button_index)
                end_time = lib.gettimestamp()
                if clicked:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    api_status = False

                lib.report_elapsed_time(start_time, end_time, "Click with index", status)
                lib.report("API: Click with index", status, image_required=True)

            test_scenario = test_data[scenario]
            lib.log_info(" ----- Test Scenario - {} -----".format(test_scenario[0]))
            if scenario == "move_out_chkpt_screen":
                if not dut.Tap(*config.c_tap_for_yt_playback):
                    lib.report("Tap on video", "FAILED", image_required=True)
                    return False

            if (dut.validator.StartCaptureZapFrames(30)):
                start_time = lib.gettimestamp()
                screen_changed = dut.validator.GetScreenTransitionTime(*test_scenario[2])
                end_time = lib.gettimestamp()
                lib.log_error("screen_changed - {}".format(screen_changed))
                stopped = dut.validator.StopCaptureZapFrames()
                if not stopped:
                    lib.report("Failed: StopCaptureZapFrames", "FAILED", image_required=True)
                    # api_status = False

                if screen_changed:
                    screen_transition = True
                else:
                    screen_transition = False

                if screen_transition == test_scenario[1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    api_status = False

                lib.report_elapsed_time(start_time, end_time, "GetScreenTransitionTime", status)
                lib.report("API: GetScreenTransitionTime API", status, image_required=True)
            else:
                lib.report("Faile: StartCaptureZapFrames", "FAILED", image_required=True)
                api_status = False

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
