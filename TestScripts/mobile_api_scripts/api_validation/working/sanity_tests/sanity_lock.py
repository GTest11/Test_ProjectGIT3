# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :   Rohith P V
# Date              :   05-10-2018
# Script Version    :   1.1
# Modification details: Fixed review comments, date 17/10/2018
# APIs covered      :   Lock, Unlock
# Test Scenario     :   Launches youtube application -> Lock API executed -> Unlock API executed
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, os, time
sys.path.append('../')
from library.api_test_base import apiTestBase
#''''''''''''''''''''''''''''''END IMPORTS''''''''''''''''''''''''''''''''

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class api_test(apiTestBase):

    # the class which handles the script intention.
    # this overrides base class run_api_test()

    apis = ("Lock", "Unlock")

    script_name = os.path.basename(__file__)
    

    def run_api_test(self):
        '''
        Executes the test script

        :return:
        '''

        api_test_status = True
        status = "PASSED"

        try:
            api = "Lock/Unlock"
            
            # getting platform details
            cur_dev_platform = self.lib.get_dut_platform()
            self.logger.Log("DUT Platform :- " +str(cur_dev_platform))
            if not self.dut.CloseApp():
                api_test_status = False
                self.logger.Error("CloseApp API failed. Hence, skipping test execution")
                self.lib.report("CloseApp API", "FAILED", ss_required=True)
            else:
                w, h = self.lib.get_image_resolution()
                self.logger.Log("w - {}, h - {}".format(w, h))
                ref_img_path = self.dut.validator.CaptureImage(0, 0, w, h, "ref_img", 90, 0)
                start_time = self.lib.gettimestamp()
                self.dut.Lock()
                end_time = self.lib.gettimestamp()
                try:
                    self.dut.validator.QuickCapture("locked_image")
                except Exception as e:
                    self.logger.Log("Could not capture image, trying to get screenshot")
                    self.lib.upload_ss()

                self.lib.report_api_status(start_time, end_time, "Lock", "", ss_required=False)

                if cur_dev_platform == "iOS":
                    self.logger.Log("*** UNLOCK () API IS AVAILABLE ONLY FOR ANDROID DEVICES ***\n *** Phone will unlock automatically after 10 sec ***")
                    # Introducing a delay as iOS devices will automatically unlock after 10 sec
                    time.sleep(15)
                else:
                    time.sleep(5)
                    start_time = self.lib.gettimestamp()
                    self.dut.Unlock()
                    end_time = self.lib.gettimestamp()
                    self.dut.validator.QuickCapture("unlocked_image")
                    self.lib.report_api_status(start_time, end_time, "Unlock", "", ss_required=False)
                    # Introducing a delay for device to unlock
                    time.sleep(5)
                test_img_path = self.dut.validator.CaptureImage(0, 0, w, h, "test_img", 90, 0)
                matched = self.dut.validator.ImageMatch("ref_img", "test_img", 2, "13")
                if matched:
                    api_test_status = True
                    status = "PASSED"
                else:
                    api_test_status = False
                    status = "FAILED"
               
                self.lib.report("API {} ".format(api), status, ss_required=True)

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
