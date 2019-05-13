# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :   Shameena HA
# Date              :   08-10-2018
# Script Version    :   1.1
# APIs covered      :   PressAndMove
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, os, time
sys.path.append('../')
import library.common_functions as lib

dut = lib.dut
# msl = lib.msl

#''''''''''''''''''''''''''''''END IMPORTS''''''''''''''''''''''''''''''''


apis_in_the_script = ("PressAndMove")
config = lib.set_config()


#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# @Function Name       : clear_screen()
# @Description        : Clears the screen by removing the top bar
# @Input arguments    : width and height of the screen
# @Output values        : True or False
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def clear_screen(w, h):
    img_path1 = dut.validator.CaptureImage(0, 0, w, h, "img1", 90, 1)
    swiped = dut.VerticalSwipe(*config.c_v_swipe)

    if not swiped:
        lib.log_error("Swipe Up Failed")
    time.sleep(10)
    img_path2 = dut.validator.CaptureImage(0, 0, w, h, "img2", 90, 1)
    return not dut.validator.ImageMatch("img1", "img2", 2, "13")


#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# @Function Name       : test_api()
# @Description        : validates PressAndMove
# @Input arguments    : None
# @Output values        : True or False
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def test_api():
    api_status = True
    try:
        lib.log_info("w - {}, h - {}".format(10, 20))
        w, h = lib.get_image_resolution()
        if not w and not h:
            lib.report("Image Resolution", "FAILED", image_required=True)
            api_status = False
            return api_status

        lib.report("Validating PressAndMove API. Screenshot", "PASSED", image_required=True)
        lib.log_info("w - {}, h - {}".format(w, h))

        # closes the application
        # dut.CloseApp()

        time.sleep(3)
        ref_img_path = dut.validator.CaptureImage(0, 0, w, h, "ref_img", 90, 1)
        start_time = lib.gettimestamp()
        moved = dut.PressAndMove(*config.c_press_move)
        end_time = lib.gettimestamp()
        time.sleep(10)
        test_img_path = dut.validator.CaptureImage(0, 0, w, h, "test_img", 90, 1)

        matched = dut.validator.ImageMatch("ref_img", "test_img", 2, "13")

        if (not matched) and moved:
            status = "PASSED"
        else:
            api_status = False
            status = "FAILED"

        lib.report_elapsed_time(start_time, end_time, "PressAndMove")
        lib.report("API: PressAndMove API", status, image_required=True)

        # cleared = clear_screen(w, h)
        # if not cleared:
        #     lib.report("Failed to clear the screen", "FAILED", image_required=True)
        #     api_status = False

    except Exception as e:
        lib.log_error("Exception thrown by python from test_api(): " + str(e))
        api_status = False

    finally:
        return api_status


#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# @Function Name          : main()
# @Description        : logs API names, script name,
#                       updates the script status based on the test_api() function result
# @Input arguments    : None
# @Output values        : None
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
