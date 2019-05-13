# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :   Rohith P V
# Date              :   05-10-2018
# Script Version    :   1.1
# APIs covered      :   "HideKeyboard", "ClearText", "SendKeys", "Click"
# Test Scenario     :   init to Youtube
#                       Search for master chef australia
#                       Hide the keyboard
#                       Clear the text in search field.
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
        "HideKeyboard",
        "ClearText",
        "SendKeys",
        "Click",
    )
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        '''
        Executes the test script

        :return: test status as True or False
        '''


        api_test_status = False
        status = "FAILED"

        try:
            if not self.lib.search_in_youtube():
                self.lib.report("Search in youtube", "FAILED", ss_required=True)
                return False

            cleared = self.lib.cleartext(self.config.search_txt_box)
            time.sleep(3)

            hidden = self.lib.hide_keyboard()
            if cleared and hidden:
                api_test_status = True
                status = "PASSED"
            else:
                status = "FAILED"
            self.lib.report("Click, SendKeys, ClearText, HideKeyboard", status, ss_required=True)

        except Exception as e:
            self.logger.Error("Error in run_api_test() " + str(e))
            api_test_status = False

        finally:
            self.test_result = api_test_status


def main():
    testobj = api_test()
    testobj.run_test(testobj.script_name, testobj.apis)


if __name__ == '__main__':
    main()
