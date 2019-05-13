# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            :   Lincy Robert
# Date              :   02-04-2019
# Script Version    :   1.0
# APIs covered      :   "Tap, getOCRText"
# Test Scenario     :   "Tap on any valid coordinate which results in a UI change and
#                       validate the UI change using getOCRText API"
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
    apis = ('Tap','getOCRText',)
    script_name = os.path.basename(__file__)

    def run_api_test(self):
        """
        Script part of the framework.
        :return: True or False
        """

        test_result = True

        try:
            self.logger.Log("--- Scenario: Tap on any valid coordinate which results in a UI change and validate the "
                            "UI change using getOCRText API ---")
            cur_dut_name = self.lib.get_dut_name()
            if cur_dut_name in self.config.home_in_home_menu:
                self.logger.Log('111111111111111')
                tap_coordinates = self.config.home_in_home_menu[cur_dut_name]
            else:
                self.logger.Log('2222222')
                self.logger.Error("Tap coordinates not available for the specific DUT.")
                test_result = False
                return
            start_time = self.lib.get_time_stamp()
            tap_result = self.dut.Tap(*tap_coordinates)
            end_time = self.lib.get_time_stamp()

            if not tap_result:
                self.logger.Error("Tap failed.")
                self.logger.Log("Return value obtained for Tap API is : "+str(tap_result))
                status = "FAILED"
                test_result = False
            else:
                if self.validate_expected_screen_until_given_time(6):
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False

            self.lib.report_api_status(start_time, end_time, "Tap", status, ss_required=True)

        except Exception as e:
            self.logger.Error("Error in run_api_test() " + str(e))
            test_result = False

        finally:
            self.test_result = test_result

    def validate_expected_screen_until_given_time(self, period):
        """
        Verifies if the expected string appears in the screen by validating using getOCRText output for given period
        :param period: time to validate using getOCRText output
        :return: True if expected string is obtained, else False
        """
        validated = False
        status = "FAILED"
        trial_count = period/2
        start_time = end_time = 0
        cur_dut_name = self.lib.get_dut_name()
        if cur_dut_name in self.config.home_launched:
            ocr_params = self.config.home_launched[cur_dut_name]
        else:
            self.logger.Error("Tap coordinates not available for the specific DUT.")
            test_result = False
            return
        for trial in range(trial_count):
            start_time = self.lib.get_time_stamp()
            obtained_string = self.dut.validator.getOCRText(*ocr_params)
            end_time = self.lib.get_time_stamp()
            self.logger.Log('Expected string : '+str(self.config.home_string))
            self.logger.Log('Obtained string : ' + str(obtained_string))
            if obtained_string == self.config.home_string:
                self.logger.Log('Expected string obtained using getOCRText API.')
                validated = True
                status = "PASSED"
                break
            else:
                self.logger.Error('Failed to find expected string using getOCRText API.')
            time.sleep(2)

        self.lib.report_api_status(start_time, end_time, "getOCRText", status, ss_required=True)
        return validated

def main():
    testobj = api_test()
    testobj.run_test(testobj.script_name, testobj.apis)


if __name__ == '__main__':
    main()
