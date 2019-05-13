# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author                :   Lincy Robert
# Date                  :   04-02-2019
# Script Version        :   1.0
# Modification details  :
# APIs covered          :   "SetActiveFrameSource", "GetScreenshot"
# Test Scenario         :   "Sets video source to valid frame sources"
#                           "Sets video source to invalid frame source"
# Evaluation of this script needs to be done manually by analyzing the captured images after each source-change
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


import os
import sys
import time
sys.path.append('../')

from library.api_test_base import apiTestBase


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class api_test(apiTestBase):

    # the class which handles the script intention.
    # this overrides base class run_api_test()

    apis = ("SetActiveFrameSource", "GetScreenshot")
    script_name = os.path.basename(__file__)
    

    def run_api_test(self):
        '''
        Executes the test script
        :return:
        '''

        api_test_status = True
        try:
            self.logger.Log("Scenario: Valid video sources")
            sources = self.config.video_sources

            for source in sources:
                self.logger.Log("*** Video Source changing to {} ***".format(source))
                start_time = self.lib.gettimestamp()
                source_changed = self.dut.validator.SetActiveFrameSource(source)
                end_time = self.lib.gettimestamp()
                if source_changed:
                    source_change_status = "PASSED"
                    if self.lib.get_image_resolution() is not None:
                        w, h = self.lib.get_image_resolution()
                        path_quick_capture = self.dut.validator.QuickCapture("QuickCaptureImage")
                        if not path_quick_capture:
                            self.lib.report("QuickCapture API ", "FAILED")
                        path_capture_image = self.dut.validator.CaptureImage(0, 0, w, h, "CaptureImageOutput", 90, 0)
                        if not path_capture_image:
                            self.lib.report("CaptureImage API ", "FAILED")
                    else:
                        api_test_status = False
                        self.logger.Error("Error while obtaining image resolution using QuickCapture!")
                        self.logger.Error("Skipping QuickCapture and CaptureImage APIs after changing source to "
                                          + str(source))
                else:
                    source_change_status = "FAILED"
                    api_test_status = False
                self.lib.report_api_status(start_time, end_time, "SetActiveFrameSource", source_change_status,
                                           ss_required=True)
                time.sleep(2)
                screenshot_start_time = self.lib.gettimestamp()
                screenshot_obtained = self.dut.GetScreenshot()
                screenshot_end_time = self.lib.gettimestamp()
                if screenshot_obtained:
                    screenshot_status = "PASSED"
                else:
                    screenshot_status = "FAILED"
                    api_test_status = False
                self.lib.report_api_status(screenshot_start_time, screenshot_end_time, "GetScreenshot",
                                                   screenshot_status, ss_required=True)

            self.logger.Log("Scenario: Invalid video source")
            invalid_source = self.config.non_existing_source
            start_time = self.lib.gettimestamp()
            invalid_source_changed = self.dut.validator.SetActiveFrameSource(invalid_source)
            end_time = self.lib.gettimestamp()
            if not invalid_source_changed:
                source_change_status = "PASSED"
            else:
                source_change_status = "FAILED"
                api_test_status = False

            self.lib.report_api_status(start_time, end_time, "SetActiveFrameSource", source_change_status, ss_required=True)
            self.lib.report("SetActiveFrameSource: Scenario - Invalid video source", source_change_status)

        except Exception as e:
            self.logger.Error("Exception raised in test_api function : " + str(e))
            api_test_status = False
        finally:
            self.test_result = api_test_status


def main():
    testobj = api_test()
    testobj.run_test(testobj.script_name, testobj.apis)


if __name__ == '__main__':
    main()
