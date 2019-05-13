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
       
try: 
    if(dut.InitApp(config)): 
        logger.Log("App launched.") 
        if dut.WaitForElement(MobileScriptingLibrary.Constants.ElementType.XPath, "//android.widget.ImageView[@content-desc='YouTube']", 30):
            logger.Log("Home launched") 
        else:
            logger.Log("Home launched") 


finally: 
    dut.Stop() 

#'''''''''''''''''''''''''END AUTOGENERATED CODE''''''''''''''''''''''''''' 
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
