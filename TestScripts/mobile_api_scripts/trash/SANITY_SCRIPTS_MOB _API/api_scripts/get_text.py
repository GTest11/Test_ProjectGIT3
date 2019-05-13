# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase Name     :   get_text.py
# Author            :
# Date              :   01-10-2018
# FE Version        :   FE 5.1.0.3
# APIs covered      :   "GetText", "GetTextIndex",
# Test scenario     :   Launch App. Call GetText API & GetText with index APIs. If text obtained,
#                       log it as pass else failure
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
try:
    import os
    import sys
    sys.path.append('../')
    import library.common_functions as lib
except Exception as e:
    print ("Exception in Import " + str(e))
    sys.exit()

# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
apis_in_the_script = ("GetText", "GetTextIndex")
config = lib.set_config()
file_name = os.path.basename(__file__)

"""
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Function Name       : get_text_index()
Description         : Tests the GetText with index APIs
Input arguments     : Null
Output values		: string  :   text obtained from the API
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""


def get_text_index():
    read_text = False
    try:
        if not lib.dut.Click(
                lib.fe_mob_lib.Constants.ElementType.XPath, config.click_gettext):
            lib.report("Failed to click", "FAILED", image_required=True)
            return False

        start_time = lib.gettimestamp()
        get_text = lib.dut.GetText(
            lib.fe_mob_lib.Constants.ElementType.XPath,
            config.GETTEXT_XPath,
            config.GETTEXT_index)
        end_time = lib.gettimestamp()
        if get_text:
            lib.commit_step_result("Text obtained", get_text)
            read_text = True
            status = "PASSED"
        else:
            status = "FAILED"
        lib.report_elapsed_time(start_time, end_time, "GetText with Index")
        lib.report("GetText with Index", status, image_required=True)

    except Exception as e:
        lib.log_error("Exception from get_text_index() " + str(e))
        read_text = False
    finally:
        return read_text


"""
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Function Name       : test_api()
Description         : Tests the GetText & GetText with index APIs
Input arguments     : Null
Output values		: bool  :   API status
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""


def test_api():
    api_test_status = False
    try:
        start_time = lib.gettimestamp()
        get_text = lib.dut.GetText(
            lib.fe_mob_lib.Constants.ElementType.XPath,
            config.APP_GETTEXT)
        end_time = lib.gettimestamp()
        if get_text:
            status = "PASSED"
            api_test_status = True
        else:
            status = "FAILED"

        lib.report_elapsed_time(start_time, end_time, "GetText")
        lib.report("GetText API", status, image_required=True)

        api_test_status = get_text_index()

    except Exception as e:
        lib.log_error("Exception raised in test_api function : " + str(e))
        api_test_status = False
    finally:
        return api_test_status


"""
``````````````````````````````````````````````````````````````````````````
Function Name	  	: main
Description		    : main function
Input arguments	    : null
Output values		: null
``````````````````````````````````````````````````````````````````````````
"""


def main():
    script_status = False
    try:
        if not config:
            lib.report("Invalid Config", "FAILED")
            return False

        'updating the Test Script details'
        lib.update_tc_details()
        lib.log_script_info(file_name, apis_in_the_script)

        'launching application'
        if lib.start_run(home=config.app_home):
            script_status = test_api()
        else:
            lib.report("Script Status", "FAILED", image_required=True)

    except Exception as e:
        lib.log_error("Exception raised in main function : " + str(e))
    finally:
        lib.stop_run()
        lib.CommitScriptResult(script_status)
        lib.log_info("-- Execution End --")


if __name__ == "__main__":
    main()
