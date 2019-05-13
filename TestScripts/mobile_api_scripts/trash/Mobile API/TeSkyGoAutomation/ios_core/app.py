# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Base class for scripts running in iOS devices
# Initializes FalconEye modules and defines the flow script execution
#
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import clr,sys,os,time
clr.AddReference("MobileScriptingLibrary")
import MobileScriptingLibrary
from ios_core.config import IOSConfig
from ios_core.common import TestResult
from ios_core.utils import log_screen_shot
from ios_core.msg import IOSMessage


class IOSBase(object):
    description = ''

    # ** Basic Configurations for FalconEye *******************************
    def __init__(self):
        self.dut = MobileScriptingLibrary.MobileDUT()
        self.logger = MobileScriptingLibrary.Logger()
        self.check_point = MobileScriptingLibrary.CheckPoint()
        self.msl_test_result = MobileScriptingLibrary.TestResult()
        self.script_path = os.path.realpath(__file__)
        args = sys.argv
        self.dut.Configure(args[1], args[2], args[3], args[4], self.script_path)
        self.logger.Configure(args[1], args[2], args[3], args[4], self.script_path)

        # Set final test result
        self.test_result = False
        self.step = 0


    #** Launches App ******************************************************
    def init_app(self):
        device_config = MobileScriptingLibrary.DeviceConfig()
        device_config.DeviceType = IOSConfig.DEVICE_TYPE
        device_config.AppName = IOSConfig.APP_NAME

        app_initialized = self.dut.InitApp(device_config)
        if app_initialized:
            self.logger.Log(IOSMessage.INIT_SUCCESS)
            return True
        else:
            self.logger.Log(IOSMessage.INIT_FAILED)
            self.dut.CommitTestResult(TestResult.ERROR)
            return False


    # ***** Preconditions ************************************
    # 1. Waits for Home screen to launch
    #***************************************************************************
    def run_preconditions(self, dut, logger, MobileScriptingLibrary):
        time.sleep(IOSConfig.MX_SLEEP_TIME)
        if not dut.IsElementPresent(
            MobileScriptingLibrary.Constants.ElementType.Name,
            IOSConfig.APP_HOME):
            self.report(
                "Home page did not displayed",
                TestResult.FAILED, stage='Precondition')
            return False

        self.report("Home Page displayed", TestResult.PASSED, stage='Precondition')
        return True


    # Main Script - To be overriden by the actual script inherting this class **
    def run_script(self, dut, logger, MobileScriptingLibrary):
        pass

    # Updates final Test result based on the parameter set by run_script method*
    def update_test_result(self):
        if self.test_result:
            self.dut.CommitTestResult(TestResult.PASSED)
            self.logger.Log("TEST CASE PASS: " + self.description)
        else:
            self.dut.CommitTestResult(TestResult.FAILED)
            self.logger.Log("TEST CASE FAIL: " + self.description)


    #  Aborts script execution **************************************************

    def abort_script(self, msg=None):
        if msg:
            self.logger.Log(msg)
        self.dut.CommitTestResult(TestResult.ABORTED)
        self.logger.Log("TEST CASE ABORTED: " + self.description)


    # ** Default cleanup action is to stop App *********************************
    def cleanup(self):
        self.dut.Stop()


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
            log_screen_shot(self.dut)
        self.step += 1
        self.dut.CommitStepResult(
            "{}-{}: {}".format(stage, self.step, message), step_status)
        self.logger.Log(message)



    # ** Defines the flow of script execution ***************************
    def run(self):
        app_initialized = self.init_app()
        if not app_initialized:
            self.abort_script()
            return
        try:
            pre_cond_status = self.run_preconditions(
                self.dut, self.logger, MobileScriptingLibrary)
            self.step = 0
            if (pre_cond_status):
                self.run_script(self.dut, self.logger, MobileScriptingLibrary)
                self.update_test_result()
            else:
                self.abort_script("Pre-conditions failed")
        except:
            self.logger.Log("Exception: " + str(sys.exc_info()[0]))
        finally:
            self.cleanup()
