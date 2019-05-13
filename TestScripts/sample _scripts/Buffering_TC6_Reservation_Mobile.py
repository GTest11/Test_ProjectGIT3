#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' 
#TestCase ID: 
#Description: 
#Author: 
#Date: 
#Version: 

#''''''''''''''''''''AUTOGENERATED CODE - DO NOT MODIFY'''''''''''''''''''' 
import clr,sys,os,time 
from System.Collections.Generic import List 
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
#config.AppName = "in.startv.hotstar" #ios


#''''''''''''''''''''''''''''FOR ANDROID DEVICE'''''''''''''''''''''''''''' 
#config.DeviceType = "Android" 
#config.AppPackage = "com.bskyb.nowtv.beta" 
#config.AppActivity = "com.nowtv.view.activity.StartupActivity" 

#config.DeviceType = "Android" 
#config.AppPackage = "com.bskyb.skygo" 
#config.AppActivity = "com.bskyb.uma.app.bootstrap.BootstrapActivity" 

config.DeviceType = "Android" 
config.AppPackage = "com.tv.v18.viola" 
config.AppActivity = "com.tv.v18.viola.views.activities.RSHomeActivity" 
args = sys.argv 
scriptPath = os.path.realpath(__file__) 
dut.Configure(args[1],args[2],args[3],args[4],scriptPath) 
logger.Configure(args[1],args[2],args[3],args[4],scriptPath) 


        

try: 
    if(dut.InitApp(config)): 
        time.sleep(20)
        dut.Tap(551,1017)
        time.sleep(10)               
        logger.Log("App launched.") 
        #dut.TapElement(ElementType,"Element Id",index) 
        reservationRequest = MobileScriptingLibrary.HighPrecisionValidationService.SlotReservationRequest() 
        reservationRequest.AlgorithmCount = 1 
        reservationResponse = dut.ReserveSlotForHPA(reservationRequest) 
        logger.Log("Response - " + reservationResponse.Data.Token) 
        if(reservationResponse.Status): 
            request = MobileScriptingLibrary.HighPrecisionValidationService.VideoAnalysisRequest() 
            deviceInfo = MobileScriptingLibrary.HighPrecisionValidationService.DeviceInfo() 
            algorithmList =List[MobileScriptingLibrary.HighPrecisionValidationService.Algorithm]() 
            #algorithm = MobileScriptingLibrary.HighPrecisionValidationService.Algorithm() 
            #algorithm.Name = "Histogram" 
            #algorithm.Params = "eyAgICAicmdiRGV0YWlsc0xpc3QiOiBbewogICAgICAgICJyIjogMTAwLAogICAgICAgICJnIjogMzEsCiAgICAgICAgImIiOiAxNDAsCiAgICAgICAgInBpeGVsQ291bnRUaHJlc2hvbGQiOiA4MAogICAgfSwgewogICAgICAgICJyIjogMjU1LAogICAgICAgICJnIjogMTE2LAogICAgICAgICJiIjogNSwKICAgICAgICAicGl4ZWxDb3VudFRocmVzaG9sZCI6IDgwCiAgICB9LCB7CiAgICAgICAgInIiOiA0MSwKICAgICAgICAiZyI6IDEzOSwKICAgICAgICAiYiI6IDI2LAogICAgICAgICJwaXhlbENvdW50VGhyZXNob2xkIjogODAKICAgIH0sIHsKICAgICAgICAiciI6IDAsCiAgICAgICAgImciOiAxMDEsCiAgICAgICAgImIiOiAyNTUsCiAgICAgICAgInBpeGVsQ291bnRUaHJlc2hvbGQiOiA4MAogICAgfV0sCiAgICAibWFza0RldGFpbHMiOiB7CiAgICAgICAgInhjb3JkIjogNTkxLAogICAgICAgICJ5Y29yZCI6IDMxMywKICAgICAgICAid2lkdGgiOiA5OCwKICAgICAgICAiaGVpZ2h0IjogODkKICAgIH0KfQ=="
            #algorithmList.Add(algorithm) 
            algorithm = MobileScriptingLibrary.HighPrecisionValidationService.Algorithm() 
            algorithm.Name = "HoughCircles" 
            algorithm.Params = "CuKAiwp7CiAgIm1hc2tEZXRhaWxzIjogewogICAgInhjb3JkIjogMzIyLAogICAgInljb3JkIjogMjAzLAogICAgIndpZHRoIjogNzYsCiAgICAiaGVpZ2h0IjogOTAKICB9LAogICJjaXJjbGVUaHJlc2hvbGRzIjogewogICAgImNpcmNsZVBlcmNlbnRhZ2VMb3dMaW1pdCI6IDMwLAogICAgImNpcmNsZVBlcmNlbnRhZ2VVcExpbWl0IjogODUsCiAgICAiY2lyY2xlUmFkaXVzTG93TGltaXQiOiAzMCwKICAgICJjaXJjbGVSYWRpdXNVcExpbWl0IjogNDAsCiAgICAiY2lyY2xlQ2VudGVyWE9mZnNldCI6IDE1LAogICAgImNpcmNsZUNlbnRlcllPZmZzZXQiOiAxOC4wLAogICAgImNpcmNsZUNlbnRlcldpZHRoIjogMzAuMCwKICAgICJjaXJjbGVDZW50ZXJIZWlnaHQiOiAzMC4wCiAgfSwKICAibWlzY1RocmVzaG9sZHMiOiB7CiAgICAiY2FubnlUaHJlc2hvbGQxIjogMzUsCiAgICAiY2FubnlUaHJlc2hvbGQyIjogODAsCiAgICAiaG91Z2hEcCI6IDEuNCwKICAgICJob3VnaE1pbkRpc3QiOiA1MC4wLAogICAgImhvdWdoUGFyYW0xIjogODAuMCwKICAgICJob3VnaFBhcmFtMiI6IDM3LjAsCiAgICAiZGlzdFRyYW5zZm9ybUZpbHRlckRpc3QiOiAzCiAgfQp9"
            algorithmList.Add(algorithm) 
            request.Duration = 120
            request.Token = reservationResponse.Data.Token 
            request.Algorithms = algorithmList 
            request.DeviceInfo = deviceInfo 
            response = dut.validator.StartHighPrecisionFrameAnalysis(request) 
            #time.sleep(30) 
            #dut.Tap(265,721)   #Android   NowTv 
            #dut.Tap(586,894) #Voot on Android            
            dut.TapPercent(54,46)  # Tap Percent on Voot to check working of TapPercent in HPAs,it is working
            #dut.TapElement(MobileScriptingLibrary.Constants.ElementType.XPath,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout")
            #time.sleep() 
            #dut.Tap(523, 530) 
            #time.sleep(30) 
            #dut.Tap(497, 1210) 
            #time.sleep(10) 
            #dut.Tap(1625, 966)
            #dut.validator.StopHighPrecisionFrameAnalysis(response.Data.Token)
            #dut.validator.StopAllHighPrecisionFrameAnalysis()
            #time.sleep(1) 
            #dut.Tap(1625, 966) 
            time.sleep(300) 
            logger.Log("Response - " + str(response.Data)) 
            logger.Log("Response Token- " + response.Data.Token)             
            statusRequest = MobileScriptingLibrary.HighPrecisionValidationService.VideoAnalysisStatusRequest() 
            time.sleep(200)
            statusRequest.Token = response.Data.Token 
            statusRespose = dut.validator.GetHighPrecisionFrameAnalysisResult(statusRequest) 
            #statusRespose.Token = statusRespose.Data.Token
            logger.Log("StatusRespose - " + str(statusRespose.Data)) 
            #dut.CommitTestResult("PASSED") 

finally:
    dut.Stop()
    #dut.validator.StopAllHighPrecisionFrameAnalysis()
    #dut.CloseApp() 
    #time.sleep(30)

#'''''''''''''''''''''''''END AUTOGENERATED CODE''''''''''''''''''''''''''' 
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' 