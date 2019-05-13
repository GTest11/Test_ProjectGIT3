# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase Name     :   WaitImageMatch.py
# Author            :
# Date              :   22-April-2019
# Script Version    :   1.0
# APIs covered      :   WaitImageMatch, CaptureImage
# Test Scenario     :   Launch the app, capture an image using params in the config.
#                       Compare this image at run time using WaitImageMatch API and update the status
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


import sys, os, time
sys.path.append('../')
from library.api_test_base import ApiTestBase
#''''''''''''''''''''''''''''''END IMPORTS''''''''''''''''''''''''''''''''

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class api_test(ApiTestBase):

    # the class which handles the script intention.
    # this overrides base class run_api_test()

    apis = ("WaitImageMatch", "CaptureImage")

    script_name = os.path.basename(__file__)
    

    def run_api_test(self):
        '''
        Executes the test script

        :return:
        '''

        api_test_status = True
        test_data = self.lib.get_test_params(
            self.config.sanity_wait_image_match_params,
            self.config.wait_image_match_params
        )

        try:

            capture_time1 = self.lib.get_time_stamp()
            if not self.dut.validator.CaptureImage(
                    self.config.C_WAIT_IMG_MATCH[0],
                    self.config.C_WAIT_IMG_MATCH[1],
                    self.config.C_WAIT_IMG_MATCH[2],
                    self.config.C_WAIT_IMG_MATCH[3],
                    self.config.img_wait_im_match,
                    self.config.CAP_IMG_DEFAULT_QUALITY,
                    2
            ):
                self.logger.Log("CaptureImage API Failed. Hence, skipping WaitImageMatch API")
            else:
                capture_time2 = self.lib.get_time_stamp()
                self.lib.report_api_status(capture_time1, capture_time2, "CaptureImage", "PASSED",
                                           ss_required=True)

                for key, value in test_data.items():
                    self.logger.Log(" ----- Test Scenario - {} -----".format(value[0]))
                    param_list = value[2]
                    if key == 2:
                        w, h = self.lib.get_image_resolution()
                        param_list = [w if param=="max_width" else param for param in param_list]
                        param_list = [h if param=="max_height" else param for param in param_list]
                    start_time = self.lib.get_time_stamp()
                    match_found = self.dut.validator.WaitImageMatch(*param_list)
                    end_time = self.lib.get_time_stamp()
                    self.logger.Log("Match detected - {}".format(match_found))

                    if match_found == value[1]:
                        status = "PASSED"
                    else:
                        api_test_status = False
                        status = "FAILED"
                    self.lib.report_api_status(start_time, end_time, "WaitImageMatch", status, ss_required = True)

            
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
