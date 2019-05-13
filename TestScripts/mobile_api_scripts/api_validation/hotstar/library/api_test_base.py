# ''''''''''''''''''''''''''' BASE CLASS FOR ALL TEST SCRIPTS '''''''''''''''''''''''''''''''''''''''''
# Author            : Shameena HA
# Date              :   26-11-2018
# Script Version     : 1.0
# Modification details:
#
# ''''''''''''''''''''''''''' BASE CLASS FOR ALL TEST SCRIPTS - END '''''''''''''''''''''''''''''''''

from library.common_functions import common_functions, dut, \
                            device_config, logger, chkpt, mob_lib

class ApiTestBase(object):
    '''
    This functions as a base class for all scripts. The scripts can override run_api_test()
    function for the script implementation

    '''


    def __init__(self):
        '''
        initializes all class variables
        '''

        self.lib = common_functions()
        self.dut = dut
        self.logger = logger
        self.test_result = False
        self.init_run = False
        self.config = None
        self.chkpt = chkpt
        self.mob_lib = mob_lib

        # self.test_params = None


    def init_test(self):
        '''
        test case execution initializes the application under test here
        :return: True on success
                    False on Failure
        '''

        init_run = False
        status = "FAILED"
        self.lib.set_config('hotstar')
        self.config = self.lib.config
        # self.test_params = self.lib.test_params
        if not self.config:
            logger.Error("Invalid config")
            return False

        # self.elm_type = self.lib.config.elm_types_in_config[self.lib.config.index]

        try:
            start_time = self.lib.get_time_stamp()
            init_run = dut.InitApp(device_config)
            end_time = self.lib.get_time_stamp()

            if init_run:
                status = "PASSED"
            self.lib.report_api_status(start_time, end_time, "InitApp",status, ss_required=True)

        except Exception as e:
            self.logger.Error("Failed to init app" + str(e))
            init_run = False
        finally:
            return init_run


    def precondition(self):
        '''
        Precondition of the test script

        :return: The status of the precondition as True, or False
        '''

        done = False
        elm_type, type = self.lib.choose_elm_type(self.config.home)
        # if not (elm_type and type):
        if not type:
            logger.Error("Could not find suitable element type")
            return False

        try:
            start_time = self.lib.get_time_stamp()
            done = dut.WaitForElement(elm_type, self.config.home[type], 50)
            end_time = self.lib.get_time_stamp()
            if done:
                status = "PASSED"
            else:
                status = "FAILED"
            self.lib.report_api_status(start_time, end_time, "WaitForElement", status, ss_required=True)

        except Exception as e:
            logger.Error("Failed to find the Home element" + str(e))
            done = False
        finally:
            return done


    def run_api_test(self):
        pass


    def run_test(self, script_name, apis_covered):
        '''


        :return: The status of the run as True, or False
        '''

        self.log_script_info(script_name, apis_covered)

        try:
            self.init_run = self.init_test()
            if not self.init_run:
                logger.Error("Failed to configure the test")
                return False

            done = self.precondition()
            if not done:
                logger.Error("Failed to verify the precondition")
                return False

            self.run_api_test()

        except Exception as e:
            logger.Error("Error in running test " + str(e))
        finally:
            self.cleanup()
            self.report_test_result()


    def cleanup(self):
        '''
        test run cleanup

        :return: None
        '''

        try:
            if self.init_run:
                self.lib.close_app()
        except Exception as e:
            self.logger.Error("Failed to close app" + str(e))
        finally:
            self.lib.stop_driver()


    def report_test_result(self):
        '''
        To report the final status of the test

        :return: None
        '''
        try:
            if self.test_result is True:
                dut.CommitTestResult("PASSED")

            if self.test_result is False:
                dut.CommitTestResult("FAILED")

            if self.test_result is None:
                dut.CommitTestResult("ERROR")

        except Exception as e:
            dut.CommitTestResult("ABORT")


    def log_script_info(self, file_name, apis_covered):
        logger.Log("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        logger.Log("--- Application Name: HOTSTAR ---")
        logger.Log("Script Name: {}".format(file_name))
        logger.Log("Validating APIs - {}".format(apis_covered))
        logger.Log("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
