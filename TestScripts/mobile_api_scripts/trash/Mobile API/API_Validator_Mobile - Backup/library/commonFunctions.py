#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#TestScript ID  : FE_STB_API_Commonfunctions
#TestCase ID    :
#Description    :
#Author         : Arya L
#Date           : 14 March 2018, 22 March 2018
#Script Version : 2.0
#''''''''''''''''''''AUTOGENERATED CODE - DO NOT MODIFY''''''''''''''''''''
import clr
import sys
sys.path.append('../')
import os
import datetime
import time
from PIL import Image
import urllib
import cStringIO

import configuration.constants as constant
import configuration.android_config as android_conf
import configuration.ios_config as ios_conf

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
config.CreateNewServer = "true"

#''''''''''''''''''''''''''''''''IMPORTS''''''''''''''''''''''''''''''''''

#importing user defined modules
sys.path.append('../')
try:
    from configuration.config import homeKey, screenKeyRegionMapping
except ImportError:
    logger.Log("Failed to import config file")
    sys.exit()

try:
    from configuration.constants import DEFAULT_KEY_FIRE_TIME_OUT
except ImportError:
    logger.Log("Failed to import constants file")
    sys.exit()
#''''''''''''''''''''''''''''''END IMPORTS''''''''''''''''''''''''''''''''

#'''''''''''''''''''''''''END AUTOGENERATED CODE'''''''''''''''''''''''''''
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Use defined variables and functions
testStatus = True

#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#@Function Name	  	: preCondition()
#@Description		: Function to press the home Key
#@Input arguments	: Null
#@Output values		: Null
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def preCondition():
    #dut.controller.sendCommand(homeKey)    
    pass

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
            time.sleep(15)
            end_time = str_to_milli_second_time()
            init_app_api_time = get_duration(start_time, end_time)
            commit_step_result("InitApp API", "PASSED")
            dut.validator.QuickCapture("OpenAPP_imageName")
        else:
            commit_step_result("InitApp", "FAILED")
            logger.Log("InitAPP API Failed.")
            dut.validator.QuickCapture("OpenAPP_imageName")
        commit_step_result("Time taken by InitApp API", str(init_app_api_time))
        return init_app_api_time
    except Exception as ex:
        logger.Log("Exception raised in open_app: " + str(ex))


def close_app():
    try:
        start_time = str_to_milli_second_time()
        if dut.CloseApp():
            end_time = str_to_milli_second_time()
            close_app_api_time = get_duration(start_time, end_time)
            commit_step_result("CloseApp API", "PASSED")
            commit_step_result("Time taken by CloseApp API", str(close_app_api_time))
        else:
            logger.Log("CloseApp API is not working.")
            commit_step_result("CloseApp API", "FAILED")
    except Exception as ex:
        logger.Log("Exception raised in close_app: " + str(ex))


def stop_driver():
    try:
        start_time = str_to_milli_second_time()
        dut.Stop()
        end_time = str_to_milli_second_time()
        stop_time = get_duration(start_time, end_time)
        commit_step_result("Time taken by Stop API", str(stop_time))
    except Exception as ex:
        logger.Log("Exception raised in stop_driver : " + str(ex))


def get_dut_platform():
    try:
        dut_platform = dut.ReadProperty(3)
        commit_step_result("DUT Platform :", str(dut_platform))
        return dut_platform
    except Exception as ex:
        logger.Log("Exception raised in get_dut_platform: " + str(ex))


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
        logger.Log("Exception raised in update_dut_config: " + str(ex))


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
        logger.Log("Exception raised in str_to_milli_second_time: " + str(ex))


def commit_step_result(message, step_value):
    log_info("Committing step Result")
    dut.CommitStepResult(message, step_value)


def log_info(message):
    logger.Log(message)


def get_duration(start_time, end_time):
    try:
        duration = round(((end_time - start_time) / 1000.0), 3)
        log_info("Duration calculated: " + str(duration))
        return duration
    except Exception as ex:
        logger.Log("Exception raised get_duration: " + str(ex))






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
    miliseconds = int(3600000 * hours + 60000 * minutes + 1000 * seconds)
    return miliseconds


#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#@Function Name	  	: getTimestamp()
#@Description		: Function to get the current time in ("%H:%M:%S.%f")
#@Input arguments	: Null
#@Output values		: miliseconds- time in milliseconds
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def getTimestamp():
    timestamp = datetime.datetime.now().strftime("%H:%M:%S.%f")
    return strtomillisecond(timestamp)


#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#@Function Name	  	: getTimestamp()
#@Description		: Takes initial and final times in milliseconds and finds
#the difference as duration
#@Input arguments	: t1, t2- nitial and final times in milliseconds
#@Output values		: duration in miliseconds
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def getAPIduration(t1, t2):
    duration = round(((t2 - t1) / 1000.0), 3)
    logger.Log("Duration calculated: "+str(duration))
    return duration


#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#@Function Name	  	: UpdateTestCaseResult()
#@Description		: compares observed and expected and update the test case status
#@Input arguments	: status- API return status, observed- behavior, expected-behavior
#@Output values		: Null
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def UpdateTestCaseResult(status, observed, expected):
    try:
        global testStatus
        if status:
            logger.Log("API Passed")
        else:
            logger.Log("API Failed")
        dut.CommitStepResult("Expected : "+expected, "Observed:" + observed)
        if observed == expected:
            dut.CommitStepResult("TestCaseResult  : ","PASSED")
        else:
            testStatus = False
            dut.CommitStepResult("TestCaseResult  : ","FAILED")
        logger.Log("******************TEST CASE END *******************************")
    except Exception as e:
         logger.Warn("Exception raised in UpdateTestCaseResult function.")
         logger.Error("Exception thrown by python : " + str(e))

#def UpdateTestCaseResult(status, observed, expected):
#    global testStatus
#    dut.CommitStepResult("Expected : "+expected,"Observed:" + observed)
#    if status and observed == expected:
#        dut.CommitStepResult("TestCaseResult  : ","PASSED")
#    else:
#        testStatus = False
#        dut.CommitStepResult("TestCaseResult  : ","FAILED")
#    logger.Log("******************TEST CASE END *****************************")


#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#@Function Name	  	: UpdateTestScriptResult()
#@Description		: Updates script status, pass if all th testcase results are true
#@Input arguments	: Null
#@Output values		: Null
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def UpdateTestScriptResult(testStatus=False):
    try:
        if testStatus:
            dut.CommitStepResult("API: ", "Passed")
            dut.CommitTestResult("PASSED")
        else:
            dut.CommitStepResult("API: ", "Failed")
            dut.CommitTestResult("FAILED")
    except Exception as e:
         logger.Warn("Exception raised in UpdateTestScriptResult function.")
         logger.Error("Exception thrown by python : " + str(e))

#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#@Function Name	  	: reachCheckpointScreen()
#@Description		: To reach the particular screen based on the checkpoint name
#@Input arguments	: checkpointName
#@Output values		: Returns the list of co ordinates
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def reachScreen(screenName, CoOrdinate = False):
    screenList = screenKeyRegionMapping[screenName]
    #for i in screenList[0]:
        #dut.controller.sendCommand(i)
        #time.sleep(DEFAULT_KEY_FIRE_TIME_OUT)
    #screenList = screenKeyRegionMapping[screenName]
    #logger.Log(str(screenList[0]))
    #dut.controller.sendCommandSequence(screenList[0], DEFAULT_KEY_FIRE_TIME_OUT)
    if CoOrdinate:
        return screenList[1:]
