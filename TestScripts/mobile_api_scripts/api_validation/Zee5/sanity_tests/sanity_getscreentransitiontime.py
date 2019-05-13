# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :   26-April-2019
# Script Version    :   1.0
# APIs covered      :   "GetScreenTransitionTime", "StartCaptureZapFrames",
#                       "StopCaptureZapFrames"
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

    apis = ("GetScreenTransitionTime", "StartCaptureZapFrames",
                      "StopCaptureZapFrames",
         )
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        '''
        Executes the test script

        :return:
        '''

        api_test_status = True

        scenarios = self.config.sanity_get_screen_transition_time_params
        params = self.config.get_screen_transition_time_params

        try:
            time.sleep(10)
            # starting the playback
#            if not self.dut.Tap(*self.config.C_TAP_PLAYBACK):
#                self.lib.report("Playback failed", "FAILED")
#                api_test_status = False
#                return False

            for scenario in scenarios:
                self.logger.Log("--- Scenario: {} ---".format(params[scenario][0]))
                if scenario == 'move_out_chkpt_screen':
                    if not self.lib.tap_element(self.config.search_icon):
                        self.lib.report("Failed to tap on search icon", "FAILED", ss_required=False)
                        api_test_status = False
                        continue

                if self.dut.validator.StartCaptureZapFrames(30):
                    start_time = self.lib.get_time_stamp()
                    transit_time = self.dut.validator.GetScreenTransitionTime(*params[scenario][2])
                    end_time = self.lib.get_time_stamp()
                    self.logger.Log("--- Screen transition time - {} ---".format(transit_time))
                    stopped = self.dut.validator.StopCaptureZapFrames()
                    if stopped:
                        status = "PASSED"
                    else:
                        status = "FAILED"
                        api_test_status = False
                    self.lib.report("API: StopCaptureZapFrames", status, ss_required=True)

                    # if transit_time >= 0:
                    #     screen_transition = True
                    # else:
                    #     screen_transition = False

                    if transit_time != params[scenario][1]:
                        status = "PASSED"
                    else:
                        status = "FAILED"
                        api_test_status = False

                    self.lib.report_api_status(
                        start_time, end_time,
                        'GetScreenTransitionTime: {}'.format(params[scenario][0]),
                        status, ss_required=True
                    )
                else:
                    self.lib.report("API: StartCaptureZapFrames", "FAILED", ss_required=True)
                    api_test_status = False

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
