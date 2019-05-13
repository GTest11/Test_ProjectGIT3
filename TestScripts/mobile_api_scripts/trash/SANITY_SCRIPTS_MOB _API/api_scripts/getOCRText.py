# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :   Rohith P V
# Date              :   05-10-2018
# Script Version    :   1.1
# Modification details: Fixed review comments, date 17/10/2018
# APIs covered      :   "getOCRText"
# Test Scenario     :   Launches youtube application -> Gets text using getOCRText API
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os
import sys
import time

sys.path.append('../')
import library.common_functions as lib
import mobile_config.test_params as params

# dut = lib.dut
# msl = lib.msl
chkpt = lib.chkpt

#''''''''''''''''''''''''''''''END IMPORTS''''''''''''''''''''''''''''''''

# Use defined variables and functions
test_data = params.get_ocr_text_params

apis_in_the_script = ("getOCRText"
                      )
config = lib.set_config()

def test_api():
    api_status = False
    status = "FAILED"
    dut_mob_name = lib.get_dut_name() # Read the name of the mobile DUT
    try:
        if dut_mob_name in config.get_ocr_text_coordinates_dict:
            x, y, w, h = config.get_ocr_text_coordinates_dict[dut_mob_name] # Takes coordinates from get_ocr_text_coordinates_dict dictionary according to the dut name
        for key, value in test_data.items():
            lib.log_info(" ----- Test Scenario - {} -----".format(value[0]))

            time.sleep(3)
            #x, y, w, h = config.c_get_ocr_text
            f, l = value[2]
            start_time = lib.gettimestamp()
            read = lib.dut.validator.getOCRText(x, y, w, h, f, l)
            end_time = lib.gettimestamp()
            lib.log_info("getOCRText API - {}".format(read))
            if read == "Home":
                status = "FAILED"
                api_status = True

            lib.report_elapsed_time(start_time, end_time, "getOCRText", status)
            lib.report("getOCRText API", status, image_required=True)

    except Exception as e:
         lib.log_info("Exception from test_api(): " + str(e))
    finally:
        return api_status


def main():
    driver = False
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
