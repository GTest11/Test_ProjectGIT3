# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :   16-April-2019
# Script Version    :   1.0
# APIs covered      :   "Tap", "DetectMotion", "VolumeUp", "VolumeDown"
# Test Scenario     :   Taps on the given coordinate (on the video - results a video playback),
#                         verify playback using 'DetectMotion' api,
#                         increases/decreases the player volume
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

    apis = ("Tap", "DetectMotion", "VolumeUp", "VolumeDown",
         )
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        '''
        Executes the test script
        :return:
        '''

        api_test_status = True
        platform = self.lib.get_dut_platform()

        test_data = self.lib.get_test_params(
            self.config.sanity_detect_motion_params,
            self.config.detect_motion_params
        )

        try:
            # start playback
            start_time = self.lib.get_time_stamp()
            tapped = self.dut.Tap(*self.config.C_TAP_PLAYBACK)
            end_time = self.lib.get_time_stamp()
            if tapped:
                status = "PASSED"
            else:
                status = "FAILED"
                api_test_status = False

            time.sleep(1)
            self.lib.report_api_status(start_time, end_time, 'Tap', status, ss_required=True)
            if not tapped:
                self.lib.report("Tap Failed, but proceeding the script", "FAILED", ss_required=False)
                api_test_status = False

            for data in test_data:
                self.logger.Log(" ----- Test Scenario - {} -----".format(test_data[data][0]))
                start_time = self.lib.get_time_stamp()
                detected = self.dut.validator.DetectMotion(*test_data[data][2])
                end_time = self.lib.get_time_stamp()

                if detected == test_data[data][1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    api_test_status = False

                self.lib.report_api_status(start_time, end_time, "DetectMotion", status, ss_required=True)

            if "Android" == platform:
                apis = [self.dut.VolumeUp,
                        self.dut.VolumeDown,
                        ]
                str_api = ("VolumeUp", "VolumeDown")
                idx = -1

                for api in apis:
                    start_time = self.lib.get_time_stamp()
                    changed = api(self.config.volume_levels)
                    end_time = self.lib.get_time_stamp()

                    if changed:
                        status = "PASSED"
                    else:
                        status = "FAILED"
                        api_test_status = False
                    idx += 1

                    self.lib.report_api_status(start_time, end_time, str_api[idx], status, ss_required=True)
            else:
                self.lib.report("Volume APIs are not available for this platform", "FAILED", ss_required=True)

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
