# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Script name       :   orientation.py
# Author            :
# Date              :   01-10-2018
# Script Version    :   1.1
# APIs covered      :   "GetOrientation", "ChangeOrientation", "SetOrientation"
# Common Functions  :   set_config(), log_info(), report(), gettimestamp(), search_in_youtube(), commit_step_result(),
#                       report_elapsed_time(), CommitScriptResult(), start_run
# Test Scenario     :   Launch the APP, call the GetOrientation API to get the current orientation
#                       Call the ChangeOrientation API to change the current orientation. Take the
#                       Image resolution before and after ChangeOrientation API call. If the Image resolution changed,
#                       commit the API Status as PASS.
#                       Call SetOrientation API to change the orientation. compare the image resolution to commit the
#                       API Status.
#                       Finally Close the APP and stop the appium driver.
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
try:
    import os
    import sys
    sys.path.append('../')
    import library.common_functions as lib
except Exception as e:
    print ("Exception in Import " + str(e))
    sys.exit()

apis_in_the_script = ("GetOrientation", "ChangeOrientation", "SetOrientation")
file_name = os.path.basename(__file__)
config = lib.set_config()

"""
``````````````````````````````````````````````````````````````````````````
Function Name	  	: resolution_changed
Description		    : Function to compare the resolutions
Input arguments	    : before    :   Resolution before change orientation
                      after     :   Resolution after change orientation
Output values		: bool
``````````````````````````````````````````````````````````````````````````
"""


def resolution_changed(before, after):
    if before[0] == after[1] and before[1] == after[0]:
        return True
    return False

"""
``````````````````````````````````````````````````````````````````````````
Function Name	  	: start_playback
Description		    : Function to start play back
Input arguments	    : null
Output values		: bool
``````````````````````````````````````````````````````````````````````````
"""


def start_playback():
    status = False
    try:
        searched = lib.search_in_youtube(config)
        if not searched:
            lib.report("Search", "FAILED", image_required=True)
        else:
            status = True
    except Exception as e:
        lib.log_error("Exception in start_playback Function" + str(e))
        status = False
    finally:
        return status

"""
``````````````````````````````````````````````````````````````````````````
Function Name	  	: get_orientation
Description		    : Function to call GetOrientation API
Input arguments	    : null
Output values		: string    :   orientation
``````````````````````````````````````````````````````````````````````````
"""


def get_orientation():
    orientation = None
    try:
        start_time = lib.gettimestamp()
        orientation = lib.dut.GetOrientation()
        end_time = lib.gettimestamp()
        if orientation:
            lib.report("GetOrientation API", orientation, image_required=True)
            lib.commit_step_result("GetOrientation", "PASSED")
        else:
            lib.commit_step_result("GetOrientation", "FAILED")
        lib.report_elapsed_time(start_time, end_time, "GetOrientation")
    except Exception as e:
        orientation = None
        lib.log_error("Exception in get_orientation Function" + str(e))
    finally:
        return orientation

"""
``````````````````````````````````````````````````````````````````````````
Function Name	  	: change_orientation
Description		    : Function to call ChangeOrientation API
Input arguments	    : null
Output values		: string    :   orientation
``````````````````````````````````````````````````````````````````````````
"""


def change_orientation():
    orientation = None
    try:
        start_time = lib.gettimestamp()
        changed = lib.dut.ChangeOrientation()
        end_time = lib.gettimestamp()
        if changed:
            status = "PASSED"
        else:
            status = "FAILED"
        lib.report("API: ChangeOrientation", status, image_required=True)
        lib.report_elapsed_time(start_time, end_time, "ChangeOrientation")
        orientation = lib.dut.GetOrientation()
    except Exception as e:
        orientation = None
        lib.log_error("Exception in change_orientation Function" + str(e))
    finally:
        return orientation

"""
``````````````````````````````````````````````````````````````````````````
Function Name	  	: set_orientation
Description		    : Function to call SetOrientation API
Input arguments	    : string    :   Orientation to change
Output values		: string    :   Orientation after API call
``````````````````````````````````````````````````````````````````````````
"""


def set_orientation(orient):
    orientation = None
    try:
        lib.log_info("Setting orientation to {}".format(orient))
        start_time = lib.gettimestamp()
        set_changed = lib.dut.SetOrientation(orient)
        end_time = lib.gettimestamp()
        if set_changed:
            status = "PASSED"
        else:
            status = "FAILED"
        lib.report("API: SetOrientation", status, image_required=True)
        lib.report_elapsed_time(start_time, end_time, "SetOrientation")
        orientation = lib.dut.GetOrientation()
    except Exception as e:
        orientation = None
        lib.log_error("Exception in set_orientation Function" + str(e))
    finally:
        return orientation

"""
``````````````````````````````````````````````````````````````````````````
Function Name	  	: test_api
Description		    : Function to test the APIs
Input arguments	    : null
Output values		: bool  :   script execution status
``````````````````````````````````````````````````````````````````````````
"""


def test_api():
    script_status = False
    try:
        orientation_before_change = get_orientation()
        if None == orientation_before_change:
            lib.commit_step_result("API: GetOrientation", "FAILED")
            return script_status    # returns if GetOrientation API fails
        resln_before_change = lib.get_image_resolution()
        lib.commit_step_result("Image Resolution on " + str(orientation_before_change), str(resln_before_change))

        if not lib.dut.Tap(*config.c_tap_for_yt_playback):
            lib.report("Failed to tap on video", "FAILED", image_required=True)

        lib.delay(10)   # delay for play back
        orientation_after_change = change_orientation()
        if None == orientation_after_change:
            lib.commit_step_result("API: ChangeOrientation", "FAILED")
            return script_status    # returns if ChangeOrientation API fails
        else:
            resln_after_change = lib.get_image_resolution()
            lib.commit_step_result("Image Resolution on " + str(orientation_after_change), str(resln_after_change))
            lib.log_info("Orientation after ChangeOrientation: " + str(orientation_after_change))

        changed = resolution_changed(resln_before_change, resln_after_change)
        if not changed:
            lib.commit_step_result("API: ChangeOrientation API", "FAILED")
            lib.commit_step_result("API: Reason", "No change in orientation after the API call")
            return script_status    # returns if ChangeOrientation API fails
        else:
            lib.commit_step_result("API: ChangeOrientation API", "Passed")
        if orientation_after_change == "Landscape":
            orientation_after_set = set_orientation("Portrait")
        else:
            orientation_after_set = set_orientation("Landscape")

        if None == orientation_after_set:
            lib.commit_step_result("API: SetOrientation API", "FAILED")
            return script_status    # returns if SetOrientation API fails
        resln_after_set = lib.get_image_resolution()
        lib.log_info("Orientation after SetOrientation: " + str(orientation_after_change))

        changed_set = resolution_changed(resln_after_change, resln_after_set)
        if not changed_set:
            lib.commit_step_result("API: SetOrientation API", "Failed")
            lib.commit_step_result("API: Reason", "No change in orientation after the API call")
        else:
            lib.commit_step_result("API: SetOrientation API", "Passed")
            script_status = True
    except Exception as e:
        script_status = False
        lib.log_error("Exception raised in test_api() function : " + str(e))
    finally:
        lib.dut.SetOrientation("Portrait")
        return script_status

"""
``````````````````````````````````````````````````````````````````````````
Function Name	  	: main
Description		    : main function
Input arguments	    : null
Output values		: null
# ``````````````````````````````````````````````````````````````````````````
"""


def main():
    status = False
    try:
        if not config:
            lib.report("Invalid Config", "FAILED")
            return False    # returns if the configuration is invalid
        'updating the Test Script details'
        lib.update_tc_details()
        lib.log_script_info(file_name, apis_in_the_script)
        if lib.start_run(home=config.app_home):
            status = test_api()
    except Exception as e:
        lib.log_error("Exception raised in main function: " + str(e))
        status = False
    finally:
        lib.stop_run()
        lib.CommitScriptResult(status)
        lib.log_info("-- Execution End --")

if __name__ == "__main__":
    main()