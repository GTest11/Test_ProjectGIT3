# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :   Rohith P V
# Date              :   05-10-2018
# Script Version    :   1.1
# Modification details: Fixed review comments, date 17/10/2018
# APIs covered      :   Logger APIs, CommitStepResult, CommitTestResult, GetServerTimeStamp, ReadProperty
# Test Scenario     :   Launches youtube application -> WaitForElement API executed and validates the app launch -> Unlock API executed
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import sys, os, time
import datetime

#importing user defined functions
sys.path.append('../')


from library.api_test_base import apiTestBase


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class api_test(apiTestBase):

    # the class which handles the script intention.
    # this overrides base class run_api_test()

    apis = ("WaitForElement", "Error", "Log", "Warn", "GetServerTimeStamp", "CommitStepResult",
                      "CommitTestResult", "ReadProperty")
    script_name = os.path.basename(__file__)
    

    def commit(self, api):
        '''
        Calls CommitTestResult, CommitStepResult apis
        :param api: CommitTestResult or CommitStepResult
        :return:
        '''
        ret_val = False
        rep_status = "FAILED"
        try:
            api_status = self.config.commit_apis_valid_status
            stepname = self.config.VALID_STEP_NAME + " "
            no = 0
            for status in api_status:
                if api == "CommitStepResult":
                    no += 1
                    self.dut.CommitStepResult(self.config.VALID_STEP_NAME + str(no), status)
                else:
                    self.dut.CommitTestResult(status)
            ret_val = True
            rep_status = "PASSED"

        except Exception as e:
            self.logger.Log("Failed: CommitStepResult with valid params")
            ret_val = False
        finally:
            self.lib.report(api, rep_status, ss_required=False)
            return ret_val


    def run_api_test(self):
        '''
        Executes the test script

        :return:
        '''

        test_status = True
        status = "FAILED"

        try:
            read_property_api_status = self.validate_read_property()
            logger_apis_status = self.test_api()
            test_status =  logger_apis_status and read_property_api_status #wait_for_elem_api_status and read_property_api_status and logger_apis_status

        except Exception as e:
            self.logger.Error("Exception raised in main function : " + str(e))
            test_status = False

        finally:
            self.test_result = test_status


    def test_api(self):
        api_test_status = True
        status = "PASSED"
        try:

            apis = ("Error", "Log",
                    "Warn", "GetServerTimeStamp", "CommitTestResult", "CommitStepResult"
                  )

            apis_call = {
                "Error": self.logger.Error,
                "Log": self.logger.Log,
                "Warn": self.logger.Warn,
                "GetServerTimeStamp" : self.dut.validator.GetServerTimeStamp,
                "CommitTestResult": self.commit,
                "CommitStepResult": self.commit,
            }

            # api parameters
            api_val = {
                "Error" : ("ERROR MESSAGE"),
                "Log" : ("INFO MESSAGE"),
                "Warn" : ("WARNING MESSAGE"),
                "GetServerTimeStamp" : (),
                "CommitTestResult" : ("CommitTestResult"),
                "CommitStepResult": ("CommitStepResult"),
            }

            for api in apis:
                try:
                    start_time = self.lib.gettimestamp()
                    if api_val[api]:
                        apis_call[api](api_val[api])
                    else:
                        apis_call[api]()
                    end_time = self.lib.gettimestamp()
                    status = "PASSED"
                except Exception as e:
                    status = "FAILED"
                    api_test_status = False
                    self.logger.Error("Exception during {} call".format(api))
                finally:
                    self.lib.report_api_status(start_time, end_time, api, status, ss_required=False)

        except Exception as e:
            self.logger.Error("Exception raised in test_api function : " + str(e))
            api_test_status = False

        finally:
            return api_test_status


    def validate_read_property(self):
        property = False
        try:
            property_value = self.dut.GetDUTAttribute("platformname")
            start_time = self.lib.gettimestamp()
            read_property_out = self.dut.ReadProperty(3)
            end_time = self.lib.gettimestamp()
            if property_value == read_property_out:
                property = True
                status = "PASSED"
            else:
                status = "FAILED"
            self.lib.report_api_status(start_time, end_time, "ReadProperty", status, ss_required=False)

        except Exception as e:
            self.logger.Log("Exception in validate_read_property() - {}".format(e))
            property = False
        finally:
            return property


def main():
    testobj = api_test()
    testobj.run_test(testobj.script_name, testobj.apis)


if __name__ == '__main__':
    main()
