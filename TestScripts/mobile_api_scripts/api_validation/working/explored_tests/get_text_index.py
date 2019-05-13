# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            :   Arathy P.S.
# Date              :   04-02-2019
# Script Version    :   1.0
# APIs covered      :   "GetText with index"
# Test Scenario     :   "Invalid: Index outside boundary"
#                       "Invalid: Non existing element"
#                       "Valid: Element without text"
#                       "Valid: Element with lengthy text"
#                       "Invalid: Negative value for index"
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

    apis = 'GetText with index'
    script_name = os.path.basename(__file__)

    def run_api_test(self):
        test_result = True
        test_params = self.config.get_text_index_params
        try:
            for value in test_params.keys():
                self.logger.Log("---------------- Scenario: {} -----------------".format(test_params[value][0]))
                element_params = test_params[value][-1]
                elm_type, type = self.lib.choose_elm_type(element_params[0])
                if not type:
                    self.logger.Error("Invalid element type")
                    return False
                start_time = self.lib.gettimestamp()
                get_text = self.dut.GetText(elm_type, element_params[0][type], element_params[1])
                end_time = self.lib.gettimestamp()
                if (value is 0 or 1 or 4) and (get_text == test_params[value][1]):
                    status = "PASSED"
                elif (value is 2 or 3) and (get_text != test_params[value][1]):
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False
                self.lib.report_api_status(start_time, end_time, "GetText with index", status, ss_required=True)
                self.lib.report("GetText with index: {}".format(test_params[value][0]), status)

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
