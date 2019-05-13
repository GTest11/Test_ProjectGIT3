# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :
# Date              :   05-10-2018
# Script Version    :   1.1
# APIs covered      :   "StartCaptureZapFrames", "WaitColorMatch", "StopCaptureZapFrames"
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, os, time
sys.path.append('../')
from library.api_test_base import ApiTestBase
#''''''''''''''''''''''''''''''END IMPORTS''''''''''''''''''''''''''''''''

class api_test(ApiTestBase):

    # the class which handles the script intention.
    # this overrides base class run_api_test()

    apis = ("StartCaptureZapFrames", "WaitColorMatch", "StopCaptureZapFrames")

    script_name = os.path.basename(__file__)
    

    def run_api_test(self):
        '''
        Executes the test script

        :return:
        '''

        api_test_status = True

        try:
            stopped = self.dut.validator.StopCaptureZapFrames()

            test_data = self.lib.get_test_params(self.config.sanity_wait_color_match_params,self.config.wait_color_match_params)
            cur_dut = self.lib.get_dut_name()
            for key, value in test_data.items():
                self.logger.Log(" ----- Test Scenario - {} -----".format(value[0]))
                param = value[2]
                if cur_dut in self.config.c_colour_match:
                    param[1], param[2], param[3], param[4]  = self.config.c_colour_match[cur_dut]
                else:
                    self.logger.Log("Current DUT is not available in Config")
                    api_test_status = False
                    return False

                if "Multiple occurrences" in param[0]:
                    param[3], param[4] = self.lib.get_image_resolution()

                api_executed = False
                time.sleep(3)
                if self.dut.validator.StartCaptureZapFrames(self.config.captureZapTime):
                    self.lib.report("API: StartCaptureZapFrames", "PASSED", ss_required=True)
                    start_time = self.lib.get_time_stamp()
                    match_found = self.dut.validator.WaitColorMatch(*value[2])
                    end_time = self.lib.get_time_stamp()
                    api_executed = True

                    time1 = self.lib.get_time_stamp()
                    stopped = self.dut.validator.StopCaptureZapFrames()
                    time2 = self.lib.get_time_stamp()
                    if stopped:
                        status = "PASSED"
                    else:
                        status = "FAILED"
                        api_test_status = False
                    self.lib.report_api_status(time1, time2, "StopCaptureZapFrames", status, ss_required = False)

                    if api_executed and match_found == value[1]:
                        status = "PASSED"
                    elif not api_executed:
                        status = "NOT RUN"
                        api_test_status = False
                    else:
                        status = "FAILED"
                        api_test_status = False
                    self.lib.report_api_status(start_time, end_time, "WaitColorMatch", status, ss_required = True)
                
                else:
                    api_test_status = False
                    self.logger.Log("StartCaptureZapFrames API Failed. Hence, skipping WaitColorMatch and StopCaptureZapFrames APIs")
                    self.lib.report("API - StartCaptureZapFrames", "FAILED", ss_required=True)

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
