# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID: QoE8
# TestCase Name: NowTV_QoE_LIVE_TestVector_All

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


class TC_QOE8(AndroidBase):
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
            time.sleep(confFile.TIMEOUT)
            if self.category_type == "Kids":
                if dut.WaitForElement(MobileScriptingLibrary.Constants.ElementType.Id,
                                      confFile.ID_KIDS_LEAVE_NOW, confFile.MAXTIMEOUT):
                    dut.Click(MobileScriptingLibrary.Constants.ElementType.Id,
                              confFile.ID_KIDS_LEAVE_NOW)
                time.sleep(confFile.TIMEOUT)
                if dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.XPath,
                                        confFile.MOVIES_BUTTON):
                    dut.Click(MobileScriptingLibrary.Constants.ElementType.XPath,
                              confFile.MOVIES_BUTTON)
                    time.sleep(confFile.TIMEOUT)
                time.sleep(confFile.TIMEOUT)
                if dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.XPath,
                                        confFile.WATCH_LIVE):
                    dut.Click(MobileScriptingLibrary.Constants.ElementType.XPath, confFile.WATCH_LIVE)
                    time.sleep(confFile.TIMEOUT)
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

#********************Navigate back to channels screen*******************
    def back_to_channel_screen(self, dut, logger, MobileScriptingLibrary ):
        try:
            confFile = self.confFile
            element_check_count = 0
            if self.category_type == "Kids":
                while not dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.Id,
                                                       confFile.ON_NOW):
                    element_check_count += 1
                    time.sleep(confFile.TIMEOUT)
                    if not common.send_back_key(dut, maxcount=confFile.MAXCOUNT):
                        self.report("Sending Back key failed", common.TestResult.FAILED)
                        self.test_result = False
                    if element_check_count == confFile.MAXCOUNT:
                        self.report("Failed to navigate back to channel screen", common.TestResult.FAILED)
                        self.test_result = False
                        break
                    time.sleep(confFile.TIMEOUT)
                else:
                    logger.Log("Navigated back to Kids Live screen successfully")
            else:
                while not common.WaitForElement(dut, MobileScriptingLibrary.Constants.ElementType.Id,
                                                confFile.WATCH_LIVE_TITLE, "Watch Live Title", confFile.MAXTIMEOUT):
                    element_check_count += 1
                    time.sleep(confFile.TIMEOUT)
                    if not common.send_back_key(dut, maxcount=confFile.MAXCOUNT):
                        self.report("Sending Back key failed", common.TestResult.FAILED)
                        self.test_result = False
                    if element_check_count == confFile.MAXCOUNT:
                        self.report("Failed to navigate back to channel screen", common.TestResult.FAILED)
                        self.test_result = False
                        break
                else:
                    self.navigate_to_home(dut, logger, MobileScriptingLibrary)
        except:
            logger.Log("Exception raised in back_to_channel_screen function " +
                       str(sys.exc_info()[0]) + str(sys.exc_info()[1]) + str(sys.exc_info()[2].tb_lineno)
                       + str(os.path.split(sys.exc_info()[2].tb_frame.f_code.co_filename)[1]))
#*************************Swiping checking if end of screen is reached******
    def swipe_check(self, dut, MobileScriptingLibrary, logger, end_screen):
        confFile = self.confFile
        swipe_retry_count = 1
        ImageName = dut.ReadProperty(1) + "_swipecheckimage"
        try:
            if not end_screen:
                imagePath = dut.validator.CaptureImage(confFile.SWIPE_CHECK_AREA_X,
                                                       confFile.SWIPE_CHECK_AREA_Y,
                                                       confFile.SWIPE_CHECK_AREA_W,
                                                       confFile.SWIPE_CHECK_AREA_H,
                                                       ImageName, confFile.DEFAULT_JPEGQUALITY,
                                                       confFile.DEFAULT_OVERWRITEACTION)
                logger.Log("ImagePath : " + imagePath)
                imageName = "swipecheckimage"
                dut.validator.CacheImageFromUrl(imagePath, imageName)
                swipe_retry_count = 1
                while True:
                    if self.category_type == "Kids":
                        dut.HorizontalSwipe(confFile.Kids_Generic_Swipe_Horizontal_BottomToTop_x1,
                                            confFile.Kids_Generic_Swipe_Horizontal_BottomToTop_x2,
                                            confFile.Kids_Generic_Swipe_Horizontal_BottomToTop_y2,
                                            confFile.KIDS_HORIZONTAL_LIVE_SWIPE_TIME)
                    else:
                        dut.VerticalSwipe(confFile.Swipe_Vertical_BottomToTop_y1,
                                          confFile.Swipe_Vertical_BottomToTop_y2,
                                          confFile.Swipe_Vertical_BottomToTop_x2,
                                          confFile.MOVIES_LIVE_SWIPE_TIME)
                    if (dut.validator.DynamicImageCompare(imageName, confFile.SWIPE_CHECK_AREA_X,
                                                          confFile.SWIPE_CHECK_AREA_Y,
                                                          confFile.SWIPE_CHECK_AREA_W,
                                                          confFile.SWIPE_CHECK_AREA_H,
                                                          '5')):
                        logger.Log("Dynamic image match obtained")
                        if swipe_retry_count == 2:
                            logger.Log("End of screen reached")
                            end_screen = True
                            break
                        else:
                            time.sleep(confFile.SHORT_WAITTIME)
                            swipe_retry_count += 1
                    else:
                        break
            else:
                logger.Log("Already at the end of screen")
            return end_screen
        except:
            self.test_result = False
            logger.Log("Exception raised in swipe_check function " +
                       str(sys.exc_info()[0]) + str(sys.exc_info()[1]) + str(sys.exc_info()[2].tb_lineno)
                       + str(os.path.split(sys.exc_info()[2].tb_frame.f_code.co_filename)[1]))

#************************Getting the programme name**************
    def get_pgm_name(self, pgm,  dut, logger, MobileScriptingLibrary ):
        pgm_name = ""
        try:
            confFile = self.confFile
            if self.category_type == "Kids":
                if dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.XPath,
                                        common.get_text_kids_item(self.asset_count)):
                    pgm_name = common.GetText(dut, MobileScriptingLibrary.Constants.ElementType.XPath,
                                              common.get_text_kids_item(self.asset_count))
                else:
                    logger.Log("Failed to get programme name")
            else:
                if dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.XPath, pgm):
                    dut.Click(MobileScriptingLibrary.Constants.ElementType.XPath, pgm)
                    if dut.WaitForElement(MobileScriptingLibrary.Constants.ElementType.Id, confFile.ALL_MOVIES_ITEM_NAME,
                                          confFile.MAXTIMEOUT):
                        pgm_name = dut.GetText(MobileScriptingLibrary.Constants.ElementType.Id,
                                               confFile.ALL_MOVIES_ITEM_NAME)
                    self.back_to_channel_screen(dut, logger, MobileScriptingLibrary)
                else:
                    logger.Log("Failed to get programme name")

            return pgm_name

        except:
            self.test_result = False
            logger.Log("Exception raised in get_pgm_name function " +
                       str(sys.exc_info()[0]) + str(sys.exc_info()[1]) + str(sys.exc_info()[2].tb_lineno)
                       + str(os.path.split(sys.exc_info()[2].tb_frame.f_code.co_filename)[1]))

# ***************************** select_channel *******************************
    def select_channel(self, channel, dut, logger, MobileScriptingLibrary):
        try:
            confFile = self.confFile
            self.count = 1
            found_channel = False
            endscreen_reached_flag = False
            self.asset_count = 1
            dut.SetOrientation("Portrait")
            time.sleep(confFile.MAXTIMEOUT)
            if dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.XPath, confFile.MENU_ICON):
                dut.Click(MobileScriptingLibrary.Constants.ElementType.XPath,
                                          confFile.MENU_ICON)
                time.sleep(confFile.MAXTIMEOUT)
            time.sleep(confFile.SHORT_WAITTIME)
            retry = 0
            while retry < confFile.TIMEOUT:
                if dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.XPath,
                                        confFile.CATEGORY_BUTTON.format(self.category_type)):
                    dut.Click( MobileScriptingLibrary.Constants.ElementType.XPath,
                                 confFile.CATEGORY_BUTTON.format(self.category_type))
                    break
                else:
                    retry += 1
            time.sleep(confFile.MAXTIMEOUT)
            retry_val = 0
            while retry_val < confFile.TIMEOUT:
                if self.category_type == "Sports":

                    if dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.XPath,
                                            confFile.SPORTS_WATCH_LIVE):
                        dut.Click(MobileScriptingLibrary.Constants.ElementType.XPath,
                                  confFile.SPORTS_WATCH_LIVE )
                        break
                    else:
                        retry_val += 1
                elif self.category_type == "Kids":
                    if dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.Id,
                                            confFile.OK):
                        common.Click(dut, MobileScriptingLibrary.Constants.ElementType.Id,
                                     confFile.OK)
                    if dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.XPath,
                                            confFile.CATEGORY_BUTTON.format(self.category_type)):
                        common.Click(dut, MobileScriptingLibrary.Constants.ElementType.XPath,
                                     confFile.CATEGORY_BUTTON.format(self.category_type))
                    if not dut.WaitForElement(MobileScriptingLibrary.Constants.ElementType.XPath,
                                              confFile.NOW_TV,
                                              confFile.MORETIMEOUT):
                        logger.Log("Failed to load assets")
                        self.test_result = False
                        return found_channel
                    while not dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.XPath,
                                                   confFile.X_ON_NOW):
                        dut.VerticalSwipe(confFile.Kids_Swipe_Vertical_BottomToTop_y1,
                                          confFile.Kids_Swipe_Vertical_BottomToTop_y2,
                                          confFile.Kids_Swipe_Vertical_BottomToTop_x2,
                                          confFile.KIDS_LIVE_SWIPE_TIME)
                    else:
                        dut.VerticalSwipe(confFile.Kids_Swipe_Vertical_BottomToTop_y1,
                                          confFile.Kids_Swipe_Vertical_BottomToTop_y2,
                                          confFile.Kids_Swipe_Vertical_BottomToTop_x2,
                                          confFile.KIDS_LIVE_SWIPE_TIME)
                        logger.Log("Found On Now in Kids")
                        break
                else:
                    if dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.XPath,
                                     confFile.WATCH_LIVE):
                        dut.Click(MobileScriptingLibrary.Constants.ElementType.XPath,
                                    confFile.WATCH_LIVE)
                        break
                    else:
                        retry_val += 1
            time.sleep(confFile.MAXTIMEOUT)
            if self.category_type == "Movies":
                self.on_now_pgm = confFile.ON_NOW_PGM
                next_pgm = confFile.NEXT_PGM
            elif self.category_type == "Kids":
                self.on_now_pgm = confFile.KIDS_ON_NOW_PGM
            else:
                self.on_now_pgm = confFile.ON_NOW_PGM_ENT
                next_pgm = confFile.NEXT_PGM_ENT

            if self.category_type == "Kids":
                if not dut.WaitForElement(MobileScriptingLibrary.Constants.ElementType.XPath,
                                          self.on_now_pgm.format(1), confFile.DEFAULT_SLEEP_TIME):
                    self.report("Failed to load {} LIVE home page".format(self.category_type), common.TestResult.FAILED)
                    self.test_result = False
            else:
                if not dut.WaitForElement(MobileScriptingLibrary.Constants.ElementType.XPath,
                                          self.on_now_pgm.format(1,1) , confFile.DEFAULT_SLEEP_TIME):
                    self.report("Failed to load {} LIVE home page".format(self.category_type), common.TestResult.FAILED)
                    self.test_result = False

            if self.test_result:
                on_now_pgm_name = ""
                next_pgm_name = ""
                pgm_list = []
                channel_list = []
                while not found_channel:
                    retry_count = 0
                    retry_num = 0
                    next_channel = False

                    if self.category_type == "Movies":
                        self.on_now_pgm = confFile.ON_NOW_PGM
                        next_pgm = confFile.NEXT_PGM
                    elif self.category_type == "Kids":
                        self.on_now_pgm = confFile.KIDS_ON_NOW_PGM
                    else:
                        self.on_now_pgm = confFile.ON_NOW_PGM_ENT
                        next_pgm = confFile.NEXT_PGM_ENT

                    if endscreen_reached_flag:
                        if self.asset_count < confFile.ITERATION:  # #assumes maximum 5 assets row in
                            self.asset_count += 1
                            if self.category_type == "Kids":
                                self.on_now_pgm = self.on_now_pgm.format(self.asset_count)
                            else:
                                self.on_now_pgm = self.on_now_pgm.format(self.asset_count, 1)
                                next_pgm = next_pgm.format(self.asset_count, 2)

                    else:
                        if self.category_type == "Kids":
                            self.on_now_pgm = self.on_now_pgm.format(1)
                        else:
                            self.on_now_pgm = self.on_now_pgm.format(1, 1)
                            next_pgm = next_pgm.format(1, 2)
                    while retry_count<confFile.MAXCOUNT:
                        on_now_pgm_name = str(self.get_pgm_name(self.on_now_pgm, dut, logger, MobileScriptingLibrary))
                        if not on_now_pgm_name == "":
                            logger.Log("Current Programme is " + on_now_pgm_name)
                            break
                        else:
                            retry_count += 1
                        if retry_count== confFile.MAXCOUNT:
                            logger.Log("Failed to get the Current Programme name")
                            return found_channel
                    if pgm_list == []:
                        logger.Log("Programme list is empty")
                        pass
                    elif on_now_pgm_name in pgm_list:
                        logger.Log("Current programme is already in the programme list")
                        endscreen_reached_flag = self.swipe_check(dut, MobileScriptingLibrary, logger, end_screen=endscreen_reached_flag)
                        continue
                    else:
                        logger.Log("Navigated to next channel")
                        pgm_list = []
                        pass
                    if not self.category_type == "Kids":
                        while retry_num < confFile.MAXCOUNT:
                            next_pgm_name = str(self.get_pgm_name(next_pgm,dut, logger, MobileScriptingLibrary))
                            if not next_pgm_name == "":
                                logger.Log("Next Programme is "+next_pgm_name)
                                break
                            else:
                                retry_num += 1
                            if retry_num==confFile.MAXCOUNT:
                                logger.Log("Failed to get the Next Programme name")
                                return found_channel
                    if self.category_type == "Kids":
                        pgm_list.append(on_now_pgm_name)
                    else:
                        pgm_list.extend((on_now_pgm_name, next_pgm_name))
                    logger.Log("Programme list is "+ str(pgm_list))
                    channel_list.append(pgm_list)
                    logger.Log("List of Programmes in each channel are"+ str(channel_list))
                    num_channel = len(channel_list)
                    logger.Log("Current Channel's Number is "+ str(num_channel))
                    logger.Log("Channel Number to be selected is "+ str(channel))
                    if str(num_channel) == str(channel):
                        logger.Log("Channel found ...Going to select the channel")
                        if self.category_type == "Kids":
                            found_channel = True
                            return found_channel
                        else:
                            if dut.WaitForElement(MobileScriptingLibrary.Constants.ElementType.XPath,
                                                      self.on_now_pgm, confFile.DEFAULT_SLEEP_TIME):
                                dut.Click(MobileScriptingLibrary.Constants.ElementType.XPath,
                                          self.on_now_pgm)
                                if dut.WaitForElement(MobileScriptingLibrary.Constants.ElementType.Id,
                                                       confFile.ALL_MOVIES_PLAYBUTTON, confFile.MAXTIMEOUT):
                                    found_channel = True
                                    return found_channel
                            else:
                                return found_channel
                    else:
                        endscreen_reached_flag = self.swipe_check(dut, MobileScriptingLibrary, logger, end_screen = endscreen_reached_flag)

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
            # Reading the values from excel files
            test_args = comQoe.get_test_args(dut)

            # variables from excel
            loopcount = int(test_args.LOOP_COUNT)
            self.category_type = test_args.CATEGORY_NAME
            channel_nos = test_args.CHANNEL_LIST
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
                    status = self.select_channel(channel, dut, logger, MobileScriptingLibrary)
                    if not status:
                        self.report("Select channel " + str(channel) + " in " + str(self.category_type) +" failed.", common.TestResult.FAILED)
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
                                if (not status) or (not channel_count == no_of_channels-1):
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
                        if self.category_type == "Kids":
                            if dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.XPath, self.on_now_pgm):
                                self.custom_dict.update({'channel': channel})
                                time.sleep(confFile.MAXTIMEOUT)
                                dut.Click(MobileScriptingLibrary.Constants.ElementType.XPath, self.on_now_pgm)
                        else:
                            if dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.Id,
                                                    confFile.ALL_MOVIES_PLAYBUTTON):
                                self.custom_dict.update({'channel': channel})
                                logger.Log("Entered all movies")
                                time.sleep(confFile.MAXTIMEOUT)
                                common.Click(dut, MobileScriptingLibrary.Constants.ElementType.Id,
                                                     confFile.ALL_MOVIES_PLAYBUTTON)
                                check_Time_start = timeit.default_timer()
                                checking_time = 0
                                if(dut.WaitForElement(MobileScriptingLibrary.Constants.ElementType.Id,
                                                      confFile.MOVIES_RESUME_BUTTON, confFile.MINTIMEOUT)):
                                    if not (common.Click(dut,MobileScriptingLibrary.Constants.ElementType.Id,
                                            confFile.MOVIES_RESUME_BUTTON)):
                                        break
                                else:
                                    checking_time = timeit.default_timer() - check_Time_start
                        comQoe.find_qoe_parameters(self, checking_time, channel, self.capped_bw, confFile, dut, logger, MobileScriptingLibrary)
                        element_check_count = 0
                        while not common.WaitForElement(dut, MobileScriptingLibrary.Constants.ElementType.XPath,
                                                        confFile.MENU_ICON, "Menu Icon",confFile.MAXTIMEOUT):
                            element_check_count += 1
                            time.sleep(confFile.TIMEOUT)
                            if not common.send_back_key(dut, maxcount=confFile.MAXCOUNT):
                                self.report("Sending Back key failed",common.TestResult.FAILED)
                                self.test_result = False
                            if self.category_type == "Kids":
                                if dut.WaitForElement(MobileScriptingLibrary.Constants.ElementType.Id,
                                                      confFile.ID_KIDS_LEAVE_NOW, confFile.MAXTIMEOUT):
                                    dut.Click(MobileScriptingLibrary.Constants.ElementType.Id,
                                              confFile.ID_KIDS_LEAVE_NOW)
                                if dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.XPath,
                                                        confFile.MOVIES_BUTTON):
                                    dut.Click(MobileScriptingLibrary.Constants.ElementType.XPath,
                                              confFile.MOVIES_BUTTON)
                                    time.sleep(confFile.TIMEOUT)
                                if dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.XPath,
                                                        confFile.WATCH_LIVE):
                                    dut.Click(MobileScriptingLibrary.Constants.ElementType.XPath, confFile.WATCH_LIVE)
                                    time.sleep(confFile.TIMEOUT)
                            if element_check_count == confFile.MAXCOUNT:
                                self.report("Failed to navigate back to channel screen",common.TestResult.FAILED)
                                self.test_result = False
                                break
                        else:
                            dut.SetOrientation("Portrait")
                            self.navigate_to_home(dut, logger, MobileScriptingLibrary)

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
            logger.Log("Calling closeapp......")
            dut.CloseApp()


if __name__ == "__main__":
    test_script = TC_QOE8()
    test_script.run()

# =============================================================================
# Author: Linda
# Date: 18/06/2018
# Device Type: Android
# =============================================================================
