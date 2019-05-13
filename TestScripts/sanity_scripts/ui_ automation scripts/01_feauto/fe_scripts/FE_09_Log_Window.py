# --------------------------------------------------------------------------------------
# TC Id: FE_09
# Module: Script Editor
# TC Summary:  To verify Checkpoint Explorer button functionality
# TC Steps: 1) Launch the application.
#           2) Input valid user name and valid password.
#           3) Select the Display Log window in the DUT View.
#   Expected: 3) Log shall be updated with the details of all the tabs.
# --------------------------------------------------------------------------------------

# imports
import time, os
import logging
from fe_auto_config.fe_variables import fe_var as config
from fe_auto_config.feauto import feautotest


# Note: to verify the log from tabs need to add ocr support


class FE_09(feautotest):
    def run(self):
        try:

            # time.sleep(20)
            # clicked = self.lib.test()
            # time.sleep(20)
            # return clicked

            # home = self.lib.goto_screen("home")
            # if not home:
            #     self.report("Navigate to Dut View", "FAILED", logging.WARNING)
            #     self.script_status = False
            #     return False
            # self.report("Navigate to Dut View", "PASSED", logging.INFO)

            time.sleep(20)

            clicked = self.lib.find_and_click("btn_display_log.png")
            time.sleep(20)
            # clicked = self.lib.find_and_click("btn_chpt_explr.png")
            if not clicked:
                self.report("Click on Display User Log Button", "FAILED", logging.WARNING)
                self.script_status = False
                return False
            self.report("Click on Display User Log Button", "PASSED", logging.INFO)

            if not self.lib.window_present("Log Window"):
                self.report("User Log Window did not appear", "FAILED", logging.WARNING, True)
                self.script_status = False
                return False
            self.report("User Log Window appeared", "PASSED", logging.INFO, True)

        except Exception as e:
            self.logger.debug(str(e))


def main():
    test_obj = FE_09()
    test_obj.run_test("FE_09", os.path.basename(__file__))
    test_obj.report_test_result()
    test_obj.exit_test()


if __name__ == "__main__":
    main()

# --------------------------------------------------------------------------------------
# Author:
# Date:
# Developed FE Version:
# --------------------------------------------------------------------------------------
