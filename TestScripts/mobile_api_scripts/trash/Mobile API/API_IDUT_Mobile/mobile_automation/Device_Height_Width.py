# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :   M_API_04
# Author            :   Rohith P V
# Date              :   20-03-2018
# FE Version        :   5.0.9.4
# APIs covered      :   GetDeviceHeight, GetDeviceWidth
# Description       :   GetDeviceHeight, GetDeviceWidth API testing.
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
Function Name	  	: test_device_height_width()
Description		    : Function to test the GetDeviceHeight, GetDeviceWidth API
Input arguments	    : Null
Output values		: Int32
``````````````````````````````````````````````````````````````````````````
"""


def test_device_height_width():
    try:
        fn_return = False
        # GetDeviceHeight API
        start_time = com_lib.str_to_milli_second_time()
        DeviceHeight = com_lib.dut.GetDeviceHeight()
        end_time = com_lib.str_to_milli_second_time()
        GetDeviceHeight_time = com_lib.get_duration(start_time, end_time)
        com_lib.commit_step_result(
            "API: Time taken by GetDeviceHeight API ",
            str(GetDeviceHeight_time))
        com_lib.commit_step_result("API: GetDeviceHeight API", "Passed")
        com_lib.commit_step_result("Device Height : ", str(DeviceHeight))
        com_lib.log_info("GetDeviceHeight : " + str(DeviceHeight))
        # GetDeviceWidth API
        start_time = com_lib.str_to_milli_second_time()
        DeviceWidth = com_lib.dut.GetDeviceWidth()
        end_time = com_lib.str_to_milli_second_time()
        GetDeviceWidth_time = com_lib.get_duration(start_time, end_time)
        com_lib.commit_step_result(
            "API: Time taken by GetDeviceWidth API ",
            str(GetDeviceWidth_time))
        com_lib.commit_step_result("API: GetDeviceWidth API", "Passed")
        com_lib.log_info("GetDeviceWidth : " + str(DeviceWidth))
        # Provide device height and width according to the DUT
        if (((DeviceHeight == com_lib.constant.HEIGHT_ios) & (DeviceWidth == com_lib.constant.WIDTH_ios)) or
                ((DeviceHeight == com_lib.constant.HEIGHT_21435) & (DeviceWidth == com_lib.constant.WIDTH_21435))):
            fn_return = True

        else:
            fn_return = False

    except Exception as e:
        com_lib.log_error(
            "Exception raised in test_device_height_width function : " +
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
                status = test_device_height_width()
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
