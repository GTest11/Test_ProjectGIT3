# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author                :   Arathy P S
# Date                  :   01-02-2019
# Script Version        :   1.0
# Modification details  :
# APIs covered          :   "DetectMotion"
# Test Scenario         :
# '''''''''''''''''''''''''''TEST CASE DETAILS' - END '''''''''''''''''''''''''''''''''

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

    apis = 'DetectMotion'
    script_name = os.path.basename(__file__)

    def run_api_test(self):
        '''
        :return:
        '''

        test_result = True
        test_params = self.config.detect_motion_params
        w, h = self.lib.get_image_resolution()

        try:
            if not self.dut.Tap(*self.config.C_TAP_PLAYBACK):
                self.lib.report("Failed to start playback", "FAILED", ss_required=True)
                test_result = False

            for key, value in test_params.items():
                self.logger.Log(" ----- Test Scenario - {} -----".format(value[0]))
                param_lst = list(test_params[6][2])
                param_lst[2], param_lst[3] = w, h
                test_params[6][2] = tuple(param_lst)
                start_time = self.lib.gettimestamp()
                api_status = self.dut.validator.DetectMotion(*value[2])
                end_time = self.lib.gettimestamp()
                if api_status == value[1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False
                self.lib.report_api_status(start_time, end_time, "DetectMotion", status, ss_required=True)
                self.lib.report("DetectMotion: {}".format(value[0]), status, ss_required=False)

            self.logger.Log(" --------- Test Scenario - DetectMotion on Static screen ----------------")
            self.dut.CloseApp()

            start_time = self.lib.gettimestamp()
            api_status = self.dut.validator.DetectMotion(*self.config.detect_motion_check)
            end_time = self.lib.gettimestamp()
            if api_status:
                status = "FAILED"
                test_result = False
            else:
                status = "PASSED"
            self.lib.report_api_status(start_time, end_time, "DetectMotion", status, ss_required=True)
            self.lib.report("DetectMotion: DetectMotion on Static screen", status, ss_required=False)

        except Exception as run_e:
            test_result = False
            self.logger.Error("Exception in run_api_test " + str(run_e))

        finally:
            self.test_result = test_result


def main():
    try:
        test_obj = api_test()
        test_obj.run_test(test_obj.script_name, test_obj.apis)

    except Exception as ex:
        print "Exception from main function" + str(ex)

if __name__ == '__main__':
    main()
