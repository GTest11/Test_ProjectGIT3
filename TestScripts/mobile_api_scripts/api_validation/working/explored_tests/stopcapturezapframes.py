# ''''''''''''''''''''''''''' TEST CASE DETAILS '''''''''''''''''''''''''''''''''''''''''
# Author            :   Shameena HA
# Date              :   28-11-2018
# Script Version    :   1.0
# APIs covered      :   "StopCaptureZapFrames"
# Test Scenarios    :   this API used without using startcapture API
#                       Call multiple times without calling StartCaptureZapFrames
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
    apis = ('StopCaptureZapFrames',)
    script_name = os.path.basename(__file__)

    def multiple_stopcapture(self, param):
        '''
        Scenario: Call multiple times

        :param param: parameter list with scenario, expected status
        :return: None
        '''

        stopped = False
        try:
            iteration_count = self.config.zap_frame_iter_count
            for count in range(0, iteration_count):
                start_time = self.lib.gettimestamp()
                captured = self.dut.validator.StopCaptureZapFrames()
                end_time = self.lib.gettimestamp()
                if captured == param[1]:
                    status = "PASSED"
                    stopped = True
                else:
                    status = "FAILED"
                    stopped = False

                self.lib.report_api_status(start_time, end_time, "StopCaptureZapFrames", status, ss_required=True)
                self.lib.report("API: StopCaptureZapFrames", status, ss_required=False)
                time.sleep(10) # wait between multiple capture calls

        except Exception as e:
            self.logger.Error("Error in Multiple calls to StopCaptureZapFrames")
            stopped = False

        finally:
            return stopped


    def run_api_test(self):
        '''
        This overrides the run_api_test() in Base class

        :return: script status; True or False
        '''

        test_result = True
        params = self.config.stop_capture_frame_params
        start_time = 0
        end_time = 0

        try:
            for param in params.keys():
                self.logger.Log("--- Scenario: {} ---".format(params[param][0]))
                if param == 1:
                    stopped = self.multiple_stopcapture(params[param])
                else:
                    start_time = self.lib.gettimestamp()
                    stopped = self.dut.validator.StopCaptureZapFrames()
                    end_time = self.lib.gettimestamp()
                if stopped:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False
                if param == 0:
                    self.lib.report_api_status(start_time, end_time, "StopCaptureZapFrames", status, ss_required=True)
                self.lib.report("API: StopCaptureZapFrames - {}".format(params[param][0]), status)

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
