# --------------------------------------------------------------------------------------
# TC Id: FE_15
# Module: Checkpoint Explorer
# TC Summary:  To verify UI Behaviour of  Checkpoint Explorer
# TC Steps: 1) Launch the application.
#           2) Click on Script Editor tab from the main form
#               Select Scripting from View menu item (CTRL + Q short cut).
#           3)Click on Checkpoint Explorer button.
# Expected: 3)  i) Checkpoint Explorer will have
#                     Checkpoint list
#                     Checkpoint Search box
#                     Screenshot area
#                     Box Type Selector
#                     Slot selector
#                     Co ordinates area
#                     Checkpoint details area
#                 ii) Tool buttons
#                      New
#                      Delete
#                      Save
#                      Refresh
#                      Quick Capture
#                      Open Frame
# --------------------------------------------------------------------------------------

# imports
import time, os
import logging
from fe_auto_config.fe_variables import fe_var as config
from fe_auto_config.feauto import feautotest


class FE_15(feautotest):
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
                self.report("Click on Checkpoint Explorer Button", "FAILED", logging.WARNING)
                self.script_status = False
                return False
            self.report("Click on Checkpoint Explorer Button", "PASSED", logging.INFO)

            time.sleep(1)
            if not self.lib.window_present(config.check_point_explorer_title):
                self.report("Failed to open Checkpoint Explorer Window", "FAILED", logging.WARNING, True)
                self.script_status = False
                return False
            self.report("Checkpoint Explorer Window opened", "PASSED", logging.INFO, True)

            #     maximize window
            self.lib.window_maximize(config.check_point_explorer_title)

            # verifying tool buttons
            tool_buttons = ("new", "delete_inactive", "save_inactive" , "refresh" , "quick_capture", "open_frame_inactive")

            all_tools_present = True
            for tool_button in tool_buttons:
                if not self.lib.image_present(config.check_point_explorer_ui[tool_button]):
                    all_tools_present = False
                    self.report("Checkpoint Explorer UI - {} - no found".format(tool_button), "FAILED", logging.WARNING, True)
                else:
                    self.report("Checkpoint Explorer UI - {} - found".format(tool_button), "PASSED", logging.INFO, True)

            # create a checkpoint
            clicked = self.lib.find_and_click(config.check_point_explorer_ui['new'])
            if not clicked:
                self.report("Failed to click on New Checkpoint Button", "FAILED", logging.WARNING)
                self.script_status = False
                return False
            self.report("Clicked on New Checkpoint Button", "PASSED", logging.INFO)

            self.lib.sendkey(config.kbd_keys['DOWN'])
            self.lib.sendkey(config.kbd_keys['ENTER'])
            time.sleep(2)
            # if self.lib.window_present(config.new_chkpt_win_title):
            #     self.report("Failed to find New Checkpoint Window", "FAILED", logging.WARNING)
            #     self.script_status = False
            #     return False
            # self.report("New Checkpoint Window appeared", "PASSED", logging.INFO)

            current_time = self.get_timestamp_formatted()
            chkpt_name = config.fe_test_job_name.format(current_time)

            self.lib.sendkey(chkpt_name)
            self.lib.sendkey(config.kbd_keys['ENTER'])

            # if not self.lib.window_getfocus(config.new_chkpt_win_title):
            #     self.report("Failed to focus on New Checkpoint - {}".format(chkpt_name), "FAILED", logging.WARNING)
            #     self.script_status = False
            #     return False


            time.sleep(3)
            all_present = True
            chkpt_details_ui = ("box_type_selector" , "search_chkpt", "chkpt_coordinate_area", "chkpt_test_ocr", "chkpt_list")
            for item in chkpt_details_ui:
                if item == "chkpt_list":
                    for chkpt in config.check_point_explorer_ui[item]:
                        is_present = self.lib.image_present(chkpt)
                        if not is_present:
                            all_present = False
                    present = all_present

                else:
                    present = self.lib.image_present(config.check_point_explorer_ui[item])
                if not present:
                    all_present = False
                    self.report("Checkpoint Explorer UI - {} - no found".format(item), "FAILED", logging.WARNING,
                                True)
                else:
                    self.report("Checkpoint Explorer UI - {} - found".format(item), "PASSED", logging.INFO, True)

            if all_tools_present and all_present:
                self.report("Checkpoint Explorer UI - all items are present",
                            "PASSED", logging.INFO, True
                            )
            else:
                self.report("Checkpoint Explorer UI - all items are not present",
                            "FAILED", logging.WARNING, True
                            )
            self.script_status = all_present

        except Exception as e:
            self.logger.debug(str(e))


def main():
    test_obj = FE_15()
    test_obj.run_test("FE_15", os.path.basename(__file__))
    test_obj.report_test_result()
    test_obj.exit_test()


if __name__ == "__main__":
    main()

# --------------------------------------------------------------------------------------
# Author:
# Date:
# Developed FE Version:
# --------------------------------------------------------------------------------------
