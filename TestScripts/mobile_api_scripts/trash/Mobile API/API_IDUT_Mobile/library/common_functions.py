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

import mobile_config.coordinates as coordinate
import mobile_config.constants as constant
import mobile_config.android_config as android_conf
import mobile_config.ios_config as ios_conf

clr.AddReference("MobileScriptingLibrary")
import MobileScriptingLibrary
dut = MobileScriptingLibrary.MobileDUT()
logger = MobileScriptingLibrary.Logger()
scriptPath = os.path.realpath(__file__)
args = sys.argv
dut.Configure(args[1], args[2], args[3], args[4], scriptPath)
logger.Configure(args[1], args[2], args[3], args[4], scriptPath)
chkpt = MobileScriptingLibrary.CheckPoint()
config = MobileScriptingLibrary.DeviceConfig()
config.CreateNewServer="True"
config.UseNewWDA = True
#'''''''''''''''''''''''''END AUTO GENERATED CODE'''''''''''''''''''''''''''"""


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


def open_app():
    try:
        log_info("Opening the App under test")
        init_app_api_time = 0
        start_time = str_to_milli_second_time()
        if dut.InitApp(config):
            end_time = str_to_milli_second_time()
            init_app_api_time = get_duration(start_time, end_time)
            commit_step_result("API: InitApp", "PASSED")
            dut.validator.QuickCapture("OpenAPP_imageName")
        else:
            commit_step_result("API: InitApp", "FAILED")
            log_error("InitAPP API Failed.")
            dut.validator.QuickCapture("OpenAPP_imageName")
        commit_step_result("API: Time taken by InitApp API", str(init_app_api_time))
        return init_app_api_time
    except Exception as ex:
        log_error("Exception raised in open_app: " + str(ex))

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
        if dut.CloseApp():
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
        if dut.CloseApp():
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
        if dut.validator.DetectMotion(constant.Motion_AREA_x, constant.Motion_AREA_y,
                                      constant.Motion_AREA_w, constant.Motion_AREA_h,
                                      constant.WAIT_TIME, constant.WAIT_GAP, "15"):
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
        log_info("Duration calculated: " + str(duration))
        return duration
    except Exception as ex:
        log_error("Exception raised get_duration: " + str(ex))
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
        commit_step_result("DUT Platform :", str(dut_platform))
        return dut_platform
    except Exception as ex:
        log_error("Exception raised in get_dut_platform: " + str(ex))

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
Input arguments	    : config    : config = MobileScriptingLibrary.DeviceConfig()
                      platform  : device platform
Output values		: null
``````````````````````````````````````````````````````````````````````````
"""


def update_dut_config(platform):
    try:
        if platform == "iOS":
            log_info("Configuring the DUT - iOS for Automation")
            config.DeviceType = platform
            config.AppName = ios_conf.ios_app_name
            config.AppPackage = ios_conf.ios_app_package
            config.AppActivity = ios_conf.ios_app_activity
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
        log_info("****************************************************************")
        log_info("---------------Starting script Execution------------------------")
        log_info("Updating the Script details")
        commit_step_result("Build Number", str(constant.BUILD_NO))
        commit_step_result("DUT under test", str(dut.ReadProperty(1)))
        commit_step_result("DUT Platform", str(dut.ReadProperty(3)))
        commit_step_result("DUT Slot Number", str(dut.ReadProperty(10)))
        log_info("****************************************************************")
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
        if dut.Click(MobileScriptingLibrary.Constants.ElementType.XPath,
           android_conf.android_app_click, constant.youtube_search_index):
            commit_step_result("Click on Search", "PASSED")
            dut.SendKeys(MobileScriptingLibrary.Constants.ElementType.XPath,
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
        if dut.Click(MobileScriptingLibrary.Constants.ElementType.ClassName,
           ios_conf.nowtv_app_click, constant.nowtv_search_index):
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
        if dut.Click(MobileScriptingLibrary.Constants.ElementType.XPath,
           ios_conf.ios_app_click):
            commit_step_result("API: Click on Search", "PASSED")
            dut.SendKeys(MobileScriptingLibrary.Constants.ElementType.XPath,
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
def youtube_search():
    try:
        global fn_status
        fn_status=False
        if str(dut.ReadProperty(3)) == "Android":
            click_xpath = android_conf.ELEMENT_XPATH_CLICK_INDEX
            sendkeys_xpath= android_conf.ELEMENT_XPATH_SENDKEYS
        else:
            click_xpath = ios_conf.ELEMENT_XPATH_CLICK_INDEX
            sendkeys_xpath=ios_conf.ELEMENT_XPATH_SENDKEYS
        start_time = str_to_milli_second_time()
        if dut.Click(MobileScriptingLibrary.Constants.ElementType.XPath, click_xpath):
            end_time = str_to_milli_second_time()
            delay(constant.CLICK_DELAY)
            dut.validator.QuickCapture("Youtube_imageName")
            click_time = get_duration(start_time, end_time)
            commit_step_result("API: Click", "Passed")
            commit_step_result("API: Time taken by Click API", str(click_time))
            log_info("Click API Pressed")
            delay(constant.CLICK_DELAY)
            start_time = str_to_milli_second_time()
            if(dut.SendKeys(MobileScriptingLibrary.Constants.ElementType.XPath, sendkeys_xpath, constant.KEYS)):                
				end_time = str_to_milli_second_time()
				dut.validator.QuickCapture("Youtube_imageName")
				sendkeys_index_time = get_duration(start_time, end_time)
				commit_step_result("API: Time taken by SendKeys API ", str(sendkeys_index_time))
				commit_step_result("API: SendKeys API","Passed")
				log_info("SendKeys API Passed")
				fn_status=True

            else:
                commit_step_result("API: SendKeys API","Failed")
                log_info("SendKeys API Failed")

        else:
            log_info("Click API Failed")
            commit_step_result("API: Click API","Failed")
    except Exception as e:
        log_error("Exception raised in youtube_search function : " + str(e))
    finally:
        return fn_status


"""
``````````````````````````````````````````````````````````````````````````
Author   			: Rohith P V
Function Name	  	: tap_video
Description		    : Function to tap and play a video in youtube
Input arguments	    : null
Output values		: bool
``````````````````````````````````````````````````````````````````````````
"""
def tap_video():
    try:
        global fn_status
        fn_status=False
        if(dut.Tap(coordinate.TAP_X, coordinate.TAP_Y)):
            if validate_screen(constant.CHKPNT_TAP_SENDANDROIDKEYCODE_PRESSANDMOVE):
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

"""
``````````````````````````````````````````````````````````````````````````
Author   			: Rohith P V
Function Name	  	: youtube_launch_video
Description		    : Function to launch and play a video in youtube
Input arguments	    : null
Output values		: bool
``````````````````````````````````````````````````````````````````````````
"""
def youtube_launch_video():
    try:
        global fn_status
        fn_status=False
        if youtube_search():
            if str(dut.ReadProperty(3)) == "Android":
                start_time = str_to_milli_second_time()
                if dut.SendAndroidKeyCode(constant.KEYCODE_ENTER):
                    end_time = str_to_milli_second_time()
                    SendAndroidKeyCode_time = get_duration(start_time, end_time)
                    commit_step_result("API: Time taken by SendAndroidKeyCode API ", str(SendAndroidKeyCode_time))
                    delay(5)
                    if validate_screen(constant.CHKPNT_CLICK_INDEX):
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
                if dut.Click(MobileScriptingLibrary.Constants.ElementType.XPath, ios_conf.ELEMENT_XPATH_CLICK_ENTER):
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

