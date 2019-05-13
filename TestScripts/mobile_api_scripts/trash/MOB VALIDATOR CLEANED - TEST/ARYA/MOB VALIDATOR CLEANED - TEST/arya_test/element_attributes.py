# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :   01-10-2018 22 Oct 2018, 24 Oct 2018
#Script Version     : 1.1
#Modification details: 22 Oct 2018, fixed review comments - Arya
# APIs covered      :   "GetAllAttributeValues", "GetAllChildAttributeValues",
# "GetAttribute" and GetLocation
#Test Scenario:
#init to Youtube
#and calls GetAllAttributeValues", "GetAllChildAttributeValues", "GetAttribute"
# and GetLocation
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
apis_in_the_script = ("GetAttribute", "GetLocation", "GetAllAttributeValues", "GetAllChildAttributeValues")
config = lib.set_config()
# ''''''''''''''''''''' ''''''''USER DEFINED VARIABLES' - END '''''''''''''''''''''''''

# ''''''''''''''''''''''''''''USER DEFINED FUNCTIONS'''''''''''''''''''''''''''''''''''
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#@Function Name	  	: validate_result()
#@Description		: returns true if any of the attribute is true
#@Input arguments	: None
#@return values		: returns true if any of the attribute is true
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def validate_result(result):
    attr_list = lib.constants.ATTRIBUTE_LIST_GETALLATTRIBUTEVALUES
    lib.log_info("attr_list not formatted {}".format(attr_list))
    lib.log_info("result {}".format(result))
    attr_lst = list(attr_list.split(","))
    lib.log_info("attr_list formatted {}".format(attr_lst))
    attr_present = False
    for attr in attr_lst:
        lib.log_info("attr in attr_lst {}".format(attr))
        lib.log_info("result[attr] in attr_lst {}".format(result[attr]))
        if result[attr] == ['true']:
            attr_present = True
    return attr_present



#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#@Function Name	  	: test_api()
#@Description		: Positive scenario testing of following APIs:
#                     "CloseApp", "LaunchApp","SendAppToBackground"
#@Input arguments	: None
#@Output values		: None
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def test_api():
    api_test_status = True
    try:
        attr_list = lib.constants.ATTRIBUTE_LIST_GETALLATTRIBUTEVALUES
        test_attribute = "enabled"
        api_list = [("GetAttribute", lib.dut.GetAttribute), ("GetLocation", lib.dut.GetLocation),
                    ("GetAllAttributeValues", lib.dut.GetAllAttributeValues),
                    ("GetAllChildAttributeValues", lib.dut.GetAllChildAttributeValues)]

        api_call = lib.OrderedDict(api_list)
        api_params = {
            "GetAllAttributeValues": (lib.fe_mob_lib.Constants.ElementType.XPath,
                                      config.ELEMENT_XPATH_GETALLATTRIBUTEVALUES, attr_list),
            "GetAllChildAttributeValues": (lib.fe_mob_lib.Constants.ElementType.XPath,
                                        config.ELEMENT_XPATH_GETALLATTRIBUTEVALUES, attr_list),
            "GetAttribute": (lib.fe_mob_lib.Constants.ElementType.XPath,
                                           config.ELEMENT_XPATH_GETALLATTRIBUTEVALUES, test_attribute),
            "GetLocation": (lib.fe_mob_lib.Constants.ElementType.XPath,config.X_CLICK_INDEX )}

        attr_present = False
        for api in api_call:
            if api_params[api]:
                start_time = lib.gettimestamp()
                api_result = api_call[api](*api_params[api])
                end_time = lib.gettimestamp()
            #this else part is not required for the script right now, if a function does not take any parameter
            # apis_params will have a empty tuple () for that function and the else part call will work for that function.
            else:
                start_time = lib.gettimestamp()
                api_result = api_call[api]()
                end_time = lib.gettimestamp()


            time.sleep(5)
            #if (api != "GetAttribute") and (api != "GetLocation"):
            if (api == "GetAllAttributeValues") and (api == "GetAllChildAttributeValues"):
                # validate_result returns true if any of the attribute is true, but there can be some
                # element without any attribute so not using this function, currently used element can be validated using this function
                # attr_present = validate_result(ret_val)
                if len(api_result) > 0:
                    attr_present = True
            else:
                attr_present = api_result
            if attr_present:
                status = "PASSED"
                #If the
                #if (api == "GetLocation"):
                #    if not (api_result.X or api_result.Y):
                #        status = "FAILED"
            else:
                status = "FAILED"
                api_test_status = False

            lib.log_info("API: {} returned - ".format(api) + str(api_result))
            lib.report_elapsed_time(start_time, end_time, api, status)
            lib.report(api, status, image_required=True)
    except Exception as e:
        lib.log_error("Exception raised in test_api function : " + str(e))
        api_test_status = False
    finally:
        return api_test_status
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
            script_status = test_api()
        else:
            lib.log_error("App launch failed " )
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
