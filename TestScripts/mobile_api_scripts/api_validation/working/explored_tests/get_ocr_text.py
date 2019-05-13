# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :   Lincy Robert
# Date              :   05-02-2019
# Script Version    :   1.0
# APIs covered      :   "getOCRText"
# Test Scenario     :   "Valid parameters", API_PASS, (DEFAULT_FILTER, DEFAULT_LANG),
#                       "Valid parameter: language: hin", API_PASS, (DEFAULT_FILTER, "hin")
#                       "Valid parameter: language: empty", API_PASS, (DEFAULT_FILTER, "")
#                       "Out of boundary coordinates", API_FAIL, (DEFAULT_FILTER, DEFAULT_LANG)
#                       "Multiple filters", API_FAIL, (MULTIPLE_FILTER, DEFAULT_LANG)
#                       "Invalid language", API_PASS, (DEFAULT_FILTER, INVALID_LANG)
#                       "Non-supported language", API_FAIL, (DEFAULT_FILTER, NON_SUPPORTED_LANG)
#                       "Invalid filter", API_FAIL, (INVALID_FILTER, DEFAULT_LANG)
#                       "Filters with out-of boundary values", API_FAIL, (OUT_OF_BOUND_FILTER, DEFAULT_LANG)
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

    apis= ("getOCRText",)
    script_name = os.path.basename(__file__)

    def run_api_test(self):
        """
        Executes the test script
        :return:
        """

        test_data = self.config.get_ocr_text_params
        api_test_status = True
        cur_dut_name = self.lib.get_dut_name()
        self.logger.Log("Currently selected DUT Name : "+str(cur_dut_name))

        try:
            if cur_dut_name in self.config.c_getocrtext:
                x, y, w, h = self.config.c_getocrtext[cur_dut_name]
                for scenario in test_data.keys():
                    self.logger.Log(" ----- Scenario - {} -----".format(test_data[scenario][0]))
                    f, l = test_data[scenario][-1]
                    if scenario == 3:
                        x = -10  # out of boundary coordinate

                    start_time = self.lib.gettimestamp()
                    read = self.dut.validator.getOCRText(x, y, w, h, f, l)
                    end_time = self.lib.gettimestamp()
                    self.logger.Log("OCR output of getOCRText API :- {}".format(read))
                    text_verified = True
                    if read != self.config.txt_getocrtext:
                        text_verified = False
                    
                    if text_verified != test_data[scenario][1]:
                        status = "FAILED"
                        api_test_status = False
                    else:
                        status = "PASSED"

                    self.lib.report_api_status(start_time, end_time, "getOCRText", status, ss_required=True)
                    self.lib.report("getOCRText: {}".format(test_data[scenario][0]), status)
                    time.sleep(3)
            else:
                self.logger.Log("GetOCRText parameter values not available in config for the selected DUT!")
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
