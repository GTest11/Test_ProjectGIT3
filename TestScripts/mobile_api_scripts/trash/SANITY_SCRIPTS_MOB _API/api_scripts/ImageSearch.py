# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :
# Date              :   04-10-2018
# Script Version    :   1.1
# APIs covered      :   "ImageSearch",
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os
import sys
import time

sys.path.append('../')
import library.common_functions as lib
import mobile_config.test_params as params

dut = lib.dut
fe_mob_lib = lib.fe_mob_lib

#''''''''''''''''''''''''''''''END IMPORTS''''''''''''''''''''''''''''''''

# Use defined variables and functions
test_data = params.image_search_params

apis_in_the_script = ("ImageSearch",
                      )
config = lib.set_config()


#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# @Function Name          : test_api()
# @Description        : to test ImageSearch API
# @Input arguments    : None
# @Output values        : True or False
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def test_api():
    api_status = True
    try:
        response = fe_mob_lib.ImageComparisonService.Response()
        for key, value in test_data.items():
            time.sleep(10)
            lib.log_info(" ----- Test Scenario - {} -----".format(value[0]))
            start_time = lib.gettimestamp()
            response = dut.validator.ImageSearch(*value[2])
            end_time = lib.gettimestamp()
            if response.OpStatus  == value[1]:
                status = "PASSED"
            else:
                status = "FAILED"
                api_status = False

            lib.report_elapsed_time(start_time, end_time, "ImageSearch", status)
            lib.report("API: ImageSearch API", status, image_required=True)

    except Exception as e:
        lib.log_error("Exception thrown by python from test_api(): " + str(e))
        api_status = False
    finally:
        return api_status


#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# @Function Name          : main()
# @Description        : logs API names, script name,
#                       updates the script status based on the test_api()
#                       function result
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
