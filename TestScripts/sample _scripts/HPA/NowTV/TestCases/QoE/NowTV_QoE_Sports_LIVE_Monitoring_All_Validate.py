# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: QOE1
# TestCase Name: NowTV_QoE_Sports_LIVE_Monitoring_All

# GIVEN I am on Sports LIVE page within the NOW TV
# WHEN I play Sports channel continuously in configured interval
# THEN I should be able to find the startup failures, tuning time
# and video buffering time

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import sys, time, os, datetime, importlib, timeit

sys.path.append("../../")

# *********************************Importing required Files*********************
from android_core.app import AndroidBase
from android_core import common as common
from Library import Common_Library_QoE as comQoe
from android_core.msg import Message as msg
from Library.FalconEyeCube.Library import CubeAPI as cubeAPI


class TC_QOE1(AndroidBase):

    description = "Looping through the Sports channels and finding the QoE parameters"
    category_type = 'Sports'
    asset_name = 'Live'
    last_channel_programme = ""
    #down_bw_ranges = [512,1024,2048,4086]
    down_bw_ranges = list(xrange(100))
    swipe_count = 1
    # ***************** Implementation of the functionality ********************
    def run_script(self, dut, logger, MobileScriptingLibrary):
        try:
            confFile = self.confFile
            if not dut.WaitForElement(MobileScriptingLibrary.Constants.ElementType.Id,
                                       confFile.APP_HOME, confFile.MORETIMEOUT):
                logger.Log("App not launched")
                self.test_result = False
            else:
                logger.Log("Now TV App is launched successfully")

                cubeAPI.InitializeCube(dut, logger, confFile.QOE_DB)
                cubeAPI.CubeDeleteNetworkParams()

                # navigation to watch live video
                for capped_bw in self.down_bw_ranges:
                    self.swipe_count = 1
                    imageName = "QoE_" + comQoe.getUniqueFileName(dut) + "_StartLoop"
                    dut.validator.QuickCapture(imageName)
                    cubeAPI.CubeChokeNetwork(limited_bandwidth_down = capped_bw)
                    if not (common.Click(dut,MobileScriptingLibrary.Constants.ElementType.XPath,
                                         confFile.MENU_ICON)):
                        break

                    time.sleep(confFile.MAXTIMEOUT)
                    if not (common.Click(dut,MobileScriptingLibrary.Constants.ElementType.XPath,
                                         confFile.SPORTS_BUTTON)):
                        break

                    time.sleep(confFile.SHORT_WAITTIME)
                    if not (common.Click(dut,MobileScriptingLibrary.Constants.ElementType.XPath,
                                         confFile.SPORTS_WATCH_LIVE)):
                        break

                    time.sleep(confFile.MAXTIMEOUT)
                    dut.SetOrientation("Portrait")
                    time.sleep(5)
                    if not dut.WaitForElement(MobileScriptingLibrary.Constants.ElementType.XPath,
                                              "(//android.widget.ImageView[@content-desc='Play button'])["+str(self.swipe_count)+"]",
                                               confFile.MORETIMEOUT):
                        logger.Log("Failed to load assets")
                        self.test_result = False
                    i = 0

                    while i < confFile.NO_OF_CHANNELS and self.test_result == True:
                        tuning_time = 0
                        tune_failure = 0
                        buffering_ratio = 0
                        checking_time = 0
                        current_channel_programme = dut.GetText(MobileScriptingLibrary.Constants.ElementType.XPath,
                                                                confFile.FIRST_CHANNEL_PROGRAMME_NAME)

                        cubeAPI.CubeEnableNetworkdataPush()
                        play_button_xpath = ''

                        if not current_channel_programme == self.last_channel_programme:
                            self.last_channel_programme = current_channel_programme
                            #if not (common.Click(dut,MobileScriptingLibrary.Constants.ElementType.XPath,
                            play_button_xpath = "(//android.widget.ImageView[@content-desc='Play button'])["+str(self.swipe_count)+"]"
                                # imageName = "QoE_" + comQoe.getUniqueFileName(dut) + "_PlayButton1NotFound"
                                # dut.validator.QuickCapture(imageName)
                                # break
                        else:
                            self.swipe_count += 1
                            if dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.XPath,
                                          "(//android.widget.ImageView[@content-desc='Play button'])["+
                                                                                str(self.swipe_count)+"]"):
                                #if not (common.Click(dut,MobileScriptingLibrary.Constants.ElementType.XPath,
                                play_button_xpath = "(//android.widget.ImageView[@content-desc='Play button'])["+str(self.swipe_count)+"]"
                                    # imageName = "QoE_" + comQoe.getUniqueFileName(dut) + "_PlayButton"+str(self.swipe_count)+"NotFound"
                                    # dut.validator.QuickCapture(imageName)
                                    # break
                            else:
                                logger.Log("All the channels have been played successfully")
                                break
                        # Calculating startup time
                        # check_Time_start = timeit.default_timer()
                        # checking_time = 0
                        # if (dut.WaitForElement(MobileScriptingLibrary.Constants.ElementType.Id,
                        #                        confFile.WATCH_FROM_BEGIN_BUTTON, confFile.MINTIMEOUT)):
                        #     if not (common.Click(dut, MobileScriptingLibrary.Constants.ElementType.Id,
                        #                          confFile.WATCH_FROM_BEGIN_BUTTON)):
                        #         break
                        # else:
                        #     checking_time = timeit.default_timer() - check_Time_start

                        retry = 0
                        #detect_motion_date_time = datetime.datetime.utcnow()
                        # Calculating startup time
                        tuning_time, detect_motion_date_time = comQoe.start_up_time(dut, [
                            MobileScriptingLibrary.Constants.ElementType.XPath,
                            play_button_xpath])
                        while retry <= 1:

                            if tuning_time <= 0:
                                if (dut.WaitForElement(MobileScriptingLibrary.Constants.ElementType.Id,
                                                       confFile.WATCH_FROM_BEGIN_BUTTON, confFile.SHORT_WAITTIME)):
                                    tuning_time, detect_motion_date_time = comQoe.start_up_time(dut, [MobileScriptingLibrary.Constants.ElementType.Id,
                                                 confFile.WATCH_FROM_BEGIN_BUTTON])
                                    checking_time = 0
                                    retry += 1
                                else:
                                    break
                            else:
                                break

                        i += 1
                        channel = "Sports channel " + str(i)
                        self.custom_dict.update({'channel_name': channel})
                        if tuning_time > 0:
                            #date_time = datetime.datetime.utcnow()
                            pushStatus = cubeAPI.QoePush(common.QoEParams.START_UP_FAILURE, detect_motion_date_time, tune_failure,
                                                          self.category_type, self.asset_name, capped_bw, self.custom_dict)
                            logger.Log("No Startup Failure detected for " + channel)
                            pushStatus = cubeAPI.QoePush(common.QoEParams.START_UP_TIME, detect_motion_date_time, tuning_time,
                                                          self.category_type, self.asset_name, capped_bw, self.custom_dict)
                            logger.Log("Startup Time for " + channel + " : " + str(tuning_time) + " sec")
                            dut.CommitStepResult("[" + channel + "] Startup time : " + str(tuning_time),
                                                       common.TestResult.PASSED)
                            if pushStatus[common.QoEParams.STATUS]:
                                logger.Log(msg.STARTUP_TIME_PUSHED)
                            else:
                                logger.Log(msg.STARTUP_TIME_PUSH_FAILED)
                            # Calculating buffering time at unrestricted bandwidth
                            buffering_ratio = comQoe.CalculateBufferingTime1(dut, 20,
                                                    self.category_type,self.asset_name, capped_bw, self.custom_dict)
                            date_time = datetime.datetime.utcnow()
                            cubeAPI.CubeDisableNetworkdataPush()
                            if buffering_ratio > 0:
                                pushStatus = cubeAPI.QoePush(common.QoEParams.BUFFERING_RATIO, date_time, buffering_ratio,
                                                          self.category_type, self.asset_name, capped_bw, self.custom_dict)
                                if pushStatus[common.QoEParams.STATUS]:
                                    logger.Log(msg.BUFFERING_RATIO_PUSHED)
                                else:
                                    logger.Log(msg.BUFFERING_RATIO_PUSH_FAILED)
                                dut.CommitStepResult(
                                    "[" + channel + "] Buffer ratio =" + str(buffering_ratio),
                                    common.TestResult.PASSED)
                                logger.Log("Buffer Ratio for " + channel + " = " + str(buffering_ratio))
                            else:
                                dut.CommitStepResult(
                                    "[" + channel + "] Buffer ratio = " + str(buffering_ratio),
                                    common.TestResult.PASSED)
                            comQoe.CheckVideoPlaybackFailure(dut, self.category_type, self.asset_name, capped_bw, self.custom_dict)
                        else:
                            cubeAPI.CubeDisableNetworkdataPush()
                            tune_failure = 1
                            date_time = datetime.datetime.utcnow()
                            imageName = "QoE_" + comQoe.getUniqueFileName(dut) + "_Startup_failure"
                            imagePath = dut.validator.QuickCapture(imageName)

                            logger.Log("Video startup failure detected. Image Name : " + imageName)

                            pushStatus = cubeAPI.QoePush(common.QoEParams.START_UP_FAILURE, date_time, tune_failure,
                                                       self.category_type, self.asset_name, capped_bw, self.custom_dict)
                            logger.Log(
                             "Startup Failure detected for " + channel)
                            dut.CommitStepResult("[" + channel + "] Startup failure detected",
                                                   common.TestResult.FAILED)
                            if pushStatus[common.QoEParams.STATUS]:
                             logger.Log(msg.STARTUP_FAILURE_PUSHED)
                            else:
                                 logger.Log(msg.STARTUP_FAILURE_PUSH_FAILED)

                        element_check_count = 0
                        while not dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.XPath,
                                                     "(//android.widget.ImageView[@content-desc='Play button'])["+str(self.swipe_count)+"]"):
                            element_check_count += 1
                            if element_check_count == confFile.MAXCOUNT:
                                dut.CommitStepResult("Play button could not be found.",common.TestResult.FAILED)
                                imageName = "QoE_" + comQoe.getUniqueFileName(dut) + "_PlayButtonNotFound"
                                dut.validator.QuickCapture(imageName)
                                self.test_result = False
                                break
                            time.sleep(confFile.TIMEOUT)
                            if not common.send_back_key(dut, confFile.MAXCOUNT):
                                dut.CommitStepResult("Sending Back key failed", common.TestResult.FAILED)
                                self.test_result = False
                                break
                            time.sleep(confFile.TIMEOUT)

                        else:
                            logger.Log("Navigated back to Sports Live screen successfully")
                            dut.CommitStepResult("[" + channel + "] Navigated back to Sports Live screen"
                                                                                    , common.TestResult.PASSED)
                            dut.SetOrientation("Portrait")
                            time.sleep(confFile.MAXTIMEOUT)
        except:
            self.test_result = False
            logger.Log("Exception raised in main function" +
            str(sys.exc_info()[0])+ str(sys.exc_info()[1]) + "Line No:"+str(sys.exc_info()[2].tb_lineno) + \
            str(os.path.split(sys.exc_info()[2].tb_frame.f_code.co_filename)[1]))
        finally:
            time.sleep(5)
            cubeAPI.CubeDisableNetworkdataPush()
            cubeAPI.CubeDeleteNetworkParams()
            logger.Log("Calling closeapp......")
            dut.CloseApp()


if __name__ == "__main__":
    test_script = TC_QOE1()
    test_script.run()

# =============================================================================
# Author: Faisal/Tharun
# Date: 15-Mar-2018
# Device Type: Android
# =============================================================================
