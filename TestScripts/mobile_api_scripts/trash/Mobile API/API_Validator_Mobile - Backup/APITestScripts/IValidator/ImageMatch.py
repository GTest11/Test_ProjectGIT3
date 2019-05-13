#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#TestScript ID  : FE_STB_API_VAL_09
#Description    : Validation of ImageMatch
#API Description: Validates a Checkpoint. Checkpoint validation gets executed in real-time.
#Test description:
#Author         : Arya L
#Date           : 13 April 2018, 17 April 2018
#Script Version : 2.0
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
    from configuration.constants import BUILD_NO, API_PASS, API_FAIL, DEFAULT_SLEEP_DELAY, CAP_DEFAULT_QUALITY
except ImportError:
    comLib.logger.Warn("Failed to import constants file")
    comLib.dut.CommitTestResult("ABORTED")
    sys.exit()

try:
    from configuration.coordinates import Capt_x, Capt_y, Capt_width, Capt_height

except ImportError:
    comLib.logger.Warn("Failed to import coordinates file")
    comLib.dut.CommitTestResult("ABORTED")
    sys.exit()


try:
    from configuration.config import imageMatchInputDict, imageMatchTCaseCount, skySelectKey, homeKey, skyExitKey

except ImportError:
    comLib.logger.Warn("Failed to import config file")
    comLib.dut.CommitTestResult("ABORTED")
    sys.exit()
#''''''''''''''''''''''''''''''END IMPORTS''''''''''''''''''''''''''''''''

#'''''''''''''''''''''''''END AUTOGENERATED CODE'''''''''''''''''''''''''''
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Use defined variables and functions
inputDict = imageMatchInputDict

APIname = "ImageMatch"
testCaseMax = imageMatchTCaseCount
exceptionOccured = False
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#@Function Name	  	: TestAPI()
#@Description		: Tests the ImageMatch API with diffrent parameters and logs its response (status, duration)
#@Input arguments	: Iteration count
#@Output values		: Null
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def TestAPI(i):
    try:
        # Getting inputs from global dict
        testScenario = inputDict[i][0]
        expected = inputDict[i][1]

        refImage = inputDict[i][2]
        testImage = inputDict[i][3]
        algorithm = inputDict[i][4]
        tolerance = inputDict[i][5]

        testCaseName = APIname + "_" + str(i)

        #Logging test case details
        comLib.logger.Log( "TestCase:  " +str (testCaseName))
        comLib.dut.CommitStepResult("TestCase", testCaseName)
        comLib.logger.Log( "Test scenario:  " +str (testScenario))
        comLib.dut.CommitStepResult("Test Scenario", testScenario)

        #Logging input parameters
        comLib.logger.Log( " ********** Input details ********** ")
        comLib.logger.Log("refImage: " + str(refImage))
        comLib.logger.Log("testImage: " + str(testImage))
        comLib.logger.Log("algorithm: " + str(algorithm))
        comLib.logger.Log("tolerance: " + str(tolerance))


        # Test case 0: non existing ref image
        if i != 0:
            comLib.dut.validator.CaptureImage(Capt_x, Capt_y, Capt_width, Capt_height, refImage + str(i), CAP_DEFAULT_QUALITY, 0)

        # Test case 4: ref image and test image from different screens
        # Test case 7: tolerance = 100, so the API will pass for ref image and test image from different screens
        if i == 4 or i == 7:
            #comLib.dut.controller.sendCommand(skyExitKey)
            comLib.close_app()
            time.sleep(DEFAULT_SLEEP_DELAY)

        # Test case 1: non existing test image
        if i != 1:
            comLib.dut.validator.CaptureImage(Capt_x, Capt_y, Capt_width, Capt_height, testImage + str(i), CAP_DEFAULT_QUALITY, 0)

        if i == i == 7:
            #comLib.dut.controller.sendCommand(homeKey)
            comLib.open_app()

        #API call and duration calculation
        time1 = comLib.getTimestamp()
        APIstatus = comLib.dut.validator.ImageMatch(refImage + str(i),testImage + str(i), algorithm, tolerance)
        time2 = comLib.getTimestamp()
        APIduration = comLib.getAPIduration(time1, time2)
        comLib.logger.Log( "Time taken by the API to return:  " +str (APIduration))
        comLib.dut.CommitStepResult("API: duration ", str(APIduration))
        

        #Updating test case status
        if APIstatus:
            observed = API_PASS
            comLib.UpdateTestCaseResult(True, observed, expected)
            comLib.dut.CommitStepResult("API: Test case" + str(testCaseName), "Passed")            
        else:
            observed = API_FAIL
            comLib.UpdateTestCaseResult(False, observed, expected)
            comLib.dut.CommitStepResult("API: Test case" + str(testCaseName), "Failed")
    except Exception as e:
         comLib.logger.Error ("Exception thrown by python from TestAPI: " + str(e))
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
                comLib.logger.Error("WaitforElement Failed for YouTube")
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
         global exceptionOccured
         exceptionOccured = True
         #comLib.UpdateTestCaseResult(False, observed, )

         #if i < testCaseMax:
             #TestAPI()
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
