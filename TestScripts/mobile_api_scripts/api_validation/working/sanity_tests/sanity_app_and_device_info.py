# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :
#Script Version     : 1.1
# APIs covered      :   "GetAdbAPIVersion", "GetAdbVersion",
#                       "GetApkVersion", "GetDeviceHeight", "GetDeviceWidth",
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
              "GetApkVersion", "GetDeviceHeight", "GetDeviceWidth",
         )
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        '''
        Executes the test script

        :return:
        '''

        api_test_status = True
        dict_out = {}
        dut_mob_name = self.lib.get_dut_name() # Read the name of the mobile DUT
        status = "FAILED"

        try:

            and_apis_call = {
                "GetAdbAPIVersion": self.dut.GetAdbAPIVersion,
                "GetAdbVersion": self.dut.GetAdbVersion,
                "GetApkVersion": self.dut.GetApkVersion,
            }

            apis_call = {
                # "GetAdbAPIVersion": lib.dut.GetAdbAPIVersion,
                # "GetAdbVersion": lib.dut.GetAdbVersion,
                # "GetApkVersion": lib.dut.GetApkVersion,
                "GetDeviceHeight" : self.dut.GetDeviceHeight,
                "GetDeviceWidth" : self.dut.GetDeviceWidth,
            }
            # getting platform
            cur_dev_platform = self.lib.get_dut_platform()
            self.logger.Log("cur_dev_platform - " +str(cur_dev_platform))
            api_dict = apis_call.copy()
            if cur_dev_platform == "Android":
                api_dict.update(and_apis_call)

            dict_mob = None
            if dut_mob_name in self.config.dict_dut_name:
                dict_mob = self.config.dict_dut_name[dut_mob_name]

            if not dict_mob:
                self.logger.Error("Config does not have dict for current dut")
                api_test_status = False
                return

            self.logger.Log("dict_mob {}".format(dict_mob))

            for api in self.apis:
                if api in api_dict:
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

                else:
                    self.logger.Log("API {} not available for this platform".format(api))

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
