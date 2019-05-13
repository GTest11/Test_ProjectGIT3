# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :
# Date              :   01-10-2018
# Script Version    :   1.1
# APIs covered      :   "WaitCheckPointMatch", "init"
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, os, time
sys.path.append('../')
from library.api_test_base import apiTestBase
#''''''''''''''''''''''''''''''END IMPORTS''''''''''''''''''''''''''''''''

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class api_test(apiTestBase):

    # the class which handles the script intention.
    # this overrides base class run_api_test()

    apis = ("WaitCheckPointMatch", "init")

    script_name = os.path.basename(__file__)
    

    def run_api_test(self):
        '''
        Executes the test script

        :return:
        '''

        api_test_status = True

        try:
            test_data = self.lib.get_test_params(self.config.sanity_wait_chkpt_match_params,self.config.wait_chkpt_match_params)

            if not test_data:
                self.lib.report("Could not populate the test data params", "FAILED")
                api_test_status = False
                return api_test_status

            for key, value in test_data.items():

                self.logger.Log(" ----- Test Scenario - {} -----".format(value[0]))
                init_time1 = self.lib.gettimestamp()
                self.chkpt.init(value[2])
                init_time2 = self.lib.gettimestamp()

                time.sleep(3)
                start_time = self.lib.gettimestamp()
                validated = self.dut.validator.WaitCheckPointMatch(self.chkpt, value[3], value[4])
                end_time = self.lib.gettimestamp()
                # we use this double comparison for including negative scenarios as well
                if validated == value[1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    api_test_status = False
                
                self.lib.report_api_status(init_time1, init_time2, "init", "", ss_required = False)
                self.lib.report_api_status(start_time, end_time, "WaitCheckPointMatch", status, ss_required = True)

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
