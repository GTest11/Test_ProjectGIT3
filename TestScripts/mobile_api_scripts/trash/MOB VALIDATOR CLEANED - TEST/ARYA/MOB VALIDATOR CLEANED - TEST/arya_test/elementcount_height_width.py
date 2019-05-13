# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :   01-10-2018, 17-10-2018, 22 Oct 2018, 24 Oct 2018
#Script Version     : 1.1
#Modification details: fixed review comments - Arya
# APIs covered      :   "GetElementCount", "GetHeight", "GetWidth"
#Test Scenario:
#init to Youtube
# get GetElementCount, "GetHeight" and "GetWidth"
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
# ''''''''''''''''''''''''''''''''''''''''IMPORTS - END'''''''''''''''''''''''''''''''

# ''''''''''''''''''''' ''''''''USER DEFINED VARIABLES'''''''''''''''''''''''''''''''''
#Variables
apis_in_the_script = ('GetElementCount','GetHeight', 'GetWidth')
config = lib.set_config()
# ''''''''''''''''''''' ''''''''USER DEFINED VARIABLES' - END '''''''''''''''''''''''''

# ''''''''''''''''''''''''''''USER DEFINED FUNCTIONS'''''''''''''''''''''''''''''''''''

def test_api():
    api_test_status = True
    try:
        apis = [("GetElementCount", lib.dut.GetElementCount), ("GetHeight", lib.dut.GetHeight), ("GetWidth", lib.dut.GetWidth)]
        apis_call = lib.OrderedDict(apis)

        apis_params = {
        "GetElementCount": (lib.fe_mob_lib.Constants.ElementType.XPath, config.ELEMENT_XPATH_COUNT_HEIGHT_WIDTH),
        "GetHeight": (lib.fe_mob_lib.Constants.ElementType.XPath, config.ELEMENT_XPATH_COUNT_HEIGHT_WIDTH),
        "GetWidth": (lib.fe_mob_lib.Constants.ElementType.XPath, config.ELEMENT_XPATH_COUNT_HEIGHT_WIDTH)
        }

        for api in apis_call:
            if apis_params[api]:
                start_time = lib.gettimestamp()
                api_result = apis_call[api](*apis_params[api])
                end_time = lib.gettimestamp()
            #this else part is not required for the script right now, if a function does not take any parameter
            # apis_params will have a empty tuple () for that function and the else part call will work for that function.
            else:
                start_time = lib.gettimestamp()
                api_result = apis_call[api]()
                end_time = lib.gettimestamp()
            time.sleep(3)
            if not api_result:
                status = "FAILED"
                api_test_status = False
            else:
                status = "PASSED"

            lib.logger.Log("API: {} ".format(api) + " returned - "+ str(api_result))
            lib.report_elapsed_time(start_time, end_time, api, status)
            lib.report("API: {} - Return value: {}".format(api, api_result), status, image_required=True)

    except Exception as e:
        lib.log_error("Exception raised in test_api() : " + str(e))
        api_test_status = False
    finally:
        return api_test_status
# ''''''''''''''''''''''''''''USER DEFINED FUNCTIONS - END '''''''''''''''''''''''''''


# ''''''''''''''''''''''''''''MAIN ''''''''''''''''''''''''''''''''''''''''''''''''''''
# ``````````````````````````````````````````````````````````````````````````
# Function Name	  	: main()
# Description		: main
# Input arguments	: Null
# Output values		: Null
# ``````````````````````````````````````````````````````````````````````````
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
