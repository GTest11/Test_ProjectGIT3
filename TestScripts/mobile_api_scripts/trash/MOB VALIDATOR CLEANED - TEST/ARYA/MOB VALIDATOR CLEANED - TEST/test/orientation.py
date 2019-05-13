# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :
# Date              :   01-10-2018
# FE Version        :   FE 5.1.0.3
# APIs covered      :   "GetOrientation", "ChangeOrientation"
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import sys, clr, time, os
sys.path.append('../')
import library.common_functions as lib

dut = lib.dut
msl = lib.fe_mob_lib

apis_in_the_script = ("GetOrientation", "ChangeOrientation", "SetOrientation")

config = lib.set_config()


def log_script_info():
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    lib.log_info("Script Name: {}".format(os.path.basename(__file__)))
    lib.log_info("Validating APIs - {}".format(apis_in_the_script))
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def resolution_changed(before, after):
    if (before[0] == after[1] and before[1] == after[0]):
        return True
    return False

def start_playback():
    searched = lib.search_in_youtube(config)
    if not searched:
        lib.report("Search", "FAILED", image_required=True)
        return False

    # tap on an item to start playback
    return True



def get_orientation():
    start_time = lib.gettimestamp()
    orientation = dut.GetOrientation()
    end_time = lib.str_to_milli_second_time()
    get_time = lib.getAPIduration(start_time, end_time)
    if orientation:
        status = lib.constants.STATUS[0]
    else:
        status = lib.constants.STATUS[1]
    lib.report("GetOrientation API :  {}".format(str(orientation)), status, image_required=True)
    lib.commit_step_result("API: GetOrientation API", status)
    lib.report("API: Time taken by GetOrientation API :  {}".format(str(get_time)), status)
    return orientation


def change_orientation():
    start_time = lib.gettimestamp()
    changed = dut.ChangeOrientation()
    end_time = lib.str_to_milli_second_time()
    time.sleep(5)
    if changed:
        status = "PASSED"
    else:
        status = "FAILED"
    lib.report_elapsed_time(start_time, end_time, "ChangeOrientation", status)
    lib.report("API: ChangeOrientation API", status, image_required=True)

    orientation = get_orientation()
    return orientation


def set_orientation(orient):
    lib.log_info("Setting orientation to {}".format(orient))
    start_time = lib.gettimestamp()
    set = dut.SetOrientation(orient)
    end_time = lib.str_to_milli_second_time()
    time.sleep(5)
    if set:
        status = "PASSED"
    else:
        status = "FAILED"
    lib.report("API: SetOrientation API", status, image_required=True)
    lib.commit_step_result("API: Reason", "Orientation Changed")

    orientation = get_orientation()
    return orientation


def test_api():
    script_status = True
    try:
        api_list = ("GetOrientation", "ChangeOrientation", "SetOrientation")
        api_call = {
            "GetOrientation" : get_orientation(),
            "ChangeOrientation" : dut.ChangeOrientation(),

        }

        status = "PASSED"
        orientation_before_change = get_orientation()
        if not orientation_before_change:
            lib.report("GetOrientation", "FAILED", image_required=True)
            return False

        time.sleep(2)
        resln_before = lib.get_image_resolution()
        lib.commit_step_result("Image Resolution on "
                                   + str(orientation_before_change), str(resln_before))

        if not dut.Tap(*config.c_tap_for_yt_playback):
            lib.report("Failed to tap on video", "FAILED", image_required=True)
            return False

        # to start the playback
        time.sleep(10)
        orientation_after_change = change_orientation()
        if not orientation_after_change:
            lib.report("ChangeOrientation", "FAILED", image_required=True)
            return False

        lib.log_info("GetOrientation after ChangeOrientation call: " + str(orientation_after_change))
        resln_after = lib.get_image_resolution()
        lib.commit_step_result("Image Resolution on "
                                   + str(orientation_after_change), str(resln_after))

        changed = resolution_changed(resln_before, resln_after)
        if not changed:
            lib.commit_step_result("API: ChangeOrientation API", "Failed")
            lib.commit_step_result("API: Reason", "No change in orientation after the API call")
            script_status = False

        if resln_after == "Landscape":
            orientation = set_orientation("Portrait")
        else:
            orientation = set_orientation("Landscape")

        if not orientation:
            lib.report("SetOrientation", "FAILED", image_required=True)
            return False

        resln_set = lib.get_image_resolution()
        lib.commit_step_result("Image Resolution on "
                               + str(orientation), str(resln_set))

        changed = resolution_changed(resln_after, resln_set)
        if not changed:
            lib.commit_step_result("API: SetOrientation API", "Failed")
            lib.commit_step_result("API: Reason", "No change in orientation after the API call")
            script_status = False
        else:
            lib.commit_step_result("API: SetOrientation API", "Passed")

        # return script_status
    except Exception as e:
        lib.log_error("Exception raised in test_api() function : " + str(e))
        script_status = False

    finally:
        return script_status


def main():
    status = False
    try:

        if not config:
            lib.report("Invalid Config", "FAILED")
            return False

        'updating the Test Script details'
        lib.update_tc_details()
        log_script_info()

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
