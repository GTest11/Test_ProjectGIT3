# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :   M_API_04
# Author            :   Rohith P V
# Date              :   20-03-2018
# FE Version        :   5.0.9.4
# APIs covered      :   GetAdbAPIVersion, GetAdbVersion, GetApkVersion
# Description       :   GetAdbAPIVersion, GetAdbVersion, GetApkVersion API testing.
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
Function Name	  	: test_app_info()
Description		    : Function to test the GetAdbAPIVersion, GetAdbVersion, GetApkVersion API
Input arguments	    : Null
Output values		: String
``````````````````````````````````````````````````````````````````````````
"""


def test_app_info():
    try:
        fn_return = False
        # GetAdbAPIVersion API
        start_time = com_lib.str_to_milli_second_time()
        AdbAPIVersion = com_lib.dut.GetAdbAPIVersion()
        end_time = com_lib.str_to_milli_second_time()
        GetAdbAPIVersion_time = com_lib.get_duration(start_time, end_time)
        com_lib.commit_step_result(
            "API: Time taken by GetAdbAPIVersion API ",
            str(GetAdbAPIVersion_time))
        com_lib.log_info("GetAdbAPIVersion : " + str(AdbAPIVersion))
        # GetAdbVersion API
        start_time = com_lib.str_to_milli_second_time()
        AdbVersion = com_lib.dut.GetAdbVersion()
        end_time = com_lib.str_to_milli_second_time()
        GetAdbVersion_time = com_lib.get_duration(start_time, end_time)
        com_lib.commit_step_result(
            "API: Time taken by GetAdbVersion API ",
            str(GetAdbVersion_time))
        com_lib.log_info("GetAdbVersion : " + str(AdbVersion))
        # GetApkVersion API
        start_time = com_lib.str_to_milli_second_time()
        ApkVersion = com_lib.dut.GetApkVersion()
        end_time = com_lib.str_to_milli_second_time()
        GetApkVersion_time = com_lib.get_duration(start_time, end_time)
        com_lib.commit_step_result("API: Time taken by GetApkVersion API ",
                                   str(GetApkVersion_time))
        com_lib.log_info("GetApkVersion : " + str(ApkVersion))
        if(AdbAPIVersion != "") & (AdbVersion != "") & (ApkVersion != ""):
            com_lib.commit_step_result("API: GetAdbAPIVersion API", "Passed")
            com_lib.commit_step_result("API: GetAdbVersion API", "Passed")
            com_lib.commit_step_result("API: GetApkVersion API", "Passed")
            com_lib.commit_step_result(
                "API: Reason", "ApkVersion & AdbVersion returned expected values")
            fn_return = True
        else:
            com_lib.commit_step_result("API: GetAdbAPIVersion API", "Failed")
            com_lib.commit_step_result("API: GetAdbVersion API", "Failed")
            com_lib.commit_step_result("API: GetApkVersion API", "Failed")
            com_lib.commit_step_result(
                "API: Reason", "ApkVersion & AdbVersion returned empty string")
            fn_return = False
    except Exception as e:
        com_lib.log_error(
            "Exception raised in test_app_info function : " + str(e))
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
                if not com_lib.dut.WaitForElement(
                        com_lib.MobileScriptingLibrary.Constants.ElementType.XPath, element_id, 20):
                    com_lib.log_error("App not launched")
                else:
                    status = test_app_info()
            else:
                com_lib.commit_step_result(
                    "API: AppInfo.py is only for Android", "Skipped")

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
