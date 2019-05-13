# --------------------------------------------------------------------------------------
# TC Id      : FE_14
# Module     : Users and Roles UI
# TC Summary : To check the UI of Users and Roles
# TC Steps   : 1) Launch the application.
#              2) Go to Users & Roles tab
#              3) Verify the UI behavior
# Expected   : 3. Three tabs will be available, User Management, Role Management and User Group Management
# --------------------------------------------------------------------------------------

# imports
import logging
import os.path
from fe_auto_config.fe_variables import fe_var as config
from fe_auto_config.feauto import feautotest


class FE_14(feautotest):
    def run(self):
        try:
            sl = self.lib.goto_screen("users_and_roles")
            if not sl:
                self.report("Failed to navigate to Users & Roles", "FAILED", logging.WARNING)
                self.script_status = False
                return False
            self.report("Navigated to Users & Roles", "PASSED", logging.INFO)

            user_ui_items = ("Add", "Remove", "Refresh")
            item_screen_usr = config.user_management_screen
            all_items_usr = self.lib.verify_button_screen(user_ui_items, item_screen_usr)
            if all_items_usr:
                self.report("User Management Screen does have all UI items", "PASSED", logging.INFO, True)
            else:
                self.script_status = all_items_usr
                self.report("User Management Screen does not have all UI items", "FAILED", logging.WARNING, True)

            clicked = self.lib.find_and_click("btn_role_management.png")
            if not clicked:
                self.report("Click on Role Management", "FAILED", logging.WARNING)
                self.script_status = False
                return False
            else:
                self.report("Click on Role Management", "PASSED", logging.INFO)
                role_ui_items = ("Add", "Remove", "Save", "Refresh")
                item_screen_role = config.role_grp_management_screen
                all_items_role = self.lib.verify_button_screen(role_ui_items, item_screen_role)
            if all_items_role:
                self.report("Role Management Screen does have all UI items", "PASSED", logging.INFO, True)
            else:
                self.script_status = all_items_usr
                self.report("Role Management Screen does not have all UI items", "FAILED", logging.WARNING, True)

            clicked = self.lib.find_and_click("btn_usr_grp_management.png")
            item_screen_usr_grp = config.usr_grp_management_screen
            if not clicked:
                self.report("Click on User Group Management", "FAILED", logging.WARNING)
                self.script_status = False
                return False
            else:
                self.report("Click on User Group Management", "PASSED", logging.INFO)
                usr_grp_ui_items = ("Add", "Remove", "Save", "Refresh")
                all_items_role = self.lib.verify_button_screen(usr_grp_ui_items, item_screen_usr_grp)
            if all_items_role:
                self.report("User Group Management Screen does have all UI items", "PASSED", logging.INFO, True)
            else:
                self.script_status = all_items_usr
                self.report("User Group Management Screen does not have all UI items", "FAILED", logging.WARNING, True)
        except Exception as e:
            self.logger.debug(str(e))


def main():
    test_obj = FE_14()
    test_obj.run_test("FE_14", os.path.basename(__file__))
    test_obj.report_test_result()
    test_obj.exit_test()


if __name__ == "__main__":
    main()