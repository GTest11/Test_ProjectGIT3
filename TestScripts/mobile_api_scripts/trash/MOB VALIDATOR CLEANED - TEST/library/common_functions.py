#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author          :   Arathy P S
# Date            :   08-03-2018
# FE Version      :   5.0.9.4
# Description     :   This is a Library for commonly used methods in FE
#''''''''''''''''''''AUTO GENERATED CODE - DO NOT MODIFY''''''''''''''''''''


import clr
import sys
sys.path.append('../')
import os
import datetime
import time
from PIL import Image
import urllib
import cStringIO
from collections import OrderedDict

import mobile_config.coordinates as coordinate
import mobile_config.constants as constants
import mobile_config.android_config as android_conf
import mobile_config.ios_config as ios_conf

clr.AddReference("MobileScriptingLibrary")
import MobileScriptingLibrary as msl
dut = msl.MobileDUT()
logger = msl.Logger()
scriptPath = os.path.realpath(__file__)
args = sys.argv
dut.Configure(args[1], args[2], args[3], args[4], scriptPath)
logger.Configure(args[1], args[2], args[3], args[4], scriptPath)
chkpt = msl.CheckPoint()
device_config = msl.DeviceConfig()
device_config.CreateNewServer="True"
device_config.UseNewWDA = True

#'''''''''''''''''''''''''END AUTO GENERATED CODE'''''''''''''''''''''''''''"""


"""
``````````````````````````````````````````````````````````````````````````
Author   			: Arathy P S
Function Name	  	: get_dut_platform
Description		    : Function to get the DUT platform (android/iOS)
Input arguments	    : null
Output values		: dut_platform  :  return the dut platform.
                      possible values are Android and iOS
``````````````````````````````````````````````````````````````````````````
"""


def get_dut_platform():
    try:
        dut_platform = dut.ReadProperty(3)
        return dut_platform
    except Exception as ex:
        logger.Error("Exception raised in get_dut_platform: " + str(ex))
        return None


# platform = get_dut_platform()
# config = None

"""
``````````````````````````````````````````````````````````````````````````
Author   			: Arathy P S
Function Name	  	: validate_screen(check_pnt_name)
Description		    : Function to validate checkpoints
Input arguments	    : check_pnt_name    :   checkpoint to be validated
Output values		: validation_time   :   time to complete validation in milli sec
``````````````````````````````````````````````````````````````````````````
"""


def validate_screen(check_pnt_name):
    try:
        chkpt.init(check_pnt_name)  # checkpoint initialization
        log_info("Checkpoint validation started")
        commit_step_result("Validation of " + str(check_pnt_name), "Started")
        chkpt.init(check_pnt_name)
        start_time = str_to_milli_second_time()
        if dut.validator.validateCheckPoint(chkpt):
            end_time = str_to_milli_second_time()
            validation_api_time = get_duration(start_time, end_time)
            commit_step_result("Time for Validation", str(validation_api_time))
            log_info("Screen validation completed successfully. Expected screen launched")
            commit_step_result(check_pnt_name, "Validation Success")
            return True
        else:
            end_time = str_to_milli_second_time()
            validation_api_time = get_duration(start_time, end_time)
            commit_step_result("Time for Validation", str(validation_api_time))
            log_warn("Screen validation completed successfully. Expected screen not launched")
            commit_step_result(check_pnt_name, "Validation Failed")
            return False
    except Exception as ex:
        log_error("Exception raised in validate_screen: " + str(ex))
"""
``````````````````````````````````````````````````````````````````````````
Author   			: Arathy P S
Function Name	  	: open_app(mobile_config)
Description		    : Function to start the Appium server and also initialise the driver
                      which in-turn will launch the application.
Input arguments	    : mobile_config     :   FE config object
Output values		: init_app_time     :   the time taken to complete initApp API call
``````````````````````````````````````````````````````````````````````````
"""


def init_app():
    try:
        app_init = False
        log_info("Opening the App under test")
        start_time = gettimestamp()
        if dut.InitApp(device_config):
            end_time = gettimestamp()
            commit_step_result("API: InitApp", "PASSED")
            dut.validator.QuickCapture("OpenAPP_imageName")
            app_init = True
        else:
            end_time = gettimestamp()
            commit_step_result("API: InitApp", "FAILED")
            log_error("InitAPP API Failed.")
            dut.validator.QuickCapture("OpenAPP_imageName")
        init_app_api_time = getAPIduration(start_time, end_time)
        commit_step_result("API: Time taken by InitApp API", str(init_app_api_time))
        return app_init
    except Exception as ex:
        log_error("Exception raised in open_app: " + str(ex))
    finally:
        pass
        # return app_init

"""
``````````````````````````````````````````````````````````````````````````
Author   			: Arathy P S
Function Name	  	: open_app_with_validation(mobile_config, check_pnt_name)
Description		    : Function to start the Appium server and also initialise the driver
                      which in-turn will launch the application.
Input arguments	    : mobile_config     :   FE config object
                      check_pnt_name    :   checkpoint name
Output values		: init_app_time     :   the time taken to complete initApp API call
``````````````````````````````````````````````````````````````````````````
"""


def open_app_with_validation(mobile_config, check_pnt_name):
    try:
        init_app_api_time = 0
        start_time = str_to_milli_second_time()
        if dut.InitApp(mobile_config):
            commit_step_result("API: InitApp API", "PASSED")
            end_time = str_to_milli_second_time()
            if validate_screen(check_pnt_name):
                init_app_api_time = get_duration(start_time, end_time)
                log_info("Application launched successfully")
            else:
                log_info("Application launch failed")
        else:
            commit_step_result("API: InitApp", "FAILED")
            log_error("InitAPP API Failed.")
        return init_app_api_time
    except Exception as ex:
        log_error("Exception raised in open_app_with_validation: " + str(ex))

"""
``````````````````````````````````````````````````````````````````````````
Author   			: Arathy P S
Function Name	  	: str_to_milli_second_time
Description		    : Function to calculate time in milli seconds
Input arguments	    : null
Output values		: return time in milli seconds
``````````````````````````````````````````````````````````````````````````
"""


def str_to_milli_second_time():
    try:
        time_in_str = datetime.datetime.now().strftime("%H:%M:%S.%f")
        hours, minutes, seconds = (["0", "0"] + time_in_str.split(":"))[-3:]
        hours = int(hours)
        minutes = int(minutes)
        seconds = float(seconds)
        milli_seconds = int(3600000 * hours + 60000 * minutes + 1000 * seconds)
        return milli_seconds
    except Exception as ex:
        log_error("Exception raised in str_to_milli_second_time: " + str(ex))

"""
``````````````````````````````````````````````````````````````````````````

Author   			: Arathy P S
Function Name	  	: wait_for_checkpoint
Description		    : Function to calculate time of the first frame matching
Input arguments	    : check_pnt_name    :   Checkpoint screen name
                      time_to_wait      :   Time until which the function has to wait before returning
                      initial_delay     :   Time in seconds to wait before frame comparison starts.
Output values		: wait_time         :   wait time in seconds

``````````````````````````````````````````````````````````````````````````
"""


def wait_for_checkpoint(check_pnt_name, time_to_wait, initial_delay):
    try:
        fn_status=False
        wait_time = 0
        dut.validator.StopCaptureZapFrames()
        if dut.validator.StartCaptureZapFrames(10):
            commit_step_result("API: StartCaptureZapFrames", "PASSED")
            wait_time = dut.validator.WaitForCheckpoint(check_pnt_name, time_to_wait, initial_delay)
            if wait_time > 0:
                log_info("Wait time obtained by calling WaitForCheckpoint:" + str(wait_time))
                commit_step_result("WaitForCheckpoint time", str(wait_time))
                fn_status=True
            else:
                log_warn("Unable to obtain checkpoint match")
        else:
            commit_step_result("API: StartCaptureZapFrames", "FAILED")
            log_info("Unable to start frame capture")
        #return fn_status
    except Exception as ex:
        log_error("Exception raised in wait_for_checkpoint : " + str(ex))
    finally:
        return fn_status
        dut.validator.StopCaptureZapFrames()

"""
``````````````````````````````````````````````````````````````````````````
Author   			: Arathy P S
Function Name	  	: close_app_with_validation
Description		    : Function to close an application and confirm the working
Input arguments	    : check_pnt_name:   checkpoint to validate
Output values		: boolean       :   return true if app closed else false
``````````````````````````````````````````````````````````````````````````
"""


def close_app_with_validation(check_pnt_name):
    try:
        start_time = str_to_milli_second_time()
        if dut.CloseApp:
            end_time = str_to_milli_second_time()
            close_app_api_time = get_duration(start_time, end_time)
            commit_step_result("API: Time taken by CloseApp API", str(close_app_api_time))
            app_close_result = validate_screen(check_pnt_name)
            if app_close_result:
                log_info("Application closed successfully")
                commit_step_result("API: CloseAPP API", "PASSED")
                return True
            else:
                commit_step_result("API: CloseAPP API", "APP NOT CLOSED")
                log_warn("CloseApp API return success but Application is not closed. please re-run the script")
                return False
        else:
            log_error("CloseApp API is not working.")
            commit_step_result("API: CloseApp API", "FAILED")
            return False
    except Exception as ex:
        log_error("Exception raised in close_app_with_validation: " + str(ex))

"""
``````````````````````````````````````````````````````````````````````````
Author   			: Arathy P S
Function Name	  	: close_app
Description		    : Function to close an application
Input arguments	    : null
Output values		: null
``````````````````````````````````````````````````````````````````````````
"""


def close_app():
    try:
        start_time = str_to_milli_second_time()
        if dut.CloseApp:
            end_time = str_to_milli_second_time()
            close_app_api_time = get_duration(start_time, end_time)
            commit_step_result("API: CloseApp API", "PASSED")
            commit_step_result("API: Time taken by CloseApp API", str(close_app_api_time))
        else:
            log_error("CloseApp API is not working.")
            commit_step_result("API: CloseApp API", "FAILED")
    except Exception as ex:
        log_error("Exception raised in close_app: " + str(ex))

"""
``````````````````````````````````````````````````````````````````````````
Author   			: Arathy P S
Function Name	  	: stop_driver
Description		    : Function to stop Appium driver
Input arguments	    : null
Output values		: null
``````````````````````````````````````````````````````````````````````````
"""


def stop_driver():
    try:
        start_time = str_to_milli_second_time()
        dut.Stop()
        end_time = str_to_milli_second_time()
        stop_time = get_duration(start_time, end_time)
        commit_step_result("API: Time taken by Stop API", str(stop_time))
    except Exception as ex:
        log_error("Exception raised in stop_driver : " + str(ex))

"""
``````````````````````````````````````````````````````````````````````````
Author   			: Arathy P S
Function Name	  	: motion_detection
Description		    : Function to detect motion in a specific region
Input arguments	    : Null
Output values		: boolean    :   return true if motion detected else false
``````````````````````````````````````````````````````````````````````````
"""


def motion_detection():
    try:
        commit_step_result("Motion Detection", "STARTED")
        start_time = str_to_milli_second_time()
        if dut.validator.DetectMotion(constants.Motion_AREA_x, constants.Motion_AREA_y,
                                      constants.Motion_AREA_w, constants.Motion_AREA_h,
                                      constants.WAIT_TIME, constants.WAIT_GAP, "15"):
            end_time = str_to_milli_second_time()
            log_info("test")
            detect_motion_api_time = get_duration(start_time, end_time)
            commit_step_result("API: Time taken by DetectMotion API", str(detect_motion_api_time))
            commit_step_result("API: Motion Detection", "PASSED")
            return True
        else:
            commit_step_result("API: Motion Detection", "FAILED")
            return False
    except Exception as ex:
        log_error("Exception raised in motion_detection: " + str(ex))
"""
``````````````````````````````````````````````````````````````````````````
Author   			: Arathy P S
Function Name	  	: get_image_resolution
Description		    : Function to get the image resolution
Input arguments	    : null
Output values		: boolean   :   return the image resolution
``````````````````````````````````````````````````````````````````````````
"""


def get_image_resolution():
    try:
        image_url = dut.validator.QuickCapture("get_image_resolution")
        file_name = cStringIO.StringIO(urllib.urlopen(image_url).read())
        img = Image.open(file_name)
        return img.size
    except Exception as ex:
        log_error("Exception raised in get_image_resolution: " + str(ex))
"""
``````````````````````````````````````````````````````````````````````````
Author   			: Arathy P S
Function Name	  	: delay
Description		    : Function to put some delay in seconds
Input arguments	    : delay_in_sec  :  delay in seconds
Output values		: boolean       :  null
``````````````````````````````````````````````````````````````````````````
"""


def delay(delay_in_sec):
    try:
        delay_str = str(delay_in_sec)
        log_info("Introducing delay of " + delay_str + "seconds")
        time.sleep(delay_in_sec)
    except Exception as ex:
        log_error("Exception raised in delay: " + str(ex))
"""
``````````````````````````````````````````````````````````````````````````
Author   			: Arathy P S
Function Name	  	: get_duration
Description		    : Function to calculate time difference
Input arguments	    : start_time  :  time in seconds
                      end_time    :  time in seconds
Output values		: duration    :  difference between end_time & start_time
``````````````````````````````````````````````````````````````````````````
"""


def get_duration(start_time, end_time):
    try:
        duration = round(((end_time - start_time) / 1000.0), 3)
        # log_info("Duration calculated: " + str(duration))
        return duration
    except Exception as ex:
        log_error("Exception raised get_duration: " + str(ex))



def set_config(app="youtube"):
    config = None
    platform = get_dut_platform()
    if platform not in ["Android", "iOS"]:
        logger.Log("Wrong Platform")
        return False

    if platform == "Android":
        config = android_conf
        device_config.AppPackage = config.package[app]
    if platform == "iOS":
        config = ios_conf
        device_config.AppName = config.app_name[app]

    device_config.DeviceType = platform
    device_config.AppActivity = config.activity[app]


    return config

"""
``````````````````````````````````````````````````````````````````````````
Author   			: Arathy P S
Function Name	  	: get_dut_details
Description		    : Function to get the DUT platform (android/iOS)
Input arguments	    : null
Output values		: dut_details  :  return a list with dut details.
                      possible values are  MobileDUT_ID, MobileDUT_NAME,
                      MobileDUT_TYPE, MobileDUT_PLATFORMNAME, MobileDUT_PLATFORMVERSION,
                      MobileDUT_BROWSERNAME, MobileDUT_UDID, MobileDUT_MANUFACTURER,
                      MobileDUT_MODELDESCRIPTION, MobileDUT_RACKNO,MobileDUT_SLOTNO,
                      MobileDUT_LOCKEDUSER, MobileDUT_SLOTSTATE
``````````````````````````````````````````````````````````````````````````
"""


def get_dut_details():
    try:
        dut_id = dut.ReadProperty(0)
        dut_name = dut.ReadProperty(1)
        dut_type = dut.ReadProperty(2)
        dut_platform_name = dut.ReadProperty(3)
        dut_platform_ver = dut.ReadProperty(4)
        dut_browser = dut.ReadProperty(5)
        dut_udid = dut.ReadProperty(6)
        dut_manufacturer = dut.ReadProperty(7)
        dut_description = dut.ReadProperty(8)
        dut_rack_no = dut.ReadProperty(9)
        dut_slot_no = dut.ReadProperty(10)
        dut_locked_user = dut.ReadProperty(11)
        dut_slot_state = dut.ReadProperty(12)
        dut_details = [dut_id, dut_name, dut_type, dut_platform_name, dut_platform_ver,
                       dut_browser, dut_udid, dut_manufacturer, dut_description, dut_rack_no,
                       dut_slot_no, dut_locked_user, dut_slot_state]
        return dut_details
    except Exception as ex:
        log_error("Exception raised in get_dut_details : " + str(ex))
"""
``````````````````````````````````````````````````````````````````````````
Author   			: Arathy P S
Function Name	  	: update_dut_config
Description		    : Function to configure the DUT for automation
Input arguments	    : config    : config = msl.DeviceConfig()
                      platform  : device platform
Output values		: null
``````````````````````````````````````````````````````````````````````````
"""


def update_dut_config(platform):
    try:
        if platform == "iOS":
            log_info("Configuring the DUT - iOS for Automation")
            device_config.DeviceType = platform
            device_config.AppName = ios_conf.ios_app_name
            device_config.AppPackage = ios_conf.ios_app_package
            device_config.AppActivity = ios_conf.ios_app_activity
        elif platform == "Android":
            log_info("Configuring the DUT - Android for Automation")
            config.DeviceType = platform
            config.AppPackage = android_conf.android_app_package
            config.AppActivity = android_conf.android_app_activity
        log_info(platform + "  configuration completed successfully")
    except Exception as ex:
        log_error("Exception raised in update_dut_config: " + str(ex))


"""
``````````````````````````````````````````````````````````````````````````
Author   			: Arathy P S
Function Name	  	: log_info(message)
Description		    : Function to log Info messages to execution log
Input arguments	    : message   :   log message
Output values		: Null
``````````````````````````````````````````````````````````````````````````
"""


def log_info(message):
    logger.Log(message)


"""
``````````````````````````````````````````````````````````````````````````
Author   			: Arathy P S
Function Name	  	: log_error(message)
Description		    : Function to log Error messages to execution log
Input arguments	    : message   :   error message
Output values		: Null
``````````````````````````````````````````````````````````````````````````
"""


def log_error(message):
    logger.Error(message)


"""
``````````````````````````````````````````````````````````````````````````
Author			    : Arathy P S
Function Name	  	: log_warn(message)
Description		    : Function to log Warning messages to execution log
Input arguments	    : message   :   warn message
Output values		: Null
``````````````````````````````````````````````````````````````````````````
"""


def log_warn(message):
    logger.Warn(message)


"""
``````````````````````````````````````````````````````````````````````````
Author			    : Arathy P S
Function Name	  	: CommitScriptResult(status)
Description		    : Function to commit final test result
Input arguments	    : Script final result (pass/fail/error)
Output values		: Null
``````````````````````````````````````````````````````````````````````````
"""


def CommitScriptResult(status):
    try:
        if status is True:
            log_info("Test Execution Passed")
            dut.CommitTestResult("PASSED")
        elif status is False:
            log_warn("Test Execution Failed")
            dut.CommitTestResult("FAILED")
        else:
            dut.CommitTestResult("ERROR")
    except Exception as e:
        dut.CommitTestResult("ABORT")
        log_error("Exception in CommitScriptResult: " + str(e))

"""
``````````````````````````````````````````````````````````````````````````
Author			    : Arathy P S
Function Name	  	: commit_step_result(message, step_value)
Description		    : Function to commit test step result
Input arguments	    : message    :  message to be committed
                      step_value :  Step value to be committed
Output values		: Null
``````````````````````````````````````````````````````````````````````````
"""


def commit_step_result(message, step_value):
    log_info("Committing step Result")
    dut.CommitStepResult(message, step_value)

"""
``````````````````````````````````````````````````````````````````````````
Author   			: Arathy P S
Function Name	  	: update_TC_details
Description		    : Function to update the Test case details
Input arguments	    : null
Output values		: null
``````````````````````````````````````````````````````````````````````````
"""


def update_tc_details():
    try:
        log_info("--------------- Starting script Execution ------------------------")
        log_info("Updating the Script details")
        commit_step_result("Build Number", str(constants.BUILD_NO))
        # dev_dict = OrderedDict()
        dev_dict = OrderedDict(constants.DEVICE_DETAILS)
        for key, value in dev_dict.items():
            commit_step_result(key, str(dut.ReadProperty(value)))


    except Exception as ex:
        log_error("Exception raised in update_tc_details: " + str(ex))
"""
``````````````````````````````````````````````````````````````````````````
Author   			: Arathy P S
Function Name	  	: youtube_search_click_type
Description		    : Function to click on search and send search key word
Input arguments	    : null
Output values		: null
``````````````````````````````````````````````````````````````````````````
"""


def youtube_search_click_type_android():
    try:
        if dut.Click(msl.Constants.ElementType.XPath,
           android_conf.android_app_click, constants.youtube_search_index):
            commit_step_result("Click on Search", "PASSED")
            dut.SendKeys(msl.Constants.ElementType.XPath,
            android_conf.android_app_sendkeys, "MasterChef Australia")
            time.sleep(3)
            if dut.SendAndroidKeyCode("Keycode_ENTER"):
                time.sleep(3)
                log_info("Video started.")
            dut.validator.QuickCapture("Youtube_imageName")
        else:
            log_warn("Click failed")
    except Exception as ex:
        log_error("Exception raised in youtube_search_click_type_android: " + str(ex))
        """
``````````````````````````````````````````````````````````````````````````
Author   			: Arathy P S
Function Name	  	: nowtv_launch_video
Description		    : Function to click on search and send search key word
Input arguments	    : null
Output values		: null
``````````````````````````````````````````````````````````````````````````
"""

'''
def nowtv_launch_video():
    try:
        if dut.Click(msl.Constants.ElementType.ClassName,
           ios_conf.nowtv_app_click, constants.nowtv_search_index):
            commit_step_result("Click on Search", "PASSED")
            time.sleep(3)
            dut.validator.QuickCapture("Youtube_imageName")
        else:
            log_warn("Click failed")
    except Exception as ex:
        log_error("Exception raised in nowtv_launch_video: " + str(ex))
'''

def youtube_search_click_type_iOS():
    try:
        if dut.Click(msl.Constants.ElementType.XPath,
           ios_conf.ios_app_click):
            commit_step_result("API: Click on Search", "PASSED")
            dut.SendKeys(msl.Constants.ElementType.XPath,
            ios_conf.ios_app_sendkeys, "MasterChef Australia")
            time.sleep(3)
            if dut.Tap(coordinate.IOS_TAP_X, coordinate.IOS_TAP_Y):
                time.sleep(20)
                log_info("Video started.")
            dut.validator.QuickCapture("Youtube_imageName")
        else:
            log_warn("Click failed")
    except Exception as ex:
        log_error("Exception raised in youtube_search_click_type_iOS: " + str(ex))

"""
``````````````````````````````````````````````````````````````````````````
Author   			: Rohith P V
Function Name	  	: youtube_search
Description		    : Function to search in youtube
Input arguments	    : null
Output values		: bool
``````````````````````````````````````````````````````````````````````````
"""
def search_in_youtube(config):
    searched = False
    try:
        start_time = gettimestamp()
        clicked = dut.Click(msl.Constants.ElementType.XPath, config.X_CLICK_INDEX)
        end_time = gettimestamp()
        if clicked:
            status = "PASSED"
        else:
            status = "FAILED"
        report_elapsed_time(start_time, end_time, "clicked", status)
        report("API: Click API", status, image_required=True)
        if not clicked:
            return False

        log_info("Clicked on the given element")
        start_time = gettimestamp()
        keys_sent = dut.SendKeys(msl.Constants.ElementType.XPath, config.X_SENDKEYS_EDIT_BOX, constants.KEYS)
        end_time = gettimestamp()
        if keys_sent:
            status = "PASSED"
        else:
            status = "FAILED"
        report_elapsed_time(start_time, end_time, "SendKeys", status)
        report("SendKeys API", status, image_required=True)
        if not keys_sent:
            return False

        searched = True
    except Exception as e:
        log_error("Exception raised in search_in_youtube function : " + str(e))
    finally:
        return searched


# ``````````````````````````````````````````````````````````````````````````
# Author   			: Rohith P V
# Function Name	  	: tap_video
# Description		    : Function to tap and play a video in youtube
# Input arguments	    : null
# Output values		: bool
# ``````````````````````````````````````````````````````````````````````````
def tap_video():
    try:
        global fn_status
        fn_status=False
        if(dut.Tap(coordinate.TAP_X, coordinate.TAP_Y)):
            if validate_screen(constants.CHKPNT_TAP_SENDANDROIDKEYCODE_PRESSANDMOVE):
                commit_step_result("API: Tap API","Passed")
                log_info("Tap API Passed")
                fn_status = True
            else:
                log_info("Tapping failed")
                commit_step_result("API: Tap API", "Failed")
        else:
            log_info("Tapping failed")
            commit_step_result("API: Tap API", "Failed")
    except Exception as e:
        log_error("Exception raised in tap_video function : " + str(e))
    finally:
        return fn_status


# ``````````````````````````````````````````````````````````````````````````
# Author   			: Rohith P V
# Function Name	  	: youtube_launch_video
# Description		    : Function to launch and play a video in youtube
# Input arguments	    : null
# Output values		: bool
# ``````````````````````````````````````````````````````````````````````````
def youtube_launch_video():
    try:
        global fn_status
        fn_status=False
        if search_in_youtube():
            if str(dut.ReadProperty(3)) == "Android":
                start_time = str_to_milli_second_time()
                if dut.SendAndroidKeyCode(constants.KEYCODE_ENTER):
                    end_time = str_to_milli_second_time()
                    SendAndroidKeyCode_time = get_duration(start_time, end_time)
                    commit_step_result("API: Time taken by SendAndroidKeyCode API ", str(SendAndroidKeyCode_time))
                    delay(5)
                    if validate_screen(constants.CHKPNT_CLICK_INDEX):
                        commit_step_result("API: SendAndroidKeyCode API","Passed")
                        log_info("SendAndroidKeyCode API Passed")
                        if tap_video():
                            log_info("Video started")
                            fn_status=True
                        else:
                            log_info("Video not started")
                            commit_step_result("tap_video function","Failed")
                    else:
                        commit_step_result("API: SendAndroidKeyCode API","Failed")
                        log_info("SendAndroidKeyCode API Failed")
                else:
                    commit_step_result("API: SendAndroidKeyCode API","Failed")
                    log_info("SendAndroidKeyCode API Failed")
            else:
                if dut.Click(msl.Constants.ElementType.XPath, ios_conf.ELEMENT_XPATH_CLICK_ENTER):
                    if tap_video():
                        log_info("Video started")
                        fn_status=True
                    else:
                        log_info("Video not started")
                        commit_step_result("tap_video function","Failed")
                else:
                    log_info("Click Failed")
                    commit_step_result("API: Click API","Failed")
        else:
            log_info("youtube_search function failed")
            commit_step_result("youtube_search function", "Failed")
    except Exception as e:
        log_error("Exception raised in youtube_launch_video function : " + str(e))
    finally:
        return fn_status

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#@Function Name	  	: getTimestamp()
#@Description		: Function to get the current time in ("%H:%M:%S.%f")
#@Input arguments	: Null
#@Output values		: miliseconds- time in milliseconds
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def gettimestamp():
    '''
    :return:
    '''
    timestamp = datetime.datetime.now().strftime("%H:%M:%S.%f")
    return strtomillisecond(timestamp)


#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#@Function Name	  	: strtomillisecond()
#@Description		: Function to convert the time to miliseconds
#@Input arguments	: timeinstr- timestamp to be coverted to milliseconds
#@Output values		: miliseconds- time in milliseconds
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def strtomillisecond(timeinstr):
    hours, minutes, seconds = (["0", "0"] + timeinstr.split(":"))[-3:]
    hours = int(hours)
    minutes = int(minutes)
    seconds = float(seconds)
    milliseconds = int(3600000 * hours + 60000 * minutes + 1000 * seconds)
    return milliseconds

#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#@Function Name	  	: getAPIduration()
#@Description		: Takes initial and final times in milliseconds and finds
#the difference as duration
#@Input arguments	: t1, t2- nitial and final times in milliseconds
#@Output values		: duration in miliseconds
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def getAPIduration(t1, t2):
    duration = round(((t2 - t1) / 1000.0), 3)
    logger.Log("Duration calculated: "+str(duration))
    return duration


def report(message, status, image_required = False):
    if image_required:
        timestamp = datetime.datetime.now().strftime("%H:%M:%S.%f")
        timestamp = timestamp.replace(":", "_")
        timestamp = timestamp.replace(".", "_")
        image_name = "img_{}".format(timestamp)
        dut.validator.QuickCapture(image_name)
    dut.CommitStepResult(message, status)
    logger.Log("{} : {}".format(message, status))

def log_duration(api_name, duration):
    pass


def stop_run():
    close_app()
    stop_driver()


def start_run(elm_type=msl.Constants.ElementType.XPath, home=None):
    # com_lib.update_tc_details()
    ready = False
    # log_script_data()
    try:
        if init_app():
            logger.Log("1111")
            time.sleep(10)
            # ready = dut.WaitForElement(elm_type, home, 50)
            ready = dut.IsElementPresent(elm_type, home)
            logger.Log("2222")
            if not ready:
                log_error("App not launched")
                report("Initialize run", "FAILED")
            else:
                log_info("App launched")
                report("Initialize run", "PASSED")
            # return ready
        else:
            logger.Log("3333")
            report("Failed to initialize", "FAILED", image_required=True)
            # return ready

    except Exception as e:
        logger.Log("Exception from start_run() - {}".format(e))
        ready = False
    finally:
        return ready


def report_elapsed_time(t1, t2, api, status):
    time_taken = getAPIduration(t1, t2)
    report("API: Time Time taken by {} API :  {}".format(api, str(time_taken)), status)
