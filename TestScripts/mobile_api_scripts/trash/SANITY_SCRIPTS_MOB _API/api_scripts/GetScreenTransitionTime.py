# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :
# Date              :   05-10-2018
# Script Version    :   1.1
# APIs covered      :   "GetScreenTransitionTime", "Click(ElementType, String, Int32)", "StartCaptureZapFrames",
#                       "StopCaptureZapFrames"
# Test Scenario     :   Launch app. Three scenarios covered for testing the API.
#                       1. Not on checkpoint screen : move out of the screen by click API
#                       2. Move out of checkpoint screen : play a video
#                       3. On checkpoint screen
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
test_data = params.get_screen_transition_time_params

apis_in_the_script = ("GetScreenTransitionTime", "Click(ElementType, String, Int32)", "StartCaptureZapFrames")
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
        scenarios = ("chkpt_screen", "move_out_chkpt_screen", "not_on_chkpt_screen")
        for scenario in scenarios:

            test_scenario = test_data[scenario]
            lib.log_info(" ----- Test Scenario - {} -----".format(test_scenario[0]))
            if scenario == "not_on_chkpt_screen":
                start_time = lib.gettimestamp()
                clicked = lib.dut.Click(lib.fe_mob_lib.Constants.ElementType.ClassName, config.ELEMENT_CLASSNAME_CLICK_INDEX,
                                        config.search_button_index)
                end_time = lib.gettimestamp()
                if clicked:
                    status = "PASSED"
                else:
                    status = "FAILED"

                lib.report_elapsed_time(start_time, end_time, "Click with index", status)
                lib.report("API: Click with index", status, image_required=True)

            elif scenario == "move_out_chkpt_screen":
                if not lib.dut.Tap(*config.c_tap_for_yt_playback):
                    lib.report("Tap on video", "FAILED", image_required=True)
                    return False
            else:
                pass
            if lib.dut.validator.StartCaptureZapFrames(30):
                start_time = lib.gettimestamp()
                screen_changed = lib.dut.validator.GetScreenTransitionTime(*test_scenario[2])
                end_time = lib.gettimestamp()
                lib.log_error("screen_changed time - {}".format(screen_changed))
                stopped = lib.dut.validator.StopCaptureZapFrames()
                if not stopped:
                    lib.report("API: StopCaptureZapFrames", "FAILED", image_required=True)

                if screen_changed >= 0:
                    screen_transition = True
                else:
                    screen_transition = False

                if screen_transition == test_scenario[1]:
                    status = "PASSED"
                    api_status = True
                else:
                    status = "FAILED"
                    api_status = False

                lib.report_elapsed_time(start_time, end_time, "GetScreenTransitionTime")
                lib.report("API: GetScreenTransitionTime API", status, image_required=True)
            else:
                lib.report("API: StartCaptureZapFrames", "FAILED", image_required=True)
                api_status = False

    except Exception as exe:
        lib.log_error("Exception thrown by python from test_api(): " + str(exe))
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

    except Exception as ex:
        lib.log_error("Exception raised in main function : " + str(ex))
        script_status = False

    finally:
        lib.stop_run()
        lib.CommitScriptResult(script_status)
        lib.log_info("-- Execution End --")

if __name__ == "__main__":
    main()