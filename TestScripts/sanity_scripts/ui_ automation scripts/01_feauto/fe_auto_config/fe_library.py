import sys, os
import time
import datetime
import autoit
import pyautogui
import logging
from PIL import Image
from pytesseract import image_to_string
import string

from fe_variables import fe_var as config
image_path = config.im_dir
logger = logging.getLogger()


class fe_lib(object):

    def locate_image(self, image_name):
        try:
            '''
            :param image_name: name of the image to be searched
            :return:
            '''
            located = pyautogui.locateOnScreen(image_path + image_name, minSearchTime=30)
            return pyautogui.center(located)
        except Exception as e:
            print "location_image" + str(e)

    def click_on_item(self, posx, posy, button='left'):
        '''
        :param posx: x position of the image
        :param posy: y position of the image
        :return:
        '''

        if not (posx and posy):
            return False

        pyautogui.click(posx, posy)
        return True


    def find_and_click(self, image_name):
        try:
            '''
            :param image_name: name of the image to be found and clicked
            :return: true/false
            '''

            xpos, ypos = self.locate_image(image_name)
            print "{} ->{} - {} ".format(image_name, xpos,ypos)
            if not (xpos and ypos):
                logger.warning("FAIL: Failed to find the searched image")
                return False

            self.click_on_item(xpos, ypos)
            return True
        except Exception as e:
            print "Exception from find_and_click" +str(e)

    def is_fe_home(self, window_title):#=None):
        '''
        :param window_title: title text of the window
        :return:
        '''
        if not autoit.win_wait_active(window_title, 10):
            fe_home_exists =  autoit.win_exists(window_title)
            if fe_home_exists:
                return True
        else:
            return True
        return False


    def goto_screen(self, screen_name):
        '''
        :param screen_name: Name of the window
        :return: True if window exists, else False
        '''
        if screen_name in config.screens:
            autoit.send(config.screens[screen_name][0])
            time.sleep(10)
            fe_window = autoit.win_exists(config.fe_win_title.format(config.fe_version, config.fe_username, config.screens[screen_name][1]))
            if fe_window:
                return True
            else:
                return autoit.win_wait_active(
                    config.fe_win_title.format(config.fe_username, config.screens[screen_name][1]),
                    config.t_waittime_for_window)
        else:
            logger.warning("Given Screen Name does not exist, waiting for the window")
            return False


    def window_present(self, win_title):
        '''
        :param win_title: title of the window to check the presence
        :return:
        '''
        fe_window = autoit.win_exists(win_title)
        if fe_window:
            return True
        else:
            return False


    def image_present(self, image_name=None):
        '''
        :param image_name: name of the image to be searched
        :return: True if image found, else False
        '''

        time.sleep(2)
        location = pyautogui.locateOnScreen(image_path + image_name, minSearchTime=30)
        if not location:
            logger.warning("{} not found on the screen".format(image_name))
            return False
        logger.info("{} found on the screen".format(image_name))
        return True


    def sendkey(self, key):
        '''
        :param key: keyboard shortcut/characters as string. Eg - sendkey("{TAB}") or  sendkey("shameena")
        :return: None
        '''
        sent = False
        try:
            autoit.send(key)
            sent = True
        except Exception as e:
            logger.warning("Failed to send key {}".format(key))
            sent = False
        finally:
            return sent


    def test(self):
        clicked = False
        try:
            win_title = config.fe_win_title.format(config.fe_username, config.fe_home_title_text)
            # clicked = autoit.control_click(win_title,
            #                            "[ID:properties, CLASS:WindowsForms10.Window.8.app.0.62e449_r13_ad1]")

                       # print "click 11"
            # time.sleep(5)
            #
            # clicked = autoit.control_click(win_title,
            #                                "{title:toolStripButton1, control_type=Button}")


            time.sleep(5)

            clicked = autoit.control_click(win_title,
                                           "{Name:toolStripButton1, INSTANCE:14}")

            print "click 2"
            time.sleep(5)
        except Exception as e:
            print str(e)

        print clicked
        return clicked


    def sendkeys(self, keys, interval=1):
        '''
        :param keys: comma separated list/tuple of keys - keyboard shortcut/characters as string.
        :return: True or False
        '''
        if not keys:
            logger.warning("Empty key list")
            return  False

        for key in keys:
            if self.sendkey(key):
                logger.info("Key sent - {}".format(key))
                time.sleep(interval)
            else:
                logger.warning("Failed to send the sequence")
                return False
        return True


    def create_job(self, job_name, trigger_time=None):
        try:
            if not self.window_present(config.fe_win_title.format(config.fe_username, config.scheduler_title)):
                logger.warning("Not on scheduler window, so navigating to Scheduler")
                if not self.goto_screen("scheduler"):
                    logger.warning("Failed to navigate to scheduler window")
                    return False

            clicked = self.find_and_click(config.img_create_job)
            if not clicked:
                logger.warning("Failed to click on create job")
                return False

            time.sleep(2)
            self.sendkey(job_name)
            time.sleep(1)

            self.sendkey(config.tab)
            time.sleep(1)
            self.sendkey(job_name)

            clicked = self.find_and_click(config.img_testcases_job_details)
            if not clicked:
                logger.warning("Failed to click on add test case")
                return False
            else:
                time.sleep(10)
                clicked = self.find_and_click(config.img_expand_icon)
                if not clicked:
                    logger.warning("Failed to click on expand folder button")
                    return False

                # if not self.sendkeys((config.down, config.right), 1):
                #     logger.warning("Navigate to script failed")
                #     return False

                print "clicked on 'Test scripts'"
                clicked = self.find_and_click(config.img_select_folder)
                if not clicked:
                    print "failed selecting tc folder"
                    logger.warning("Failed to click on the test case folder")
                    return False
                print "selecting tc folder - done"

                time.sleep(5)
                clicked = self.find_and_click(config.img_add_tc)
                if not clicked:
                    print "failed to add tc "
                    logger.warning("Failed to add testcase")
                    return False

            print "choose device "
            clicked = self.find_and_click(config.img_device_details)
            if not clicked:
                print "failed to choose device "
                logger.warning("Failed to click on add device")
                return False
            else:
                time.sleep(10)
                print "expand device list"
                clicked = self.find_and_click(config.img_expand_icon)
                if not clicked:
                    logger.warning("Failed to click on expand device list")
                    return False

                clicked = self.find_and_click(config.img_select_device)
                if not clicked:
                    logger.warning("Failed to choose the device")
                    return False

                clicked = self.find_and_click(config.img_add_device)
                if not clicked:
                    logger.warning("Failed to choose the device")
                    return False

                if trigger_time:    # if trigger time is required
                    added = self.add_trigger_time(fire_time=trigger_time)
                    if not added:
                        logger.warning("Failed to set the trigger time")
                        return False

                return self.save_job()

        except Exception as e:
            logger.warning(str(e))
            print e


    def save_job(self):
        clicked = self.find_and_click(config.img_save_job)
        if not clicked:
            logger.warning("Failed to click on Save button")
            return False
        time.sleep(1)   # wait for the conflict window to appear
        if self.window_present(config.sched_conflict_window_title):
            clicked = self.find_and_click(config.sched_conflict_yes)
            if not clicked:
                logger.warning("Failed to click on Yes Button")
                return False

            time.sleep(1)
        return True


    def set_trigger_time(self, fire_time):

        set = False
        try:
            current_time = datetime.datetime.now()
            if not fire_time:
                fire_time = (0, 0, 10, 0)  # 10 minutes
                current_time = datetime.datetime.now()

            trigger_time = current_time + datetime.timedelta(days=fire_time[0],
                                                             hours=fire_time[1],
                                                             minutes=fire_time[2],
                                                             seconds=fire_time[3]
                                                             )
            for attr in ['day', 'month', 'year', 'hour', 'minute', 'second']:
                val = getattr(trigger_time, attr)
                self.sendkey(str(val))
                time.sleep(1)
                self.sendkey(config.kbd_keys['RIGHT'])
            set = True
        except  Exception as e:
            logger.warning("FAiled to set trigger time")
            set = False
        finally:
            return set


    def add_trigger_time(self, fire_time=None):
        '''

        :param fire_time: next trigger time in number of days, hours, mins, seconds
                        Eg: self.add_trigger_time(fire_time=(1, 2, 3, 0)
                            This means next trigger time will be after a day, 2hours, 3 mins from the current time

                            if current time is 1:10 PM (24/10/2018), trigger time would be 25/10/2018 15:13:00
        :return: True or False
        '''
        time_set = False
        try:

            clicked = self.find_and_click(config.img_triggers_job_details)
            if not clicked:
                logger.warning("Failed to click on Triggers tab")
                return False

            logger.info("Clicked on Triggers tab")
            clicked = self.find_and_click(config.img_new_trigger)
            if not clicked:
                logger.warning("Failed to click on New Trigger")
                return False

            time.sleep(1)
            self.sendkey(config.kbd_keys['TAB'])
            self.sendkey(config.kbd_keys['TAB'])
            time.sleep(1)

            if not fire_time:
                fire_time = (0, 0, 10, 0)

            time_set = self.set_trigger_time(fire_time)
            if not time_set:
                logger.warning("Failed to add trigger time")
                return False
            logger.info("Trigger time added")

            clicked = self.find_and_click(config.img_save_job)
            if not clicked:
                logger.warning("Failed to choose the device")
                return False

            time_set = True

        except Exception as e:
            logger.error("Execption in setting trigger time - {}".format(e))
            time_set = False
        finally:
            return time_set


    def doubleclick_on_item(self, item=None, xpos=None, ypos=None):
        print "----doubleclick_on_item ---"
        clicked = False
        try:
        #     if not (xpos and ypos) and item:
        #         xpos, ypos = self.locate_image(item)
        #         print "hererererere"
        #     elif item == None and not (xpos and ypos):
        #         logger.warning("No image name and coordinate info to click")
        #         print "------"
        #         return clicked
        #     else:
        #         print "here"

            if not xpos and not ypos:
                if not item:
                    logger.warning("No image name or location given")
                    clicked = False
                    return clicked
                else:
                    xpos, ypos = self.locate_image(item)


            print "doubleclick_on_itemdoubleclick_on_item"
            pyautogui.doubleClick(xpos, ypos, interval=0)
            print "doubleclick_on_item"
            clicked = True
        except Exception as e:
            logger.warning("Double Click Failed")
            print "failed"
            clicked = False

        finally:
            return clicked


    def delete_job(self):
        if self.find_and_click(config.scheduler_screen['removejob_active']):
            time.sleep(1)   # wait for the confirmation pop up to appear
            self.sendkey(config.kbd_keys['ENTER'])
            time.sleep(1)
            self.sendkey(config.kbd_keys['ENTER'])
            logger.info("Deleted the selected job")
            return True
        else:
            logger.warning("Failed to delete the job")
            return False


    def window_maximize(self, win_title):
        '''
        :param win_title: window title
        :return:
        '''
        win = pyautogui.getWindow(win_title)
        win.maximize()


    def window_getfocus(self, title):
        '''
        :param title: window title
        :return:
        '''
        focused = autoit.control_get_focus(title)
        return focused


    def right_click_on_item(self, item = None, xpos = None, ypos = None):
        if not (xpos and ypos) and item:
            xpos, ypos = self.locate_image(item)
        elif item == None and not (xpos and ypos):
            logger.warning("No image name and coordinate info to click")
            return False
        else:
            pass
        pyautogui.rightClick(xpos, ypos)
        return True

    def verify_button_screen(self, ui_items, item_screen):
        global all_items
        try:
            for item in ui_items:
                if item in item_screen:
                    item_present = self.image_present(item_screen[item])
                    if not item_present:
                        item_present = self.image_present(item_screen[item])
                    if item_present:
                        all_items = True
                    else:
                        all_items = False
                else:
                    all_items = False
                    logger.error("UI element not found in config - {}".format(item), "FAILED", logging.WARNING, True)
        except Exception as e:
            print "error from verify button screen" + str(e)
        finally:
            return all_items

    def search_scheduler_job(self, jobname):
        searched = False
        try:
            xpos, ypos = self.locate_image(config.img_search_job_edit_box)
            clicked = self.find_and_click(config.img_search_job_edit_box)
            if not clicked:
                logger.warning("Failed to click on Search Job edit box")
                return searched

            logger.warning("Clicked on Search Job edit box")
            time.sleep(2)

            print "search"
            self.sendkey(jobname)
            self.sendkey(config.kbd_keys["ENTER"])

            if not self.image_present(config.img_fe_test_job):
                logger.warning("Failed to get the Search Result")
            else:
                logger.info("Search result for job name {} obtained".format(jobname))
                searched = True
        except Exception as e:
            logger.warning("Exception from search_scheduler_job() - {}".format(e))
            searched = False
        finally:
            return searched


    def timestamp(self):
        timestr = datetime.datetime.now().strftime("%H:%M:%S.%f").replace(".", "_")
        return timestr.replace(":", "_")


    def get_text(self, region=None):
        read_text = None
        try:
            print "111"
            tessdata_dir_config = config.ocr_param

            # print "11"
            # img_time = datetime.datetime.now().strftime("%H:%M:%S.%f").replace(".", "_")
            # img_time = img_time.replace(":", "_")
            # print "img_time", img_time

            imagename = config.ocr_dir + config.ocr_img_name.format(self.timestamp())
            print imagename
            time.sleep(3)
            im = pyautogui.screenshot(imageFilename=imagename,
                                      region=region)

            basewidth = config.basewidth
            img = Image.open(imagename)
            wpercent = (basewidth / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((basewidth, hsize), Image.ANTIALIAS)
            img.save(imagename)
            read_text = image_to_string(img, lang='eng', config=tessdata_dir_config)
            print "read_text", read_text

        except Exception as e:
            logging.warning("Failed to read from the given area")
            read_text = None
        finally:
            return read_text


    def delete_report(self):
        # deletes first item on the filtered result of the reports page
        item_pos = config.c_job_in_report
        if not self.click_on_item(item_pos[0], item_pos[1], button='right'):
            logger.warning("Failed to click on given report")
            return False

        if not self.find_and_click(config.delete_job_report):
            logger.warning("Delete context menu not found")
            return False

        # wait time for the delete confirmation popup to appear
        time.sleep(2)

        if not self.find_and_click(config.confirm_delete_job):
            logger.warning("Failed to click on confirmation popup")
            return False
        return True


    def clear_search_box(self, search_feature="scheduler"):
        clear_item = None
        if search_feature == "scheduler":
            clear_item =  config.img_search_job_edit_box
        if search_feature == "chkpt_explorer":
            clear_item = config.checkpoint_search_box

        xpos, ypos = self.locate_image(clear_item)
        clicked = self.doubleclick_on_item(xpos=xpos, ypos=ypos)
        if not clicked:
            logger.warning("Failed to click on the Search Text Field")
            return False

        self.sendkey(config.kbd_keys["BS"])
        return True


    def expand_job(self):
        '''
        expands first test result
        :return:
        '''
        if not self.find_and_click(config.img_expand_icon):
            logger.error("Failed to click to expand the reports")
            return False

        print "111111"

        time.sleep(1)
        self.sendkey(config.kbd_keys['DOWN'])
        time.sleep(1)
        xres, yres = self.locate_image(config.img_test_result)
        print "222222", xres, "--", yres
        if not (xres or yres):
            logger.warning("Failed to find the test result")
            # return False

        time.sleep(1)
        print "*****"
        # coordinates are adjusted slightly, so that the click will not interfere with the
        # job name
        if not self.doubleclick_on_item(xres + 5, yres + 3):
            logger.warning("Failed to see the test result")
            return False


        time.sleep(5)   # wait time to load the test results
        return True


    def get_test_result(self):
        '''
        reads the test result from the test summary
        :return:
        '''
        test_res = self.get_text(config.c_reports_test_result)
        if test_res in config.possible_test_results:
            return test_res
        else:
            return None


    def export_report_to_txt_file(self, windowname=None):
        log_file = None
        try:
            if not (windowname in config.export_report_pages.keys()):
                logger.warning("Wrong Window name")
                return False

            click_params = config.export_report_pages[windowname]
            print click_params
            self.click_on_item(click_params[0], click_params[1])    # to get focus on the logs area
            # if not self.click_on_item(click_params[0], click_params[1], button='right'):
            if not autoit.mouse_click('right', click_params[0], click_params[1]):
                logger.warning("Failed to click on the test result log")
                return False

            down = config.kbd_keys['DOWN']
            self.sendkeys((down, down, down, down, config.kbd_keys['ENTER']), interval=3)

            time.sleep(3)   # wait time for the file save dialog box to appear
            log_file = config.ocr_dir+"logs_{}.txt".format(self.timestamp())
            log_fil = log_file.replace("//", "\\" )
            if not self.sendkey(log_fil):
                logger.warning("Failed to send the log file name to Faile Save dialogue")
                return False

            time.sleep(3)
            try:
                print "search save button"
                if not self.find_and_click(config.img_save_job):
                    logger.warning("Failed to click on Save button")
                else:
                    print "save button found"

            except Exception as e:
                logger.warning("Save button not found")
            finally:
                print "enter key"
                self.sendkey(config.kbd_keys['ENTER'])
                time.sleep(2)

        except Exception as e:
            logger.warning("Could not save the log file")
            log_file = None

        finally:
            return  log_file


    def read_test_status_from_log_file(self, file_name=None):

        test_status = None
        try:
            print file_name
            if not file_name:
                logger.warning("No file given")
                return test_status

            error = 0
            log_file = open(file_name)
            print "opened"
            line = log_file.readline()
            print "line", line
            while(line):

            # for i in range(0, 30):
                # if line.count("ERROR"):
                #     error += 1

                if line.count(config.str_test_result):
                    result = line.split("|")
                    result = result[1].strip()
                    test_status = result
                    print "test_status", test_status
                    break

                line = log_file.readline()

        except Exception as e:
            logger.warning("Error in reading status")
            test_status = None

        finally:
            return test_status


    def treeview_action(self, node_name=None, action="Expand"):

        if not autoit.control_tree_view(
                "TestScripts",
                "[CLASS:{}; NAME:{}]".format(config.class_tree_view, config.script_editor_node),
                command=action
                ):
            logger.warning("Failed to expand the tree")
            return False
        return True


    def open_script(self, keys_to_open_script=None):
        if not keys_to_open_script:
            logger.warning("No keys given to open script")
            return False

        if not self.sendkeys(config.keys_to_open_script, 1):
            logger.warning("Failed to send navigation keys")
            return False

        return True


    def start_local_execution(self):
        # if not self.open_script(config.keys_to_open_script):
        #     logger.warning("Could not open script")
        #     return False

        if not self.find_and_click(config.choose_dut):
            logger.warning("Failed to find the Select Dut drop down")
            return False

        if not self.sendkeys((config.down, config.enter), 1):
            logger.warning("Failed to choose device")
            return False

        if not self.find_and_click(config.start_execution):
            logger.warning("Failed to find the start execution button")
            return False

        return True
		
		
		
    def create_ocr_checkpoint(self, checkpoint_name):
        try:
            self.window_maximize("Checkpoint Explorer ")
            time.sleep(1)
            clicked = self.find_and_click(config.create_new_checkpoint)
            time.sleep(1)
            if clicked:
                self.sendkeys([config.down, config.enter], 1)
                time.sleep(1)
                self.sendkey(checkpoint_name)
                time.sleep(1)
                self.sendkey(config.enter)
                time.sleep(2)
                dut_clicked = self.find_and_click(config.checkpoint_dut_type)
                if not dut_clicked:
                    logger.warning("failed to find the Dut Type")
                    return False

                time.sleep(1)
                select_dut_clicked = self.find_and_click(config.checkpoint_select_dut)
                if not select_dut_clicked:
                    return False
                time.sleep(1)
                self.sendkeys([config.down, config.enter], 1)
                capture_clicked = self.find_and_click(config.checkpoint_quick_capture)
                time.sleep(10)
                if not capture_clicked:
                    return False
                coord_click = self.find_and_click(config.checkpoint_coordinates)
                if not coord_click:
                    return False
                self.sendkeys(["51", config.kbd_keys['TAB'], "335", config.kbd_keys['TAB'], "267", config.kbd_keys['TAB'], "60"], 1)
                click_ref_text = self.find_and_click(config.ocr_ref_text_box)
                if click_ref_text:
                    self.sendkey(".*")
                    self.find_and_click(config.checkpoint_save_button)
                    time.sleep(1)
                    return True
            else:
                return False
        except Exception as e:
            print "Exception from create_checkpoint " + str(e)
            return False


    def create_ic_checkpoint(self, checkpoint_name):
        try:
            # self.window_maximize("Checkpoint Explorer ")
            # time.sleep(1)
            clicked = self.find_and_click(config.create_new_checkpoint)
            time.sleep(1)
            if clicked:
                self.sendkeys([config.kbd_keys['DOWN'], config.kbd_keys['DOWN'], config.kbd_keys['ENTER']], 1)
                self.sendkey(checkpoint_name)
                self.sendkey(config.kbd_keys['ENTER'])
                time.sleep(1)
                dut_clicked = self.find_and_click(config.checkpoint_dut_type)
                if not dut_clicked:
                    return False
                time.sleep(1)
                select_dut_clicked = self.find_and_click(config.checkpoint_select_dut)
                if not select_dut_clicked:
                    return False
                time.sleep(1)
                self.sendkeys([config.kbd_keys['DOWN'], config.kbd_keys['ENTER']], 1)
                capture_clicked = self.find_and_click(config.checkpoint_quick_capture)
                time.sleep(2)
                if not capture_clicked:
                    return False
                coord_click = self.find_and_click(config.checkpoint_coordinates)
                if not coord_click:
                    return False
                self.sendkeys(["51", config.kbd_keys['TAB'], "335", config.kbd_keys['TAB'], "267", config.kbd_keys['TAB'], "60"], 1)
                self.click_on_item(500, 500)
                time.sleep(1)
                ref_img_btn_clicked = self.find_and_click(config.ic_ref_img_btn)
                time.sleep(2)
                if ref_img_btn_clicked:
                    self.find_and_click(config.checkpoint_save_button)
                    return True
            else:
                return False
        except Exception as e:
            print "Exception in create_ic_checkpoint() " + str(e)
            return False

    def delete_checkpoint(self, checkpoint_name, chkpt_type):
        try:
            clicked = self.find_and_click(config.checkpoint_search_box)
            if clicked:
                self.sendkeys([checkpoint_name, config.enter], 1)
                if chkpt_type == "IC":
                    search_list_chkpt = config.search_list_ic_chkpt
                else:
                    search_list_chkpt = config.search_list_ocr_chkpt
                clicked = self.find_and_click(search_list_chkpt)
                if clicked:
                    self.right_click_on_item(search_list_chkpt)
                    self.sendkeys([config.kbd_keys['DOWN'], config.kbd_keys['DOWN'], config.kbd_keys['DOWN'], config.kbd_keys['ENTER'], config.kbd_keys['ENTER']], 1)
                    return True
                else:
                    return False
        except Exception as e:
            print e

    def clear_search_list(self):
        try:
            clicked = self.find_and_click(config.filled_checkpoint_search_box)
            time.sleep(2)
            if clicked:
                self.right_click_on_item(config.filled_checkpoint_search_box)
                time.sleep(10)
                self.sendkeys([config.kbd_keys['DOWN'], config.kbd_keys['DOWN'], config.kbd_keys['DOWN'],
                               config.kbd_keys['DOWN'], config.kbd_keys['DOWN'], config.kbd_keys['DOWN'],
                               config.kbd_keys['ENTER']], 1)
                self.sendkeys([config.kbd_keys['BS']], 1)
        except Exception as e:
            pass
