# --------------------------------------------------------------------------------------
# TC Id: FE_02
# Module: Script Editor
# TC Summary:  To verify Checkpoint Explorer button functionality
# TC Steps: 1) Launch the application.
#           2) Navigate to Script Editor.
#           3) Click on Checkpoint Explorer button
# Expected: 3) Checkpoint Explorer shall be loaded with all the existing checkpoints.
#              Here user shall able to select, create, modify and delete checkpoints
# --------------------------------------------------------------------------------------

# imports
import time
import logging
import os
from fe_auto_config.fe_variables import fe_var as config
from fe_auto_config.feauto import feautotest


class FE_02(feautotest):
    def run(self):
        try:
            sl = self.lib.goto_screen("script_editor")
            if not sl:
                self.report("Navigate to Script Editor", "FAILED", logging.WARNING)
                self.script_status = False
                return False
            self.report("Navigate to Script Editor", "PASSED", logging.INFO)

            clicked = self.lib.find_and_click(config.chkpt_explr_icon)
            if not clicked:
                self.report("Failed to click on Checkpoint Explorer Button", "FAILED", logging.WARNING)
                self.script_status = False
                return False
            self.report("Clicked on Checkpoint Explorer Button", "PASSED", logging.INFO)
            time.sleep(10)
            if not self.lib.window_present(config.check_point_explorer_title):
                self.report("Failed to open Checkpoint Explorer Window", "FAILED", logging.WARNING, True)
                self.script_status = False
                return False
            self.report("Checkpoint Explorer Window opened", "PASSED", logging.INFO, True)
            current_time = self.get_timestamp_formatted()

            ocr_checkpoint_name = config.ocr_checkpoint_name.format(current_time)
            ic_checkpoint_name = config.ic_checkpoint_name.format(current_time)

            if not self.lib.create_ocr_checkpoint(ocr_checkpoint_name):
                self.report("Failed to create OCR checkpoint", "FAILED", logging.INFO, True)
                self.script_status = False
                return False
            self.report("OCR Checkpoint created", "PASSED", logging.INFO, True)

            if not self.lib.delete_checkpoint(ocr_checkpoint_name, chkpt_type="OCR"):
                self.report("OCR checkpoint delete", "FAILED", logging.INFO, True)
                self.script_status = False
                return False
            self.report("OCR checkpoint delete", "PASSED", logging.INFO, True)

            self.lib.clear_search_list()
            if not self.lib.create_ic_checkpoint(ic_checkpoint_name):
                self.report("IC Checkpoint create", "FAILED", logging.INFO, True)
                self.script_status = False
                return False
            self.report("IC Checkpoint create", "PASSED", logging.INFO, True)

            if not self.lib.clear_search_box("chkpt_explorer"):
                self.report("Failed to clear search box", "FAILED", logging.INFO, True)
                self.script_status = False
                return False

            if not self.lib.delete_checkpoint(ic_checkpoint_name, chkpt_type="IC"):
                self.report("IC checkpoint delete", "FAILED", logging.INFO, True)
                self.script_status = False
                return False
            self.report("IC checkpoint delete", "PASSED", logging.INFO, True)

        except Exception as e:
            self.logger.debug(str(e))


def main():
    test_obj = FE_02()
    test_obj.run_test("FE_02", os.path.basename(__file__))
    test_obj.report_test_result()
    test_obj.exit_test()


if __name__ == "__main__":
    main()

# --------------------------------------------------------------------------------------
# Author:
# Date:
# Developed FE Version:
# --------------------------------------------------------------------------------------
