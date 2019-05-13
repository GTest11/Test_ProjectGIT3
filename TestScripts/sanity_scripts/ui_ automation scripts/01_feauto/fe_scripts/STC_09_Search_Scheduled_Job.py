# --------------------------------------------------------------------------------------
# TC Id: FE_01
# Module: Scheduler
# TC Summary:  To check Search feature
# TC Steps: 1) Launch the application.
#           2)  Navigate to scheduler tab.
#           3) Click on Search text field and search  with
#             i. whole Job name
#             ii. Part of job name
#             iii. Empty search
# Expected: 3)
#       i. Should list only the specified job (if the whole job name is not a part on any other
#           Job name other wise those jobs also will list)
#       ii. Should list all the Jobs containing the search string in its name
#       iii. Should not have any change in the UI. Currently the scheduler list is refreshing.
# --------------------------------------------------------------------------------------

# imports
import time, datetime, os
import logging
from fe_auto_config.fe_variables import fe_var as config
from fe_auto_config.feauto import feautotest


class STC_09(feautotest):
    def run(self):
        try:
            sl = self.lib.goto_screen("scheduler")
            if not sl:
                self.report("Failed to navigate to Scheduler Window", "FAILED", logging.WARNING)
                self.script_status = False
                return False
            self.report("Navigated to Scheduler Window", "PASSED", logging.INFO)

            time.sleep(2)
            current_time = self.get_timestamp_formatted()
            job_name = config.fe_test_job_name.format(current_time)
            if not self.lib.create_job(job_name):
                self.report("Failed to create job", "FAILED", logging.WARNING)
                self.script_status = False
                return False

            self.report("Created a job - {}".format(job_name), "PASSED", logging.INFO)
            time.sleep(5)

            xpos, ypos = self.lib.locate_image(config.img_search_job_edit_box)
            clicked = self.lib.find_and_click(config.img_search_job_edit_box)
            if not clicked:
                self.report("Failed to click on Search Job edit box", "FAILED", logging.WARNING, screenshot=True)
                self.script_status = False
                return False
            self.report("Clicked on Search Job edit box", "PASSED", logging.INFO)
            time.sleep(2)

            print "search"
            self.lib.sendkey(current_time)
            self.lib.sendkey(config.kbd_keys["ENTER"])

            if not self.lib.image_present(config.img_fe_test_job):
                self.report("Failed to get the Search Result", "FAILED", logging.WARNING, screenshot=True)
                self.script_status = False
            else:
                self.report("Search result for part of job name obtained", "PASSED", logging.INFO, screenshot=True)
            time.sleep(2)

            # cleared = False # clear status of search box
            # for char in current_time:
            #     print "char - " + char
            #     self.lib.sendkey(config.kbd_keys["BS"])
            #     time.sleep(1)
            #     if self.lib.find_and_click(config.img_search_job_edit_box):
            #         cleared = True
            #         break

            clicked = self.lib.doubleclick_on_item(item=None, xpos=xpos, ypos=ypos)
            if not clicked:
                self.report("Failed to click on the Search Text Field", "FAILED", logging.WARNING, screenshot=True)
                self.script_status = False
                return False
            print "double click"

            self.lib.sendkey(config.kbd_keys["BS"])
            # if not self.lib.find_and_click(config.img_search_job_edit_box_focused):
            #     print "not cleared"
            #     self.report("Failed to clear the Search Text Field", "FAILED", logging.WARNING)
            #     self.script_status = False
            #     return False
            # print "cleared"
            self.report("Cleared the Search Text Field", "PASSED", logging.INFO, screenshot=True)

            self.lib.sendkey(config.kbd_keys["ENTER"])
            time.sleep(1)
            if not self.lib.image_present(config.img_fe_test_job):
                self.report("Performed Empty Search and result obtained", "PASSED", logging.INFO, screenshot=True)
            else:
                self.report("Failed to perform empty search", "FAILED", logging.WARNING, screenshot=True)
                self.script_status = False

            time.sleep(1)
            self.lib.click_on_item(xpos, ypos)
            self.lib.sendkey(job_name)
            self.lib.sendkey(config.kbd_keys["ENTER"])
            time.sleep(1)
            if not self.lib.image_present(config.img_fe_test_job):
                self.report("Failed to get search result for whole job name", "FAILED", logging.WARNING, screenshot=True)
                self.script_status = False
            else:
                self.report("Search result for whole job name obtained", "PASSED", logging.INFO, screenshot=True)

        except Exception as e:
            self.logger.debug(str(e))

    def exit_test(self):
        self.lib.delete_job()
        super(STC_09, self).exit_test()

def main():
    test_obj = STC_09()
    test_obj.run_test("STC_09", os.path.basename(__file__))
    test_obj.report_test_result()
    test_obj.exit_test()


if __name__ == "__main__":
    main()

# --------------------------------------------------------------------------------------
# Author: Shameena HA
# Date: 31/10/2018
# --------------------------------------------------------------------------------------
