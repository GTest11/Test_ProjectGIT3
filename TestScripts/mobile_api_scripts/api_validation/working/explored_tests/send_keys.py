# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            :   Arathy P.S.
# Date              :   06-02-2019
# Script Version    :   1.0
# APIs covered      :   "SendKeys"
# Test Scenario     :   Valid: send to edit box
#                         Valid: Send lengthy string
#                         Valid: Send spl chars & nums
#                         Invalid: Send to non-text field
#
# '''''''''''''''''''''''''''TEST CASE DETAILS' - END '''''''''''''''''''''''''''''''''

try:
    import os
    import sys
    import re
    sys.path.append('../')
    from library.api_test_base import apiTestBase
except Exception as e:
    print ("Exception in Import " + str(e))
    sys.exit()


class api_test(apiTestBase):
    # the class which handles the script intention.
    # this overrides base class run_api_test()

    apis = 'SendKeys'
    script_name = os.path.basename(__file__)

    def run_api_test(self):
        test_result = True
        test_params = self.config.send_keys_params
        try:
            clicked = self.lib.element_ops(self.config.search_icon, index=None, action='click')
            if not clicked:
                self.lib.report("Failed to click on search icon", "FAILED", ss_required=True)
                test_result = False
                return False

            for value in test_params.keys():
                self.logger.Log("---------------- Scenario: {} -----------------".format(test_params[value][0]))
                elm_type, e_type = self.lib.choose_elm_type(test_params[value][2])
                if not e_type:
                    self.logger.Error("Invalid element type")
                    test_result = False
                    continue

                start_time = self.lib.gettimestamp()
                send_keys = self.dut.SendKeys(elm_type, test_params[value][2][e_type], test_params[value][3])
                end_time = self.lib.gettimestamp()
                if send_keys == test_params[value][1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False
                self.lib.report_api_status(start_time, end_time, "SendKeys", status, ss_required=True)
                self.lib.report("SendKeys: {}".format(test_params[value][0]), status, ss_required=False)

                if not self.lib.launch_app():
                    self.lib.report("Failed to relaunch the application", "FAILED", ss_required=True)
                    test_result = False
                    continue

        except Exception as ex:
            self.logger.Error("Error in run_api_test() " + str(ex))
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
