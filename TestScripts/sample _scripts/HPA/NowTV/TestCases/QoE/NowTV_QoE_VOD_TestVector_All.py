# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: QoE9
# TestCase Name: NowTV_QoE_VOD_TestVector_All

# *********************TestCase Description**********************************
# Finding the QoE Parameters startup time, buffering ratio, startup failure
# and playback failure based on the inputs/usecase given in the TestScenario
# file while choking the network as per the inputs from the TestVector file.

# Prerequisites:
# 1) TestScenario File : An excel file having the details like category name,
#    asset type, Channel No, usecase, name of the TestVector file to be
#    used, Channel Play Time (in minutes) and loopcount.
#    It is saved in TestScenarios folder. The name of this file should be
#    given as the value of custom property 'qoe_scenario_file'.
# 2) TestVector File : An excel file having the details like Time,
#    limited bandwidth up(kbps), limited bandwidth down(kbps), delay, jitter
#    and packetloss.
#    It is saved in TestVectors folder.

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import sys, time, os, datetime, timeit, threading, difflib, re

sys.path.append("../../")

# ********************************Importing required Files*********************
from android_core.app import AndroidBase
from android_core import common as common
from android_core.msg import Message as msg
from Library import Common_Library_QoE as comQoe
from Library.FalconEyeCube.Library import CubeAPI as cubeAPI


class TC_QOE9(AndroidBase):
    timer = None  # Timer object to thread the Choke functionality
    test_vector_list = None  # Test vector class obj list
    choke_index = 0  # Current Choke network index
    asset_name = ''
    capped_bw = 0

# ***************************** navigate_to_home *******************************
    def navigate_to_home(self, dut, logger, MobileScriptingLibrary):

        confFile = self.confFile
        reached_home = False
        check_count = 0
        while not dut.WaitForElement(MobileScriptingLibrary.Constants.ElementType.Id,
                                        confFile.SEARCH_BUTTON, confFile.MAXTIMEOUT):
            check_count += 1
            time.sleep(confFile.TIMEOUT)
            if not common.send_back_key(dut, maxcount=confFile.MAXCOUNT):
                self.report("Sending Back key failed", common.TestResult.FAILED)
                self.test_result = False
            if check_count == confFile.MAXCOUNT:
                self.report("Failed to navigate back to Home screen", common.TestResult.FAILED)
                self.test_result = False
                break
        else:
            logger.Log("Navigated back to Home screen successfully")
            reached_home = True
            dut.SetOrientation("Portrait")
            time.sleep(confFile.MAXTIMEOUT)
        if not reached_home:
            self.report("Failed to navigate back to home screen", common.TestResult.FAILED)
            self.test_result = False
        else:
            self.report("Successfully navigated back to home screen", common.TestResult.PASSED, image=False)

# ***************************** select_channel *******************************
    def select_channel(self, channel, dut, logger, MobileScriptingLibrary):
        selected_kids_vod = False
        try:
            confFile = self.confFile
            found_channel = False
            # Tapping on Search icon
            tapped = common.tap_if_present(dut, MobileScriptingLibrary.Constants.ElementType.Id, confFile.SEARCH_BUTTON,
                                         "Search Icon", logger)
            time.sleep(confFile.TIMEOUT)
            if not tapped:
                self.report("Failed to tap on Search icon", common.TestResult.FAILED)
                return found_channel

            # Entering programme name on search field
            sent = dut.SendKeys(MobileScriptingLibrary.Constants.ElementType.XPath, confFile.X_EDIT_BOX, channel)
            if not sent:
                self.report("Failed to enter movie name on search field", common.TestResult.FAILED)
                return found_channel

            # Verifying search results
            present = dut.WaitForElement(MobileScriptingLibrary.Constants.ElementType.XPath, confFile.X_FIRST_SEARCH_RESULT,
                                         confFile.MAX_ITERATION)
            if not present:
                self.report("Failed to fetch search results", common.TestResult.FAILED)
                return found_channel
            check_count=0
            # Selecting the first search result
            while check_count<confFile.MAXCOUNT:
                tapped = dut.TapElement(MobileScriptingLibrary.Constants.ElementType.XPath, confFile.X_FIRST_SEARCH_RESULT)
                time.sleep(confFile.TIMEOUT)
                if not tapped:
                    self.report("Failed to tap on search result", common.TestResult.FAILED)
                    return found_channel
                else:
                    if dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.XPath, confFile.X_FIRST_SEARCH_RESULT):
                        check_count += 1
                    else:
                        break
            time.sleep(confFile.WAITTIME)
            if dut.WaitForElement(MobileScriptingLibrary.Constants.ElementType.Id, confFile.ID_ALL_KIDS_ITEM_NAME_VOD, confFile.MAXTIMEOUT):
                selected_kids_vod = True
                logger.Log("Kids VOD selected")
                asset_name = dut.GetText(MobileScriptingLibrary.Constants.ElementType.Id, confFile.ID_ALL_KIDS_ITEM_NAME_VOD)
            else:
                asset_name = dut.GetText(MobileScriptingLibrary.Constants.ElementType.Id,confFile.ALL_MOVIES_ITEM_NAME)

            asset_name = (asset_name.replace(" ", "")).lower()
            channel = (channel.replace(" ", "")).lower()
            if asset_name == channel:
                retry = 1
                while retry < confFile.MAXCOUNT:
                    if dut.WaitForElement(MobileScriptingLibrary.Constants.ElementType.XPath if selected_kids_vod else
                                            MobileScriptingLibrary.Constants.ElementType.Id ,
                                            confFile.X_KIDS_PLAY_BUTTON if selected_kids_vod
                                            else confFile.ALL_MOVIES_PLAYBUTTON, confFile.MORETIMEOUT):
                        self.report("Navigated successfully to the required asset", common.TestResult.PASSED, image=False)
                        found_channel = True
                        break
                    else:
                        logger.Log("Play button not found..Swiping up.......")
                        dut.VerticalSwipe(confFile.Small_Swipe_Vertical_BottomToTop_y1,
                                          confFile.Small_Swipe_Vertical_BottomToTop_y2,
                                          confFile.Small_Swipe_Vertical_BottomToTop_x,
                                          confFile.MOVIES_VOD_SWIPE_TIME)
                        if dut.WaitForElement(MobileScriptingLibrary.Constants.ElementType.XPath, confFile.FIRST_PLAY_BUTTON, confFile.MAXTIMEOUT):
                            time.sleep(confFile.TIMEOUT)

                        else:
                            retry += 1
                            if retry==confFile.MAXCOUNT:
                                logger.Log("Play Button Not found..Sending Back")
                                return found_channel
            else:
                self.report("The required asset is not available on demand", common.TestResult.FAILED)

            return found_channel

        except:
            self.test_result = False
            logger.Log("Exception raised in select_channel function" +
                       str(sys.exc_info()[0]) + str(sys.exc_info()[1]) + str(sys.exc_info()[2].tb_lineno)
                       + str(os.path.split(sys.exc_info()[2].tb_frame.f_code.co_filename)[1]))

# ***************** Implementation of the functionality ********************
    def run_script(self, dut, logger, MobileScriptingLibrary):  # Executing Teststeps
        confFile = self.confFile
        self.timer = None
        try:
            logger.Log("run script***************")
            # Reading the values from excel files
            test_args = comQoe.get_test_args(dut)

            # variables from excel
            loopcount = int(test_args.LOOP_COUNT)
            self.category_type = test_args.CATEGORY_NAME
            channel_nos = test_args.CHANNEL_LIST
            logger.Log("r2*********")
            self.playback_time = test_args.CHANNEL_PLAY_TIME
            self.asset_name = test_args.ASSET_TYPE
            usecase = int(test_args.USECASE)
            self.test_vector_list = test_args.TEST_VECTOR_OBJLIST
            no_of_channels = len(channel_nos)
            if usecase == 3:
                channel_nos = channel_nos*(len(self.test_vector_list))

            cubeAPI.InitializeCube(dut,logger, confFile.QOE_DB)
            cubeAPI.CubeDeleteNetworkParams()
            for loop in range(0, loopcount):
                logger.Log("Loop " + str(loop+1))
                channel_count = 0
                self.choke_index = 0
                for channel in channel_nos:
                    kids_vod_selected = False
                    status = self.select_channel(channel, dut, logger, MobileScriptingLibrary)
                    if not status:
                        logger.Log("Select channel " + str(channel) + " in " + str(self.category_type) +" failed.")
                        logger.Log("Navigating back to home screen")
                        self.navigate_to_home(dut, logger, MobileScriptingLibrary)
                        continue
                    else:
                        if self.test_vector_list is not None and len(self.test_vector_list) > self.choke_index:
                            if usecase == 3:  # usecase3 does not require a time for choking
                                if channel_count == 0:
                                    cubeAPI.CubeChokeNetwork(
                                        limited_bandwidth_up=self.test_vector_list[self.choke_index].LIMITED_BW_UP,
                                        limited_bandwidth_down=self.test_vector_list[self.choke_index].LIMITED_BW_DOWN,
                                        delay=self.test_vector_list[self.choke_index].DELAY,
                                        jitter=self.test_vector_list[self.choke_index].JITTER,
                                        packetloss=self.test_vector_list[self.choke_index].PACKET_LOSS
                                    )
                                    self.capped_bw = self.test_vector_list[self.choke_index].LIMITED_BW_DOWN
                                    self.choke_index += 1
                                if not channel_count == no_of_channels-1:
                                    channel_count += 1
                                else:
                                    channel_count = 0
                            else:
                                if usecase == 2 and self.timer is not None:
                                    # For usecase2 need to restart the choking from beginning
                                    self.timer.cancel()
                                    self.choke_index = 0
                                    self.timer = None
                                if self.timer is None:
                                    self.timer = threading.Timer(0, comQoe.choke_network, [self])
                                    self.timer.start()
                        cubeAPI.CubeEnableNetworkdataPush()
                        checking_time = 0
                        if dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.Id,
                                                confFile.ALL_MOVIES_PLAYBUTTON):
                            self.custom_dict.update({'channel': channel})
                            common.Click(dut, MobileScriptingLibrary.Constants.ElementType.Id,
                                         confFile.ALL_MOVIES_PLAYBUTTON)
                        elif dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.XPath,
                                                    confFile.FIRST_PLAY_BUTTON):
                            self.custom_dict.update({'channel': channel})
                            common.Click(dut, MobileScriptingLibrary.Constants.ElementType.XPath,
                                         confFile.FIRST_PLAY_BUTTON)
                        else:
                            if dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.XPath,
                                                 confFile.X_KIDS_PLAY_BUTTON):
                                self.custom_dict.update({'channel': channel})
                                kids_vod_selected = True
                                common.Click(dut, MobileScriptingLibrary.Constants.ElementType.XPath,
                                        confFile.X_KIDS_PLAY_BUTTON)
                        comQoe.find_qoe_parameters(self, checking_time, channel, self.capped_bw, confFile, dut, logger, MobileScriptingLibrary)
                        element_check_count = 0
                        retry_val = 0
                        while not common.WaitForElement(dut, MobileScriptingLibrary.Constants.ElementType.Id,
                                                        confFile.SEARCH_BUTTON, "Search Icon",confFile.MAXTIMEOUT):
                            element_check_count += 1

                            time.sleep(confFile.TIMEOUT)
                            if kids_vod_selected:
                                while not common.WaitForElement(dut,MobileScriptingLibrary.Constants.ElementType.Id,
                                                                confFile.ID_KIDS_LEAVE_NOW,"Leave Now", confFile.MORETIMEOUT ):
                                    retry_val += 1
                                    if not common.send_back_key(dut, maxcount=confFile.MAXCOUNT):
                                        self.report("Sending Back key failed",common.TestResult.FAILED)
                                        self.test_result = False
                                    if retry_val==confFile.MAXCOUNT:
                                        self.report("Failed to Navigate to the Kids-Leave Now Button", common.TestResult.FAILED)
                                        self.test_result = False
                                        break
                                else:
                                    logger.Log("Are You sure want to leave Kids Page??..Leave now?")
                                    common.Click(dut, MobileScriptingLibrary.Constants.ElementType.Id,
                                                 confFile.ID_KIDS_LEAVE_NOW)
                                    common.send_back_key(dut, maxcount=confFile.MAXCOUNT)
                                    break

                                if element_check_count == confFile.MAXCOUNT:
                                    self.report("Failed to navigate back to Home screen", common.TestResult.FAILED)
                                    self.test_result = False
                                    break
                            else:
                                if not common.send_back_key(dut, maxcount=confFile.MAXCOUNT):
                                    self.report("Sending Back key failed",common.TestResult.FAILED)
                                    self.test_result = False
                                if element_check_count == confFile.MAXCOUNT:
                                    self.report("Failed to navigate back to Home screen",common.TestResult.FAILED)
                                    self.test_result = False
                                    break
                        else:
                            logger.Log("Navigated back to Home screen successfully")
                            self.report("[ VOD "+str(channel)+"Navigated back to Home screen",
                                common.TestResult.PASSED)
                            dut.SetOrientation("Portrait")
                            time.sleep(confFile.MAXTIMEOUT)

        except:
            self.test_result = False
            logger.Log("Exception raised in step-1" +
                       str(sys.exc_info()[0]) + str(sys.exc_info()[1]) + str(sys.exc_info()[2].tb_lineno)
                       + str(os.path.split(sys.exc_info()[2].tb_frame.f_code.co_filename)[1]))

        finally:
            if(self.timer != None):
                logger.Log(
                    "Timer is not None")
                self.timer.cancel()
            cubeAPI.CubeDisableNetworkdataPush()
            cubeAPI.CubeDeleteNetworkParams()
            logger.Log("Calling CloseApp......")
            dut.CloseApp()

if __name__ == "__main__":
    test_script = TC_QOE9()
    test_script.run()

# =============================================================================
# Author: Linda
# Date: 11/06/2018
# Device Type: Android
# =============================================================================
