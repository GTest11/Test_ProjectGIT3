# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: QOE3
# TestCase Name: NowTV_QoE_Movies_VOD_Monitoring_All

# GIVEN I am on Movies VOD page within the NOW TV
# WHEN I play movies assets continuously in configured interval
# THEN I should be able to find the startup failures, tuning time
# and video buffering time

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import sys, time, os, datetime, timeit

sys.path.append("../../")

# *********************************Importing required Files*********************
from android_core.app import AndroidBase
from android_core import common as common
from Library import Common_Library_QoE as comQoe
from android_core.msg import Message as msg
from Library.FalconEyeCube.Library import CubeAPI as cubeAPI


class TC_QOE3(AndroidBase):
    description = "Looping through the Movies VOD assets and finding the QoE parameters"
    category_type = 'Movies'
    asset_name = 'VOD'
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
                    self.test_result = True
                    end_reached_flag = False
                    imageName = "QoE_" + comQoe.getUniqueFileName(dut) + "_StartLoop"
                    dut.validator.QuickCapture(imageName)
                    cubeAPI.CubeChokeNetwork(limited_bandwidth_down=capped_bw)
                    # Navigation to Movies VOD video
                    if not (common.Click(dut, MobileScriptingLibrary.Constants.ElementType.XPath, confFile.MENU_ICON)):
                        break

                    time.sleep(confFile.MAXTIMEOUT)
                    if not (common.Click(dut, MobileScriptingLibrary.Constants.ElementType.XPath,
                                         confFile.MOVIES_BUTTON)):
                        break

                    time.sleep(confFile.SHORT_WAITTIME)
                    if not (common.Click(dut, MobileScriptingLibrary.Constants.ElementType.XPath,
                                         confFile.ALL_MOVIES_OPTION)):
                        break

                    time.sleep(confFile.SHORT_WAITTIME)
                    dut.SetOrientation("Portrait")
                    time.sleep(confFile.SHORT_WAITTIME)
                    if not dut.WaitForElement(MobileScriptingLibrary.Constants.ElementType.XPath,
                                              confFile.ALL_MOVIES_FIRST_TILE, confFile.MORETIMEOUT):
                        logger.Log("Failed to load VOD assets")
                        self.test_result = False
                    item_played = 0

                    while self.test_result:
                        i = 1
                        j = i + confFile.VOD_ASSET_COUNT_IN_ONE_ROW # first item in next row
                        if (dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.XPath,
                                                 common.get_movies_tile(i))):
                            play_count = i
                        elif (dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.XPath,
                                                   common.get_movies_tile(j))):
                            play_count = j
                        else:
                            break

                        for loop in range(confFile.VOD_ASSET_COUNT_IN_ONE_ROW):
                            item_played += 1

                            common.Click(dut,MobileScriptingLibrary.Constants.ElementType.XPath,
                                         common.get_movies_tile(play_count))
                            dut.WaitForElement(MobileScriptingLibrary.Constants.ElementType.Id,
                                               confFile.ALL_MOVIES_ITEM_NAME, confFile.MORETIMEOUT)
                            channel = dut.GetText(MobileScriptingLibrary.Constants.ElementType.Id,
                                                     confFile.ALL_MOVIES_ITEM_NAME)
                            self.custom_dict.update({'channel_name': channel})
                            cubeAPI.CubeEnableNetworkdataPush()

                            if not(dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.Id,
                                                        confFile.ALL_MOVIES_PLAYBUTTON)):
                                logger.Log("Play button is not found. Pressing back")
                                common.send_back_key(dut)
                                play_count += 1
                                continue

                            else:
                                common.Click(dut, MobileScriptingLibrary.Constants.ElementType.Id,
                                             confFile.ALL_MOVIES_PLAYBUTTON)

                                check_Time_start = timeit.default_timer()
                                checking_time = 0
                                if (dut.WaitForElement(MobileScriptingLibrary.Constants.ElementType.Id,
                                                       confFile.MOVIES_RESUME_BUTTON, confFile.MINTIMEOUT)):
                                    common.Click(dut, MobileScriptingLibrary.Constants.ElementType.Id,
                                                 confFile.MOVIES_RESUME_BUTTON)
                                else:
                                    checking_time = timeit.default_timer() - check_Time_start

                            tuning_time = 0
                            tune_failure = 0
                            buffering_ratio = 0

                            retry = 0
                            detect_motion_date_time = datetime.datetime.utcnow()
                            while retry <= 1:
                                # Calculating startup time
                                tuning_time, detect_motion_date_time = comQoe.start_up_time(dut)
                                if tuning_time <= 0:
                                    if (dut.WaitForElement(MobileScriptingLibrary.Constants.ElementType.Id,
                                                       confFile.MOVIES_RESUME_BUTTON, confFile.SHORT_WAITTIME)):
                                        common.Click(dut, MobileScriptingLibrary.Constants.ElementType.Id,
                                                     confFile.MOVIES_RESUME_BUTTON)
                                        checking_time = 0
                                        retry += 1
                                    else:
                                        break
                                else:
                                    break

                            i += 1
                            if tuning_time > 0:
                                tuning_time += checking_time
                                #date_time = datetime.datetime.utcnow()
                                pushStatus = cubeAPI.QoePush(common.QoEParams.START_UP_FAILURE, detect_motion_date_time, tune_failure,
                                                              self.category_type, self.asset_name, capped_bw, self.custom_dict)
                                logger.Log("No Startup Failure detected for Movies VOD " + str(item_played))
                                pushStatus = cubeAPI.QoePush(common.QoEParams.START_UP_TIME, detect_motion_date_time, tuning_time,
                                                              self.category_type, self.asset_name, capped_bw, self.custom_dict)
                                logger.Log("Startup Time for Movies VOD " + str(item_played) + " : " + str(tuning_time) + " sec")
                                dut.CommitStepResult("[Movies VOD " + str(item_played) + "] Startup time : " + str(tuning_time),
                                                           common.TestResult.PASSED)
                                if pushStatus[common.QoEParams.STATUS]:
                                    logger.Log(msg.STARTUP_TIME_PUSHED)
                                else:
                                    logger.Log(msg.STARTUP_TIME_PUSH_FAILED)
                                # Calculating buffering time at unrestricted bandwidth
                                buffering_ratio = comQoe.CalculateBufferingTime(dut, confFile.QoEMONITORING_INTERVAL,
                                                        self.category_type,self.asset_name,capped_bw, self.custom_dict)
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
                                        "[Movies VOD " + str(item_played) + "] Buffer ratio =" + str(buffering_ratio),
                                        common.TestResult.PASSED)
                                    logger.Log("Buffer Ratio for Movies VOD " + str(item_played) + " = " + str(buffering_ratio))
                                else:
                                    dut.CommitStepResult(
                                        "[Movies VOD " + str(item_played) + "] Buffer ratio = " + str(buffering_ratio),
                                        common.TestResult.PASSED)
                                comQoe.CheckVideoPlaybackFailure(dut, self.category_type, self.asset_name,
                                                                 capped_bw, self.custom_dict)
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
                                    "Startup Failure detected for Movies VOD " + str(item_played))
                                dut.CommitStepResult("[Movies VOD " + str(item_played) + "] Startup failure detected",
                                                     common.TestResult.FAILED)
                                if pushStatus[common.QoEParams.STATUS]:
                                    logger.Log(msg.STARTUP_FAILURE_PUSHED)
                                else:
                                    logger.Log(msg.STARTUP_FAILURE_PUSH_FAILED)

                            play_count += 1

                            element_check_count = 0
                            while not dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.XPath,
                                                           confFile.ALL_MOVIES_TITLE):
                                element_check_count += 1
                                if element_check_count == confFile.MAXCOUNT:
                                    dut.CommitStepResult("Failed to navigate to All Movies menu", common.TestResult.FAILED)
                                    imageName = "QoE_" + comQoe.getUniqueFileName(dut) + "_PlayButtonNotFound"
                                    dut.validator.QuickCapture(imageName)
                                    self.test_result = False
                                    break
                                time.sleep(confFile.TIMEOUT)
                                if not common.send_back_key(dut,confFile.MAXCOUNT):
                                    dut.CommitStepResult("Sending Back key failed",common.TestResult.FAILED)
                                    self.test_result = False
                                    break
                                time.sleep(confFile.TIMEOUT)

                            else:
                                logger.Log("Navigated back to Movies VOD screen successfully")
                                dut.CommitStepResult("[Movies VOD " + str(item_played) + "] Navigated back to Movies VOD screen",
                                                     common.TestResult.PASSED)
                                dut.SetOrientation("Portrait")
                                time.sleep(confFile.MAXTIMEOUT)
                            if item_played < confFile.NO_OF_VOD:
                                pass
                            else:
                                end_reached_flag = True
                                break

                        if not end_reached_flag:
                            dut.VerticalSwipe(confFile.AllMovie_Swipe_Vertical_BottomToTop_y1,
                                              confFile.AllMovie_Swipe_Vertical_BottomToTop_y2,
                                              confFile.AllMovie_Swipe_Vertical_BottomToTop_x2, confFile.MOVIES_VOD_SWIPE_TIME)
                            time.sleep(confFile.SHORT_WAITTIME)
                        else:
                            common.Click(dut,MobileScriptingLibrary.Constants.ElementType.XPath, confFile.MENU_ICON)
                            time.sleep(confFile.TIMEOUT)
                            common.Click(dut, MobileScriptingLibrary.Constants.ElementType.XPath,
                                         confFile.MOVIES_BUTTON)
                            time.sleep(confFile.TIMEOUT)
                            common.Click(dut, MobileScriptingLibrary.Constants.ElementType.XPath,
                                         confFile.WATCH_LIVE)
                            time.sleep(confFile.TIMEOUT)
                            break
        except:
            self.test_result = False
            logger.Log("Exception raised in main function" +
            str(sys.exc_info()[0])+ str(sys.exc_info()[1]) + "Line No:"+str(sys.exc_info()[2].tb_lineno) + \
            str(os.path.split(sys.exc_info()[2].tb_frame.f_code.co_filename)[1]))
        finally:
            time.sleep(10)
            cubeAPI.CubeDisableNetworkdataPush()
            cubeAPI.CubeDeleteNetworkParams()
            logger.Log("Calling closeapp......")
            dut.CloseApp()


if __name__ == "__main__":
    test_script = TC_QOE3()
    test_script.run()

# =============================================================================
# Author: Faisal/Tharun
# Date: 15-Mar-2018
# Device Type: Android
# =============================================================================