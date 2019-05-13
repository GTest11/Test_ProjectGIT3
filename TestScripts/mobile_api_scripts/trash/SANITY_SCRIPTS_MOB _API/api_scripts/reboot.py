# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :   Rohith P V
# Date              :   05-10-2018
# Script Version    :   1.1
# Modification details: Fixed review comments, date 17/10/2018
# APIs covered      :   Reboot
# Test Scenario     :   Launches youtube application -> Reboot API executed
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, os, time
sys.path.append('../')
import library.common_functions as lib

#dut = lib.dut
#msl = lib.msl

#''''''''''''''''''''''''''''''END IMPORTS''''''''''''''''''''''''''''''''

apis_in_the_script = ("Reboot")
config = lib.set_config()

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# @Function Name	: test_api()
# @Description		: Tests the Reboot API and logs its response (status, duration)
# @Input arguments	: Null
# @Output values	: Bool
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def test_api():
    api_status = False
    try:
        w, h = lib.get_image_resolution()
        lib.report("Validating Reboot API. Screenshot before reboot >", "PASSED", image_required=True)
        lib.log_info("w - {}, h - {}".format(w, h))
        lib.dut.CloseApp() # Closes the app for capturing the image of home screen before reboot
        time.sleep(5)
        ref_img_path = lib.dut.validator.CaptureImage(0, 0, w, h, "ref_img", 90, 1)
        start_time = lib.gettimestamp()
        rebooted = lib.dut.Reboot()
        end_time = lib.gettimestamp()
        time.sleep(80) # waiting for the device to come up
        test_img_path = lib.dut.validator.CaptureImage(0, 0, w, h, "test_img", 90, 1)
        matched = lib.dut.validator.ImageMatch("ref_img", "test_img", 2, "13")
        if rebooted and matched:
            status = "PASSED"
            api_status = True
        else:
            status = "FAILED"

        lib.report_elapsed_time(start_time, end_time, "Reboot", status)
        lib.report("API: Reboot API", status, image_required=True)

    except Exception as e:
        lib.log_error("Exception thrown by python from test_api(): " + str(e))

    finally:
        return api_status


def main():
    driver = False
    script_status = False
    try:
        if not config:
            lib.report("Invalid Config", "FAILED")
            return False

        lib.log_info("*** FOR ANDROID DEVICES, SET THE SCREEN LOCK TYPE TO 'None' BEFORE RUNNING THIS TEST ***")
        lib.log_info("*** FOR iOS DEVICES, REMOVE PASS CODE BEFORE RUNNING THIS TEST ***")

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

if __name__ == "__main__":
    main()
