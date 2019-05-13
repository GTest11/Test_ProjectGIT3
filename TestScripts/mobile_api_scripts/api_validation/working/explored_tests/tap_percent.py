# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :   Lincy Robert
# Date              :   01-02-2019
# Script Version    :   1.0
# APIs covered      :   "TapPercent"
# Test Scenarios    :   "Parameter out of boundary",
#                       "Tap on element with Clickable-False, but available on the screen",
#                       "Tap on lock screen",
#                       "Tap on Clickable element"
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import os
import sys
import time
import json
sys.path.append('../')

from library.api_test_base import apiTestBase


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class api_test(apiTestBase):

    # the class which handles the script intention.
    # this overrides base class run_api_test()

    apis = ("TapPercent", )
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        '''
        Executes the test script
        :return:
        '''

        api_test_status = True

        try:
            test_params = self.config.tap_percent_params
            for scenario in test_params.keys():
                self.logger.Log("Scenario: {}".format(test_params[scenario][0]))

                if scenario == 2:
                    self.dut.Lock()
                start_time = self.lib.gettimestamp()
                api_result = self.dut.TapPercent(*test_params[scenario][-1])
                end_time = self.lib.gettimestamp()
                self.execute_post_condition_of_scenario(scenario)

                if api_result == test_params[scenario][1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    api_test_status = False

                self.lib.report_api_status(start_time, end_time, "TapPercent", status, ss_required=True)
                self.lib.report("TapPercent: {}".format(test_params[scenario][0]), status)

        except Exception as e:
            self.logger.Error("Error in run_api_test() " + str(e))
            api_test_status = False

        finally:
            self.test_result = api_test_status

    def execute_post_condition_of_scenario(self, scenario):
        """executes the post condition which needs to be done as per the scenario """
        if scenario == 2:
            if self.lib.get_dut_platform() == 'iOS':
                time.sleep(12)  # iOS devices gets automatically unlocked after 10 seconds
            else:
                self.dut.Unlock()
                time.sleep(3)


def main():
    testobj = api_test()
    testobj.run_test(testobj.script_name, testobj.apis)


if __name__ == '__main__':
    main()
