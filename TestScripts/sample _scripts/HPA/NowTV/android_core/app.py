# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Base class for scripts running in android devices
# Initializes FalconEye modules and defines the flow script execution
#
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import clr, sys, os, time, importlib, datetime
clr.AddReference("MobileScriptingLibrary")
import MobileScriptingLibrary
from android_core.config import ConfigBase as confFile
from android_core.common import TestResult
from android_core.msg import Message


class AndroidBase(object):
    description = ''
    custom_dict = {'app_name':'NowTV', 'app_version' : '6.2.9', 'connection':'WiFi', 'region' : 'UK'}

    # ********************* Script Level Basic Configurations *****************
    def __init__(self):
        self.dut = MobileScriptingLibrary.MobileDUT()
        self.logger = MobileScriptingLibrary.Logger()
        self.check_point = MobileScriptingLibrary.CheckPoint()
        self.msl_test_result = MobileScriptingLibrary.TestResult()
        self.script_path = os.path.realpath(__file__)
        args = sys.argv
        self.dut.Configure(args[1], args[2], args[3], args[4], self.script_path)
        self.logger.Configure(args[1], args[2], args[3], args[4], self.script_path)

        #Start Importing dynamic Config file using DUT Type
        dutType = self.dut.ReadProperty(2)
        try:
            dynamic_module = importlib.import_module("Configuration."+ dutType)
            Config = getattr(dynamic_module, "Config")
            self.logger.Log("Imported " + dutType + " config file")
        except:
            self.logger.Log("Importing Default config file")
            from Configuration.Default import Config
        self.confFile = Config()
        #End Importing dynamic Config file using DUT Type

        self.test_result = True
        self.step = 0

    #** Launches App ******************************************************
    def init_app(self):
        device_config = MobileScriptingLibrary.DeviceConfig()
        device_config.DeviceType = confFile.DEVICE_PLATFORM
        device_config.AppPackage = "com.bskyb.nowtv.beta"
        device_config.AppActivity = "com.nowtv.view.activity.StartupActivity"
        device_config.CreateNewServer = True

        app_initialized = self.dut.InitApp(device_config)
        if app_initialized:
            self.logger.Log(Message.INIT_SUCCESS)
            return True
        else:
            self.logger.Log(Message.INIT_FAILED)
            self.dut.CommitTestResult(TestResult.ERROR)
            return False

    # ****************************** Precondition *****************************
    def run_preconditions(self, dut, logger, MobileScriptingLibrary):
        if not dut.WaitForElement(
            MobileScriptingLibrary.Constants.ElementType.Id,
                confFile.APP_HOME, confFile.DEFAULT_SLEEP_TIME):
            if dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.XPath, confFile.MOVIES_BUTTON):
                dut.Click(MobileScriptingLibrary.Constants.ElementType.XPath, confFile.MOVIES_BUTTON)
                time.sleep(confFile.TIMEOUT)
            if dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.XPath, confFile.WATCH_LIVE):
                dut.Click(MobileScriptingLibrary.Constants.ElementType.XPath, confFile.WATCH_LIVE)
                time.sleep(confFile.TIMEOUT)
            if dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.Id, confFile.APP_HOME):
                time.sleep(confFile.TIMEOUT)
            else:
                self.report("Home page did not displayed", TestResult.FAILED, stage='Precondition')
                return False
        self.report("Home Page displayed", TestResult.PASSED, stage='Precondition')
        return True

    # **************** Main Script - Overrides in the Script which calls this method ***************
    def run_script(self, dut, logger, MobileScriptingLibrary):
        pass

    # ********************** Test result updates *****************************
    def update_test_result(self):
        if self.test_result:
            self.dut.CommitTestResult(TestResult.PASSED)
            self.logger.Log("TEST CASE PASS: " + self.description)
        else:
            self.dut.CommitTestResult(TestResult.FAILED)
            self.logger.Log("TEST CASE FAIL: " + self.description)


    # ****************** Cleanup - Overrides in main script if requires additional cleanups **************
    def cleanup(self):
        self.logger.Log("Cleanup : calling DUT.stop ")
        self.dut.Stop()

    #  Aborts script execution ************************************************
    def abort_script(self, msg=None):
        if msg:
            self.logger.Log(msg)
        self.dut.CommitTestResult(TestResult.ABORTED)
        self.logger.Log("TEST CASE ABORTED: " + self.description)

    def report(self, message, step_status, image=True, stage='Step'):
        '''
        :param self:
        :param dut:
        :param message: message to be appear in the log and step
        :param status: Passed/Failed - eg: TestResult.PASSED
        :param logger: logger
        :param image: True if image to be attached, else False
        :return: None
        '''
        if image:
            self.log_screen_shot(self.dut)
        self.step += 1
        self.dut.CommitStepResult(
            "{}-{}: {}".format(stage, self.step, message), step_status)
        self.logger.Log(message)

    def getNowStr(self):
        return datetime.datetime.utcnow().strftime("%d%m%Y_%H%M%S")

    def log_screen_shot(self, dut):
        dut.validator.QuickCapture(self.getNowStr())

    # ************* run() - calls the script methods in order *****************
    def run(self):
        app_initialized = self.init_app()
        if not app_initialized:
            self.abort_script()
            return
        try:
            pre_cond_status = self.run_preconditions(self.dut, self.logger, MobileScriptingLibrary)
            self.step = 0
            if (pre_cond_status):
                self.run_script(self.dut, self.logger, MobileScriptingLibrary)
                self.update_test_result()
            else:
                self.abort_script("Pre-conditions failed")
        except:
            self.logger.Log("Exception: " + str(sys.exc_info()[0]) + str(sys.exc_info()[1]) + "Line No:" + str(sys.exc_info()[2].tb_lineno) + \
                       str(os.path.split(sys.exc_info()[2].tb_frame.f_code.co_filename)[1]))
        finally:
            self.cleanup()

