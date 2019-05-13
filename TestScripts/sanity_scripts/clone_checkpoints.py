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


chkpt.init("shameena_ocr1")
if(dut.validator.validateCheckPoint((chkpt))):
    logger.Log("Pass - {}".format("shameena_ocr1"))
else:
    logger.Log("Fail - {}".format("shameena_ocr1"))
time.sleep(1)

chkpt.init("shameena_ocr2")
if(dut.validator.validateCheckPoint((chkpt))):
    logger.Log("Pass - {}".format("shameena_ocr2"))
else:
    logger.Log("Fail - {}".format("shameena_ocr2"))
time.sleep(1)

chkpt.init("shameena_ocr3")
if(dut.validator.validateCheckPoint((chkpt))):
    logger.Log("Pass - {}".format("shameena_ocr3"))
else:
    logger.Log("Fail - {}".format("shameena_ocr3"))
time.sleep(1)

chkpt.init("shameena_ocr4")
if(dut.validator.validateCheckPoint((chkpt))):
    logger.Log("Pass - {}".format("shameena_ocr4"))
else:
    logger.Log("Fail - {}".format("shameena_ocr4"))
time.sleep(1)


chkpt.init("shameena_ocr_multiline1")
if(dut.validator.validateCheckPoint((chkpt))):
    logger.Log("Pass - {}".format("shameena_ocr_multiline1"))
else:
    logger.Log("Fail - {}".format("shameena_ocr_multiline1"))
time.sleep(1)

chkpt.init("shameena_ocr_multiline2")
if(dut.validator.validateCheckPoint((chkpt))):
    logger.Log("Pass - {}".format("shameena_ocr_multiline2"))
else:
    logger.Log("Fail - {}".format("shameena_ocr_multiline2"))
time.sleep(1)

chkpt.init("shameena_ocr_multiline3")
if(dut.validator.validateCheckPoint((chkpt))):
    logger.Log("Pass - {}".format("shameena_ocr_multiline3"))
else:
    logger.Log("Fail - {}".format("shameena_ocr_multiline3"))
time.sleep(1)


chkpt.init("shameena_ic1_pixel")
if(dut.validator.validateCheckPoint((chkpt))):
    logger.Log("Pass - {}".format("shameena_ic1_pixel"))
else:
    logger.Log("Fail - {}".format("shameena_ic1_pixel"))
time.sleep(1)

chkpt.init("shameena_ic2_pixel")
if(dut.validator.validateCheckPoint((chkpt))):
    logger.Log("Pass - {}".format("shameena_ic2_pixel"))
else:
    logger.Log("Fail - {}".format("shameena_ic2_pixel"))
time.sleep(1)

chkpt.init("shameena_ic3_pixel")
if(dut.validator.validateCheckPoint((chkpt))):
    logger.Log("Pass - {}".format("shameena_ic3_pixel"))
else:
    logger.Log("Fail - {}".format("shameena_ic3_pixel"))
time.sleep(1)

chkpt.init("shameena_ic1_rmse")
if(dut.validator.validateCheckPoint((chkpt))):
    logger.Log("Pass - {}".format("shameena_ic1_rmse"))
else:
    logger.Log("Fail - {}".format("shameena_ic1_rmse"))
time.sleep(1)

chkpt.init("shameena_ic2_rmse")
if(dut.validator.validateCheckPoint((chkpt))):
    logger.Log("Pass - {}".format("shameena_ic2_rmse"))
else:
    logger.Log("Fail - {}".format("shameena_ic2_rmse"))
time.sleep(1)

chkpt.init("shameena_ic3_rmse")
if(dut.validator.validateCheckPoint((chkpt))):
    logger.Log("Pass - {}".format("shameena_ic3_rmse"))
else:
    logger.Log("Fail - {}".format("shameena_ic3_rmse"))
time.sleep(1)

