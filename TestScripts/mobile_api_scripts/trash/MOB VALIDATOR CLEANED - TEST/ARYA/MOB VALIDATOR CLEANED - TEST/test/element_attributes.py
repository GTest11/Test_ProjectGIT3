# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :
# Date              :   01-10-2018
# FE Version        :   FE 5.1.0.3
# APIs covered      :   "GetAllAttributeValues", "GetAllChildAttributeValues", "GetAttribute"
#
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, os, time
sys.path.append('../')
import library.common_functions as lib

dut = lib.dut
msl = lib.fe_mob_lib


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
apis_in_the_script = ("GetAllAttributeValues", "GetAllChildAttributeValues", "GetAttribute")
config = lib.set_config()


def log_script_info():
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    lib.log_info("Script Name: {}".format(os.path.basename(__file__)))
    lib.log_info("Validating APIs - {}".format(apis_in_the_script))
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



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


def test_api():
    api_test_status = True
    try:
        attr_list = lib.constants.ATTRIBUTE_LIST_GETALLATTRIBUTEVALUES
        # lib.log_info(attr_list)
        api_list = ("GetAttribute", "GetLocation", "GetAllAttributeValues", "GetAllChildAttributeValues")
        api_call = {
            "GetAllAttributeValues": dut.GetAllAttributeValues(msl.Constants.ElementType.XPath,
                                                               config.ELEMENT_XPATH_GETALLATTRIBUTEVALUES,
                                                               attr_list
                                                               ),
            # "GetAllChildAttributeValues": dut.GetAllChildAttributeValues(msl.Constants.ElementType.ClassName,
            #                                                              config.GET_ALL_CHILD_ELM, attr_list),
            "GetAllChildAttributeValues": dut.GetAllChildAttributeValues(msl.Constants.ElementType.XPath,
                                        config.ELEMENT_XPATH_GETALLATTRIBUTEVALUES, attr_list),
            "GetAttribute" : dut.GetAttribute(msl.Constants.ElementType.XPath,
                                           config.ELEMENT_XPATH_GETALLATTRIBUTEVALUES, "enabled"),
            "GetLocation" : dut.GetLocation(msl.Constants.ElementType.XPath,
                                           config.X_CLICK_INDEX)

        }

        attr_present = False
        for api in api_list:
            start_time = lib.gettimestamp()
            # if api == "GetLocation":
            #    location = msl.Models.Location()
            ret_val = api_call[api]
            end_time = lib.gettimestamp()
            lib.log_info("API: {} returned - ".format(api) + str(ret_val))
            time.sleep(5)
            if (api != "GetAttribute") and (api != "GetLocation"):
                # attr_present = validate_result(ret_val)
                if len(ret_val) > 0:
                    attr_present = True
            else:
                attr_present = ret_val
            if attr_present:
                status = "PASSED"
            else:
                status = "FAILED"
                api_test_status = False
            lib.report(api, status, image_required=True)
            lib.commit_step_result("API: Time taken by {} API {}".format(
                api, str(lib.getAPIduration(start_time, end_time))),
                status
            )

    except Exception as e:
        lib.log_error("Exception raised in test_api function : " + str(e))
        api_test_status = False
    finally:
        return api_test_status


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
