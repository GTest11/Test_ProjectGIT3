# ''''''''''''''''''''''''''' COMMON FUNCTIONS '''''''''''''''''''''''''''''''''''''''''
# Author            : Shameena HA
# Date              :   26-11-2018
# Script Version     : 1.0
# Modification details:
#
# ''''''''''''''''''''''''''' COMMON FUNCTIONS - END '''''''''''''''''''''''''''''''''

import clr
import sys
import os
import datetime
import time
from PIL import Image

clr.AddReference("MobileScriptingLibrary")
import MobileScriptingLibrary as mob_lib
dut = mob_lib.MobileDUT()
logger = mob_lib.Logger()
scriptPath = os.path.realpath(__file__)
args = sys.argv
dut.Configure(args[1], args[2], args[3], args[4], scriptPath)
logger.Configure(args[1], args[2], args[3], args[4], scriptPath)
chkpt = mob_lib.CheckPoint()
device_config = mob_lib.DeviceConfig()
device_config.CreateNewServer="True"
device_config.UseNewWDA = True

# =========================== Script Level Imports
from config.androidphone import androidPhone
from config.ipad import iPad
from config.iphone import iPhone


class common_functions(object):
    '''
    This class contains common functions applicable to all devices.
    Keeps all functions to be accessed by all scripts regardless of the platform

    '''


    list_element_types = {
        'xpath': mob_lib.Constants.ElementType.XPath,
        'id': mob_lib.Constants.ElementType.Id,
        'name': mob_lib.Constants.ElementType.Name,
        'class': mob_lib.Constants.ElementType.ClassName,
        'access_id': mob_lib.Constants.ElementType.AccessibilityID,
    }

    def __init__(self):
        '''
        This functions initalizes the class variables

        '''


        # config variables are stored in the below variable
        self.config = None

        # As per the configuration data - this will not change
        self.element_type_to_test = None


    def get_dut_platform(self):
        '''

        :return: reads the Dut Platform if available
                    returns None, if it could not read
        '''

        dut_platform = None
        try:
            dut_platform = dut.ReadProperty(3)
        except Exception as e:
            logger.Error("Failed to read the platform name" + str(e))
            dut_platform = None
        finally:
            return dut_platform


    def set_config(self, app_name=None):
        '''
        Sets the config file to a variable as per the device type and platform

        :param app_name: application under test,
                        give its name as configured in the config.py file
        :return: returns the config file to be used for the script execution, if available.
                    else returns None.
        '''

        config = None
        platform = self.get_dut_platform()
        try:
            dut_type = dut.ReadProperty(2)
            if platform not in ["Android", "iOS"]:
                logger.Log("Wrong Platform")
                return config

            if platform == "Android":
                config = androidPhone
                device_config.AppActivity = config.activity[app_name]
                device_config.AppPackage = config.package[app_name]

            if platform == "iOS" and dut_type == "iPhone":
                config = iPhone
                device_config.AppName = config.app_name[app_name]

            if platform == "iOS" and dut_type == "iPad":
                config = iPad
                device_config.AppName = config.app_name[app_name]

            device_config.DeviceType = platform

            self.element_type_to_test = config.element_type_to_test
            logger.Log("self.element_type_to_test {}".format(self.element_type_to_test))

        except Exception as e:
            logger.Error("Failed to read the platform name" + str(e))
            config = None

        finally:
            self.config = config
            # self.test_params = self.config.test_params()
            return config


    def gettimestamp(self):
        '''
        :return: current time in milliseconds,
                else returns None
        '''

        time_converted = None
        try:
            timestamp = datetime.datetime.now().strftime("%H:%M:%S.%f")
            time_converted = self.time_in_millisecond(timestamp)
        except Exception as e:
            logger.Error("Failed to get the time" + str(e))
            time_converted = None
        finally:
            return time_converted


    def time_in_millisecond(self, timeinstr):
        '''
        :param timeinstr: time in string format
        :return: coverts the given time in string format to milliseconds
        '''

        converted_time = None
        try:
            hours, minutes, seconds = (["0", "0"] + timeinstr.split(":"))[-3:]
            hours = int(hours)
            minutes = int(minutes)
            seconds = float(seconds)
            converted_time = int(3600000 * hours + 60000 * minutes + 1000 * seconds)
        except Exception as e:
            logger.Error("Failed to convert the given time to milli seconds" + str(e))
            time_converted = None
        finally:
            return converted_time


    def commit_step(self, step_name, message):
        '''
        :param step_name: Name of the step or step number
        :param message: Message to be printed for the step
        :return: None
        '''

        dut.CommitStepResult(step_name, message)


    def report(self, step_name, status, image_required=False):
        '''

        :param step_name: Name of the step or step number
        :param message: Message to be printed for the step
        :param image_required: whether image to be attached or not
        :return:
        '''

        if image_required:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            # timestamp = timestamp.replace(":", "")
            image_name = "img_{}".format(timestamp)
            try:
                ss = dut.GetScreenshot()
                time.sleep(1)
                dut.validator.UploadScreenshot(image_name, ss)
            except Exception as e:
                logger.Error("Could not take/upload Screenshot")

        self.commit_step(step_name, status)
        logger.Log("{} : {}".format(step_name, status))


    def report_api_status(self, t1, t2, api_name, api_status="FAILED", ss_required=False):
        '''

        This function used to report the API status,
        for reporting other steps, please use function commit_step()

        :param t1: api start time
        :param t2:  api end time
        :param api_name: api name
        :param api_status: status of the api. eg: "PASSED", or "FAILED"
        :param ss_required:
        :return: None
        '''

        try:
            time_taken = round(((t2 - t1) / 1000.0), 3)
            self.report("API:  Time taken by {} API".format(api_name), str(time_taken))
            self.report("API: {}".format(api_name), api_status, ss_required)

        except Exception as e:
            logger.Error("Failed to calculate the time " + str(e))


    def close_app(self):
        '''
        Closes the application if open
        :return: None
        '''

        status = "FAILED"
        try:
            start_time = self.gettimestamp()
            closed = dut.CloseApp
            end_time = self.gettimestamp()
            if closed:
                status = "PASSED"
            self.report_api_status(start_time, end_time, "CloseApp", status, ss_required=True)

        except Exception as e:
            logger.Error("Failed to close the application " + str(e))


    def stop_driver(self):
        '''
        stops the Dut
        :return: None
        '''

        try:
            start_time = self.gettimestamp()
            dut.Stop()
            end_time = self.gettimestamp()
            self.report_api_status(start_time, end_time, "Stop", "PASSED", ss_required=False)

        except Exception as e:
            logger.Error("Failed to stop the driver " + str(e))


    def choose_elm_type(self, elm_name):
        '''
        this function inspects the config variable, whether that supports the 'type_to_be_tested'
        If supports, returns the same type, else returns None or xpath as default type

        :param elm_name: name of the element as in the config file
        :return: success: returns element type, and the supporting index of the element
                failure: returns both as None
        '''

        # logger.Log("element {}".format(elm_name))
        elm_type = None
        type = None
        try:
            # if not self.elm_type in elm_name.keys():
            #     logger.Error("No element type '{}' available".format(self.elm_type))
            #     return None
            # logger.Log("self.element_type_to_test {}".format(self.element_type_to_test))

            if elm_name[self.element_type_to_test] is None:
                logger.Error("Element does not support the Element type '{}', so taking xpath..".format(self.element_type_to_test))
                elm_type = self.list_element_types['xpath']
                type = 'xpath'
            else:
                elm_type = self.list_element_types[self.element_type_to_test]
                type = self.element_type_to_test
                logger.Log("Element type to test given element is {}".format(elm_type))
                logger.Log("self.list_element_types[self.element_type_to_test] {}".format(self.list_element_types[self.element_type_to_test]))
                logger.Log("type {}".format(type))

            # logger.Log("Element type to test given element is {}".format(elm_type))
            # logger.Log("type {}".format(type))

        except Exception as e:
            logger.Error("Error in choosing element type" + str(e))
            elm_type = None
            type = None
        finally:
            return elm_type, type


    def is_present(self, elm_name=None):
        '''

        Checks the presence of the given element on the screen

        :param elm_name: name of the element as in the config
        :return: True if found,
                else False
        '''

        status = "FAILED"
        present = False
        try:
            elm_type, type = self.choose_elm_type(elm_name)
            if not type:
                logger.Error("Invalid element type")
                return False

            start_time = self.gettimestamp()
            present = dut.IsElementPresent(elm_type, elm_name[type])
            end_time = self.gettimestamp()

            if present:
                status = "PASSED"

            self.report_api_status(start_time, end_time, "IsElementPresent", status, ss_required=False)
        except Exception as e:
            logger.Error("Error in searching for element" + str(e))
            present = False

        finally:
            return present



    def element_ops(self, elm_name, index=None, action='present'):
        '''
        This function is to find the element presence, does the action as based on 'action' param

        :param elm_name: Name of the element as in the config file
        :param action: 'present' or 'tap' or 'click'
        :return: True if success
                    False if failed
        '''

        actions = ['present', 'tap', 'tapindex', 'click', 'clickindex']

        if not action in actions:
            logger.Error("Invalid action")
            return False

        status = "FAILED"
        present = False
        elm_type = None
        type = None
        try:
            elm_type, type = self.choose_elm_type(elm_name)
            if not type:
                logger.Error("Invalid element type")
                return False

            start_time = self.gettimestamp()
            present = dut.IsElementPresent(elm_type, elm_name[type])
            end_time = self.gettimestamp()

            if present:
                status = "PASSED"

            self.report_api_status(start_time, end_time, "IsElementPresent", status, ss_required=True)

        except Exception as e:
            logger.Error("Error in searching for element" + str(e))
            present = False

        finally:
            if action is 'present' or not present:
                return present


        elm_op = None
        performed = False
        start_time, end_time = 0, 0
        try:
            if action is 'tap' or action is 'tapindex':
                elm_op = dut.TapElement

            if action is 'click' or action is 'clickindex':
                elm_op = dut.Click

            if action == 'tapindex' or action == 'clickindex':
                start_time = self.gettimestamp()
                performed = elm_op(elm_type, elm_name[type], index)
                end_time = self.gettimestamp()

            if action == 'tap' or action == 'click':
                start_time = self.gettimestamp()
                performed = elm_op(elm_type, elm_name[type])
                end_time = self.gettimestamp()

            if performed:
                status = "PASSED"
            else:
                status = "FAILED"
            self.report_api_status(start_time, end_time, action, status, ss_required=True)

        except Exception as e:
            logger.Error("Failed to perform {} ".format(action) + str(e))
            performed = False
        finally:
            return performed


    def wait_for_element(self, elm_name, duration):
        '''
        Waits for the given element to appear

        :param elm_name: element name as in the config file
        :param duration: how long to wait for the element
        :return: True if successful, False if could not find the element within the given time
        '''

        status = "FAILED"
        present = False
        try:
            elm_type, type = self.choose_elm_type(elm_name)
            if not type:
                logger.Error("Invalid element type")
                return False

            start_time = self.gettimestamp()
            present = dut.WaitForElement(elm_type, elm_name[type], duration)
            end_time = self.gettimestamp()

            if present:
                status = "PASSED"
            self.report_api_status(start_time, end_time, "WaitForElement", status, ss_required=False)

        except Exception as e:
            logger.Error("Failed to wait" + str(e))
            present = False

        finally:
            return present


    def is_selected(self, elm_name):
        '''
        This verifies the selected property of the given element, and returns its status

        :param elm_name: name of element whose 'selected' property has to be checked
        :return: True if selected,
                else returns False
        '''


        status = "FAILED"
        selected = False
        try:
            elm_type, type = self.choose_elm_type(elm_name)
            if not type:
                logger.Error("Invalid element type")
                return False

            start_time = self.gettimestamp()
            selected = dut.IsSelected(elm_type, elm_name[type])
            end_time = self.gettimestamp()

            if selected:
                status = "PASSED"

            self.report_api_status(start_time, end_time, "IsSelected", status, ss_required=True)
        except Exception as e:
            logger.Error("Error in searching for element" + str(e))
            selected = False

        finally:
            return selected


    def is_enabled(self, elm_name):
        '''
        This verifies the selected property of the given element, and returns its status

        :param elm_name: name of element whose 'enabled' property has to be checked
        :return: True if enabled,
                else returns False
        '''


        status = "FAILED"
        enabled = False
        try:
            elm_type, type = self.choose_elm_type(elm_name)
            if not type:
                logger.Error("Invalid element type")
                return False

            start_time = self.gettimestamp()
            enabled = dut.IsEnabled(elm_type, elm_name[type])
            end_time = self.gettimestamp()

            if enabled:
                status = "PASSED"

            self.report_api_status(start_time, end_time, "IsSelected", status, ss_required=True)
        except Exception as e:
            logger.Error("Error in searching for element" + str(e))
            enabled = False

        finally:
            return enabled
