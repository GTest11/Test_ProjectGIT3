import clr,sys,os,time
checkPointList = ["xbox_OCR_multi", "xbox_OCR_1", "xbox_IC_rmse", "xbox_IC_pixel"]

#'''''''''''''''''''''''''''STB''''''''''''''''''''''''''''''''''''
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
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#''''''''''''''''''''''''MOBILE''''''''''''''''''''''''''''''''''''


#checkPointList = ["5_1_0_1_RMSE2"]
#checkPointList = ["17_3OCR","17_03_IC"]


#Provide valid parameters
#checkp = "5_1_0_1_RMSE2" #00_ocrTest -checkpoint Name
#chkpt.init(checkp)
##Info: Initialize checkpoint "00_ocrTest"


##Provide valid parameters
#checkp = "5_1_0_1_RMSE2" #00_ocrTest -checkpoint Name
#chkpt.init(checkp)


for i in checkPointList:
    chkpt.init(i) 
    if(dut.validator.validateCheckPoint(chkpt)):
        logger.Log("Passed")
    else:
        logger.Log("Failed")

imagePath = dut.validator.QuickCapture("capture")

