# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :   18-April-2019
# Script Version    :   1.0
# APIs covered      :   "IsElementPresent",
#                       "TapElement",
#                       "IsEnabled",
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

    apis = (
            "IsElementPresent",
            "TapElement",
            "IsEnabled",
         )
    script_name = os.path.basename(__file__)


    def enabled_element_present(self, elm_list):
        presence = {}
        enabled = {}
        idx = 0
        for elm in elm_list:
            presence[idx] = self.lib.is_present(elm)
            enabled[idx] = self.lib.is_enabled(elm)
            idx += 1

        return presence, enabled


    def run_api_test(self):
        '''
        Executes the test script

        :return: True or False
        '''

        api_test_status = True

        api_status = True

        try:
            present, enabled = self.enabled_element_present(self.config.list_iselm)
            for key, value in present.items():
                if present[key] == False:
                    api_status = False
                    api_test_status = False
            if api_status:
                status = "PASSED"
            else:
                status = "FAILED"
            self.lib.report("API: IsElementPresent", status, ss_required=True)

            for key, value in enabled.items():
                if enabled[key] == False:
                    api_status = False
                    api_test_status = False
            if api_status:
                status = "PASSED"
            else:
                status = "FAILED"
            self.lib.report("API: IsEnabled", status, ss_required=True)

            tapped = False
            for key, value in present.items():
                if value == True:
                    tapped = self.lib.tap_element(self.config.list_iselm[key])
                    break

            if tapped:
                status = "PASSED"
            else:
                status = "FAILED"
            self.lib.report("API: TapElement", status, ss_required=True)

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
