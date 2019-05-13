# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              : 22-April-2019
# Script Version    : 1.0
# APIs covered      : WaitOCRMatch
# Test Scenario     : Launch the App, call WaitOCRMatch API
#                       1. OCR checkpoint
#                       2. Multi line OCR
#
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

    apis = ("WaitOCRMatch",)

    script_name = os.path.basename(__file__)
    

    def run_api_test(self):
        '''
        Executes the test script

        :return:
        '''

        api_test_status = True

        try:

            test_data = self.lib.get_test_params(self.config.sanity_wait_ocr_match_params,
                                                 self.config.wait_ocr_match_params)

            if not test_data:
                self.lib.report("Could not populate the test data params", "FAILED")
                api_test_status = False
                return api_test_status

            for key, value in test_data.items():
                self.logger.Log(" ----- Test Scenario - {} -----".format(value[0]))

                time.sleep(3)
                if "Multiline" in value[0]:
                    tapped = self.lib.tap_element(self.config.home)
                    time.sleep(2) # to show the all shows screen
                    if not tapped:
                        self.lib.report("Failed to tap", "FAILED", ss_required=True)
                        api_test_status = False
                        return api_test_status



                matched = False
                start_time = None
                end_time = None
                if (self.dut.validator.StartCaptureZapFrames(30)):
                    start_time = self.lib.get_time_stamp()
                    matched = self.dut.validator.WaitOCRMatch(*value[2])
                    end_time = self.lib.get_time_stamp()
                self.dut.validator.StopCaptureZapFrames()

                # we use this double comparison for including negative scenarios as well
                if matched >= 0:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    api_test_status = False

                self.lib.report_api_status(start_time, end_time, "WaitOCRMatch", status, ss_required = True)
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
