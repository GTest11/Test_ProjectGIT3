# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :   04-04-2019
# Script Version    :   1.0
# APIs covered      :
# Test Scenario     :   "Swipe on the application till the page ends"
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
    apis = ('CaptureImage', 'Swipe', 'DynamicImageCompare', )
    script_name = os.path.basename(__file__)

    def run_api_test(self):
        """
        Script part of the framework.
        :return: True or False
        """

        test_result = True

        try:
            cur_dut_name = self.lib.get_dut_name()
            if cur_dut_name in self.config.c_swipe:
                coords = self.config.c_swipe[cur_dut_name]
            else:
                self.logger.Error("Swipe coordinates not available for current dut")
                test_result = False
                return False
            self.logger.Log("------ 123")

            ref = "ref_image"
            test = "test_image"
            if cur_dut_name in self.config.c_capture_image:
                ref_coods = list(self.config.c_capture_image[cur_dut_name])
                test_coods = list(self.config.c_capture_image[cur_dut_name])
                test_coods[4] = test
            else:
                self.logger.Error("CaptureImage coordinates not available for current dut")
                test_result = False
                return False

            status = "FAILED"
            count=50

            while(True):
                start_time =self.lib.get_time_stamp()
                # captured = self.dut.validator.CaptureImage(*capture_coods)
                captured = self.dut.validator.CaptureImage(*ref_coods)
                end_time = self.lib.get_time_stamp()

                if captured:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False
                self.lib.report_api_status(start_time, end_time, "CaptureImage", status, ss_required=True)
                time.sleep(1)

                start_time = self.lib.get_time_stamp()
                swiped = self.dut.Swipe(*coords)
                end_time = self.lib.get_time_stamp()
                if not swiped:
                    status = "FAILED"
                    test_result = False
                else:
                    status = "PASSED"
                self.lib.report_api_status(start_time, end_time, "Swipe", status, ss_required=True)
                time.sleep(1)

                start_time = self.lib.get_time_stamp()
                captured = self.dut.validator.CaptureImage(*test_coods)
                end_time = self.lib.get_time_stamp()

                if captured:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False
                self.lib.report_api_status(start_time, end_time, "CaptureImage", status, ss_required=True)
                time.sleep(1)

                start_time = self.lib.get_time_stamp()
                matched = self.dut.validator.ImageMatch(ref, test, 2, "13")
                end_time = self.lib.get_time_stamp()
                if matched:
                    status = "PASSED"
                else:
                    test_result = False
                self.lib.report_api_status(start_time, end_time, "ImageMatch", status, ss_required=True)

                count -=1
                if matched or not count:
                    break
            self.lib.report("CaptureImage, Swipe, ImageMatch", status, ss_required=False)

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
