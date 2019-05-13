# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :   Shameena HA
# Date              :   31-01-2019
# Script Version    :   1.0
# APIs covered      :   "ClearText",
# Test Scenario     :   1. with text entered to the text field
#                       2. with empty text field
#                       3. with search results
#                       4. with a non-text field
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import os
import sys
import time
sys.path.append('../')

from library.api_test_base import apiTestBase


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class api_test(apiTestBase):

    # the class which handles the script intention.
    # this overrides base class run_api_test()

    apis = (
        "ClearText",

    )
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        '''
        Executes the test script

        :return: test status as True or False
        '''

        test_status = True
        params = self.config.clear_text_params
        elm = self.config.search_icon

        try:
            for param in params:
                self.logger.Log("---------- Scenario {} ---------".format(params[param][0]))

                if param == 1:
                    elm = self.config.search_txt_box
                    clicked = self.lib.element_ops(self.config.search_icon, index=None, action='click')
                    if not clicked:
                        self.lib.report("Failed to click on search icon", "FAILED", ss_required=True)
                        test_status = False
                        return False

                if param == 2:  # assuming text field is open, sending keys
                    elm = self.config.search_txt_box
                    sent = self.lib.send_keys(self.config.search_txt_box, keys=self.config.search_text)
                    if not sent:
                        self.lib.report("Failed to send keys to search box", "FAILED", ss_required=True)
                        test_status = False
                        return False

                # the edit box name gets changed after calling clear text/entering text.
                # To handle this keeping different sections for param 2 and 3

                if param == 3:  # assuming text field is open, sending keys
                    elm = self.config.search_box_with_text
                    sent = self.lib.send_keys(self.config.search_txt_box, keys=self.config.search_text)
                    if not sent:
                        self.lib.report("Failed to send keys to search box", "FAILED", ss_required=True)
                        test_status = False
                        return False

                    self.dut.SendAndroidKeyCode(self.config.ENTER)
                    time.sleep(3) # wait for the results to load

                if param == 4:
                    elm = self.config.invalid_click

                cleared = self.lib.cleartext(elm)
                if cleared == params[param][1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_status = False
                self.lib.report("ClearText: {}".format(params[param][0]), status, ss_required=True)

        except Exception as e:
            self.logger.Error("Error in run_api_test() " + str(e))
            test_status = False

        finally:
            self.test_result = test_status


def main():
    testobj = api_test()
    testobj.run_test(testobj.script_name, testobj.apis)


if __name__ == '__main__':
    main()
