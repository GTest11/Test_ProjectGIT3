# ''''''''''''''''''''''''''' TEST CASE DETAILS '''''''''''''''''''''''''''''''''''''''''
# Author            : Shameena HA
# Date              :   27-11-2018
# Script Version    : 1.0
# APIs covered      :   "IsSelected"
# Test Scenarios    : For a non supporting element
#                      select and unselect the element and observe the property value.
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
    apis = ('IsSelected',)
    script_name = os.path.basename(__file__)

    def check_selected(self, elm_name):
        selected_status = False
        count = 4
        try:
            l_select_status = []
            for c in range(0, count):
                selected = self.lib.is_selected(elm_name)
                l_select_status.append(selected)
                tapped = self.lib.element_ops(elm_name, action='tap')
                if not tapped:
                    self.logger.Error("Could not tap on the element")
                    break

            if not l_select_status:
                selected_status = False

            if l_select_status.count(True) == 2:
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
        params = self.config.is_selected_params
        try:

            # tapping on the video to start playback
            start_time = self.lib.gettimestamp()
            tapped = self.dut.Tap(*self.config.C_TAP_PLAYBACK)
            end_time = self.lib.gettimestamp()
            if tapped:
                status = "PASSED"
            else:
                status = "FAILED"
            self.lib.report_api_status(start_time, end_time, "Tap", status,ss_required=True)
            if not tapped:
                self.logger.Error("Tap failed, exiting the test..")
                test_result = False
                return False

            appeared = self.lib.wait_for_element(self.config.with_selected_prop, self.config.T_MD_WAIT)
            if not appeared:
                self.logger.Error("Autoplay button did not appear, exiting the test..")
                test_result = False
                return False

            for param in params.keys():
                self.logger.Log("Scenario: {}".format(params[param][0]))
                if param == 0:
                    self.logger.Log("params[param][-1] {}".format (params[param][-1],))
                    selected = self.lib.is_selected(params[param][-1])
                else:
                    selected = self.check_selected(params[param][-1])

                if param == 0 and (not selected) and selected == params[param][1]:
                    status = "PASSED"
                elif selected and selected == params[param][1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False
                self.lib.report("API: IsSelected: {}".format(params[param][0]), status)

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
