import sys, os
import time, datetime
import autoit
import pyautogui
import logging
import xlsxwriter


from fe_variables import fe_var as config
from fe_auto_config.fe_library import fe_lib
base_dir = config.base_dir
image_path = config.im_dir


class feautotest(object):
    def __init__(self):
        '''
        initializes variables
        '''
        self.script_status = True
        self.step = 0
        self.tc_name = None
        self.tc_id = None
        self.script_path = os.path.realpath(__file__)
        self.report_string = []
        self.lib = fe_lib()
        self.base_dir = config.base_dir
        self.log_file = None
        self.test_report_xl = None
        self.logger = None



    def init(self, tc_id, tc_name):
        '''
        :param tc_name: test case id/ name
        :return: true/false
        '''
        self.tc_name=tc_name
        self.tc_id = tc_id
        screen_width, screen_height = pyautogui.size()
        # creates report file

        self.create_report_files()
        self.logger.info("Initializing.. Starting run - {}".format(tc_name))
        # self.logger.info("Screen Size", "Height - {}, Width - {}".format(screen_height, screen_width))

        login = self.felogin(config.fe_username, config.fe_password)
        if not login:
            self.report("Login to FE", "FAILED", logging.WARNING)
            return False
        else:
            self.report("Login to FE", "PASSED", logging.INFO)
            return True


    def get_timestamp_formatted(self):
        time_stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        # time_stamp = time_stamp.replace(".", "_")
        # time_stamp = time_stamp.replace(" ", "_")
        # time_stamp = time_stamp.replace("-", "")
        return time_stamp.replace(":", "")


    def create_report_files(self):
        '''
        :param message:
        :param type:
        :return:
        '''

        if not (self.log_file and self.test_report_xl):
            timestamp = self.get_timestamp_formatted()
            self.log_file = config.log_dir + self.tc_id + "_" + str(timestamp) + ".log"
            self.filehandler = logging.FileHandler(self.log_file, 'a')
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            # filehandler.setLevel(logging.DEBUG)
            self.filehandler.setFormatter(formatter)
            # create handle to log file
            self.logger = logging.getLogger()  # root logger
            for hdlr in self.logger.handlers[:]:  # remove all old handlers
                self.logger.removeHandler(hdlr)
                self.logger.setLevel(logging.DEBUG)
            self.logger.addHandler(self.filehandler)
            self.logger.info("FE Test Execution Starts..")
            # createad report XL
            self.test_report_xl = config.report_dir + self.tc_id + "_" + str(timestamp) + ".xlsx"

        else:
            self.logger.info("Log file, XL report created - {}, {}".format(self.log_file, self.test_report_xl))


    def precondition(self):
        '''
        : description: verifies fe home
        :return: True if home displays, else False
        '''
        home_reached = False
        try:
            time.sleep(10)  # Initial wait for FE Home to load
            home = self.lib.is_fe_home(config.fe_win_title.format(config.fe_version,
                                                                  config.fe_username,
                                                                  config.fe_home_title_text
                                                                  )
                                       )
            if not home:
                self.report("FE Home", "FAILED", log_type=logging.WARNING, screenshot=True)
                self.script_status = False
                return False
            self.report("FE Home", "PASSED", log_type=logging.INFO, screenshot=True)
            home_reached = True
        except Exception as e:
            self.report("Login: Either user is already logged in or invalid credentials", "FAILED", log_type=logging.WARNING, screenshot=True)
            home_reached = False

        finally:
            return home_reached


    def run_test(self, tc_id, tc_name):
        '''
        :param tc_name:
        :return:
        '''
        init_test = self.init(tc_id, tc_name)
        if not init_test:
            self.script_status = False
            return self.script_status
        else:
            pre_cond = self.precondition()
            if not pre_cond:
                self.report("Precondition: FE Home", "FAILED", log_type=logging.WARNING, screenshot=True)
                return False
            else:
                self.run()


    def run(self):
        pass


    def exit_test(self):
        '''
        :description: stops the run
        :return: None
        '''
        # self.close_window()
        # sys.exit()


    def report_test_result(self):
        '''
        :return: None
        '''
        self.step += 1
        if self.script_status == True:
            status = "PASSED"
        else:
            status = "FAILED"
        self.report_string.append((self.step, self.tc_id, status, False))
        self.generate_report()


    def report(self, step_descr, step_status, log_type=logging.INFO, screenshot=False):
        '''
        :param step_status: status of the step
        :param step_descr: message to be printed for the step
        :return:
        '''

        self.log_event(message=step_descr, message_type=log_type)
        if screenshot:
            timestamp = self.get_timestamp_formatted()
            imagename = config.screenshot_dir + 'fescreenshot_{}.png'.format(timestamp)
            im = pyautogui.screenshot(imageFilename=imagename,
                                      region=config.c_fe_screenshot)
            # to append to the XL sheet and to enable hyperlink to the image file
            imagename = imagename.replace("//", "\\")
        else:
            imagename = " "
        self.step += 1
        self.report_string.append((self.step, step_descr, step_status, imagename))


    def log_event(self, message=None, message_type=logging.INFO):
        '''
        :param message: message to be appeared on the log file
        :param message_type: message type > logging.INFO, logging.WARNING
        :return: None
        '''
        self.logger.setLevel(message_type)
        self.filehandler.setLevel(message_type)
        self.logger.addHandler(self.filehandler)
        # consoleHandler.setLevel(message_type)
        if message_type == logging.INFO:
            self.logger.info(message)
        elif message_type == logging.WARNING:
            self.logger.warning(message)
        elif message_type == logging.CRITICAL:
            self.logger.critical(message)
        elif message_type == logging.ERROR:
            self.logger.error(message)
        else:
            self.logger.debug(message)


    def generate_report(self):
        '''
        :description: generates report
        :return: None
        '''

        try:
            workbook = xlsxwriter.Workbook(self.test_report_xl)
            # font formats
            header_fmt = workbook.add_format(
                {
                    'bold': True, 'border':2,
                    'font_color': 'white', 'bg_color': 'gray',
                    'align': 'center', 'valign': 'center'
                }
            )

            red = workbook.add_format({'font_color': 'red', 'border':2})
            green = workbook.add_format({'font_color': 'green', 'border':2})

            self.log_event("Generating XL report..", logging.INFO)

            report = workbook.add_worksheet("Execution Report")
            summary = ("Script Id", "Script Name", "Date", "Script Status")

            report.write_column(2, 1, summary, header_fmt)
            if self.script_status:
                script_status = "PASSED"
                font_format = green
            else:
                script_status = "FAILED"
                font_format = red

            data = (self.tc_id, self.tc_name, datetime.datetime.now().strftime("%Y-%m-%d"), script_status)
            report.write_column(2, 2, data, font_format)

            header = ("STEP NO", "ACTION", "STATUS", "IMAGE")
            report.write_row(8, 1, header, header_fmt)

            row = 9
            col = 1
            for rpt in self.report_string:
                if "FAILED" in rpt:
                    font_format = red
                elif "PASSED" in rpt:
                    font_format = green
                else:
                    font_format = None

                report.write_row(row, col, (rpt[0], rpt[1], rpt[2]), font_format)
                # if not rpt[3]:

                report.write_url(row, col+3,  rpt[3],cell_format=font_format,
                  string="Screenshot", tip="screenshot")
                row += 1
            workbook.close()
        except Exception as e:
            self.log_event(str(e), logging.WARNING)


    def close_window(self):
        '''
        :return:
        '''
        if autoit.process_exists(config.exe_file_name):
            if autoit.process_close(config.exe_file_name):
                return True
            else:
                return False
        else:
            return True


    def felogin(self, username, password):
        '''
        :param username: FE Username
        :param password: FE Password
        :return: True/False
        '''
        if autoit.process_exists(config.exe_file_name):
            autoit.process_close(config.exe_file_name)
            time.sleep(10)

        # starting the exe
        autoit.run(config.executable_name)
        time.sleep(10)
        autoit.win_wait_active(config.fe_login_win_title, 10)
        autoit.win_activate(config.fe_login_win_title)
        # autoit.control_focus(config.fe_login_win_title, "Edit2")

        # entering username and password as per the config file
        autoit.send(config.fe_username)
        time.sleep(2)
        autoit.send("{TAB}")
        time.sleep(2)
        autoit.send(config.fe_password)
        time.sleep(2)
        clicked = self.lib.find_and_click(config.btn_login)
        if clicked:
            status = "PASSED"
        else:
            status = "FAILED"
        self.report("Click on Login button", status, logging.WARNING, True)
        return clicked


        # login_btn = pyautogui.locateOnScreen(image_path +'btn_login.png')
        # if not login_btn:
        #     self.report("FE Home", "FAILED", screenshot=True)
        #     self.test_result=False
        #     return False
        # login_btnx, login_btny = pyautogui.center(login_btn)
        # if not (login_btnx and login_btny):
        #     self.logger.debug("Find Login button: Failure")
        #     return False
        # pyautogui.click(login_btnx, login_btny)
        # return True

