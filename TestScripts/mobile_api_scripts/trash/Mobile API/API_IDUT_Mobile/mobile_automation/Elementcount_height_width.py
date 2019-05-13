#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :   M_API_04
# Author            :   Rohith P V
# Date              :   20-03-2018
# FE Version        :   5.0.9.4
# APIs covered      :   GetElementCount, GetHeight, GetWidth
# Description       :   GetElementCount, GetHeight, GetWidth API testing.
# Common Fns Used   :    update_TC_details : to update the Common details. Change the build no
#                       in Constants.py file
#
#                       update_dut_config : to configure the device based on the platform.
#                       Change the app details in Config.py file
#
#                       open_app: to start the Appium server & also initialise the driver.

#''''''''''''''''''''AUTO GENERATED CODE - DO NOT MODIFY''''''''''''''''''''
import sys
sys.path.append('../')
import library.common_functions as com_lib

#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


"""
``````````````````````````````````````````````````````````````````````````
Author			    : Rohith P V
Function Name	  	: test_elementcount_height_width()
Description		    : Function to test the GetElementCount, GetHeight, GetWidth API
Input arguments	    : ElementType,ElementID
Output values		: Int32
``````````````````````````````````````````````````````````````````````````
"""

def test_elementcount_height_width():
    try:
        if str(com_lib.dut.ReadProperty(3)) == "Android":
            xpath_element = com_lib.android_conf.ELEMENT_XPATH_COUNT_HEIGHT_WIDTH
        else:
            xpath_element = com_lib.ios_conf.ELEMENT_XPATH_COUNT_HEIGHT_WIDTH
        fn_return = False
        #GetElementCount API
        start_time = com_lib.str_to_milli_second_time()
        elementcount=com_lib.dut.GetElementCount(com_lib.MobileScriptingLibrary.Constants.ElementType.XPath,xpath_element)
        end_time = com_lib.str_to_milli_second_time()
        GetElementCount_time = com_lib.get_duration(start_time, end_time)
        com_lib.commit_step_result("API: Time taken by GetElementCount API ", str(GetElementCount_time))        
        com_lib.log_info("GetElementCount : "+str(elementcount))
        #GetHeight API
        start_time = com_lib.str_to_milli_second_time()
        element_height=com_lib.dut.GetHeight(com_lib.MobileScriptingLibrary.Constants.ElementType.XPath,xpath_element)
        end_time = com_lib.str_to_milli_second_time()
        GetHeight_time = com_lib.get_duration(start_time, end_time)        
        com_lib.commit_step_result("API: Time taken by GetHeight API ", str(GetHeight_time))
        com_lib.log_info("Element Height : "+str(element_height))
        #GetWidth API
        start_time = com_lib.str_to_milli_second_time()
        element_width=com_lib.dut.GetWidth(com_lib.MobileScriptingLibrary.Constants.ElementType.XPath,xpath_element)
        end_time = com_lib.str_to_milli_second_time()
        GetWidth_time = com_lib.get_duration(start_time, end_time)
        com_lib.commit_step_result("API: Time taken by GetWidth API ", str(GetWidth_time))
        com_lib.log_info("Element Width : "+str(element_width))
        if(elementcount & element_height & element_width !=" "):            
            com_lib.commit_step_result("API: GetWidth API","Passed")
            com_lib.commit_step_result("API: GetHeight API","Passed")
            com_lib.commit_step_result("API: GetElementCount API","Passed")
            fn_return = True
    except Exception as e:
        com_lib.log_error("Exception raised in test_elementcount_height_width function : " + str(e))
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
            if not com_lib.dut.WaitForElement(com_lib.MobileScriptingLibrary.Constants.ElementType.XPath, element_id, 20):
                com_lib.log_error("App not launched")
            else:
                status = test_elementcount_height_width()
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
