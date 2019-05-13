# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :   Shameena HA
# Date              :   18-April-2019
# Script Version    :   1.1
# APIs covered      :   "WaitForCheckpoint",
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


import sys, os, time
sys.path.append('../')
from library.api_test_base import ApiTestBase
#''''''''''''''''''''''''''''''END IMPORTS''''''''''''''''''''''''''''''''

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class api_test(ApiTestBase):

    # the class which handles the script intention.
    # this overrides base class run_api_test()

    apis = ("WaitForCheckpoint")

    script_name = os.path.basename(__file__)
    

    def run_api_test(self):
        '''
        Executes the test script

        :return:
        '''

        api_test_status = True

        try:
            self.dut.validator.StopCaptureZapFrames()
            test_data = self.lib.get_test_params(self.config.sanity_wait_for_chkpt_params,self.config.wait_for_chkpt_params)

            iter = 0
            for key, value in test_data.items():
                self.logger.Log(" ----- Test Scenario - {} -----".format(value[0]))
                match_found = False
                start_time = 0
                end_time = 0

                api_executed = False
                if key == 3:
                    tapped = self.lib.tap_element(self.config.shows_view_all)
                    time.sleep(2)  # to show the all shows screen
                    if not tapped:
                        self.lib.report("Failed to tap", "FAILED", ss_required=True)
                        api_test_status = False
                        return api_test_status

                    tapped = self.lib.tap_element(self.config.filter_icon)
                    time.sleep(2)  # to show the filter options
                    if not tapped:
                        self.lib.report("Failed to tap", "FAILED", ss_required=True)
                        api_test_status = False
                        return api_test_status

                if (self.dut.validator.StartCaptureZapFrames(self.config.captureZapTime)):
                    start_time = self.lib.get_time_stamp()
                    match_found = self.dut.validator.WaitForCheckpoint(*value[2])
                    end_time = self.lib.get_time_stamp()
                    api_executed = True
                    self.dut.validator.StopCaptureZapFrames()
                else:
                    api_test_status = False
                    self.logger.Log("StartCaptureZapFrames API Failed. Hence, skipping WaitForCheckpoint API")
                    self.lib.report("API - StartCaptureZapFrames", "FAILED", ss_required=True)
                if value[1] == 1:
                    output_validated = True if match_found > 0 else False
                else:
                    output_validated = True if match_found == value[1] else False

                if api_executed and output_validated:
                    status = "PASSED"
                elif not api_executed:
                    status = "NOT RUN"
                    api_test_status = False
                else:
                    status = "FAILED"
                    api_test_status = False

                self.lib.report_api_status(start_time, end_time, "WaitForCheckpoint", status, ss_required = True)
                self.lib.report("WaitForCheckpoint: {}".format(value[0]), status)

                time.sleep(1)
                iter += 1

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
