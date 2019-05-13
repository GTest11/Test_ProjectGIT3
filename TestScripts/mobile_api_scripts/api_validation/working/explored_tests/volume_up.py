# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author                :   Arathy P S
# Date                  :   01-02-2019
# Script Version        :   1.0
# Modification details  :
# APIs covered          :   "VolumeUp"
# Test Scenario         :   "Valid: maximum volume"
#                           "Invalid: volume up when max volume"
#                           "Invalid: numberOfLevels boundary - min"
#                           "Invalid: numberOfLevels boundary - max"
#                           "Invalid: numberOfLevels negative value"
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
    apis = 'VolumeUp'
    script_name = os.path.basename(__file__)

    def run_api_test(self):
        test_result = True
        test_params = self.config.volume_up_params
        try:
            if self.lib.get_dut_platform() == "iOS":
                self.lib.report("iOS does not support this API", "FAILED", ss_required=False)
                test_result = False
                return test_result
            for key, value in test_params.items():
                self.logger.Log(" ----- Test Scenario - {} -----".format(value[0]))
                start_time = self.lib.gettimestamp()
                up_status = self.dut.VolumeUp(value[1])
                end_time = self.lib.gettimestamp()
                if up_status == value[2]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False
                self.lib.report_api_status(start_time, end_time, "VolumeUp", status, ss_required=True)
                self.lib.report("VolumeUp: {}".format(value[0]), status)
            self.logger.Log(" ----- Test Scenario - volume up during media playback")
            self.dut.Tap(self.config.C_TAP_PLAYBACK[0], self.config.C_TAP_PLAYBACK[1])
            start_time = self.lib.gettimestamp()
            up_status = self.dut.VolumeUp(self.config.volume_levels)
            end_time = self.lib.gettimestamp()
            if up_status:
                status = "PASSED"
            else:
                status = "FAILED"
                test_result = False
            self.lib.report_api_status(start_time, end_time, "VolumeUp", status, ss_required=True)
            self.lib.report("VolumeUp: During media playback", status)
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
