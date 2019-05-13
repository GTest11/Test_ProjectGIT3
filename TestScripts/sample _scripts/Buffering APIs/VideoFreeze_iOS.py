#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' 
#TestCase ID: HOughCircle_BufferingAPI
#Description: 
#Author: Samsung_a445_Youtube App
#Date: 
#Version: 

#''''''''''''''''''''AUTOGENERATED CODE - DO NOT MODIFY'''''''''''''''''''' 
import clr,sys,os,time 
import base64
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

#config.DeviceType = "Android" 
#config.AppPackage = "com.tv.v18.viola" 
#config.AppActivity = "com.tv.v18.viola.views.activities.RSHomeActivity"

config.DeviceType = "Android" 
config.AppPackage = "com.google.android.youtube" 
config.AppActivity = ".HomeActivity" 
 
args = sys.argv 
scriptPath = os.path.realpath(__file__) 
dut.Configure(args[1],args[2],args[3],args[4],scriptPath) 
logger.Configure(args[1],args[2],args[3],args[4],scriptPath) 
       

if(dut.InitApp(config)): 
    time.sleep(30)
    dut.Tap(556,830) # playing the first video
    time.sleep(5)
    #dut.Tap(353,731)
    #time.sleep(40)               
    logger.Log("App launched.") 
    #dut.TapElement(ElementType,"Element Id",index) 
#    reservationRequest = MobileScriptingLibrary.HighPrecisionValidationService.SlotReservationRequest() 
#    reservationRequest.AlgorithmCount = 2 
#    reservationResponse = dut.ReserveSlotForHPA(reservationRequest) 
#    logger.Log("Response - " + reservationResponse.Data.Token) 
#    if(reservationResponse.Status): 
#        request = MobileScriptingLibrary.HighPrecisionValidationService.VideoAnalysisRequest() 
#        deviceInfo = MobileScriptingLibrary.HighPrecisionValidationService.DeviceInfo() 
#        algorithmList =List[MobileScriptingLibrary.HighPrecisionValidationService.Algorithm]() 
#        #algorithm = MobileScriptingLibrary.HighPrecisionValidationService.Algorithm() 
#        #algorithm.Name = "Histogram" 
#        #algorithm.Params = "eyAgICAicmdiRGV0YWlsc0xpc3QiOiBbewogICAgICAgICJyIjogMTAwLAogICAgICAgICJnIjogMzEsCiAgICAgICAgImIiOiAxNDAsCiAgICAgICAgInBpeGVsQ291bnRUaHJlc2hvbGQiOiA4MAogICAgfSwgewogICAgICAgICJyIjogMjU1LAogICAgICAgICJnIjogMTE2LAogICAgICAgICJiIjogNSwKICAgICAgICAicGl4ZWxDb3VudFRocmVzaG9sZCI6IDgwCiAgICB9LCB7CiAgICAgICAgInIiOiA0MSwKICAgICAgICAiZyI6IDEzOSwKICAgICAgICAiYiI6IDI2LAogICAgICAgICJwaXhlbENvdW50VGhyZXNob2xkIjogODAKICAgIH0sIHsKICAgICAgICAiciI6IDAsCiAgICAgICAgImciOiAxMDEsCiAgICAgICAgImIiOiAyNTUsCiAgICAgICAgInBpeGVsQ291bnRUaHJlc2hvbGQiOiA4MAogICAgfV0sCiAgICAibWFza0RldGFpbHMiOiB7CiAgICAgICAgInhjb3JkIjogNTkxLAogICAgICAgICJ5Y29yZCI6IDMxMywKICAgICAgICAid2lkdGgiOiA5OCwKICAgICAgICAiaGVpZ2h0IjogODkKICAgIH0KfQ=="
#        #algorithmList.Add(algorithm) 
#        ############Test WEorking JSOn for Smamsung a445 on Youtube
#        algorithm = MobileScriptingLibrary.HighPrecisionValidationService.Algorithm() 
#        algorithm.Name = "HoughCircles" 
#        algorithm.Params = "ICAibWFza0RldGFpbHMiOiB7CiAgICAieGNvcmQiOiAyODYsCiAgICAieWNvcmQiOiAxNzQsCiAgICAid2lkdGgiOiAxNTAsCiAgICAiaGVpZ2h0IjogMTUyCiAgfSwKICAiY2lyY2xlVGhyZXNob2xkcyI6IHsKICAgICJjaXJjbGVQZXJjZW50YWdlTG93TGltaXQiOiAzMSwKICAgICJjaXJjbGVQZXJjZW50YWdlVXBMaW1pdCI6IDg2LAogICAgImNpcmNsZVJhZGl1c0xvd0xpbWl0IjogNzAsCiAgICAiY2lyY2xlUmFkaXVzVXBMaW1pdCI6IDc4LAogICAgImNpcmNsZUNlbnRlclhPZmZzZXQiOiAzMiwKICAgICJjaXJjbGVDZW50ZXJZT2Zmc2V0IjogMzIsCiAgICAiY2lyY2xlQ2VudGVyV2lkdGgiOiA3MCwKICAgICJjaXJjbGVDZW50ZXJIZWlnaHQiOiA3MAogIH0sCiAgIm1pc2NUaHJlc2hvbGRzIjogewogICAgImNhbm55VGhyZXNob2xkMSI6IDM1LAogICAgImNhbm55VGhyZXNob2xkMiI6IDgwLAogICAgImhvdWdoRHAiOiAxLjQsCiAgICAiaG91Z2hNaW5EaXN0IjogNTAuMCwKICAgICJob3VnaFBhcmFtMSI6IDgwLjAsCiAgICAiaG91Z2hQYXJhbTIiOiAzNy4wLAogICAgImRpc3RUcmFuc2Zvcm1GaWx0ZXJEaXN0IjogMwogIH0="
#        algorithmList.Add(algorithm)
#        #################################
##            json_input = '{\
##                            "maskDetails": {\
##                                "xcord": 286,\
##                                "ycord": 174,\
##                                "width": 150,\
##                                "height": 152\
##                            },\
##                            "circleThresholds": {\
##                                "circlePercentageLowLimit": 31,\
##                                "circlePercentageUpLimit": 86,\
##                                "circleRadiusLowLimit": 70,\
##                                "circleRadiusUpLimit": 78,\
##                                "circleCenterXOffset": 32,\
##                                "circleCenterYOffset": 32,\
##                                "circleCenterWidth": 70,\
##                                "circleCenterHeight": 70\
##                            },\
##                            "miscThresholds": {\
##                                "cannyThreshold1": 35,\
##                                "cannyThreshold2": 80,\
##                                "houghDp": 1.4,\
##                                "houghMinDist": 50.0,\
##                                "houghParam1": 80.0,\
##                                "houghParam2": 37.0,\
##                                "distTransformFilterDist": 3\
##                            }\
##                        }'
##            base64input = base64.b64encode(bytes(json_input), 'utf-8')
##            algorithm.Params = base64input
#        ####Voot app Json working            
#        request.Duration = 120
#        request.Token = reservationResponse.Data.Token 
#        request.Algorithms = algorithmList 
#        request.DeviceInfo = deviceInfo 
#        response = dut.validator.StartHighPrecisionFrameAnalysis(request) 
#        #time.sleep(30) 
#        #dut.Tap(265,721)   #Android   NowTv 
#        #dut.Tap(366,1109)
#        dut.Tap(315,1699) # playing video in second screen for more buffering
#        time.sleep(200) 
#        logger.Log("Response - " + str(response.Data)) 
#        logger.Log("Response Token- " + response.Data.Token)             
#        statusRequest = MobileScriptingLibrary.HighPrecisionValidationService.VideoAnalysisStatusRequest() 
#        time.sleep(100)
#        statusRequest.Token = response.Data.Token 
#        statusRespose = dut.validator.GetHighPrecisionFrameAnalysisResult(statusRequest) 
#        #statusRespose.Token = statusRespose.Data.Token
#        ##previous log details
#        #logger.Log("StatusRespose - " + str(statusRespose.Data)) 
#        logger.Log("StatusRespose - " + str(statusRespose))
#        #dut.CommitTestResult("PASSED")

    reservationRequest = MobileScriptingLibrary.HighPrecisionValidationService.SlotReservationRequest()
    reservationRequest.AlgorithmCount = 1
    reservationResponse = dut.ReserveSlotForHPA(reservationRequest)
    if(reservationResponse.Status):
        request = MobileScriptingLibrary.HighPrecisionValidationService.VideoAnalysisRequest()
        deviceInfo = MobileScriptingLibrary.HighPrecisionValidationService.DeviceInfo()
        algorithmList =List[MobileScriptingLibrary.HighPrecisionValidationService.Algorithm]()
        algorithm = MobileScriptingLibrary.HighPrecisionValidationService.Algorithm()
        algorithm.Name = "VideoFreeze"
        algorithm.IsReferenceBased = True
        algorithm.Params = "jewoJIk1hdGNoU2NvcmUiOiAwLjk5LAoJIk1hc2tEZXRhaWxzIjogewoJCSJ4Y29yZCI6IDE3NiwKCQkieWNvcmQiOiAyMjMsCgkJIndpZHRoIjogMzc4LAoJCSJoZWlnaHQiOiAyNTQKCX0KfQ=="
    #    base64input = base64.b64encode(bytes(json_input), 'utf-8')
    #    algorithm.Params = base64input
        algorithm.MinDuration = 1000
        algorithm.MinTimeGap = 1000
        algorithmList.Add(algorithm)
        request.Duration = 600#Duration in seconds. How many seconds the executor should record the frames.
        request.Token = reservationResponse.Data.Token
        request.Algorithms = algorithmList
        request.DeviceInfo = deviceInfo 
        response = dut.validator.StartHighPrecisionFrameAnalysis(request)
        logger.Log("Response - " + response.Data.Token)
        if (response.Status):
            logger.Log("TRUE")
        #for i in range(0,4):
            #dut.controller.sendCommand("Ok")
            time.sleep(1)
            dut.Tap(315,1699)
            
        time.sleep(400)
        statusRequest = MobileScriptingLibrary.HighPrecisionValidationService.VideoAnalysisStatusRequest()
        statusRequest.Token = response.Data.Token
        statusResponse = dut.validator.GetHighPrecisionFrameAnalysisResult(statusRequest)
        #dut.validator.StopHighPrecisionFrameAnalysis(response.Data.Token)
        logger.Log("StatusRespose - " + str(statusResponse))
        dut.CommitTestResult("PASSED")

        dut.Stop()
        #dut.validator.StopAllHighPrecisionFrameAnalysis()
        #dut.CloseApp() 
        time.sleep(10)






#'''''''''''''''''''''''''END AUTOGENERATED CODE''''''''''''''''''''''''''' 
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' 