# --------------------------------------------------------------------------------------
# TC Id: FE_04
# Module: Menu Bar
# TC Summary:  To verify the menu bar options
# TC Steps:      1) Launch the application.
#                 2) Login to the application.
#                 3) Verify the items in menu bar.
# Expected: 3) Menu  bar should have the following sub items
#             File => Log off, Exit
#             Edit => SPS, ALM,DUT Type Editor
#             View => DUT View, Scripting, Scheduler, Reports, Configure, User & roles [along with their shortcuts]
#             Settings => change password
#             Help => User manual, API help, About FalconEye
#             If user is in Script Editor, some sub menus should be shown(Script editor, Editor, Actions and Window.)"
# --------------------------------------------------------------------------------------

# imports
import time, os
import logging
from fe_auto_config.fe_variables import fe_var as config
from fe_auto_config.feauto import feautotest


class FE_04(feautotest):
    def run(self):
        try:
           # #  screen names to be verified - feimages - image names
           # menubar = ['menu_bar', 'filemenu_logoff',
           #                          'filemenu_exit', 'editmenu_items',
           #                          'viewmenu_items', 'settingsmenu_items',
           #                          'helpmenu_items'
           #                          ]

           all_items = True
           for submenu in config.menubar:
                if config.menubar[submenu][1]:
                    for key in config.menubar[submenu][1]:
                        self.lib.sendkey(key)
                        time.sleep(1)
                time.sleep(3)
                item_present = self.lib.image_present(config.menubar[submenu][0])
                time.sleep(1)
                # self.lib.sendkey("{ALT}") # to clear the current selection

                if item_present:
                    self.report("Menu Item - {}".format(submenu), "PASSED", logging.INFO, True)
                else:
                    self.report("Menu Item - {}".format(submenu), "FAILED", logging.WARNING, True)
                    all_items = False

           if all_items:
               self.report("Menu bar and all submenus available", "PASSED", logging.INFO, True)
           else:
               self.script_status = all_items
               self.report("Menu bar and all submenus available", "FAILED", logging.WARNING, True)

        except Exception as e:
            self.logger.debug(str(e))


def main():
    test_obj = FE_04()
    test_obj.run_test("FE_04", os.path.basename(__file__))
    test_obj.report_test_result()
    test_obj.exit_test()


if __name__ == "__main__":
    main()


# --------------------------------------------------------------------------------------
# Author:
# Date:
# Developed FE Version:
# --------------------------------------------------------------------------------------
