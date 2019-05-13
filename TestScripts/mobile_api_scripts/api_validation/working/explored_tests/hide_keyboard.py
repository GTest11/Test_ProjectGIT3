# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :   Shameena HA
# Date              :   30-01-2019
# Script Version    :   1.0
# APIs covered      :   "HideKeyboard",
# Test Scenario     :   1. not on keyboard screen
#                       2. on keyboard screen
#                       3. focused on text field, but keyboard is not visible
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

    )
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        '''
        Executes the test script

        :return: test status as True or False
        '''

        test_status = True
        img_bfr = "img_bfr"
        img_aftr = "img_aftr"

        params = self.config.hide_kbd_params
        cur_dut = self.lib.get_dut_name()
        self.logger.Log("DUT Name {}".format(cur_dut))

        try:

            x, y, w, h = (0, 0, 0, 0)
            img_before_api_call = img_after_api_call = None

            for param in params:
                self.logger.Log("---------- Scenario {} ---------".format(params[param][0]))

                if cur_dut in self.config.c_hide_kbd:
                    x, y, w, h = self.config.c_hide_kbd[cur_dut]
                else:
                    self.lib.report(
                        "The current DUT does not have an entry in Config, so skipping the test",
                        "FAILED",
                        ss_required=True
                        )
                    test_status = False
                    return False

                if param == 1:
                    clicked = self.lib.element_ops(self.config.search_icon, index=None, action='click')
                    if not clicked:
                        self.lib.report("Failed to click on search icon", "FAILED", ss_required=True)
                        test_status = False
                        return False

                time.sleep(1)
                img_before_api_call = self.dut.validator.CaptureImage(
                      x, y, w, h, img_bfr,
                      self.config.CAP_IMG_DEFAULT_QUALITY,
                      self.config.overwrite_file
                      )

                start_time = self.lib.gettimestamp()
                hidden = self.dut.HideKeyboard()
                end_time = self.lib.gettimestamp()
                time.sleep(2)

                img_after_api_call = self.dut.validator.CaptureImage(
                    x, y, w, h, img_aftr,
                    self.config.CAP_IMG_DEFAULT_QUALITY,
                    self.config.overwrite_file
                )
                if not (img_after_api_call and img_before_api_call):
                    self.lib.report("Could not capture images", "FAILED", ss_required=True)
                    test_status = False
                    return False

                matched = self.dut.validator.ImageMatch(img_bfr, img_aftr, 2, "13")
                if param == 2 and not matched:
                    matched = True

                if hidden == params[param][1] and matched:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_status = False
                self.lib.report_api_status(start_time, end_time, "HideKeyboard", status, ss_required=True)
                self.lib.report("HideKeyboard: {}".format(params[param][0]), status, ss_required=False)

        except Exception as e:
            self.logger.Error("Error in run_api_test() " + str(e))
            test_status = False

        finally:
            self.test_result = test_status

def main():
    testobj = api_test()
    testobj.run_test(testobj.script_name, testobj.apis)


if __name__ == '__main__':
    main()
