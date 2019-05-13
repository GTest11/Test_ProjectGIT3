#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#TestCase ID:
#Description:
#Author:
#Date:
#Version:

#''''''''''''''''''''AUTOGENERATED CODE - DO NOT MODIFY''''''''''''''''''''
import clr,sys,os,time
clr.AddReference("ScriptingLibrary")
import ScriptingLibrary
dut = ScriptingLibrary.DUT()
logger = ScriptingLibrary.Logger()
chkpt = ScriptingLibrary.CheckPoint()
testResult = ScriptingLibrary.TestResult()
args = sys.argv
scriptPath = os.path.realpath(__file__)
remoteFiringType = "IR"
dut.Configure(args[1],args[2],args[3],args[4],scriptPath,remoteFiringType)
logger.Configure(args[1],args[2],args[3],args[4],scriptPath)

#''''''''''''''''''''''''''''''''IMPORTS''''''''''''''''''''''''''''''''''
#''''''''''''''''''''''''''''''END IMPORTS''''''''''''''''''''''''''''''''

#'''''''''''''''''''''''''END AUTOGENERATED CODE'''''''''''''''''''''''''''
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
dut.validator.GetServerTimeStamp()
imagePath = dut.validator.QuickCapture("Image")
dut.CommitStepResult("Build Number ","5.17.1")

dut.CommitStepResult("API: WaitImageMatch ","PASSED")
dut.CommitStepResult("API: Duration ","23")
dut.CommitStepResult("API: Remarks/Reason ","got expected result")


dut.CommitStepResult("API: WaitColorMatch","FAILED")
dut.CommitStepResult("API: Duration ","3")
dut.CommitStepResult("API: Remarks/Reason ","unexpected image")

dut.CommitStepResult("API: CaptureImage","PASSED")
dut.CommitStepResult("API: Duration ","3")
dut.CommitStepResult("API: Remarks/Reason ","got expected result")


dut.CommitStepResult("API: DynamicImageCompare ","PASSED")
dut.CommitStepResult("API: Duration ","23")
dut.CommitStepResult("API: Remarks/Reason ","got expected result")



dut.CommitStepResult("API: getOCRText ","PASSED")
dut.CommitStepResult("API: Duration ","23")
dut.CommitStepResult("API: Remarks/Reason ","got expected result")


dut.CommitStepResult("API: AddCustomDUTAttribute ","PASSED")
dut.CommitStepResult("API: Duration ","23")
dut.CommitStepResult("API: Remarks/Reason ","got expected result")
dut.CommitTestResult("Failed")
