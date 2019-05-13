# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :
# Date              :   08-10-2018
# FE Version        :   FE 5.1.0.3
# APIs covered      :   PressAndMove
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, os, time
sys.path.append('../')
import library.common_functions as lib

dut = lib.dut
msl = lib.msl

#''''''''''''''''''''''''''''''END IMPORTS''''''''''''''''''''''''''''''''

# Use defined variables and functions
# test_data = params.capture_image_params

apis_in_the_script = ("Swipe", "VerticalSwipe", "HorizontalSwipe"
                      )
config = lib.set_config("skygo")

def log_script_info():
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    lib.log_info("Script Name: {}".format(os.path.basename(__file__)))
    lib.log_info("Validating APIs - {}".format(apis_in_the_script))
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# @Function Name	  	: TestAPI()
# @Description		: Tests the CaptureImage API with diffrent parameters and
# logs its response (status, duration)
# @Input arguments	: Iteration count
# @Output values		: Null
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def v_swipe(w, h):
    img_path1 = dut.validator.CaptureImage(0, 0, w, h, "img1", 90, 0)
    swiped = dut.VerticalSwipe(*config.c_v_swipe)
    img_path2 = dut.validator.CaptureImage(0, 0, w, h, "img2", 90, 0)
    return not dut.validator.ImageMatch("img1", "img2", 2, "13")

def h_swipe(w, h):
    img_path1 = dut.validator.CaptureImage(0, 0, w, h, "img1", 90, 0)
    swiped = dut.HorizontalSwipe(*config.c_h_swipe)
    time.sleep(5)
    img_path2 = dut.validator.CaptureImage(0, 0, w, h, "img2", 90, 0)
    return dut.validator.ImageMatch("img1", "img2", 2, "13")


def test_api():
    api_status = True
    try:
        w, h = lib.get_image_resolution()
        lib.log_info("w - {}, h - {}".format(w, h))

        time.sleep(5)
        ref_img_path = dut.validator.CaptureImage(0, 0, w, h, "ref_img", 90, 0)
        start_time = lib.gettimestamp()
        swiped = dut.Swipe(*config.c_press_move)
        end_time = lib.gettimestamp()
        test_img_path = dut.validator.CaptureImage(0, 0, w, h, "test_img", 90, 0)

        matched = dut.validator.ImageMatch("ref_img", "test_img", 2, "13")

        if (not matched) and swiped:
            status = "PASSED"
        else:
            api_status = False
            status = "FAILED"

        lib.report_elapsed_time(start_time, end_time, "Swipe", status)
        lib.report("API: Swipe API", status, image_required=True)

        time.sleep(2)

        swiped = v_swipe(w, h)
        if swiped:
            status = "PASSED"
        else:
            status = "FAILED"
            script_status = False

        lib.report_elapsed_time(start_time, end_time, "VerticalSwipe", status)
        lib.report("API: VerticalSwipe API", status, image_required=True)

        time.sleep(5)

        swiped = h_swipe(w, h)
        if swiped:
            status = "FAILED"
            script_status = False
        else:
            status = "PASSED"

        lib.report_elapsed_time(start_time, end_time, "HorizontalSwipe", status)
        lib.report("API: HorizontalSwipe API", status, image_required=True)


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
        if lib.start_run(msl.Constants.ElementType.Id, config.skygo_home):
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
