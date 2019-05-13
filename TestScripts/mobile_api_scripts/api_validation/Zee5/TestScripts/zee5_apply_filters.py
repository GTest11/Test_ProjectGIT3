# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :   04-04-2019
# Script Version    :   1.0
# APIs covered      :
# Test Scenario     :   "Swipe on the application till the page ends"
# '''''''''''''''''''''''''''TEST CASE DETAILS' - END '''''''''''''''''''''''''''''''''

import os
import sys
import time
sys.path.append('../')

from library.api_test_base import ApiTestBase

class api_test(ApiTestBase):
    # the class which handles the script intention.
    # this overrides base class run_api_test()

    # class variables
    apis = ('IsElement', 'TapElement', 'Click', 'GetText','IsSelected', 'IsEnabled')
    script_name = os.path.basename(__file__)

    def run_api_test(self):
        """
        Script part of the framework.
        :return: True or False
        """

        test_result = True

        try:
            if not self.lib.element_ops(self.config.shows_view_all, action="tap"):
                self.logger.Error("Failed to tap on 'View All'")
                test_result = False
                return False
            self.logger.Log("Tapped on 'View All' of TV Shows Page")

            if not self.lib.is_present(self.config.screen_title):
                self.logger.Error("Failed find screen title")
                test_result = False
                return False
            self.logger.Log("Screen Title is available")

            title = self.lib.get_text(self.config.screen_title)
            if not title == self.config.tv_shows_view_all_page_title:
                self.logger.Error("Failed read the screen title")
                test_result = False
                return False
            self.logger.Log("Screen Title is shown as {}".format(title))

            if not self.lib.element_ops(self.config.filter_icon, action="click"):
                self.logger.Error("Failed to click on 'Filer Icon' button")
                test_result = False
                return False
            self.logger.Log("Tapped on 'Filter Icon' of TV Shows Page")

            selected = False
            if self.lib.is_enabled(self.config.checkbx_filter) and  \
                    self.lib.is_selected(self.config.checkbx_filter):
                self.logger.Error("Filter is applied already")
                selected = True

            if not self.lib.element_ops(self.config.checkbx_filter, action="tap"):
                self.logger.Error("Failed to check the filter")
                test_result = False
                return False
            self.logger.Log("Checked the filter, again validating is_selected api")

            self.dut.GetAllAttributeValues(self.lib.mob_lib.Constants.ElementType.XPath, '//android.widget.CheckBox[@text="Animation"]',
                                      "name, visible, clickable, clicked, checkable, checked, selected, enabled, 12345, abcd")

            selected_1 = self.lib.is_selected(self.config.checkbx_filter)
            if selected and selected_1:
                self.logger.Log("Check IsSelected API output or whether tap happened")
            elif (not selected and selected_1) and (selected and not selected_1):
                self.logger.Log("Filter is selected based on the previous status")
            else:
                self.logger.Log("Tap not happened")
                test_result = False
                return False

            if not self.lib.element_ops(self.config.filter_apply_button, action="click"):
                self.logger.Error("Failed to click on 'Apply Filter' button")
                test_result = False
                return False
            self.logger.Log("Clicked on 'Apply Filter' button")


        except Exception as e:
            self.logger.Error("Error in run_api_test() " + str(e))
            test_result = False

        finally:
            self.test_result = test_result


def main():
    testobj = api_test()
    testobj.run_test(testobj.script_name, testobj.apis)


if __name__ == '__main__':
    main()
