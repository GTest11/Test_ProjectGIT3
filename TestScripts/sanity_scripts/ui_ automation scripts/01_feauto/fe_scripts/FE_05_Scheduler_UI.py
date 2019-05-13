# --------------------------------------------------------------------------------------
# TC Id: FE_05
# Module: Scheduler
# TC Summary:  To verify  UI behaviour of Scheduler Tab
# TC Steps: 1) Launch the application.
#           2) Click on Scheduler tab from the main form
#             or Select Scheduler from View menu item (CTRL + H shortcut)
# Expected: 2)
#                 i. All main tabs should be visible.
#                 ii. Following buttons shall displayed on Actions area:
#                      Create Job
#                     Edit Job
#                     Remove Job
#                     Stop Execution
#                     Refresh
# All buttons will be enabled but Stop Execution will be enabled only when the job is scheduled.
# iii. Jobs should be listed in the main grid with details if already existing.
# iv. More details of the selected job shall displayed on the property region.
#     Test case and device count on property grid should match with the counts in job.
# v. There are search and filter options available where jobs can be searched by the job name
#    and also jobs can be filtered based on All,Completed,In Progress and Scheduled.
# --------------------------------------------------------------------------------------

# imports
import time, os
import logging
from fe_auto_config.fe_variables import fe_var as config
from fe_auto_config.feauto import feautotest


class FE_05(feautotest):
    def run(self):
        try:
            sl = self.lib.goto_screen("scheduler")
            if not sl:
                self.report("Failed to navigate to Scheduler", "FAILED", logging.WARNING)
                self.script_status = False
                return False
            self.report("Navigated to Scheduler", "PASSED", logging.INFO)

            # scheduler ui items
            ui_items = ("createjob", "editjob", "removejob_active","stopexe_inactive", "refresh")
            all_items = True
            for item in ui_items:
                if item in config.scheduler_screen:
                    item_present = self.lib.image_present(config.scheduler_screen[item])
                    if not item_present:
                        if item == "removejob_active":
                            item = "removejob_inactive"
                            self.report("Scheduler UI - Remove job active button".format(item), "FAILED", logging.WARNING, True)
                        elif item == "stopexe_inactive":
                            item = "stopexe_active"
                            self.report("Scheduler UI - Stop Execution inactive button".format(item), "FAILED", logging.WARNING, True)
                        item_present = self.lib.image_present(config.scheduler_screen[item])


                    if item_present:
                        self.report("Scheduler UI - {} - found".format(item), "PASSED", logging.INFO, True)
                    else:
                        self.report("Scheduler UI - {} - not found".format(item), "FAILED", logging.WARNING, True)
                        all_items = False

                else:
                    all_items = False
                    self.report("UI element not found in config - {}".format(item), "FAILED", logging.WARNING, True)

            if all_items:
                self.report("Scheduler Screen does have all UI items", "PASSED", logging.INFO, True)
            else:
                self.script_status = all_items
                self.report("Scheduler Screen does not have all UI items", "FAILED", logging.WARNING, True)

        except Exception as e:
            self.logger.debug(str(e))


def main():
    test_obj = FE_05()
    test_obj.run_test("FE_05", os.path.basename(__file__))
    test_obj.report_test_result()
    test_obj.exit_test()

if __name__ == "__main__":
    main()

# --------------------------------------------------------------------------------------
# Author:
# Date:
# Developed FE Version:
# --------------------------------------------------------------------------------------
