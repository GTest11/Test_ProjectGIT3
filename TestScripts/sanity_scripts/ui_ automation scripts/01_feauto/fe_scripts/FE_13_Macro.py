# --------------------------------------------------------------------------------------
# TC Id      : FE_13
# Module     : Macro UI
# TC Summary :  To check the UI of Macro
# TC Steps   :  1) Launch the application.
#              2) Select View Macros from Menu bar items of Multi Grid form
#              3) Verify the UI behavior
# Expected   : 3. Macros will be available
# Pre-con    : At least one macro should be created for a DUT
# --------------------------------------------------------------------------------------

# imports
import time
import os
import logging
from fe_auto_config.fe_variables import fe_var as config
from fe_auto_config.feauto import feautotest


class FE_13(feautotest):
    def run(self):
        try:
            clicked = self.lib.find_and_click(config.macro_btn)
            if not clicked:
                self.report("Click on View Macro", "FAILED", logging.WARNING)
                self.script_status = False
                return False
            self.report("Click on View Macro", "PASSED", logging.INFO)

            if not self.lib.window_present("Macro List"):
                self.report("Macro List did not appear", "FAILED", logging.WARNING, True)
                self.script_status = False
                return False
            self.report("Macro List appeared", "PASSED", logging.INFO, True)

            item_present = self.lib.image_present("btn_macro_refresh.png")
            if item_present:
                self.report("Macro List - Refresh button found", "PASSED", logging.INFO, True)

            else:
                self.report("Macro List - Refresh button not found", "FAILED", logging.WARNING, True)
                self.script_status = False
                return False

        except Exception as e:
            self.logger.debug(str(e))


def main():
    test_obj = FE_13()
    test_obj.run_test("FE_13", os.path.basename(__file__))
    test_obj.report_test_result()
    test_obj.exit_test()

if __name__ == "__main__":
    main()