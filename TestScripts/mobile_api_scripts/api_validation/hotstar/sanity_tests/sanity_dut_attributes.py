# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :
# Script Version    :
# APIs covered      :   "AddCustomDUTAttribute", "GetCustomDUTAttribute", "ReadCustomProperty"
#                       "SetCustomDUTAttribute", "SetDUTAttribute", "GetDUTAttribute",
# Test Scenario     :
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import os
import sys
import datetime
sys.path.append('../')

from library.api_test_base import ApiTestBase


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class api_test(ApiTestBase):

    # the class which handles the script intention.
    # this overrides base class run_api_test()

    apis = ("AddCustomDUTAttribute", "GetCustomDUTAttribute", "ReadCustomProperty",
                      "SetCustomDUTAttribute", "SetDUTAttribute", "GetDUTAttribute",

          )
    script_name = os.path.basename(__file__)

    def custom_attribute(self):
        ret = True
        try:
            cur_time = datetime.datetime.now().strftime("%H_%M_%S")
            # cur_time = cur_time.replace(":", "_")

            start_time = self.lib.get_time_stamp()
            added = self.dut.AddCustomDUTAttribute("attr_" + cur_time)
            end_time = self.lib.get_time_stamp()
            if added:
                status = "PASSED"
            else:
                status = "FAILED"
                ret = False

            self.lib.report_api_status(start_time, end_time, "AddCustomDUTAttribute", status, ss_required=True)

            # if not added:  # and cus_att == "AddCustomDUTAttribute":
            #     return ret

            start_time = self.lib.get_time_stamp()
            set = self.dut.SetCustomDUTAttribute("attr_" + cur_time, cur_time)
            end_time = self.lib.get_time_stamp()
            if set:
                status = "PASSED"
            else:
                status = "FAILED"
                ret = False
            self.lib.report_api_status(start_time, end_time, "SetCustomDUTAttribute", status, ss_required=True)

            start_time = self.lib.get_time_stamp()
            cust_attr = self.dut.GetCustomDUTAttribute("attr_" + cur_time)
            end_time = self.lib.get_time_stamp()
            if cust_attr == cur_time:
                status = "PASSED"
            else:
                status = "FAILED"
                ret = False
            self.lib.report_api_status(start_time, end_time, "GetCustomDUTAttribute", status, ss_required=True)

            start_time = self.lib.get_time_stamp()
            cust_attr = self.dut.ReadCustomProperty("attr_" + cur_time)
            end_time = self.lib.get_time_stamp()
            if cust_attr == cur_time:
                status = "PASSED"
            else:
                status = "FAILED"
                ret = False
            self.lib.report_api_status(start_time, end_time, "ReadCustomProperty", status, ss_required=True)

        except Exception as e:
            self.logger.Error("Exception raised in custom_attribute() function : " + str(e))
            ret = False

        finally:
            return ret


    def dut_attribute(self):
        set = True
        try:
            start_time = self.lib.get_time_stamp()
            set = self.dut.SetDUTAttribute("manufacturer", "manufacturer")
            end_time = self.lib.get_time_stamp()
            if set:
                status = "PASSED"
            else:
                status = "FAILED"
                set = False
            self.lib.report_api_status(start_time, end_time, "SetDUTAttribute", status, ss_required=True)

            # if not set:  # and cus_att == "AddCustomDUTAttribute":
            #     return False

            start_time = self.lib.get_time_stamp()
            dut_attr = self.dut.GetDUTAttribute("manufacturer")
            end_time = self.lib.get_time_stamp()
            if dut_attr == "manufacturer":
                status = "PASSED"
            else:
                status = "FAILED"
                set = False
            self.lib.report_api_status(start_time, end_time, "GetDUTAttribute", status, ss_required=True)

        except Exception as e:
            self.logger.Log("Exception from dut_attribute() " + str(e))
            set = False

        finally:
            return set


    def run_api_test(self):
        '''
        Executes the test script

        :return:
        '''

        api_test_status = True

        try:
            if not self.custom_attribute():
                self.lib.report("Failed to configure Custom Attributes", "FAILED", image_required=False)
                api_test_status = False

            if not self.dut_attribute():
                self.lib.report("Failed to configure DUT Attributes", "FAILED", image_required=False)
                api_test_status = False

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
