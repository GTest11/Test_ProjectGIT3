# ''''''''''''''''''''''''''' COMMON FUNCTIONS '''''''''''''''''''''''''''''''''''''''''
# Author            : Shameena HA
# Date              :   26-11-2018
# Script Version     : 1.0
# Modification details:
# ''''''''''''''''''''''''''' COMMON FUNCTIONS - END '''''''''''''''''''''''''''''''''

import clr
import sys
import os
import datetime
import time
from PIL import Image
import cStringIO
import urllib
from collections import OrderedDict

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
from config.androidphone import AndroidPhone
from config.ipad import IPad
from config.iphone import IPhone


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

        self.mob_lib = mob_lib


    # zee5
    def get_dut_platform(self):
        """
        :return: reads the Dut Platform if available
                    returns None, if it could not read
        """

        dut_platform = None
        try:
            dut_platform = dut.ReadProperty(3)
        except Exception as e:
            logger.Error("Failed to read the platform name" + str(e))
            dut_platform = None
        finally:
            logger.Log("Obtained dut platform using ReadProperty API : " + str(dut_platform))
            return dut_platform


    def get_dut_name(self):
        """
        Reads the dut name
        :return: dut name or None
        """

        dut_name = None
        try:
            dut_name = dut.ReadProperty(1)
        except Exception as ex:
            logger.Error("Failed to read DUT Name: " + str(ex))
            return None
        finally:
            return dut_name

    # zee5
    def set_config(self, app_name=None):
        """
        Sets the config file to a variable as per the device type and platform
        :param app_name: application under test,
                        give its name as configured in the config.py file
        :return: returns the config file to be used for the script execution, if available.
                    else returns None.
        """

        config = None
        platform = self.get_dut_platform()
        logger.Log("---------- platform {}".format(platform))
        try:
            dut_type = dut.ReadProperty(2)
            logger.Log("---------- dut_type {}".format(dut_type))

            if platform not in ["Android", "iOS"]:
                logger.Log("Improper platform obtained using ReadProperty API. Platform obtained : "+str(dut_type))
                return config

            if platform == "Android":
                config = AndroidPhone
                device_config.AppActivity = config.activity[app_name]
                device_config.AppPackage = config.package[app_name]

            if platform == "iOS" and dut_type == "iPhone":
                config = IPhone
                device_config.AppName = config.app_name[app_name]

            if platform == "iOS" and dut_type == "iPad":
                config = IPad
                device_config.AppName = config.app_name[app_name]

            device_config.DeviceType = platform

            self.element_type_to_test = config.element_type_to_test
            logger.Log("Configured Element Type {}".format(self.element_type_to_test))

        except Exception as e:
            logger.Error("Failed to read device platform name" + str(e))
            config = None

        finally:
            self.config = config
            logger.Log(">>>>>>>>>>> config " + str(self.config))
            # return self.config

    # zee5
    def get_time_stamp(self):
        """
        :return: current time in milliseconds,
                else returns None
        """
        time_converted = None
        try:
            timestamp = datetime.datetime.now().strftime("%H:%M:%S.%f")
            time_converted = self.time_in_millisecond(timestamp)
        except Exception as e:
            logger.Error("Failed to get time in required format" + str(e))
            time_converted = None
        finally:
            return time_converted

    # zee5
    def time_in_millisecond(self, time_in_string):
        """
        :param time_in_string: time in string format
        :return: coverts the given time in string format to milliseconds
        """

        converted_time = None
        try:
            hours, minutes, seconds = (["0", "0"] + time_in_string.split(":"))[-3:]
            hours = int(hours)
            minutes = int(minutes)
            seconds = float(seconds)
            converted_time = int(3600000 * hours + 60000 * minutes + 1000 * seconds)
        except Exception as e:
            logger.Error("Failed to convert the given time to milli seconds" + str(e))
            converted_time = None
        finally:
            return converted_time


    def commit_step(self, step_name, message):
        '''
        :param step_name: Name of the step or step number
        :param message: Message to be printed for the step
        :return: None
        '''

        dut.CommitStepResult(step_name, message)


    def upload_ss(self):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        # timestamp = timestamp.replace(":", "")
        image_name = "img_{}".format(timestamp)
        img = None
        try:
            ss = dut.GetScreenshot()
            time.sleep(1)
            img = dut.validator.UploadScreenshot(image_name, ss)
            # logger.Log("Uploaded image {}".format(img))
        except Exception as e:
            logger.Error("Exception - " + str(e))
            img = None
        finally:
            return img


    def report(self, step_name, status, ss_required=False):
        '''

        :param step_name: Name of the step or step number
        :param message: Message to be printed for the step
        :param image_required: whether image to be attached or not
        :return:
        '''

        if ss_required:
            ss = self.upload_ss()
            if not ss:
                logger.Error("Could not take/upload Screenshot")

            # timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            # # timestamp = timestamp.replace(":", "")
            # image_name = "img_{}".format(timestamp)
            # try:
            #     ss = dut.GetScreenshot()
            #     time.sleep(1)
            #     dut.validator.UploadScreenshot(image_name, ss)
            # except Exception as e:
            #     logger.Error("Could not take/upload Screenshot")

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

        closed = False
        status = "FAILED"
        try:
            start_time = self.get_time_stamp()
            closed = dut.CloseApp()
            end_time = self.get_time_stamp()
            if closed:
                status = "PASSED"
            self.report_api_status(start_time, end_time, "CloseApp", status, ss_required=True)

        except Exception as e:
            logger.Error("Failed to close the application " + str(e))
            closed = False

        finally:
            return closed

    # zee5
    def stop_driver(self):
        """
        stops the Dut
        :return: None
        """
        try:
            start_time = self.get_time_stamp()
            dut.Stop()
            end_time = self.get_time_stamp()
            self.report_api_status(start_time, end_time, "Stop", "PASSED", ss_required=False)

        except Exception as e:
            logger.Error("Failed to stop the driver " + str(e))

    def choose_elm_type(self, elm_name):
        '''
        this function inspects the config variable, whether that is supported by any of the element attributes in config
        If supports, returns the same type, else returns None or xpath as default type

        :param elm_name: name of the element as in the config file
        :return: success: returns element type, and the supporting index of the element
                failure: returns both as None
        '''

        # logger.Log("element {}".format(elm_name))
        elm_type = None
        type = None
        try:
            element_types = ['xpath', 'id', 'name', 'class', 'access_id']
            preferred_element_type = self.config.element_type_to_test #element_types[4]  # currently 'access_id' is the preferred element type
            if elm_name[preferred_element_type] is not None:
                elm_type = self.list_element_types[preferred_element_type]
                type = preferred_element_type
            else:
                for element_type in element_types:
                    if elm_name[element_type] is not None:
                        elm_type = self.list_element_types[element_type]
                        type = element_type
                        break
                else:
                    logger.Error("Failed to find any valid attributes of the element. Check the element attributes passed!")

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

            start_time = self.get_time_stamp()
            present = dut.IsElementPresent(elm_type, elm_name[type])
            end_time = self.get_time_stamp()

            if present:
                status = "PASSED"

            self.report_api_status(start_time, end_time, "IsElementPresent", status, ss_required=False)
        except Exception as e:
            logger.Error("Error in searching for element" + str(e))
            present = False

        finally:
            return present


    def is_enabled(self, elm_name=None):
        '''

        Checks the enabled property of the given element on the screen

        :param elm_name: name of the element as in the config
        :return: True if found,
                else False
        '''

        status = "FAILED"
        enabled = False
        try:
            elm_type, type = self.choose_elm_type(elm_name)
            if not type:
                logger.Error("Invalid element type")
                return False

            start_time = self.get_time_stamp()
            enabled = dut.IsEnabled(elm_type, elm_name[type])
            end_time = self.get_time_stamp()

            if enabled:
                status = "PASSED"

            self.report_api_status(start_time, end_time, "IsEnabled", status, ss_required=False)
        except Exception as e:
            logger.Error("Error in searching for element" + str(e))
            enabled = False

        finally:
            return enabled



    def tap_element(self, elm_name=None):
        '''

        Taps on the given element on the screen

        :param elm_name: name of the element as in the config
        :return: True if tapped,
                else False
        '''

        status = "FAILED"
        tapped = False
        try:
            elm_type, type = self.choose_elm_type(elm_name)
            if not type:
                logger.Error("Invalid element type")
                return False

            start_time = self.get_time_stamp()
            tapped = dut.TapElement(elm_type, elm_name[type])
            end_time = self.get_time_stamp()

            if tapped:
                status = "PASSED"

            time.sleep(1)
            self.report_api_status(start_time, end_time, "TapElement", status, ss_required=True)

        except Exception as e:
            logger.Error("Error in searching for element" + str(e))
            tapped = False

        finally:
            return tapped


    def element_ops(self, elm_name, index=None, action='present'):
        '''
        This function is to find the element presence, does the action as based on 'action' param

        :param elm_name: Name of the element as in the config file
        :param action: 'present' or 'tap' or 'click'
        :return: True if success
                    False if failed
        '''

        actions = [
            'present', 'tap', 'tapindex',
            'click', 'clickindex', 'doubletap',
            'doubletapindex',
        ]

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

            start_time = self.get_time_stamp()
            present = dut.IsElementPresent(elm_type, elm_name[type])
            end_time = self.get_time_stamp()

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

            if action is 'doubletap' or action is 'doubletapindex':
                elm_op = dut.DoubleTapElement

            if action == 'tapindex' or action == 'clickindex' or action == 'doubletapindex':
                start_time = self.get_time_stamp()
                performed = elm_op(elm_type, elm_name[type], index)
                end_time = self.get_time_stamp()

            if action == 'tap' or action == 'click' or action == 'doubletap':
                start_time = self.get_time_stamp()
                performed = elm_op(elm_type, elm_name[type])
                end_time = self.get_time_stamp()

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

            start_time = self.get_time_stamp()
            present = dut.WaitForElement(elm_type, elm_name[type], duration)
            end_time = self.get_time_stamp()

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

            start_time = self.get_time_stamp()
            selected = dut.IsSelected(elm_type, elm_name[type])
            end_time = self.get_time_stamp()

            if selected:
                status = "PASSED"

            self.report_api_status(start_time, end_time, "IsSelected", status, ss_required=True)
        except Exception as e:
            logger.Error("Error in searching for element" + str(e))
            selected = False

        finally:
            return selected


    def send_keys(self, elm_name, keys=None):
        '''
        This verifies the selected property of the given element, and returns its status

        :param elm_name: name of element to which text has to be sent
        :return: True if sent,
                else returns False
        '''


        status = "FAILED"
        sent = False
        try:
            elm_type, type = self.choose_elm_type(elm_name)
            if not type:
                logger.Error("Invalid element type")
                return False

            start_time = self.get_time_stamp()
            sent = dut.SendKeys(elm_type, elm_name[type], keys)
            end_time = self.get_time_stamp()

            if sent:
                status = "PASSED"

            self.report_api_status(start_time, end_time, "SendKeys", status, ss_required=True)

        except Exception as e:
            logger.Error("Error in searching for element" + str(e))
            sent = False

        finally:
            return sent


    def get_text(self, elm_name, index=None):
        '''
        This verifies the selected property of the given element, and returns its status

        :param elm_name: name of element from which text has to be read
        :return: read string,
                else returns None
        '''


        status = "FAILED"
        text = None
        try:
            elm_type, type = self.choose_elm_type(elm_name)
            if not type:
                logger.Error("Invalid element type")
                return False

            if index == None:
                api_param = (elm_type, elm_name[type])
                api = "GetText"
            else:
                api_param = (elm_type, elm_name[type], index)
                api = "GetText(Index)"


            start_time = self.get_time_stamp()
            text = dut.GetText(*api_param)
            end_time = self.get_time_stamp()

            if text:
                status = "PASSED"
            self.report_api_status(start_time, end_time, api, status, ss_required=True)

        except Exception as e:
            logger.Error("Error in searching for element" + str(e))
            text = None

        finally:
            return text


    def compare_images(self, img1, img2):
        '''
        This compares two images and returns the comparison status
        The expected images should be obtained from CaptureImage

        :param img1: first image
        :param img2: second image
        :return: True if both are similar,
                Else returns False

        '''

        compared = False
        try:
            compared = dut.validator.ImageMatch(img1, img2, 2, "13")
        except Exception as e:
            logger.Log("Failed to compare")
            compared = False
        finally:
            return compared


    def get_image_resolution(self):
        '''

        :return:
        '''

        resolution = None
        try:
            # image_url = self.upload_ss()
            # if not image_url:
            #     return resolution

            image_url = dut.validator.QuickCapture("get_image_resolution")
            file_name = cStringIO.StringIO(urllib.urlopen(image_url).read())
            img = Image.open(file_name)
            resolution = img.size

        except Exception as e:
            logger.Log("Failed to get the resolution")
            resolution = None

        finally:
            return resolution


    def verify_playback(self):
        '''
        This verifies the playback in given area and returns its status

        :return: True if motion, else False
        '''

        playback = False
        try:
            playback = dut.validator.DetectMotion(*self.config.detect_motion_check)

        except Exception as e:
            logger.Log("Failed to verify media playback")
            playback = False

        finally:
            return playback


    def hide_keyboard(self):
        '''

        :return:
        '''


        hidden_status = False
        try:
            start_time = self.get_time_stamp()
            hidden = dut.HideKeyboard()
            end_time = self.get_time_stamp()
            if hidden:
                status = "PASSED"
                hidden_status = True
            else:
                status = "FAILED"

            time.sleep(3) # small delay before taking screenshot
            self.report_api_status(start_time, end_time, "HideKeyboard", status, ss_required=True)
            time.sleep(1)

        except Exception as e:
            logger.Error("Exception from hide_keyboard() " + str(e))
            hidden_status = False
        finally:
            return hidden_status


    def cleartext(self, elm_name):
        '''

        :param elm_name: name of the text field
        :return:
        '''


        cleared = False
        try:

            elm_type, type = self.choose_elm_type(elm_name)
            if not type:
                logger.Error("Invalid element type")
                return False

            start_time = self.get_time_stamp()
            cleared = dut.ClearText(elm_type, elm_name[type]) # search_txt_box
            end_time = self.get_time_stamp()
            dut.validator.QuickCapture("ClearText_imageName")
            time.sleep(5)
            gettext = dut.GetText(elm_type, elm_name[type])
            # lib.chkpt.init(lib.constants.CHKPNT_CLEARTEXT)
            if not gettext or gettext == self.config.searchbox_default_text:
                status = "PASSED"
                cleared = True
            else:
                status = "FAILED"

            self.report_api_status(start_time, end_time, "ClearText", status, ss_required=True)

        except Exception as e:
            logger.Log("Exception from cleartext() " + str(e))
            cleared = False

        finally:
            return cleared


    def search_in_app(self):
        '''
        Sends the given keyword to the text box

        :return: True or False
        '''

        searched = False
        try:

            clicked = self.element_ops(self.config.search_icon, index=None, action='click')
            if not clicked:
                return False

            logger.Log("Clicked on the given element")
            keys_sent = self.send_keys(self.config.search_box, keys=self.config.search_text)
            if not keys_sent:
                return False

            searched = True

        except Exception as e:
            logger.Error("Exception raised in search_in_youtube function : " + str(e))
            searched = False

        finally:
            return searched

    def play_back_from_search_result(self):
        """Searches for the configured string in youtube. Selects an entry from the suggestion for playback and
        verifies if playback has started. Returns Boolean output as per detect motion evaluation."""
        if self.search_in_app():
            time.sleep(5)
            dut.TapPercent(*self.config.TAP_PERCENT_FIRST_SEARCH_RESULT)
            time.sleep(5)
            dut.TapPercent(*self.config.TAP_PERCENT_VIDEO_TO_PLAY)
            time.sleep(3)
            return self.verify_playback()
        else:
            return False


    def launch_app(self):
        launched = False
        # if not self.close_app():
        #     logger.Error("Failed to close the application")
        #     return False
        #
        # # wait before launching app again
        # time.sleep(3)

        try:
            start_time = self.get_time_stamp()
            launched = dut.LaunchApp()
            end_time = self.get_time_stamp()
            if launched:
                status = "PASSED"
            else:
                status = "FAILED"
            self.report_api_status(start_time, end_time, status, ss_required=True)
            self.report("API: LaunchApp", status, False)

        except Exception as e:
            logger.Error("Exception " + str(e))
            launched = False

        finally:
            return launched


    def get_test_params(self, list_of_idices, dict_of_params):
        test_data = {}
        test_data_count = list_of_idices
        idx = 0
        for index in test_data_count:
            # test_data.update(self.config.capture_image_params[index])
            test_data[idx] = dict_of_params[index]
            idx += 1

        return test_data


    def add_custom_attribute(self, attr_name):
        '''
        :param attr_name: adds  attr_name to the list of custom dut attributes
        :return: True or False, based on the AddCustomDUTAttribute API status
        '''

        done = False
        try:

            start_time = self.get_time_stamp()
            attribute_added = dut.AddCustomDUTAttribute(attr_name)
            end_time = self.get_time_stamp()

            if attribute_added:
                status = "PASSED"
                done = True
            else:
                status = "FAILED"
                done = False
            self.report_api_status(start_time, end_time, status, "AddCustomDUTAttribute", ss_required=False)


        except Exception as e:
            logger.Log("Exception from precondition " + str(e))
            done = False

        finally:
            return done


    def is_app_open(self):
        '''
        Verifies an element presence in the application.
        If element present, returns True.
        Else returns False

        :return: True if found,
                Else returns False
        '''

        opened = False
        try:
            opened = self.is_present(elm_name=self.config.home)
        except Exception as e:
            logger.Error("Failed to verify the Application open status " + str(e))
            opened = False
        finally:
            return opened


    def send_keycode(self, key):
        '''
        Sends the given android key
        :param key:
        :return:
        '''
        start_time = self.get_time_stamp()
        sent = dut.SendAndroidKeyCode(key)
        end_time = self.get_time_stamp()
        if sent:
            status = "PASSED"
        else:
            status = "FAILED"
        logger.Log("API - {} - returned {}".format(key, sent))
        self.report_api_status(start_time, end_time, key, status, ss_required=True)
        return sent


    def handle_alert(self, action=None):
        '''

        :param type:
        :return: True or False
        '''
        done = False
        if not action:
            logger.Error("Improper Action")
            return False
        try:
            start_time = self.get_time_stamp()
            done = dut.HandleAlertMessage(action)
            end_time = self.get_time_stamp()
            if done:
                status = "PASSED"
            else:
                status = "FAILED"
            logger.Log("API - {} - returned {}".format(action, done))
            self.report_api_status(start_time, end_time, "HandleAlertMessage", status, ss_required=True)
        except Exception as e:
            logger.Error("Failed to handle the Alert {}".format(e))
        finally:
            return done


    def initiate_playback_coordinate(self, coords=None):
        try:
            pass
        except Exception as e:
            logger.Log("Failed to start the playback "+ str(e))

