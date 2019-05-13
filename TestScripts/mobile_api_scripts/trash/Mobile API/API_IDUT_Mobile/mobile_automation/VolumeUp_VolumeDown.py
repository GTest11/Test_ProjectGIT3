# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :   M_API_15
# Author            :   Rohith P V
# Date              :   16-03-2018
# FE Version        :   5.0.9.4
# APIs covered      :   VolumeUp, VolumeDown

# Description       :   VolumeUp and VolumeDown API testing.
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
Function Name	  	: test_volumeup_volumedown()
Description		    : Function to test the HideKeyboard API
Input arguments	    : Null
Output values		: bool
``````````````````````````````````````````````````````````````````````````
"""


def test_volumeup_volumedown():
    try:
        fn_return = False
        #VolumeUp API
        fn_return_volumeup = False
        start_time = com_lib.str_to_milli_second_time()
        if com_lib.dut.VolumeUp(com_lib.constant.VOLUMEUP_LEVEL):
            end_time = com_lib.str_to_milli_second_time()
            VolumeUp_time = com_lib.get_duration(start_time, end_time)
            com_lib.commit_step_result("API: Time taken by VolumeUp API ", str(VolumeUp_time))    
        # To validate the VolumeUp Level
            if(com_lib.validate_screen(com_lib.constant.CHKPNT_VOLUMEUP)):
                com_lib.commit_step_result("API: VolumeUp", "Passed")
                com_lib.commit_step_result("API: Reason", "Volume increased, confirmed by chkpt validation")
                com_lib.log_info("Volume level increased by level 1")
                fn_return_volumeup = True
            else:
                com_lib.log_info("VolumeUp API failed")                
                com_lib.commit_step_result("API: VolumeUp API", "Failed")
                com_lib.commit_step_result("API: Reason", "Volume not changed, confirmed by chkpt validation")
        else:
            end_time = com_lib.str_to_milli_second_time()
            VolumeUp_time = com_lib.get_duration(start_time, end_time)
            com_lib.commit_step_result("API: Time taken by VolumeUp API ", str(VolumeUp_time)) 
            com_lib.log_info("VolumeUp API failed")
            com_lib.commit_step_result("API: VolumeUp API", "Failed")
            com_lib.commit_step_result("API: Reason", "API returned False")

        #VolumeDown API
        fn_return_volumedown = False
        start_time = com_lib.str_to_milli_second_time()
        if com_lib.dut.VolumeDown(com_lib.constant.VOLUMEDOWN_LEVEL):
            end_time = com_lib.str_to_milli_second_time()
            VolumeDown_time = com_lib.get_duration(start_time, end_time)
            com_lib.commit_step_result("API: Time taken by VolumeUp API ", str(VolumeDown_time))
            # To validate the VolumeDown Level
            if(com_lib.validate_screen(com_lib.constant.CHKPNT_VOLUMEDOWN)):
                com_lib.commit_step_result("API: VolumeDown API", "Passed")
                com_lib.commit_step_result("API: Reason", "Volume decreased, confirmed by chkpt validation")
                com_lib.log_info("Volume level decreased by level 1")
                fn_return_volumedown = True
            else:
                com_lib.log_info("VolumeDown API failed")
                com_lib.commit_step_result("API: VolumeDown API", "Failed")
                com_lib.commit_step_result("API: Reason", "Volume not changed, confirmed by chkpt validation")            
        else:
            end_time = com_lib.str_to_milli_second_time()
            VolumeDown_time = com_lib.get_duration(start_time, end_time)
            com_lib.commit_step_result("API: Time taken by VolumeDown API ", str(VolumeDown_time))
            com_lib.log_info("VolumeDown API failed")
            com_lib.commit_step_result("API: VolumeDown API", "Failed")
            com_lib.commit_step_result("API: Reason", "API returned False")

    except Exception as e:
        com_lib.log_error(
            "Exception raised in test_volumeup_volumedown function : " +
            str(e))
    finally:
        fn_return=fn_return_volumeup & fn_return_volumedown
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
                status = test_volumeup_volumedown()
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
