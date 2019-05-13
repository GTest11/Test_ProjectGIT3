# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :   M_API_04
# Author            :   Rohith P V
# Date              :   20-03-2018
# FE Version        :   5.0.9.4
# APIs covered      :   GetAttribute
# Description       :   GetAttribute API testing.
# Common Fns Used   :    update_TC_details : to update the Common details. Change the build no
#                       in Constants.py file
#
#                       update_dut_config : to configure the device based on the platform.
#                       Change the app details in Config.py file
#
# open_app: to start the Appium server & also initialise the driver.

# ''''''''''''''''''''AUTO GENERATED CODE - DO NOT MODIFY''''''''''''''''''''
import sys
sys.path.append('../')
import library.common_functions as com_lib

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


"""
``````````````````````````````````````````````````````````````````````````
Author			    : Rohith P V
Function Name	  	: test_getattribute()
Description		    : Function to test the GetAttribute API
Input arguments	    : ElementType,ElementID,Attribute
Output values		: String
``````````````````````````````````````````````````````````````````````````
"""


def test_getattribute():
    try:
        fn_return = False
        if str(com_lib.dut.ReadProperty(3)) == "Android":
            get_attr_xpath = com_lib.android_conf.ELEMENT_XPATH_GETATTRIBUTE
        else:
            get_attr_xpath = com_lib.ios_conf.ELEMENT_XPATH_GETATTRIBUTE
        attr_list = com_lib.constant.ATTRIBUTE_LIST_GETATTRIBUTE
        start_time = com_lib.str_to_milli_second_time()
        for i in attr_list:
            start_time = com_lib.str_to_milli_second_time()
            Attribute_value = com_lib.dut.GetAttribute(com_lib.MobileScriptingLibrary.Constants.ElementType.XPath, get_attr_xpath, i)
            end_time = com_lib.str_to_milli_second_time()
            GetAttribute_time = com_lib.get_duration(start_time, end_time)
            com_lib.commit_step_result("API: Time taken by GetAttribute API for" + i +"attribute",str(GetAttribute_time))
            com_lib.log_info("Attribute Value = " + Attribute_value)
            if(Attribute_value != " " ):
                fn_return = True
                com_lib.commit_step_result("API: GetAttribute", "Passed")
            else:
                com_lib.commit_step_result("API: GetAttribute", "Failed")
        #fn_return = True
    except Exception as e:
        com_lib.log_error(
            "Exception raised in test_getattribute function : " +
            str(e))
    finally:
        return fn_return


"""
``````````````````````````````````````````````````````````````````````````
Author			    : Rohith P V
Function Name	  	: main()
Description		    : Function where script execution starts
Input arguments	    : Null
Output values		: Null
``````````````````````````````````````````````````````````````````````````
"""


def main():
    try:
        'this is a variable used to hold the Platform name'
        global platform
        platform = str(com_lib.dut.ReadProperty(3))

        'updating the Test Script details'
        com_lib.update_tc_details()

        'configuring the device for automation'
        com_lib.update_dut_config(platform)

        'this is a variable used to update the Test script status'
        global status
        status = False

        'launching application'
        init_app_time = com_lib.open_app()
        if init_app_time > 0:
            if "Android" == platform:
                element_id = com_lib.android_conf.android_APP_HOME
            else:
                element_id = com_lib.ios_conf.ios_APP_HOME
            if not com_lib.dut.WaitForElement(
                    com_lib.MobileScriptingLibrary.Constants.ElementType.XPath, element_id, 20):
                com_lib.log_error("App not launched")
            else:
                status = test_getattribute()
        else:
            com_lib.log_error("Error in InitApp API")
    except Exception as e:
        com_lib.log_error("Exception raised in main function : " + str(e))
    finally:
        com_lib.close_app()
        com_lib.stop_driver()
        com_lib.CommitScriptResult(status)


if __name__ == "__main__":
    main()
