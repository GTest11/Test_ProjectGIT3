# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestScript ID  : FE_STB_API_VAL_02
# Description    : Validation of CaptureImage
# API Description: Captures an image region with provided co-ordinates and returns
# it path for further usage within the test script.
# Author         : Arya L
# Date           : 12 March 2018, 22 March 2018, 16 April 2018
# Script Version : 2.0
# ''''''''''''''''''''AUTOGENERATED CODE - DO NOT MODIFY''''''''''''''''''''
# ''''''''''''''''''''''''''''''''IMPORTS''''''''''''''''''''''''''''''''''
# ipmorting python modules
import sys


# importing user defined modules
sys.path.append('../../')
# try:
# Import library file
import library.commonFunctions as comLib
# except ImportError:
#    print("Failed to import commonFunctions file")
#    sys.exit()

try:
    from configuration.config import captureImageTestCaseCount, captureImageInputDict
except ImportError:
    comLib.logger.Warn("Failed to import config file")
    comLib.dut.CommitTestResult("ABORTED")
    sys.exit()

try:
    from configuration.constants import BUILD_NO, API_PASS, API_FAIL
except ImportError:
    comLib.logger.Log("Failed to import constants file")
    comLib.dut.CommitTestResult("ABORTED")
    sys.exit()
# ''''''''''''''''''''''''''''''END IMPORTS''''''''''''''''''''''''''''''''
#'''''''''''''''''''''''''END AUTOGENERATED CODE'''''''''''''''''''''''''''
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Use defined variables and functions
inputDict = captureImageInputDict

APIname = "CaptureImage"
testCaseMax = captureImageTestCaseCount
exceptionOccured = False
captureLoop = 2
global platform
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# @Function Name	  	: TestAPI()
# @Description		: Tests the CaptureImage API with diffrent parameters and
# logs its response (status, duration)
# @Input arguments	: Iteration count
# @Output values		: Null
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def TestAPI(i):
    try:
        # Getting inputs from global dict
        testScenario = inputDict[i][0]
        expected = inputDict[i][1]
        xCord = inputDict[i][2]
        yCord = inputDict[i][3]
        width = inputDict[i][4]
        height = inputDict[i][5]
        ImageName = inputDict[i][6]
        jpegQuality = inputDict[i][7]
        overWriteAction = inputDict[i][8]
        #configuring the device for automation for mobile android and iOS devices'
        platform = str(comLib.dut.ReadProperty(3)) 
        #comLib.get_dut_platform() 
        comLib.update_dut_config(platform)
        if i == 10:
            if "Android" == platform:    
                width=720
                height=1280
            else:
                width=768
                height=1024
        testCaseName = APIname + "_" + str(i)

        # Logging test case details
        comLib.logger.Log("TestCase:  " + str(testCaseName))
        comLib.dut.CommitStepResult("TestCase", testCaseName)
        comLib.logger.Log("Test scenario:  " + str(testScenario))
        comLib.dut.CommitStepResult("Test Scenario", testScenario)

        # Logging input parameters
        comLib.logger.Log("Input details... ")
        comLib.logger.Log("xCord: " + str(xCord))
        comLib.logger.Log("yCord: " + str(yCord))
        comLib.logger.Log("width: " + str(width))
        comLib.logger.Log("height: " + str(height))
        comLib.logger.Log("ImageName: " + str(ImageName))
        comLib.logger.Log("jpegQuality: " + str(jpegQuality))
        comLib.logger.Log("overWriteAction: " + str(overWriteAction))

        # API call and duration calculation
        for i in range(captureLoop):
            ImageName = ImageName + str(i)
            comLib.dut.CommitStepResult("API loop ", str(i))
            time1 = comLib.getTimestamp()
            imagePath = comLib.dut.validator.CaptureImage(xCord, yCord, width,
                                                          height, ImageName, jpegQuality, overWriteAction)
            time2 = comLib.getTimestamp()
            APIduration = comLib.getAPIduration(time1, time2)
            comLib.logger.Log(
                "Time taken by the APT to return:  " +
                str(APIduration))
            comLib.dut.CommitStepResult("API: Duration ", str(APIduration))
            comLib.dut.CommitStepResult("API: CaptureImage ", "PASSED")

            comLib.logger.Log("imagePath:  " + str(imagePath))
            # Updating test case status
            if imagePath is not None and imagePath != "":
                observed = "api pass"
                comLib.UpdateTestCaseResult(True, observed, expected)
                comLib.dut.CommitStepResult("API: CaptureImage ", "PASSED")
                comLib.dut.CommitStepResult("API: Passed remarks ", "Validation True and API Returned Pass")
            else:
                observed = "api fail"
                comLib.UpdateTestCaseResult(False, observed, expected)
                comLib.dut.CommitStepResult("API: Failed remarks ", "API Returned fail/ Validation Failed")

    except Exception as e:
        comLib.logger.Error(
            "Exception thrown by python from TestAPI: " + str(e))
        global exceptionOccured
        exceptionOccured = True

# ******************************************************************************


def main():
    try:
        # Logging basic test informations
        comLib.logger.Log(
            "############### API VALIDATION START ###############")
        comLib.logger.Log("Build Number: " + BUILD_NO)
        comLib.logger.Log("API under test: " + str(APIname))
        comLib.dut.CommitStepResult("Build Number  : ", BUILD_NO)
        comLib.dut.CommitStepResult("API: ", APIname)

        # this is a variable used to hold the Platform name  
        platform = str(comLib.dut.ReadProperty(3))

        #configuring the device for automation'
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
                comLib.logger.Error("Waitfor element failed for Youtube")
                testStatus = False
                sys.exit()
            else:
                comLib.logger.Log("App launched")
        else:
            comLib.logger.Error("Error in InitApp API")
            testStatus = False
            sys.exit()

        # executing test cases
        for i in range(testCaseMax):
            TestAPI(i)

    except Exception as e:
        comLib.logger.Warn("Exception raised in main function.")
        comLib.logger.Error("Exception thrown by python : " + str(e))
        observed = "exception"
        global exceptionOccured
        exceptionOccured = True
    finally:
        comLib.close_app()
        # Updating script status
        if exceptionOccured:
            comLib.dut.CommitTestResult("ERROR")
        else:
            comLib.UpdateTestScriptResult()
        comLib.logger.Log("############### TEST SCRIPT END ##################")


# *****************************************************************************
if __name__ == "__main__":
    main()
# *****************************************************************************
