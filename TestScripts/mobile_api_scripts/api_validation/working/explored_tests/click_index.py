# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            :   Arathy P.S.
# Date              :   04-02-2019
# Script Version    :   1.0
# APIs covered      :   "Click with index"
# Test Scenario     :   1. Invalid: Index outside boundary
#                       2. Invalid: on a non click-able element
#                       3. Valid: on a click-able element
#                       4. Invalid: Invalid element value
#                       5. Invalid: Invalid index values
#                       6. Invalid: on an element with visible property False, but available on the screen
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

    apis = ("Click with index",)
    script_name = os.path.basename(__file__)

    def run_api_test(self):
        test_result = True
        test_params = self.config.click_index_params
        try:
            for value in test_params.keys():
                self.logger.Log("---------------- Scenario: {} -----------------".format(test_params[value][0]))
                element_params = test_params[value][-1]
                elm_type, type = self.lib.choose_elm_type(element_params[0])
                if not type:
                    self.logger.Error("Invalid element type")
                    test_result = False
                    return False

                start_time = self.lib.gettimestamp()
                clicked = self.dut.Click(elm_type, element_params[0][type], element_params[1])
                end_time = self.lib.gettimestamp()
                if clicked == test_params[value][1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False
                self.lib.report_api_status(start_time, end_time, "Click with index", status, ss_required=True)
                self.lib.report("Click with index: {}".format(test_params[value][0]), status)

        except Exception as run_e:
            self.logger.Error("Error in run_api_test() " + str(run_e))
            test_result = False
        finally:
            self.test_result = test_result


def main():
    try:
        test_obj = api_test()
        test_obj.run_test(test_obj.script_name, test_obj.apis)
    except Exception as m_e:
        print "Exception from main function" + str(m_e)

if __name__ == '__main__':
    main()
