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
while(1):
    dut.controller.sendCommand("Home")

    imagePath1 = dut.validator.QuickCapture("After_Home1")
    dut.controller.sendCommand("Down")
    imagePath2 = dut.validator.QuickCapture("After_Down1")
    dut.controller.sendCommand("Down")
    imagePath3 = dut.validator.QuickCapture("After_Down2")
    dut.controller.sendCommand("Exit")
    imagePath4 = dut.validator.QuickCapture("After_Down3")
    dut.controller.sendCommand("Home")
    imagePath5 = dut.validator.QuickCapture("After_Home2")
    dut.controller.sendCommand("Down")
    imagePath6 = dut.validator.QuickCapture("After_Down4")