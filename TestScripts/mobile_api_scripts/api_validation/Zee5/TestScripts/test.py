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

            ref = "ref_image"
            test = "test_image"
            if cur_dut_name in self.config.c_capture_image:
                ref_coods = list(self.config.c_capture_image[cur_dut_name])
                test_coods = ref_coods
                print "ref_coods", ref_coods
                test_coods[4] = test
                print "self.config.c_capture_image[cur_dut_name]", self.config.c_capture_image[cur_dut_name]
                print "ref_coods >>>>>>> ", ref_coods
                print "test_coods", test_coods
            else:
                self.logger.Error("CaptureImage coordinates not available for current dut")
                test_result = False
                return False
            self.logger.Log("------ 1234")

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
