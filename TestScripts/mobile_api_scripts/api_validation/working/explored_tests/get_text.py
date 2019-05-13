# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :   Arathy P.S.
# Date              :   04-02-2019
# Script Version    :   1.0
# APIs covered      :   "GetText"
# Test Scenario     :   "Element without text"
#                       "Non existing element"
#                       "Element with lengthy text"
#                       "Two elements with same Id but differs in index"
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

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
    apis = "GetText"
    script_name = os.path.basename(__file__)

    def run_api_test(self):
        test_result = True
        test_params = self.config.get_text_params
        try:
            for value in test_params.keys():
                self.logger.Log("---------------- Scenario: {} -----------------".format(test_params[value][0]))

                elm_type, e_type = self.lib.choose_elm_type(test_params[value][-1])
                if not e_type:
                    self.logger.Error("Invalid element type")
                    return False

                start_time = self.lib.gettimestamp()
                get_text = self.dut.GetText(elm_type, test_params[value][-1][e_type])
                end_time = self.lib.gettimestamp()
                if (value is 0 or 1) and (get_text == test_params[value][1]):
                    status = "PASSED"
                elif (value is 2 or 3) and (get_text != test_params[value][1]):
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False
                self.lib.report_api_status(start_time, end_time, "GetText", status, ss_required=True)
                self.lib.report("GetText: {}".format(test_params[value][0]), status)
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