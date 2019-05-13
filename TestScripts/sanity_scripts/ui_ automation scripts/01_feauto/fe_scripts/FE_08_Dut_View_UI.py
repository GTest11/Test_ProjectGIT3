# --------------------------------------------------------------------------------------
# TC Id: FE_08
# Module: Dut View
# TC Summary:  To verify UI Behaviour of DUT View Tab
# TC Steps: 1) Launch the application.
#           2) Input valid user name and valid password.
#           3) The default tab will be DUT View
#               or
#               select DUT View from View Menu item(Ctrl+D is the shortcut)
# Expected: 2)
#       DUT view is selected by default. It has
#             Rack Tree view with all the racks
#             Property window
#             Remote Control area
#             Buttons for power operations
#             Display Log window option
#             Show video button
#             Start Recording button
#             View Macros
#             Add/Remove Device Buttons
#             Refresh Button
#             Property grid
#             Edit custom attribute
# --------------------------------------------------------------------------------------

# imports
import time, os
import logging
from fe_auto_config.fe_variables import fe_var as config
from fe_auto_config.feauto import feautotest


class FE_08(feautotest):
    def run(self):
        try:
            # home = self.lib.goto_screen("home")
            # if not home:
            #     self.report("Navigate to Dut View", "FAILED", logging.WARNING)
            #     self.script_status = False
            #     return False
            # self.report("Navigate to Dut View", "PASSED", logging.INFO)
            time.sleep(20)
            # Dut View ui items
            ui_items = ("properties_window", "power_buttons" ,
                        "show_video" , "display_log", "record" ,
                        "view_macros", "add_removedevice",
                        "properties_grid" , "edit_custom_attr"
                        )

            all_items = True
            for item in ui_items:
                print "item - " + item
                # if not (item in config.dut_view_ui.items()):
                #     all_items = False
                #     self.report("UI element not found in the config - {}".format(item), "FAILED", logging.WARNING, True)
                # else:
                print "qq"
                elements = config.dut_view_ui[item]
                for elm in elements:
                    item_present = self.lib.image_present(elm)
                    print item_present
                    print elm
                    if (not item_present) and item == "view_macros":
                        clicked  = self.lib.find_and_click("btn_invoke_view_macros.png")
                        if not clicked:
                            self.report("Click on the down button to see 'View Macros'", "FAILED", logging.WARNING, True)
                        item_present = self.lib.image_present(elm)

                    if item_present:
                        self.report("Dut View UI - {} - found".format(item), "PASSED", logging.INFO, True)
                    else:
                        self.report("Dut View UI - {} - not found".format(item), "FAILED", logging.WARNING, True)
                        all_items = False
                    time.sleep(10)
                time.sleep(1)

            if all_items:
                self.report("Dut View Screen does have all UI items", "PASSED", logging.INFO, True)
            else:
                self.script_status = all_items
                self.report("Dut View Screen does not have all UI items", "FAILED", logging.WARNING, True)

        except Exception as e:
            self.logger.debug(str(e))


def main():
    test_obj = FE_08()
    test_obj.run_test("FE_08", os.path.basename(__file__))
    test_obj.report_test_result()
    test_obj.exit_test()

if __name__ == "__main__":
    main()

# --------------------------------------------------------------------------------------
# Author:
# Date:
# Developed FE Version:
# --------------------------------------------------------------------------------------
