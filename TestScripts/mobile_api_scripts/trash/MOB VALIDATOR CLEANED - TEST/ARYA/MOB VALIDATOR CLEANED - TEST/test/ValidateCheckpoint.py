# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :
# Date              :   05-10-2018
# FE Version        :   FE 5.1.0.3
# APIs covered      :   validateCheckPoint
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os
import sys
import time

sys.path.append('../')
import library.common_functions as lib
import mobile_config.test_params as params

dut = lib.dut
msl = lib.fe_mob_lib
chkpt = lib.chkpt

#''''''''''''''''''''''''''''''END IMPORTS''''''''''''''''''''''''''''''''

# Use defined variables and functions
test_data = params.validate_chkpt_params

apis_in_the_script = ("validateCheckPoint")
config = lib.set_config()


def log_script_info():
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    lib.log_info("Script Name: {}".format(os.path.basename(__file__)))
    lib.log_info("Validating APIs - {}".format(apis_in_the_script))
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def test_api():
    api_status = True
    try:

        for key, value in test_data.items():
            lib.log_info(" ----- Test Scenario - {} -----".format(value[0]))

            chkpt.init(value[2])

            time.sleep(3)
            start_time = lib.gettimestamp()
            validated = dut.validator.validateCheckPoint(chkpt)
            end_time = lib.gettimestamp()

            if validated == value[1]:
                status = "PASSED"
            else:
                status = "FAILED"
                api_status = False

            lib.report("API: Init", status, image_required=False)
            lib.report_elapsed_time(start_time, end_time, "validateCheckPoint", status)
            lib.report("API: validateCheckPoint API", status, image_required=True)

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
