# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :   04-10-2018 22 Oct 2018
#Script Version     : 1.1
#Modification details: 22 Oct 2018, fixed review comments - Arya
# APIs covered      :   DynamicImageCompare
#Test Scenario:
#init to Youtube
# '''''''''''''''''''''''''''TEST CASE DETAILS' - END '''''''''''''''''''''''''''''''''

# ''''''''''''''''''''''''''''''''''''''''IMPORTS''''''''''''''''''''''''''''''''''''''
#importing python modules
import sys
import os
import time

#importing user defined functions
sys.path.append('../')
try:
    # Import library file
    import library.common_functions as lib
except ImportError:
    print("Failed to import common_functions file")
    sys.exit()
try:
    # Import library file
    import mobile_config.test_params as params
except ImportError:
    print("Failed to import test_params file")
    sys.exit()
# ''''''''''''''''''''''''''''''''''''''''IMPORTS - END'''''''''''''''''''''''''''''''

# ''''''''''''''''''''' ''''''''USER DEFINED VARIABLES'''''''''''''''''''''''''''''''''

# Use defined variables and functions
test_data = params.dynamic_image_compare_params
# ''''''''''''''''''''' ''''''''USER DEFINED VARIABLES' - END '''''''''''''''''''''''''

# ''''''''''''''''''''''''''''USER DEFINED FUNCTIONS'''''''''''''''''''''''''''''''''''
apis_in_the_script = ("DynamicImageCompare")
config = lib.set_config()


#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#@Function Name	  	: test_api()
#@Description		: Positive scenario testing of following APIs:
#                     "CloseApp", "LaunchApp","SendAppToBackground"
#@Input arguments	: None
#@Output values		: None
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def test_api():
    api_status = True
    try:
        time.sleep(10)

        if not lib.dut.validator.CacheImageFromUrl(params.CACHE_VALID_URL_FOR_DYNAMIC_COMPARE, params.img_name):
            lib.report("CacheImageFromUrl", "FAILED", image_required=True)
            return False

        for key, value in test_data.items():
            time.sleep(10)
            lib.log_info(" ----- Test Scenario - {} -----".format(value[0]))
            start_time = lib.gettimestamp()
            compared = lib.dut.validator.DynamicImageCompare(*value[2])
            end_time = lib.gettimestamp()
            lib.log_error("detected - {}".format(compared))

            if compared == value[1]:
                status = "PASSED"
            else:
                status = "FAILED"
                api_status = False

            lib.report_elapsed_time(start_time, end_time, "DynamicImageCompare", status)
            lib.report("API: DynamicImageCompare API", status, image_required=True)

    except Exception as e:
        lib.log_error("Exception thrown by python from test_api(): " + str(e))
        api_status = False
    finally:
        return api_status
# ''''''''''''''''''''''''''''USER DEFINED FUNCTIONS - END '''''''''''''''''''''''''''


# ''''''''''''''''''''''''''''MAIN ''''''''''''''''''''''''''''''''''''''''''''''''''''
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#@Function Name	  	: main()
#@Description		: main function
#@Input arguments	: None
#@Output values		: None
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
# ''''''''''''''''''''''''''''MAIN - END'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if __name__ == "__main__":
    main()

#''''''''''''''''''''''''''''' END OF SCRIPT ''''''''''''''''''''''''''''''''''''''''''''''''''''
