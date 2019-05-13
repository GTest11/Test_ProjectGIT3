#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#TestScript ID  : FE_STB_API_VAL_07
#Description    : Validation of GetScreenTransitionTime
#API Description: Returns timestamp of the first non matching frame in seconds.
# Used with StartCaptureZapFrames and StopCaptureZapFrames for validating captured frames.
#Test descriptio:
#Author         : Arya L
#Date           : 19 March 2018, 23 March 2018,
#Script Version : 2.0
#Script modified for Sky box (testing_rack, slot 5)
#''''''''''''''''''''AUTOGENERATED CODE - DO NOT MODIFY''''''''''''''''''''
#''''''''''''''''''''''''''''''''IMPORTS''''''''''''''''''''''''''''''''''
#ipmorting python modules
import clr, sys, os, time, datetime

#importing user defined modules
sys.path.append('../../')
try:
    # Import library file
    import library.commonFunctions as comLib
except ImportError:
    print("Failed to import commonFunctions file")
    sys.exit()

try:
    from configuration.constants import BUILD_NO, API_PASS, API_FAIL, START_CAPTURE_ZAP_TIME, DEFAULT_SLEEP_DELAY
except ImportError:
    comLib.logger.Log("Failed to import constants file")
    comLib.dut.CommitTestResult("ABORTED")
    sys.exit()

try:
    from configuration.config import CheckpointScreenForTransition, skyExitKey, \
    getScreenTransitionTimeTestCaseCount, getScreenTransitionTimeInputDict
except ImportError:
    comLib.logger.Warn("Failed to import config file")
    comLib.dut.CommitTestResult("ABORTED")
    sys.exit()
#''''''''''''''''''''''''''''''END IMPORTS''''''''''''''''''''''''''''''''

#'''''''''''''''''''''''''END AUTOGENERATED CODE'''''''''''''''''''''''''''
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Use defined variables and functions
inputDict = getScreenTransitionTimeInputDict

APIname = "GetScreenTransitionTime"
testCaseMax = getScreenTransitionTimeTestCaseCount
exceptionOccured = False


#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#@Function Name	  	: TestAPI()
#@Description		: Tests the GetScreenTransitionTime API with diffrent parameters
#and logs its response (status, duration)
#@Input arguments	: Iteration count
#@Output values		: Null
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def TestAPI(i):
    try:
        # Getting inputs from global dict
        testScenario = inputDict[i][0]
        expected = inputDict[i][1]

        checkPointName = inputDict[i][2]
        timeToWait = inputDict[i][3]
        initialDelay = inputDict[i][4]


        testCaseName = APIname + "_" + str(i)

        #Logging test case details
        comLib.logger.Log( "TestCase:  " +str (testCaseName))
        comLib.dut.CommitStepResult("TestCase", testCaseName)
        comLib.logger.Log( "Test scenario:  " +str (testScenario))
        comLib.dut.CommitStepResult("Test Scenario", testScenario)

        #Logging input parameters
        comLib.logger.Log( " ********** Input details ********** ")
        comLib.logger.Log("checkPointName: " + str(checkPointName))
        comLib.logger.Log("timeToWait: " + str(timeToWait))
        comLib.logger.Log("initialDelay: " + str(initialDelay))


        #test case pre conditions
        #Reach checkpoints screen and wait.
        #0 : DUT already in some other screen
        if i != 0:
            comLib.dut.Tap(500,500)
            time.sleep(20)
            comLib.reachScreen(CheckpointScreenForTransition) # take a checkpoint from the video play screen.
        #API call and duration calculation
        comLib.dut.validator.StopCaptureZapFrames()
        platform = str(comLib.dut.ReadProperty(3))
        comLib.update_dut_config(platform)
        if(comLib.dut.validator.StartCaptureZapFrames(START_CAPTURE_ZAP_TIME)):
            #Make transition from checkpoint screen
            time.sleep(DEFAULT_SLEEP_DELAY)
            # Changing from checkpoint screen
            if i > 1:
                #comLib.dut.controller.sendCommand(skyExitKey)
                #comLib.close_app()
				# configuring the device for automation'
				
                if "Android" == platform:                 
                    comLib.dut.SendAndroidKeyCode("Keycode_BACK")
                    time.sleep(20)
                else:
                    comLib.dut.VerticalSwipe(179, 975, 500, 5)
                    time.sleep(20)


            time1 = comLib.getTimestamp()
            transitionTime = comLib.dut.validator.GetScreenTransitionTime(checkPointName, timeToWait, initialDelay)
            time2 = comLib.getTimestamp()
            #comLib.logger.Log("transitionTime:" + str(transitionTime))
            APIduration = comLib.getAPIduration(time1, time2)
            comLib.logger.Log( "Time taken by the API to return:  " +str (APIduration))
            comLib.dut.CommitStepResult("API: duration ", str(APIduration))
            

        #Updating test case status
            if(transitionTime > 0 and APIduration <= timeToWait + 1):
                comLib.logger.Log("transitionTime:" + str(transitionTime))
                comLib.logger.Log("API passed")
                observed = API_PASS
                comLib.UpdateTestCaseResult(True, observed, expected)
                comLib.dut.CommitStepResult("API: Test case" + str(testCaseName), "Passed")                
            else:
                observed = API_FAIL
                comLib.UpdateTestCaseResult(False, observed, expected)
                comLib.dut.CommitStepResult("API: Test case" + str(testCaseName), "Failed")
                comLib.logger.Log("API failed")
            #if i > 1:
                #comLib.dut.controller.sendCommand(skyExitKey)
            #    comLib.open_app()

            comLib.dut.validator.StopCaptureZapFrames()
        else:
            observed = "error"
            comLib.UpdateTestCaseResult(False, observed, expected)
            comLib.logger.Log("Unable to start frame capture")


    except Exception as e:
         comLib.logger.Error("Exception thrown by python from TestAPI: " + str(e))
         global exceptionOccured
         exceptionOccured = True


# ******************************************************************************
def main():
    try:
        comLib.dut.validator.QuickCapture("quickCapimage_Initial")
        # Logging basic test informations
        comLib.logger.Log("################## API VALIDATION START ###############")
        comLib.logger.Log("Build Number: " + BUILD_NO)
        comLib.logger.Log("API under test: " + str(APIname))
        comLib.dut.CommitStepResult("Build Number  : ", BUILD_NO)
        comLib.dut.CommitStepResult("API: ", APIname)

        # this is a variable used to hold the Platform name
        platform = str(comLib.dut.ReadProperty(3))

        # configuring the device for automation'
        comLib.update_dut_config(platform)
        # executing precondition, making the box awake by home key press
        #launching application'
        init_app_time = comLib.open_app()
        if init_app_time > 0:
            if "Android" == platform:
                element_id = comLib.android_conf.android_APP_HOME
            else:
                element_id = comLib.ios_conf.ios_APP_HOME
            if not comLib.dut.WaitForElement(
                    comLib.MobileScriptingLibrary.Constants.ElementType.XPath, element_id, 20):
                comLib.logger.Error("WaitForElement failed for youtube")
                testStatus = False
                sys.exit()
            else:
                comLib.logger.Log("App launched")
        else:
            comLib.logger.Error("Error in InitApp API")
            testStatus = False
            sys.exit()

        #executing test caases
        comLib.dut.validator.QuickCapture("quickCapimage_BeforeAPIcall")
        for i in range( testCaseMax ):
            TestAPI(i)
        comLib.dut.validator.QuickCapture("quickCapimage_AfterAPIcall")

    except Exception as e:
         comLib.logger.Warn("Exception raised in main function.")
         comLib.logger.Error("Exception thrown by python : " + str(e))
         observed = "exception"
         global exceptionOccured
         exceptionOccured = True

    finally:
        comLib.close_app()
        #Updating script status
        if exceptionOccured:
            comLib.dut.CommitTestResult("ERROR")
        else:
            comLib.UpdateTestScriptResult()

        comLib.logger.Log("################ TEST SCRIPT END #########################")
# *****************************************************************************
if __name__ == "__main__":
    main()
# *****************************************************************************
