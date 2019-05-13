# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase name     : ValidateCheckpoint.py
# Author            :
# Date              : 17-April-2019
# Script Version    : 1.0
# APIs covered      : validateCheckPoint, validateCheckpoint with base 64 image
# Test Scenario     : Launch the App, call validateCheckPoint API
#                       1. OCR checkpoint - Mobile_YouTube
#                       2. Multi line OCR - youtube_MultiOcr
#                       3. IC checkpoint, pixel - youtube_valIcPixel
#                       4. IC checkpoint, rmse - youtube_valIcRmse
# Note              : Please check the checkpoints before executing the script
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, os, time
sys.path.append('../')
from library.api_test_base import ApiTestBase
#''''''''''''''''''''''''''''''END IMPORTS''''''''''''''''''''''''''''''''

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class api_test(ApiTestBase):

    # the class which handles the script intention.
    # this overrides base class run_api_test()

    apis = ("ValidateCheckPoint")

    script_name = os.path.basename(__file__)
    

    def run_api_test(self):
        '''
        Executes the test script

        :return:
        '''

        api_test_status = True

        try:

            if self.lib.get_dut_platform() !=  "iOS":
                # validateCheckPoint base 64
                self.logger.Log(" ----- Test Scenario - Base64 image string")
                imgstring = self.dut.GetScreenshot()
                self.dut.validator.UploadScreenshot("UploadScreenshot", imgstring)
                self.chkpt.init("validate_base64_zee")

                start_time = self.lib.get_time_stamp()
                if self.dut.validator.validateCheckPoint(self.chkpt, imgstring):
                    end_time = self.lib.get_time_stamp()
                    self.lib.report_api_status(start_time, end_time, "ValidateCheckPoint_base64", "PASSED",
                                               ss_required=True)
                else:
                    api_test_status = False
                    self.lib.report("API - ValidateCheckPoint_base64", "FAILED", ss_required=True)

            test_data = self.lib.get_test_params(self.config.sanity_validate_chkpt_params,
                                                 self.config.validate_chkpt_params)

            if not test_data:
                self.lib.report("Could not populate the test data params", "FAILED")
                api_test_status = False
                return api_test_status

            for key, value in test_data.items():
                self.logger.Log(" ----- Test Scenario - {} -----".format(value[0]))
                self.chkpt.init(value[2])

                time.sleep(3)
                if "Multiline" in value[0]:
                    tapped = self.lib.tap_element(self.config.shows_view_all)
                    time.sleep(2) # to show the all shows screen
                    if not tapped:
                        self.lib.report("Failed to tap", "FAILED", ss_required=True)
                        api_test_status = False
                        return api_test_status

                    tapped = self.lib.tap_element(self.config.filter_icon)
                    time.sleep(2) # to show the filter options
                    if not tapped:
                        self.lib.report("Failed to tap", "FAILED", ss_required=True)
                        api_test_status = False
                        return api_test_status

                start_time = self.lib.get_time_stamp()
                validated = self.dut.validator.validateCheckPoint(self.chkpt)
                end_time = self.lib.get_time_stamp()

                # we use this double comparison for including negative scenarios as well
                if validated == value[1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    api_test_status = False

                self.lib.report_api_status(start_time, end_time, "ValidateCheckPoint", status, ss_required = True)
                self.lib.report("API - {}".format(value[0]), status, ss_required=False)

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
