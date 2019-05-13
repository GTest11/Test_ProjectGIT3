#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' 
#TestCase ID: 
#Description: 
#Author: 
#Date: 
#Version: 

#''''''''''''''''''''AUTOGENERATED CODE - DO NOT MODIFY'''''''''''''''''''' 
import clr,sys,os,time 
clr.AddReference("MobileScriptingLibrary") 
import MobileScriptingLibrary 
dut = MobileScriptingLibrary.MobileDUT() 
logger = MobileScriptingLibrary.Logger() 
chkpt = MobileScriptingLibrary.CheckPoint() 
config = MobileScriptingLibrary.DeviceConfig() 

#''''''''''''''''''''''''''''''''IMPORTS''''''''''''''''''''''''''''''''''' 
#''''''''''''''''''''''''''''''END IMPORTS''''''''''''''''''''''''''''''''' 

#''''''''''''''''''''''''''''''FOR iOS DEVICE'''''''''''''''''''''''''''''' 
#config.DeviceType = "iOS" 
#config.AppName = "com.google.ios.youtube" 


#''''''''''''''''''''''''''''FOR ANDROID DEVICE'''''''''''''''''''''''''''' 
config.DeviceType = "Android" 
config.AppPackage = "com.google.android.youtube" 
config.AppActivity = ".HomeActivity" 

args = sys.argv 
scriptPath = os.path.realpath(__file__) 
dut.Configure(args[1],args[2],args[3],args[4],scriptPath) 
logger.Configure(args[1],args[2],args[3],args[4],scriptPath) 
       

TAP_X = 241
TAP_Y = 370
try: 
    if(dut.InitApp(config)): 
        logger.Log("App launched.") 
        dut.Tap(TAP_X, TAP_Y)
        logger.Log("After Tap.") 

finally: 
    dut.Stop() 

#'''''''''''''''''''''''''END AUTOGENERATED CODE''''''''''''''''''''''''''' 
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
