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
for i in range(100):
    dut.AddCustomDUTAttribute("customAttributeName")
    dut.GetCustomDUTAttribute("customAttributeName")
    dut.ReadCustomProperty("customAttributeName")
    dut.SetCustomDUTAttribute("customAttributeName","customAttributeName" + str(i))
    dut.SetDUTAttribute("serialno",str(i))