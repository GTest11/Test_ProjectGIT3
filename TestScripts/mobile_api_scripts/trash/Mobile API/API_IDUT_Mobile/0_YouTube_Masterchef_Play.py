#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Description   : Check whether the You tube lauch is working & video is playing
#Date          : 23 Jan 2018
#FE_Version    : 5.0.7
#Author        : Arathy P S
#''''''''''''''''''''AUTOGENERATED CODE - DO NOT MODIFY''''''''''''''''''''
import clr, sys, os, time, re,timeit
clr.AddReference("MobileScriptingLibrary")
import MobileScriptingLibrary
dut = MobileScriptingLibrary.MobileDUT()
logger = MobileScriptingLibrary.Logger()
scriptPath = os.path.realpath(__file__)
args = sys.argv
dut.Configure(args[1],args[2],args[3],args[4],scriptPath)
logger.Configure(args[1],args[2],args[3],args[4],scriptPath)
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

chkpt = MobileScriptingLibrary.CheckPoint()
config = MobileScriptingLibrary.DeviceConfig()
config.DeviceType = "Android"

#youtube
config.AppPackage = "com.google.android.youtube"
config.AppActivity = "com.google.android.youtube.HomeActivity"
config.CreateNewServer="True"
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#variables

video_x = 10
video_y = 80
video_w = 500
video_h = 200
timeout = 20
waitGap = 5
tolerance = "10"
tap_x = 241
tap_y = 370

#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def main():
    try:
        dut.InitApp(config)        
        time.sleep(10)    
        chkpt.init("Mobile_YouTube")
        if(dut.validator.validateCheckPoint((chkpt))):
            dut.CommitStepResult("YouTube Launch","PASSED")
            logger.Log("YouTube App has launched successfully")
            time.sleep(5)
            if(dut.Click(MobileScriptingLibrary.Constants.ElementType.ClassName,"android.widget.ImageView",2)):
                dut.CommitStepResult("Click on Search","PASSED")
                time.sleep(3)                
                dut.SendKeys(MobileScriptingLibrary.Constants.ElementType.Id, "com.google.android.youtube:id/search_edit_text","MasterChef Australia")
                time.sleep(3)
                dut.SendAndroidKeyCode ("Keycode_ENTER")
                time.sleep(2)   
                dut.Tap(tap_x, tap_y)
                time.sleep(5) 
                # checking motion detection after youtube launch
                if(dut.validator.DetectMotion(video_x,video_y,video_w,video_h,timeout,waitGap,tolerance)):
                    logger.Log("Playing MasterChef Australia")
                    dut.CommitTestResult("PASSED")                    
                else:                    
                    logger.Log("Unable to Play MasterChef Australia")
                    dut.CommitTestResult("FAILED")
            else:
                dut.CommitStepResult("Click on Search","FAILED")
            
        else:
            logger.Log("YouTube App launch failed")
            dut.CommitStepResult("YouTube Launch","FAILED")
    except:
        logger.Log("Exception raised in main function.")
        dut.CommitTestResult("ERROR")
    finally:
        time.sleep(10)
        dut.CloseApp()
        dut.Stop()

if __name__ == "__main__":
    main()  
    #dut.ReadCustomProperty("cube_device_platform")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''