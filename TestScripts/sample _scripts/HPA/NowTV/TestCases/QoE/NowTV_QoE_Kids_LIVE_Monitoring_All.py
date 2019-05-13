# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: QOE6
# TestCase Name: NowTV_QoE_Kids_LIVE_Monitoring_All

# GIVEN I am on Kids LIVE page within the NOW TV
# WHEN I play Kids channel continuously in configured interval
# THEN I should be able to find the startup failures, tuning time
# and video buffering time

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import sys, time, os, datetime, timeit

sys.path.append("../../")

# *********************************Importing required Files*********************
from android_core.app import AndroidBase
from android_core import common as common
from android_core.msg import Message as msg
from Library import Common_Library_QoE as comQoe
from Library.FalconEyeCube.Library import CubeAPI as cubeAPI


class TC_QOE6(AndroidBase):
    description = "Looping through the kids channels and finding the QoE parameters"
    asset_name = 'Live'
    category_type = 'Kids'
    down_bw_ranges = [512,1024,2048,4086]

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

                for capped_bw in self.down_bw_ranges:
                    imageName = "QoE_" + comQoe.getUniqueFileName(dut) + "_StartLoop"
                    dut.validator.QuickCapture(imageName)
                    cubeAPI.CubeChokeNetwork(limited_bandwidth_down=capped_bw)
                    # navigation to watch live video
                    if not (common.Click(dut, MobileScriptingLibrary.Constants.ElementType.XPath,
                                         confFile.MENU_ICON)):  # element type is ClassName
                        break

                    time.sleep(confFile.MAXTIMEOUT)
                    if not (common.Click(dut, MobileScriptingLibrary.Constants.ElementType.XPath,
                                         confFile.KIDS_BUTTON)):
                        break
                    time.sleep(confFile.MAXTIMEOUT)
                    if not (common.Click(dut, MobileScriptingLibrary.Constants.ElementType.XPath,
                                         confFile.KIDS_BUTTON)):
                        time.sleep(confFile.MORETIMEOUT)
                        break
                    # time.sleep(confFile.SHORT_WAITTIME)
                    # dut.SetOrientation("Portrait")
                    time.sleep(confFile.SHORT_WAITTIME)
                    if dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.Id,
                                            confFile.OK):
                        common.Click(dut, MobileScriptingLibrary.Constants.ElementType.Id,
                                     confFile.OK)
                        break

                    if not dut.WaitForElement(MobileScriptingLibrary.Constants.ElementType.XPath,
                                              confFile.NOW_TV,
                                              confFile.MORETIMEOUT):
                        logger.Log("Failed to load assets")
                        self.test_result = False
                    asset_no_in_screen = 1
                    i = 0
                    re_count = 1
                    asset_count=1
                    asset_text_count=1
                    last_played_ent_name = ''
                    while True:
                        tuning_time = 0
                        tune_failure = 0
                        buffering_ratio = 0
                        checking_time = 0

                        cubeAPI.CubeEnableNetworkdataPush()

                        while not dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.Id,
                                                       confFile.ON_NOW):
                            
                            dut.VerticalSwipe(confFile.Kids_Swipe_Vertical_BottomToTop_y1,
                                                confFile.Kids_Swipe_Vertical_BottomToTop_y2,
                                                confFile.Kids_Swipe_Vertical_BottomToTop_x2,
                                                confFile.KIDS_LIVE_SWIPE_TIME)
                            

                        while asset_no_in_screen < confFile.KIDS_ITERATION:
                            if dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.XPath,
                                                    common.get_kids_live_tile(asset_count)):
                                if dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.XPath,
                                        common.get_text_kids_item(asset_text_count)):
                                    ent_name = common.GetText(dut, MobileScriptingLibrary.Constants.ElementType.XPath,
                                                common.get_text_kids_item(asset_text_count))
                                    if ent_name == last_played_ent_name:
                                        if (re_count < 4):
                                            if dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.XPath,
                                                                common.get_text_kids_item(asset_text_count)):
                                                dut.HorizontalSwipe(confFile.Kids_Swipe_Horizontal_BottomToTop_x1,
                                                                    confFile.Kids_Swipe_Horizontal_BottomToTop_x2,
                                                                    confFile.Kids_Swipe_Horizontal_BottomToTop_y2,
                                                                    confFile.KIDS_HORIZONTAL_LIVE_SWIPE_TIME)
                                                re_count +=1

                                        else:
                                            asset_text_count +=1
                                            asset_count +=1

                                    else:
                                        logger.Log("Last Played Kids channel changing to " + ent_name)
                                        last_played_ent_name = ent_name
                                        break
                            asset_no_in_screen += 1
                            logger.Log("Current asset number incremented to :" + str(asset_no_in_screen))

                        if asset_no_in_screen < confFile.KIDS_ITERATION:
                            if not (common.Click(dut, MobileScriptingLibrary.Constants.ElementType.XPath,
                                                 common.get_text_kids_item(asset_text_count) )):
                                imageName = "QoE_" + comQoe.getUniqueFileName(dut) + "_PlaybuttonNotFound"
                                dut.validator.QuickCapture(imageName)
                                break

                            tuning_time,detect_motion_date_time = comQoe.start_up_time(dut)



                            i += 1
                            channel = "Kids channel " + str(i)
                            self.custom_dict.update({'channel_name': channel})
                            if tuning_time > 0:
                                tuning_time += checking_time
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
                                buffering_ratio = comQoe.CalculateBufferingTime(dut,confFile.QoEMONITORING_INTERVAL,
                                                                                self.category_type, self.asset_name, capped_bw,
                                                                                self.custom_dict)
                                date_time = datetime.datetime.utcnow()
                                cubeAPI.CubeDisableNetworkdataPush()
                                if buffering_ratio > 0:
                                    pushStatus = cubeAPI.QoePush(common.QoEParams.BUFFERING_RATIO, date_time,
                                                                 buffering_ratio, self.category_type, self.asset_name,
                                                                 capped_bw, self.custom_dict)
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
                                comQoe.CheckVideoPlaybackFailure(dut, self.category_type, self.asset_name, capped_bw,
                                                                 self.custom_dict)
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
                            while not dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.Id,
                                                           confFile.ON_NOW):
                                element_check_count += 1
                                if element_check_count == confFile.MAXCOUNT:
                                    dut.CommitStepResult("Play button could not be found.", common.TestResult.FAILED)
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
                                logger.Log("Navigated back to Kids Live screen successfully")
                                dut.CommitStepResult("[" + channel + "] Navigated back to Kids Live screen",
                                                     common.TestResult.PASSED)


                                dut.HorizontalSwipe(confFile.Kids_Swipe_Horizontal_BottomToTop_x1,
                                                    confFile.Kids_Swipe_Horizontal_BottomToTop_x2,
                                                    confFile.Kids_Swipe_Horizontal_BottomToTop_y2,
                                                    confFile.KIDS_HORIZONTAL_LIVE_SWIPE_TIME)


                        else:  # Completed the Kids live assets
                            logger.Log("Completed Kids live assets")
                            break
                    if not (common.Click(dut, MobileScriptingLibrary.Constants.ElementType.Id,
                                                 confFile.BACK_KIDS)):

                        time.sleep(confFile.MAXTIMEOUT)
                    if not (common.Click(dut, MobileScriptingLibrary.Constants.ElementType.Id,
                                         confFile.LEAVE_NOW)):

                        time.sleep(confFile.MAXTIMEOUT)
                    if dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.XPath, confFile.MOVIES_BUTTON):
                        dut.Click(MobileScriptingLibrary.Constants.ElementType.XPath, confFile.MOVIES_BUTTON)
                        time.sleep(confFile.TIMEOUT)
                        
                    if dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.XPath, confFile.WATCH_LIVE):
                        dut.Click(MobileScriptingLibrary.Constants.ElementType.XPath, confFile.WATCH_LIVE)
                        time.sleep(confFile.TIMEOUT)
                        

        except:
            self.test_result = False
            logger.Log("Exception raised in main function" +
                       str(sys.exc_info()[0]) + str(sys.exc_info()[1]) + "Line No:" + str(sys.exc_info()[2].tb_lineno) + \
                       str(os.path.split(sys.exc_info()[2].tb_frame.f_code.co_filename)[1]))
        finally:
            time.sleep(10)
            cubeAPI.CubeDisableNetworkdataPush()
            cubeAPI.CubeDeleteNetworkParams()
            logger.Log("Calling closeapp......")
            dut.CloseApp()

if __name__ == "__main__":
    test_script = TC_QOE6()
    test_script.run()

# =============================================================================
# Author: Koustubha.K
# Date: 1-June-2018
# Device Type: Android




