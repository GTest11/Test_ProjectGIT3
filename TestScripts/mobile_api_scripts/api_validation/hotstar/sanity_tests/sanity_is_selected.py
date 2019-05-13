# ''''''''''''''''''''''''''' TEST CASE DETAILS '''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :
# Script Version    : 1.0
# APIs covered      :   "IsSelected"
# Test Scenarios    :
#                      select and unselect the element and observe the property value.
#
# ''''''''''''''''''''''''''' TEST CASE DETAILS - END '''''''''''''''''''''''''''''''''

import os
import sys
import time
sys.path.append('../')

from library.api_test_base import ApiTestBase

class api_test(ApiTestBase):
    '''
    The class which handles the script intention.
    this overrides base class run_api_test()

    '''

    # class variables
    apis = ('IsSelected',)
    script_name = os.path.basename(__file__)

    def check_selected(self, elm_name):
        selected_status = False
        count = 4
        try:

            # tapping on the video to start playback
            start_time = self.lib.get_time_stamp()
            tapped = self.dut.Tap(*self.config.C_TAP_PLAYBACK)
            end_time = self.lib.get_time_stamp()
            if tapped:
                status = "PASSED"
            else:
                status = "FAILED"
            self.lib.report_api_status(start_time, end_time, "Tap", status, ss_required=True)

            if not tapped:
                self.logger.Error("Tap failed, exiting the test..")
                return selected_status

            appeared = self.lib.wait_for_element(self.config.with_selected_prop, self.config.T_MD_WAIT)
            if not appeared:
                self.logger.Error("Autoplay button did not appear, exiting the test..")
                return selected_status

            l_select_status = []
            for c in range(0, count):
                selected = self.lib.is_selected(elm_name)
                l_select_status.append(selected)
                tapped = tapped = self.lib.tap_element(elm_name)
                if not tapped:
                    self.logger.Error("Could not tap on the element")
                    break

            if not l_select_status:
                selected_status = False

            if l_select_status.count(True) >= 2:
                selected_status = True
            else:
                selected_status = False

        except Exception as e:
            self.logger.Error("Could not verify the 'Selected' property" + str(e))
            selected_status = False

        finally:
            return selected_status


    def run_api_test(self):
        '''
        This overrides the run_api_test() in Base class

        :return: script status; True or False
        '''

        # for api status
        test_result = True
        try:
            # getting the device platform

            if self.lib.get_dut_platform() == "iOS":
                self.lib.report("Platform iOS does not support this API", "FAILED", ss_required=False)
                test_result = False
                return test_result

            test_result = self.check_selected(self.config.autoplay_toggle)

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
