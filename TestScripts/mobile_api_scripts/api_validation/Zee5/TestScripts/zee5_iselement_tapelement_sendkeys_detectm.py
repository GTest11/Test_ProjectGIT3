# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :   03-04-2019
# Script Version    :   1.0
# APIs covered      :
# Test Scenario     :   "Search for a movie, playback and verify motion"
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
    apis = ('IsElement', 'Click', 'SendKeys', 'Tap', 'DetectMotion')
    script_name = os.path.basename(__file__)

    def run_api_test(self):
        """
        Script part of the framework.
        :return: True or False
        """

        test_result = True

        try:
            cur_dut_name = self.lib.get_dut_name()
            clicked = self.lib.element_ops(self.config.search_icon, action='click')
            if not clicked:
                status = "FAILED"
                test_result = False
            else:
                status = "PASSED"

            self.lib.report("Click on the search button {}".format(status), status, ss_required=True)

            if not self.lib.send_keys(self.config.search_box, keys=self.config.search_text):
                self.logger.Error("Failed to send the search text")
                status = "FAILED"
                test_result = False
            else:
                status = "PASSED"

            self.lib.report("Send search text ".format(status), status, ss_required=True)

            if not self.dut.Tap(*self.config.c_tap_search_result):
                self.logger.Error("Failed to tap on the search text")
                status = "FAILED"
                test_result = False
            else:
                status = "PASSED"

            self.lib.report("Tap on the search result".format(status), status, ss_required=True)

            time.sleep(10)

            if not cur_dut_name in self.config.c_detect_motion:
                self.logger.Error("Detect Motion coordinates not added for this DUT Type")
                status = "FAILED"
                test_result = False

            else:
                coords = self.config.c_detect_motion[cur_dut_name]
                start_time = self.lib.get_time_stamp()
                motion = self.dut.validator.DetectMotion(*coords)
                end_time = self.lib.get_time_stamp()
                if not motion:
                    self.logger.Error("Playback not started")
                    status = "FAILED"
                    test_result = False
                else:
                    self.logger.Error("Playback started")
                    status = "PASSED"
                self.lib.report_api_status(start_time, end_time, "DetectMotion", status, ss_required=True)
                self.lib.report("Playback {}".format(status), status, ss_required=False)



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
