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

#Provide valid parameters
#checkp = "fsdf"
#chkpt.init(checkp)
#if(dut.validator.validateCheckPoint((chkpt))):
#    logger.Log("passed")
#else:
#    logger.Log("failed")

ItalianDict = ["5120_OCR_ITA_SINGLE_NoFil", "5120_OCR_ITA_SINGLE", "5120_OCR_ITA_SINGLE_MULTIFIL", "5120_OCR_ITA_Multi_NoFil", "5120_OCR_ITA_MULTI", "5120_OCR_ITA_MULTI_MULTIFIL"]
germanDict  = ["5120_OCR_GER_SINGLE_NoFil", "5120_OCR_GER_SINGLE", "5120_OCR_GER_SINGLE_MULTIFIL", "5120_GER_ITA_Multi_NoFil", "5120_OCR_GER_MULTI", "5120_OCR_GER_MULTI_MULTIFIL"]
PortugueseDict = ["5120_OCR_POR_SINGLE_NoFil", "5120_OCR_POR_SINGLE_MULTIFIL", "5120_OCR_POR_Multi_NoFil", "5120_OCR_POR_MULTI_MULTIFIL"]
PortugueseDict = ["5120_OCR_POR_SINGLE_MULTIFIL"]
spanishDict  = ["5120_OCR_SPA_SINGLE_NoFil", "5120_OCR_GER_SINGLE", "5120_OCR_GER_SINGLE_MULTIFIL", "5120_GER_ITA_Multi_NoFil", "5120_OCR_GER_MULTI", "5120_OCR_GER_MULTI_MULTIFIL"]
#spanishDict  = ["5120_OCR_SPA_SINGLE_NoFil"]
#spanishDict  = ["5120_OCR_SPA_SINGLE", "5120_OCR_SPA_SINGLE_MULTIFIL", "5120_GER_SPA_Multi_NoFil", "5120_OCR_SPA_MULTI_MULTIFIL" ]
chineseDict  = ["5120_OCR_CHI_SINGLE",]# "5120_OCR_SPA_SINGLE_MULTIFIL", "5120_GER_SPA_Multi_NoFil", "5120_OCR_SPA_MULTI_MULTIFIL" ]
hinDict = ["5120_OCR_HIN_SING"]
langDict = spanishDict

for i in range(10):
    for i in langDict:
        chkpt.init(i)
        if(dut.validator.validateCheckPoint(chkpt)):
            logger.Log("Passed")
        else:
            logger.Log("Failed")

    imagePath = dut.validator.QuickCapture("test")