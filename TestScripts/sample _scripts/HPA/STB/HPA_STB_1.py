# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID:
# Description:
# Author:
# Date:
# Version:
# ''''''''''''''''''''AUTOGENERATED CODE - DO NOT MODIFY''''''''''''''''''''
import clr
import sys
import os
import time
clr.AddReference("ScriptingLibrary")
import ScriptingLibrary
from System.Collections.Generic import List
clr.AddReference("ScriptingLibrary")
dut = ScriptingLibrary.DUT()
logger = ScriptingLibrary.Logger()
chkpt = ScriptingLibrary.CheckPoint()
testResult = ScriptingLibrary.TestResult()
args = sys.argv
scriptPath = os.path.realpath(__file__)
remoteFiringType = "IR"
dut.Configure(args[1], args[2], args[3], args[4], scriptPath, remoteFiringType)
logger.Configure(args[1], args[2], args[3], args[4], scriptPath)

# ''''''''''''''''''''''''''''''''IMPORTS''''''''''''''''''''''''''''''''''
# ''''''''''''''''''''''''''''''END IMPORTS''''''''''''''''''''''''''''''''

#'''''''''''''''''''''''''END AUTOGENERATED CODE'''''''''''''''''''''''''''
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
for i in range(100):
    dut.controller.sendCommand("Home")
    time.sleep(5)
    chkpt.init("HPA_Home")
    if(dut.validator.validateCheckPoint((chkpt))):
        dut.controller.cacheCommand("Exit")

    resp = ScriptingLibrary.APIResponse.ResponseData()
    inputParam1 = ScriptingLibrary.HighPrecisionValidationService.MotionParams()
    inputParam1.x_cord = 18
    inputParam1.y_cord = 11
    inputParam1.width = 1106
    inputParam1.height = 694
    inputParam1.sensitivity = 3
    inputParam1.enableAggressiveMode = True
    lstInputParam = List[ScriptingLibrary.HighPrecisionValidationService.MotionParams](
    )
    lstInputParam.Add(inputParam1)
#    inputParam2 = ScriptingLibrary.HighPrecisionValidationService.MotionParams()
#    inputParam2.x_cord = 25
#    inputParam2.y_cord = 249
#    inputParam2.width = 116
#    inputParam2.height = 45
#    inputParam2.sensitivity = 3
#    lstInputParam.Add(inputParam2)
#    inputParam3 = ScriptingLibrary.HighPrecisionValidationService.MotionParams()
#    inputParam3.x_cord = 0
#    inputParam3.y_cord = 249
#    inputParam3.width = 500
#    inputParam3.height = 500
#    inputParam3.sensitivity = 10
#    lstInputParam.Add(inputParam3)
#    inputParam4 = ScriptingLibrary.HighPrecisionValidationService.MotionParams()
#    inputParam4.x_cord = 0
#    inputParam4.y_cord = 500
#    inputParam4.width = 116
#    inputParam4.height = 45
#    inputParam4.sensitivity = 10

#    lstInputParam.Add(inputParam4)

    resp = dut.validator.DetectScreenChange(80, lstInputParam)
    if resp is not None and resp.MotionData is not None:
        for i in resp.MotionData:
            logger.Log("Duration " + str(i.Duration))
            dut.CommitStepResult("Duration ", str(i.Duration))
    else:
        logger.Log("Unable to Launch DetectMotionExecutor")
        dut.CommitStepResult("Duration ", "FAILED")
