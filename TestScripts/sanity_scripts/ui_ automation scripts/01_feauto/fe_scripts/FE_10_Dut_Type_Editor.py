# --------------------------------------------------------------------------------------
# TC Id: FE_09
# Module: Script Editor
# TC Summary:  To check the UI of DUT type editor
# TC Steps: 1) Launch the application.
#           2) From Edit, go to DUT Type Editor window
#           3) Verify the DUT hierarchy
#   Expected: 3. DUT Type Editor will have all the DUT types.  It will have
#      Add
#      Delete
#      Save
#      Refresh
# User can arrange the DUT types to make them linked.
# --------------------------------------------------------------------------------------

# imports
import time, os
import logging
from fe_auto_config.fe_variables import fe_var as config
from fe_auto_config.feauto import feautotest


# Note: to verify the log from tabs need to add ocr support


class FE_10(feautotest):
    def run(self):
        try:
            # home = self.lib.goto_screen("home")
            # if not home:
            #     self.report("Navigate to Dut View", "FAILED", logging.WARNING)
            #     self.script_status = False
            #     return False
            # self.report("Navigate to Dut View", "PASSED", logging.INFO)

            time.sleep(20)  #initial wait
            sent = self.lib.sendkeys(config.dut_type_editor_keys)
            if not sent:
                self.report("Failed to send keys to launch DUT Type Editor", "FAILED", logging.WARNING)
                self.script_status = False
                return False

            time.sleep(20)
            if not self.lib.image_present("title_dut_type_editor.png"):
                self.report("Failed to launch DUT Type Editor", "FAILED", logging.WARNING)
                self.script_status = False
                return False

            # ui items to verify
            ui_items = ("add", "delete", "save", "refresh")
            all_present = True
            for item in ui_items:
                print "item 1"
                if item in config.dut_type_editor_ui:
                    print "item 2"
                    item_present = self.lib.image_present(config.dut_type_editor_ui[item])
                    if item_present:
                        self.report("Dut Type Editor UI - {} button - found".format(item), "PASSED", logging.INFO, True)
                    else:
                        self.report("Dut Type Editor UI - {} button - not found".format(item), "FAILED", logging.WARNING, True)
                        all_present = False
                    print "item 3"
                    time.sleep(10)

            if not all_present:
                self.report("Dut Type Editor UI - All buttons are not available", "FAILED", logging.WARNING)
                self.script_status = False
            else:
                self.report("Dut Type Editor UI - All buttons are available", "PASSED", logging.INFO)

        except Exception as e:
            self.logger.debug(str(e))


def main():
    test_obj = FE_10()
    test_obj.run_test("FE_10", os.path.basename(__file__))
    test_obj.report_test_result()
    test_obj.exit_test()


if __name__ == "__main__":
    main()

# --------------------------------------------------------------------------------------
# Author:
# Date:
# Developed FE Version:
# --------------------------------------------------------------------------------------
