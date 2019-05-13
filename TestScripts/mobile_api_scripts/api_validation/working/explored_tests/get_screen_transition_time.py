# '''''''''''''''''''''''''''TEST CASE DETAILS''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author                :   Arathy P S
# Date                  :   26-11-2018
# Script Version        :   1.0
# Modification details  :
# APIs covered          :   "GetScreenTransitionTime"
# Test Scenario         :   "chkpt_screen": "Valid parameters, No screen transition from the checkpoint screen"
#                           "not_on_chkpt_screen": "Valid parameters, not on checkpoint screen"
#                           "move_out_chkpt_screen": "Valid parameters, screen transition from the checkpoint screen"
#                           "Invalid parameters, Non existing checkpoint"
#                           "Invalid parameters, large timeToWait & initial delay"
#                           "Invalid parameters, initial delay greater than time out"
#                           "Invalid parameters, negative timeToWait"
# '''''''''''''''''''''''''''TEST CASE DETAILS' - END ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

try:
    import os
    import sys
    sys.path.append('../')
    from library.api_test_base import apiTestBase
except Exception as e:
    print ("Exception in Import " + str(e))
    sys.exit()


class api_test(apiTestBase):
    # the class which handles the script intention.
    # this overrides base class run_api_test()
    # class variables
    apis = ("GetScreenTransitionTime'",)
    script_name = os.path.basename(__file__)

    def run_api_test(self):
        test_result = True
        try:
            test_params = self.config.get_screen_transition_time_params
            for key, value in test_params.items():
                self.logger.Log(" ----- Test Scenario - {} -----".format(value[0]))
                self.dut.validator.StopCaptureZapFrames()
                if self.dut.validator.StartCaptureZapFrames(30):
                    start_time = self.lib.gettimestamp()
                    api_status = self.dut.validator.GetScreenTransitionTime(*value[2])
                    self.logger.Log("Output value obtained for GetScreenTransitionTime API : "+str(api_status))
                    end_time = self.lib.gettimestamp()
                    self.dut.validator.StopCaptureZapFrames()
                    if (key is 0 or 1 or 2 or 3) and api_status == value[1]:
                        status = "PASSED"
                    elif api_status > value[1]:
                        status = "PASSED"
                    else:
                        status = "FAILED"
                        test_result = False
                    self.lib.report_api_status(start_time, end_time, "GetScreenTransitionTime", status, ss_required=True)
                    self.lib.report("GetScreenTransitionTime: {}".format(value[0]), status)
                else:
                    test_result = False
                    self.logger.Log("StartCaptureZapFrames API Failed. Hence, skipping GetScreenTransitionTime API")
                    self.lib.report("API - StartCaptureZapFrames", "FAILED", ss_required=True)
                    self.lib.report("API - GetScreenTransitionTime", "NOT RUN", ss_required=False)
            self.logger.Log(" ----- Test Scenario - API call without Capturing Frames -----")
            start_time = self.lib.gettimestamp()
            neg_status = self.dut.validator.GetScreenTransitionTime(self.config.chkpt_screen_elm, self.config.T_MD_WAIT,
                                                                    self.config.INITIAL_DELAY)
            end_time = self.lib.gettimestamp()
            if neg_status != -1:
                status = "FAILED"
                test_result = False
            else:
                status = "PASSED"
            self.lib.report_api_status(start_time, end_time, "GetScreenTransitionTime", status, ss_required=True)
            self.lib.report("GetScreenTransitionTime: Scenario - API call without Capturing Frames", status)
        except Exception as run_e:
            self.logger.Error("Exception in run_api_test " + str(run_e))
            test_result = False
        finally:
            self.test_result = test_result


def main():
    try:
        test_obj = api_test()
        test_obj.run_test(test_obj.script_name, test_obj.apis)
    except Exception as e:
        print "Exception from main function" + str(e)

if __name__ == '__main__':
    main()
