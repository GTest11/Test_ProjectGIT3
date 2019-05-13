# ''''''''''''''''''''''''''' TEST CASE DETAILS '''''''''''''''''''''''''''''''''''''''''
# Author            : Shameena HA
# Date              :   26-11-2018
# Script Version    : 1.0
# APIs covered      :   "StartCaptureZapFrames"
# Test Scenarios    : duration equal to WD timeout or greater
#                     Negative value for duration
#                     Call multiple times without calling StopCaptureZapFrames
#
# ''''''''''''''''''''''''''' TEST CASE DETAILS - END '''''''''''''''''''''''''''''''''

import os
import sys
import time
sys.path.append('../')

from library.api_test_base import apiTestBase

class api_test(apiTestBase):
    '''
    The class which handles the script intention.
    this overrides base class run_api_test()

    '''

    # class variables
    apis = ('StartCaptureZapFrames',)
    script_name = os.path.basename(__file__)

    def multiple_capture(self, param):
        '''
        Scenario: Call multiple times without calling StopCaptureZapFrames

        :param param: parameter list with scenario, expected status, duration for capture
        :return: None
        '''

        captured = False
        iteration_count = self.config.zap_frame_iter_count
        for count in range(0, iteration_count):
            captured = self.dut.validator.StartCaptureZapFrames(param[-1])
            if captured:
                status = "PASSED"
            else:
                status = "FAILED"
            self.lib.report("StartCaptureZapFrames: Multiple Call: Iter Count - {}".format(count), status, ss_required=True)
            # self.dut.validator.StopCaptureZapFrames()   # to stop the StartCaptureZapFrames
            time.sleep(10) # wait between multiple capture calls
        return captured


    def run_api_test(self):
        '''
        This overrides the run_api_test() in Base class

        :return: script status; True or False
        '''

        params = self.config.start_capture_zap_frame_params
        test_result = True

        try:
            for param in params.keys():
                self.logger.Log("--- Scenario: {} ---".format(params[param][0]))
                if param == 2:
                    test_result = self.multiple_capture(params[param])
                    if test_result:
                        status = "PASSED"
                    else:
                        status = "FAILED"
                    self.lib.report("StartCaptureZapFrames: {}".format(params[param][0]), status, ss_required=False)
                else:
                    start_time = self.lib.gettimestamp()
                    captured = self.dut.validator.StartCaptureZapFrames(params[param][-1])
                    end_time = self.lib.gettimestamp()
                    if captured == params[param][1]:
                        status = "PASSED"
                    else:
                        status = "FAILED"
                        test_result = False
                    self.lib.report_api_status(start_time, end_time, "StartCaptureZapFrames", status, ss_required=True)
                    self.lib.report("StartCaptureZapFrames: {}".format(params[param][0]), status)
                    self.dut.validator.StopCaptureZapFrames()  # to stop the StartCaptureZapFrames

        except Exception as e:
            self.logger.Error("Error in run_api_test() " + str(e))
            test_result = False
        finally:
            self.test_result = test_result


    def cleanup(self):
        self.logger.Log("------------------cleanup")
        self.dut.validator.StopCaptureZapFrames()  # to stop the StartCaptureZapFrames
        super(api_test, self).cleanup()


def main():
    testobj = api_test()
    testobj.run_test(testobj.script_name, testobj.apis)


if __name__ == '__main__':
    main()
