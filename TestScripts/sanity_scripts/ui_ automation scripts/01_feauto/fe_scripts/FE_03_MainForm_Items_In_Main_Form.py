# --------------------------------------------------------------------------------------
# TC Id: FE_03
# Module: Main Form
# TC Summary:  To verify items in main form
# TC Steps: 1) Launch the application.
#           2) Input login details to login to the application.
#           3) Verify the items in the main form.
# Expected: 3) Main form should have the following tabs
#                  DUT View
#                  Script Editor
#                  Scheduler
#                  Reports
#                  Configure
#                  User & Roles
# --------------------------------------------------------------------------------------

# imports
import time, os
import logging
from fe_auto_config.fe_variables import fe_var as config
from fe_auto_config.feauto import feautotest

class FE_03(feautotest):
    try:

        def run(self):
            found = self.lib.image_present("dut_view_multi_tabs.png")
            if not found:
                self.report("FE Home - Multiple tabs", "FAILED", logging.WARNING)
                return False
            self.report("FE Home - Multiple tabs", "PASSED", logging.INFO)

            # navigating to scripting library
            fe_screens = ("script_editor", "scheduler","reports", "configure", "users_and_roles", "home")
            all_screen = True
            for s in fe_screens:
                screen_found = self.lib.goto_screen(s)
                if screen_found:
                    self.report("Window - {}".format(s), "PASSED", logging.INFO)
                else:
                    self.report("Window - {}".format(s), "FAILED", logging.WARNING)
                    all_screen = False

            # if all FE Window are available
            if all_screen:
                self.report("FE_03: Items in main form", "PASSED", logging.INFO)
            else:
                self.report("FE_03: Items in main form", "FAILED", logging.WARNING)
            self.script_status = all_screen

    except Exception as e:
        logging.debug(str(e))


def main():
    test_obj = FE_03()
    test_obj.run_test("FE_03", os.path.basename(__file__))
    test_obj.report_test_result()
    test_obj.exit_test()


if __name__ == "__main__":
    main()


# --------------------------------------------------------------------------------------
# Author:
# Date:
# Developed FE Version:
# --------------------------------------------------------------------------------------
