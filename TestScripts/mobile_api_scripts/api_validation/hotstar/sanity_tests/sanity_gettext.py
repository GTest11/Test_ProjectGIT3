# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :   17-April-2019
# Script Version    :   1.0
# APIs covered      :   "GetText", "GetTextIndex"
# Test Scenario     :
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import os
import sys
import time
sys.path.append('../')

from library.api_test_base import ApiTestBase


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class api_test(ApiTestBase):

    # the class which handles the script intention.
    # this overrides base class run_api_test()

    apis = ( "GetText", "GetTextIndex",
         )
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        '''
        Executes the test script

        :return:
        '''

        api_test_status = True

        try:
            get_txt = self.lib.get_text(self.config.elm_attr, index=None)
            if get_txt == self.config.txt_gettext:
                status = "PASSED"
            else:
                status = "FAILED"
                api_test_status = False
            self.lib.report("API: GetText", status)

            get_txt_idx = self.lib.get_text(self.config.gettext_idx, index=self.config.gettext_index)
            if get_txt_idx == self.config.txt_menu[self.config.gettext_index]:
                status = "PASSED"
            else:
                status = "FAILED"
                api_test_status = False
            self.lib.report("API: GetText(Index)", status)

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
