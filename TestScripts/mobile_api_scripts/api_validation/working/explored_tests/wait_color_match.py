# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            :   Shameena HA
# Date              :   06-02-2019
# Script Version    :   1.0
# APIs covered      :  "WaitColorMatch"
# Test Scenario:
#              "Valid parameters"
#              "Valid parameters, flatness boundary condition : 0"
#               Valid parameters, flatness boundary condition : 100"
#              "Invalid parameters, waitGap greater than timeToWait"
#              "Valid parameters, Multiple occurances of Match color"
#              "Valid parameters, Match color check on non matching screen"
#
# '''''''''''''''''''''''''''TEST CASE DETAILS - END '''''''''''''''''''''''''''''''''

import sys, os, time
sys.path.append('../')
from library.api_test_base import apiTestBase


class api_test(apiTestBase):

    # the class which handles the script intention.
    # this overrides base class run_api_test()

    apis = ("WaitColorMatch",)
    script_name = os.path.basename(__file__)
    

    def run_api_test(self):
        '''
        Executes the test script

        :return:
        '''

        api_test_status = True

        try:
            test_data = self.config.wait_color_match_params
            cur_dut = self.lib.get_dut_name()
            for key, value in test_data.items():
                self.logger.Log(" ----- Test Scenario - {} -----".format(value[0]))

                if key == 4:    # searching for the match in the entire screen
                    value[2][3], value[2][4]  = self.lib.get_image_resolution()
                else:
                    if cur_dut in self.config.c_color_match:
                        param = list(value[2])
                        param[1], param[2], param[3], param[4] = self.config.c_color_match[cur_dut]
                        value[2] = tuple(param)
                    else:
                        self.lib.report(
                            "Device does not have an entry in the config, hence proceeding with the existing coordinates",
                            "FAILED", ss_required=True
                        )
                        api_test_status = False

                if key == 5:
                    if not self.dut.Tap(*self.config.C_TAP_PLAYBACK):
                        time.sleep(2) # to get clear screenshot of the state of device
                        self.lib.report("Failed to start the playback", "FAILED", ss_required=True)
                        api_test_status = False
                        continue

                time.sleep(3)
                if self.dut.validator.StartCaptureZapFrames(self.config.captureZapTime):
                    self.lib.report("API: StartCaptureZapFrames", "PASSED", ss_required=True)
                    start_time = self.lib.gettimestamp()
                    match_found = self.dut.validator.WaitColorMatch(*value[2])
                    end_time = self.lib.gettimestamp()

                    time1 = self.lib.gettimestamp()
                    stopped = self.dut.validator.StopCaptureZapFrames()
                    time2 = self.lib.gettimestamp()
                    if stopped:
                        status = "PASSED"
                    else:
                        status = "FAILED"
                        api_test_status = False
                    self.lib.report_api_status(time1, time2, "StopCaptureZapFrames", status, ss_required = False)

                    if match_found == value[1]:
                        status = "PASSED"
                    else:
                        status = "FAILED"
                        api_test_status = False
                    self.lib.report_api_status(start_time, end_time, "WaitColorMatch", status, ss_required = True)
                    self.lib.report("WaitColorMatch: {}".format(value[0]), status, ss_required=False)

                else:
                    api_test_status = False
                    self.logger.Log("StartCaptureZapFrames API Failed. Hence, skipping WaitColorMatch and StopCaptureZapFrames APIs")
                    self.lib.report("API - StartCaptureZapFrames", "FAILED", ss_required=True)
                    self.lib.report("API - WaitColorMatch", "NOT RUN", ss_required=False)

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
