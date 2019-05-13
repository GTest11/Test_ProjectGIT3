#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :   M_API_02
# Author            :   Arathy P S
# Date              :   13-03-2018
# Script Version    :   1.1
# APIs covered      :   ReadCustomProperty
# Description       :   ReadCustomProperty  API testing.
# Common Fns Used   :   update_TC_details : to update the Common details. Change the build no
#                       in Constants.py file
#
#                       update_dut_config : to configure the device based on the platform.
#                       Change the app details in Config.py file
#''''''''''''''''''''AUTO GENERATED CODE - DO NOT MODIFY''''''''''''''''''''
import sys
sys.path.append('../')
import library.common_functions as com_lib

"""
``````````````````````````````````````````````````````````````````````````
Author			    : Arathy P S
Function Name	  	: test_read_custom_property()
Description		    : Function to test the ReadCubeProperty API
Input arguments	    : property_number   :   Property number
Output values		: value             :   Property value
``````````````````````````````````````````````````````````````````````````
"""


def test_read_custom_property():
    try:
        custom_prop_lst = com_lib.constant.propertyName
        for index in custom_prop_lst:
            custom_value = com_lib.dut.ReadCustomProperty(index)
            com_lib.commit_step_result("Custom property value ", custom_value)
    except Exception as e:
        com_lib.log_error("Exception raised in test_read_custom_property function: " + str(e))

"""
``````````````````````````````````````````````````````````````````````````
Author			    : Arathy P S
Function Name	  	: main()
Description		    : Function where script execution starts
Input arguments	    : Null
Output values		: Null
``````````````````````````````````````````````````````````````````````````
"""


def main():
    try:
        'updating the Test Script details'
        com_lib.update_tc_details()

        'configuring the device for automation'
        com_lib.update_dut_config(str(com_lib.dut.ReadProperty(3)))

        'this is a variable used to update the Test script status'
        global status
        status = False

        'launching application'
        init_app_time = com_lib.open_app()
        if init_app_time > 0:
            if "Android" == str(com_lib.dut.ReadProperty(3)):
                element_id = com_lib.android_conf.android_APP_HOME
            else:
                element_id = com_lib.ios_conf.ios_APP_HOME
            if not com_lib.dut.WaitForElement(com_lib.MobileScriptingLibrary.Constants.ElementType.XPath, element_id, 20):
                com_lib.log_error("App not launched")
            else:
                test_read_custom_property()
                status = True
        else:
            com_lib.log_error("Error in InitApp API")
    except Exception as e:
        com_lib.log_error("Exception raised in main function: " + str(e))
    finally:
        com_lib.close_app()
        com_lib.stop_driver()
        com_lib.CommitScriptResult(status)

if __name__ == "__main__":
    main()



