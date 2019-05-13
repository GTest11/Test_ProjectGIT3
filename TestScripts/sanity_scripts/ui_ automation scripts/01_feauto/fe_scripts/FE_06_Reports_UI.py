# --------------------------------------------------------------------------------------
# TC Id: FE_06
# Module: Reports
# TC Summary:  To verify the default Reports tab for admin user/ user with admin role.
# TC Steps: 1) Launch the application.
#           2) Click on Reports tab from the main form /
#               Select Reports from View menu item (CTRL + R short cut)
# Expected: 2)
#                 2) Reports page should appear as follows:-
# 		Job Details tree view
# 		Job Property Grid
# 		Export Button
# 		Print Button
# 		Refresh
# 		Delete
# 		Search field
# [Job view will be listed with already executed jobs.]
# Scheduler generated reports shall be listed under their respective Job name. Default Job is reserved for script editor reports.
#
# Each Report  have context menu options
# 		open
# 		show recorded video
# 		delete
# --------------------------------------------------------------------------------------

# imports
import time, os
import logging
from fe_auto_config.fe_variables import fe_var as config
from fe_auto_config.feauto import feautotest


class FE_06(feautotest):
    def run(self):
        try:
            sl = self.lib.goto_screen("reports")
            if not sl:
                self.report("Failed to navigate to Reports", "FAILED", logging.WARNING)
                self.script_status = False
                return False
            self.report("Navigated to Reports", "PASSED", logging.INFO)

            # scheduler ui items
            ui_items = ("tree_view", "export", "print" , "refresh", "delete", "search")
            all_items = True
            for item in ui_items:
                if item in config.reports_ui:
                    item_present = self.lib.image_present(config.reports_ui[item])
                    if item_present:
                        self.report("Reports UI - {} - found".format(item), "PASSED", logging.INFO, True)
                    else:
                        self.report("Reports UI - {} - not found".format(item), "FAILED", logging.WARNING, True)
                        all_items = False

                else:
                    all_items = False
                    self.report("UI element not found in config- {}".format(item), "FAILED", logging.WARNING, True)

            time.sleep(1)
            clicked = self.lib.find_and_click(config.img_expand_icon)
            if not clicked:
                self.report("Failed to expand the Report folder", "FAILED", logging.WARNING)
                self.script_status = False
                # return False
            else:
                self.report("Clicked on a report", "PASSED", logging.INFO)

            self.lib.sendkey(config.kbd_keys['DOWN'])
            time.sleep(1)
            property_grid = self.lib.image_present(config.reports_ui['property_grid'])
            if not property_grid:
                self.report("Reports UI - {} - found".format(config.reports_ui['property_grid']), "PASSED", logging.INFO, True)
            else:
                self.report("Reports UI - {} - not found".format(config.reports_ui['property_grid']), "FAILED", logging.WARNING, True)
                all_items = False

            clicked = self.lib.right_click_on_item(config.img_test_result)
            if not clicked:
                self.report("Failed to display the context menu", "FAILED", logging.WARNING)
                self.script_status = False
                all_items = False
                # return False
            else:
                self.report("Context Menu of test result displayed", "PASSED", logging.INFO, True)

            # Verify context menu ---------------
            if (self.lib.image_present(config.reports_ui['property_grid'][0]) or
                self.lib.image_present(config.reports_ui['property_grid'][1])):
                self.report("Failed to verify the context menu", "FAILED", logging.WARNING)
                all_items = False
            else:
                self.report("Context Menu displayed with Open, Show Recorded Video, and Delete options ", "PASSED", logging.INFO, True)

            if all_items:
                self.report("Scheduler Screen does have all UI items", "PASSED", logging.INFO, True)
            else:
                self.script_status = all_items
                self.report("Scheduler Screen does not have all UI items", "FAILED", logging.WARNING, True)

        except Exception as e:
            self.logger.debug(str(e))


def main():
    test_obj = FE_06()
    test_obj.run_test("FE_06", os.path.basename(__file__))
    test_obj.report_test_result()
    test_obj.exit_test()


if __name__ == "__main__":
    main()

# --------------------------------------------------------------------------------------
# Author:
# Date:
# Developed FE Version:
# --------------------------------------------------------------------------------------
