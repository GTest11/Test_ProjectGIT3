# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author                :   Arathy P S
# Date                  :   04-02-2019
# Script Version        :   1.0
# Modification details  :
# APIs covered          :   "validateCheckPoint"
# Test Scenario         :   "Valid parameter, OCR checkpoint",
#                           "Valid parameter, Multi line OCR checkpoint",
#                           "Valid parameter, IC checkpoint, pixel",
#                           "Valid parameter, IC checkpoint, rmse",
#                           "Valid parameter, Checkpoint created for parent DUT",
#                           "Valid parameter, OCR checkpoint with multiple filters",
#                           "Valid parameter, lengthy name for checkpoint",
#                           "Invalid scenario, checkpoint not created for target device"
# '''''''''''''''''''''''''''TEST CASE DETAILS' - END '''''''''''''''''''''''''''''''''

try:
    import os
    import sys
    import time
    sys.path.append('../')
    from library.api_test_base import apiTestBase
except Exception as e:
    print ("Exception in Import " + str(e))
    sys.exit()


class api_test(apiTestBase):
    # the class which handles the script intention.
    # this overrides base class run_api_test()
    # class variables
    apis = 'validateCheckPoint'
    script_name = os.path.basename(__file__)

    def run_api_test(self):
        test_result = True
        test_params = self.config.validate_chkpt_params
        chkpt1 = self.mob_lib.CheckPoint()
        try:
            for key, value in test_params.items():
                self.logger.Log(" ----- Test Scenario - {} -----".format(value[0]))
                if key != 0:
                    self.chkpt.init(value[2])
                if key == 8:
                    tapped = self.lib.tap_element(self.config.account_icon)
                    time.sleep(1)  # to show the accounts screen
                    if not tapped:
                        self.lib.report("Failed to tap", "FAILED", ss_required=True)
                        api_test_status = False
                        return api_test_status

                start_time = self.lib.gettimestamp()
                match_found = self.dut.validator.validateCheckPoint(self.chkpt)
                end_time = self.lib.gettimestamp()
                if match_found == value[1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False
                self.lib.report_api_status(start_time, end_time, "ValidateCheckpoint", status, ss_required=True)
                self.lib.report("ValidateCheckpoint: {}".format(value[0]), status)

        except Exception as run_e:
            self.logger.Error("Exception in run_api_test " + str(run_e))
            test_result = False
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
