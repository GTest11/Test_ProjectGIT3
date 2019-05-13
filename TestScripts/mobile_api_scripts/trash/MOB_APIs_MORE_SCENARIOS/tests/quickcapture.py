# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            : Shameena HA
# Date              :   26-11-2018
#Script Version     : 1.0
#Modification details:
# APIs covered      :   "QuickCapture"
#Test Scenario:
#
# '''''''''''''''''''''''''''TEST CASE DETAILS' - END '''''''''''''''''''''''''''''''''

import os
import sys
sys.path.append('../')

from library.api_test_base import apiTestBase

class api_test(apiTestBase):
    # the class which handles the script intention.
    # this overrides base class run_api_test()

    # class variables
    apis = ('QuickCapture',)
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        self.logger.Log("Valid Scenario: QuickCapture from current active source")
        start_time = self.lib.gettimestamp()
        captured = self.dut.validator.QuickCapture("test_img")
        end_time = self.lib.gettimestamp()
        if captured:
            status = "PASSED"
        else:
            status = "FAILED"
        self.lib.report_api_status(start_time, end_time, "QuickCapture", status, ss_required=True)

        self.logger.Log("Valid Scenario: QuickCapture from changed active source")

        self.dut.validator.SetActiveFrameSource("source1")
        start_time = self.lib.gettimestamp()
        captured = self.dut.validator.QuickCapture("test_img")
        end_time = self.lib.gettimestamp()

        if captured:
            status = "PASSED"
        else:
            status = "FAILED"
        self.lib.report_api_status(start_time, end_time, "QuickCapture", status, ss_required=True)

        # to set the test status
        self.test_result = True


def main():
    testobj = api_test()
    testobj.run_test(testobj.script_name, testobj.apis)


if __name__ == '__main__':
    main()
