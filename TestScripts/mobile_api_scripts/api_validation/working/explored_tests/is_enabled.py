# ''''''''''''''''''''''''''' TEST CASE DETAILS '''''''''''''''''''''''''''''''''''''''''
# Author            :   Shameena HA
# Date              :   27-11-2018
# Script Version    :   1.0
# APIs covered      :   "IsEnabled"
# Test Scenarios    :   For a non supporting element
#                       select and unselect the element and observe the property value.
#
# ''''''''''''''''''''''''''' TEST CASE DETAILS - END '''''''''''''''''''''''''''''''''

import os
import sys
import time
sys.path.append('../')

from library.api_test_base import apiTestBase

class api_test(apiTestBase):
    '''
    The class which handles the script intention.
    this overrides base class run_api_test()

    '''

    # class variables
    apis = ('IsEnabled',)
    script_name = os.path.basename(__file__)

    def check_enabled(self, elm_name):
        enabled_status = False
        count = 4
        try:
            # tapping on the video to start playback
            start_time = self.lib.gettimestamp()
            tapped = self.dut.Tap(*self.config.C_TAP_PLAYBACK)
            end_time = self.lib.gettimestamp()
            if tapped:
                status = "PASSED"
            else:
                status = "FAILED"
            self.lib.report_api_status(start_time, end_time, "Tap", status, ss_required=True)
            if not tapped:
                self.logger.Error("Tap failed, exiting the test..")
                return enabled_status

            appeared = self.lib.wait_for_element(self.config.with_selected_prop, self.config.T_MD_WAIT)
            if not appeared:
                self.logger.Error("Autoplay button did not appear, exiting the test..")
                return enabled_status

            l_enable_status = []
            for c in range(0, count):
                enabled = self.lib.is_enabled(elm_name)
                l_enable_status.append(enabled)
                tapped = self.lib.tap_element(elm_name)
                if not tapped:
                    self.logger.Error("Could not tap on the element")
                    break
                time.sleep(3) # sleep between checks

            if not l_enable_status:
                enabled_status = False

            if l_enable_status.count(True) >= 2:
                enabled_status = True
            else:
                enabled_status = False

        except Exception as e:
            self.logger.Error("Could not verify the 'Enabled' property" + str(e))
            enabled_status = False

        finally:
            return enabled_status


    def run_api_test(self):
        '''
        This overrides the run_api_test() in Base class

        :return: script status; True or False
        '''

        # for api status
        test_result = True
        params = self.config.is_enabled_params
        try:
            for param in params.keys():
                self.logger.Log("--- Scenario: {} ---".format(params[param][0]))

                if param == 0:
                    enabled = self.lib.is_enabled(params[param][-1])
                else:
                    enabled = self.check_enabled(params[param][-1])

                if enabled == params[param][1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False
                self.lib.report("API: IsEnabled: {}".format(params[param][0]), status)

        except Exception as e:
            self.logger.Error("Error in run_api_test() " + str(e))
            test_result = False

        finally:
            # to set the test status
            self.test_result = test_result


def main():
    testobj = api_test()
    testobj.run_test(testobj.script_name, testobj.apis)


if __name__ == '__main__':
    main()
