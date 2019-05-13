# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :  04-Jan-2019
# Script Version    :   1.0
# APIs covered      : 'CacheImageFromUrl'
# Test Scenario     :  Saves an image from the given url once the application has opened
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import os
import sys
import time
sys.path.append('../')

from library.api_test_base import ApiTestBase

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class api_test(ApiTestBase):

    # the class which handles the script intention.
    # this overrides base class run_api_test()

    apis = ('CacheImageFromUrl',
         )
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        '''
        Executes the test script

        :return:
        '''

        api_test_status = True
        test_data = self.lib.get_test_params(
            self.config.sanity_cache_image_from_url_params,
            self.config.cache_image_from_url_params
        )
        try:
            for data in test_data:
                self.logger.Log(" ----- Test Scenario - {} -----".format(test_data[data][0]))
                start_time = self.lib.get_time_stamp()
                cached = self.dut.validator.CacheImageFromUrl(test_data[data][1], test_data[data][2])
                end_time = self.lib.get_time_stamp()
                if cached == test_data[data][-1]:  # value[-1] = True
                    status = "PASSED"
                else:
                    status = "FAILED"
                    api_test_status = False

                self.lib.report_api_status(start_time, end_time, "CacheImageFromUrl", status, ss_required=True)

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
