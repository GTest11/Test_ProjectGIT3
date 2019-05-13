# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author              : Lincy Robert
# Date                : 28-01-2019
# Script Version      : 1.0
# Modification details:
# APIs covered        : "GetAdbAPIVersion", "GetAdbVersion", "GetApkVersion", "GetDeviceHeight", "GetDeviceWidth"
#In Android : Verify if the device attributes retrieved using API matches with the value in config file
#In iOS: Verify if No exception is raised on API invocation and empty string is received as output
#
# '''''''''''''''''''''''''''TEST CASE DETAILS' - END '''''''''''''''''''''''''''''''''

import os
import sys
sys.path.append('../')

from library.api_test_base import apiTestBase


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class api_test(apiTestBase):

    # the class which handles the script intention.
    # this overrides base class run_api_test()

    apis = ("GetAdbAPIVersion", "GetAdbVersion",
              "GetApkVersion", "GetDeviceHeight", "GetDeviceWidth",)
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        '''
        Executes the test script

        :return:
        '''

        api_test_status = True
        dut_mob_name = self.lib.get_dut_name() # Read the name of the mobile DUT

        try:

            api_dict = {
                "GetAdbAPIVersion": self.dut.GetAdbAPIVersion,
                "GetAdbVersion": self.dut.GetAdbVersion,
                "GetApkVersion": self.dut.GetApkVersion,
                "GetDeviceHeight": self.dut.GetDeviceHeight,
                "GetDeviceWidth": self.dut.GetDeviceWidth,
            }

            dict_mob = None
            if dut_mob_name in self.config.dict_dut_name:
                dict_mob = self.config.dict_dut_name[dut_mob_name]

            if not dict_mob:
                self.logger.Error("Config does not have dict for current dut")
                api_test_status = False
                return

            for api in self.apis:
                start_time = self.lib.gettimestamp()
                api_result = api_dict[api]()
                end_time = self.lib.gettimestamp()
                self.logger.Log("API: {} returned {}".format(api, api_result))
                if api_result == dict_mob[api]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    api_test_status = False

                self.lib.report_api_status(start_time, end_time, api, status, ss_required=True)

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
