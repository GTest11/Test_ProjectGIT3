# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :   18-April-2018
# Script Version    :   1.0
# APIs covered      :   "getOCRText"
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

    apis = ("getOCRText",
         )
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        '''
        Executes the test script

        :return:
        '''

        test_data = self.config.get_ocr_text_valid_param
        api_test_status = False
        status = "FAILED"
        cur_dut_name = self.lib.get_dut_name()
        try:
            if cur_dut_name in self.config.c_getocrtext:
                x, y, w, h = self.config.c_getocrtext[cur_dut_name]

                self.logger.Log(" ----- Test Scenario - {} -----".format(test_data[0]))
                time.sleep(3)
                f, l = test_data[2]

                start_time = self.lib.get_time_stamp()
                read = self.dut.validator.getOCRText(x, y, w, h, f, l)
                end_time = self.lib.get_time_stamp()
                self.logger.Log("getOCRText API - {}".format(read))
                if read == self.config.txt_getocrtext:
                    status = "PASSED"
                    api_test_status = True

                self.lib.report_api_status(start_time, end_time, "getOCRText", status, ss_required=False)

            else:
                self.logger.Log("Device data not available in config")

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
