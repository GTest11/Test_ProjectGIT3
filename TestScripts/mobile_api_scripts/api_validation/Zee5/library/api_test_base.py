# ''''''''''''''''''''''''''' BASE CLASS FOR ALL TEST SCRIPTS '''''''''''''''''''''''''''''''''''''''''
# Author            : Lincy Robert
# Date              : 0.2-04-2019
# Script Version     : 1.0
# Modification details:
#
# ''''''''''''''''''''''''''' BASE CLASS FOR ALL TEST SCRIPTS - END '''''''''''''''''''''''''''''''''

from library.common_functions import common_functions, dut, \
                            device_config, logger, chkpt


class ApiTestBase(object):
    """
    This functions as a base class for all scripts. The scripts can override run_api_test()
    function for the script implementation
    """
    # zee5
    def __init__(self):
        """
        initializes all class variables
        """

        self.lib = common_functions()
        self.dut = dut
        self.logger = logger
        self.test_result = False
        self.init_run = False
        self.config = None
        self.chkpt = chkpt

    # zee5
    def init_test(self):
        """
        test case execution initializes the application under test here
        :return: True on success
                    False on Failure
        """

        init_run = False
        status = "FAILED"
        self.lib.set_config('zee5')
        self.config = self.lib.config
        if not self.config:
            logger.Error("Invalid config")
            return False

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

    # zee 5
    def precondition(self):
        """
        Precondition of the test script
        :return: The status of the precondition as True, or False
        """

        # done = False
        # elm_type, type = self.lib.choose_elm_type(self.config.home)
        # # if not (elm_type and type):
        # if not type:
        #     logger.Error("Could not find suitable element type")
        #     return False
        #
        # try:
        #     start_time = self.lib.get_time_stamp()
        #     done = dut.WaitForElement(elm_type, self.config.home[type], 50)
        #     end_time = self.lib.get_time_stamp()
        #     if done:
        #         status = "PASSED"
        #     else:
        #         status = "FAILED"
        #     self.lib.report_api_status(start_time, end_time, "WaitForElement", status, ss_required=True)
        #
        # except Exception as e:
        #     logger.Error("Failed to find the Home element" + str(e))
        #     done = False
        # finally:
        #     return done

        ##################
        #need to implement for zee5

        chkpt.init(self.config.zee5_home_menu)
        time_to_wait = 60   # increased the timeout since an ad is coming before the checkpoint
        wait_gap = 2
        if dut.validator.WaitCheckPointMatch(chkpt, time_to_wait, wait_gap):
            logger.Log("Home Menu Screen of Zee5 app is Visible")
            menu_screen_verified = True
        else:
            logger.Error("Failed to find Home Menu Screen of Zee5 app")
            menu_screen_verified = False
        # return menu_screen_verified

        tap_coordinates = None
        cur_dut_name = self.lib.get_dut_name()
        logger.Log("---- cur_dut_name {}".format(cur_dut_name))
        if cur_dut_name in self.config.home_in_home_menu:
            tap_coordinates = self.config.home_in_home_menu[cur_dut_name]
        else:
            # tap_coordinates = (124*0.577, 412*0.521)
            self.logger.Error("Tap coordinates not available for the specific DUT.")
            # menu_screen_verified = False # --------- commenting for ios, need to check
            # return menu_screen_verified
        start_time = self.lib.get_time_stamp()
        tap_result = self.dut.Tap(*tap_coordinates)
        end_time = self.lib.get_time_stamp()

        if not tap_result:
            self.logger.Error("Tap failed.")
            self.logger.Log("Return value obtained for Tap API is : " + str(tap_result))
            menu_screen_verified = False
            # return menu_screen_verified

        # if not self.lib.element_ops(self.config.home_button, action='tap'):
        #     logger.Log("Failed to tap on the HOME button")
        #     menu_screen_verified = False
        # else:
        #     logger.Log("Tapped on the HOME button")

        is_home = self.lib.wait_for_element(self.config.home, self.config.WAIT_FOR_HOME)
        if not is_home:
            logger.Log("Failed to verify the Home Screen")
            # menu_screen_verified = False
        else:
            logger.Log("App Home Screen launched")
            menu_screen_verified = True
        return menu_screen_verified


    def run_api_test(self):
        pass

    # zee5
    def run_test(self, script_name, apis_covered):
        """
        Invokes the init function
        Executes the precondition
        Executes the test validation as per corresponding scripts
        Invokes report_test_result to set the status of test script
        :return: None
        """

        self.log_script_info(script_name, apis_covered)
        try:
            self.init_run = self.init_test()
            if not self.init_run:
                logger.Error("Failed to configure the test")
                # return False

            done = self.precondition()
            if not done:
                logger.Error("Failed to verify the precondition")
                # return False

            self.run_api_test()

        except Exception as e:
            logger.Error("Error in running test " + str(e))
        finally:
            self.cleanup()
            self.report_test_result()

    # zee5
    def cleanup(self):
        """
        clean up which needs to be done after execution of each test script
        :return: None
        """
        try:
            if self.init_run:
                self.lib.close_app()
        except Exception as e:
            self.logger.Error("Failed to close app" + str(e))
        finally:
            self.lib.stop_driver()

    # zee5
    def report_test_result(self):
        """
        To report the final status of the test

        :return: None
        """
        try:
            if self.test_result is True:
                dut.CommitTestResult("PASSED")

            if self.test_result is False:
                dut.CommitTestResult("FAILED")

            if self.test_result is None:
                dut.CommitTestResult("ERROR")

        except Exception as e:
            dut.CommitTestResult("ABORT")

    # zee5
    def log_script_info(self, file_name, apis_covered):
        """
        :param file_name: File name of the script execution
        :param apis_covered: APIs validated in the test script
        :return:
        """
        logger.Log("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        logger.Log("--- Application Name: ZEE5 ---")
        logger.Log("Script Name: {}".format(file_name))
        logger.Log("Validating APIs - {}".format(apis_covered))
        logger.Log("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
