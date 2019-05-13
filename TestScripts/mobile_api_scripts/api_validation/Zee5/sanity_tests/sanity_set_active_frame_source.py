# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :   22-April-2019
# Script Version    :   1.0
# APIs covered      :   "SetActiveFrameSource", "GetScreenshot", "UploadScreenshot"
#                       "QuickCapture", "QuickCaptureEx"
# Test Scenario     :   Launches the application -> Change the active framesource using SetActiveFrameSource API -> Validate the framesource change
#                        by the images taken using GetScreenshot -> UploadScreenshot -> QuickCapture -> QuickCaptureEx APIs
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


import sys, os, time

#importing user defined functions
sys.path.append('../')

from library.api_test_base import ApiTestBase


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class api_test(ApiTestBase):

    # the class which handles the script intention.
    # this overrides base class run_api_test()

    apis = ("SetActiveFrameSource", "GetScreenshot", "UploadScreenshot",
                       "QuickCapture", "QuickCaptureEx")
    script_name = os.path.basename(__file__)
    

    def run_api_test(self):
        '''
        Executes the test script

        :return:
        '''

        api_test_status = False
        try:
            apis_to_test = ["GetScreenshot","QuickCapture","QuickCaptureEx"]
            sources = self.config.video_sources  # ["f3b91a95", "21435", "aa455"]
            api_failed = False

            ret_screenshot = False
            ret_QuickCaptureEx = False
            ret_QuickCapture = False
            for source in sources:
                status = "FAILED"
                self.logger.Log("*** Video Source changing to {} ***".format(source))
                start_time = self.lib.get_time_stamp()
                if self.dut.validator.SetActiveFrameSource(source):
                    end_time = self.lib.get_time_stamp()
                    status = "PASSED"
                    self.lib.report_api_status(start_time, end_time, "SetActiveFrameSource", status, ss_required = True)
                    time.sleep(2)
                    for api in apis_to_test:
                        if (api == "GetScreenshot"):
                            ret_screenshot = self.screenshot()
                            if not ret_screenshot:
                                api_failed = True
                        elif (api == "QuickCaptureEx"):
                            ret_QuickCaptureEx = self.QuickCapture_Ex()
                            if not ret_QuickCaptureEx:
                                api_failed = True
                        else:
                            ret_QuickCapture = self.Quick_Capture()
                            if not ret_QuickCapture:
                                api_failed = True
                else:
                    end_time = self.lib.get_time_stamp()
                    self.lib.report_api_status(start_time, end_time, "SetActiveFrameSource", status, ss_required = True)

            if ret_screenshot and ret_QuickCaptureEx and ret_QuickCapture and not api_failed:
                api_test_status = True

        except Exception as e:
            self.logger.Error("Exception raised in test_api function : " + str(e))
            api_test_status = False
        finally:
            self.test_result = api_test_status


    def screenshot(self):
        '''
        Tests the GetScreenshot and UploadScreenshot APIs and logs its response (status, duration)
        :return: True or False
        '''

        api_test_status = False
        ret_get = ret_upload = False
        try:
            status_Get = "FAILED"
            start_time = self.lib.get_time_stamp()
            img = self.dut.GetScreenshot()
            end_time = self.lib.get_time_stamp()
            if img:
                status_Get = "PASSED"
                ret_get = True

            self.lib.report_api_status(start_time, end_time, "GetScreenshot", status_Get, ss_required = True)

            status_Upload = "FAILED"
            start_time = self.lib.get_time_stamp()
            ret = self.dut.validator.UploadScreenshot("test", img)
            end_time = self.lib.get_time_stamp()
            
            if ret:
                status_Upload = "PASSED"
                ret_upload = True

            self.lib.report_api_status(start_time, end_time, "UploadScreenshot", status_Upload, ss_required = True)

            if ret_get & ret_upload:
                api_test_status = True

        except Exception as e:
            self.logger.Error("Exception raised in screenshot function : " + str(e))
            api_test_status = False

        finally:
            return api_test_status


    def QuickCapture_Ex(self):
        '''
        Tests the QuickCaptureEx API for different image formats and logs its response (status, duration)
        :return: True or False
        '''

        api_test_status = False
        try:
            status = "PASSED"
            formats = {"jpg", "png", "jpeg", "bmp"}
            for fmt in formats:
                start_time = self.lib.get_time_stamp()
                path = self.dut.validator.QuickCaptureEx("test_{}_image".format(fmt), fmt)
                if not path:
                    status = "FAILED"
                end_time = self.lib.get_time_stamp()

                self.lib.report_api_status(start_time, end_time, "QuickCaptureEx - {} format".format(fmt), status, ss_required = True)

            if status == "PASSED":
                api_test_status = True

        except Exception as e:
            self.logger.Error("Exception raised in QuickCapture_Ex function : " + str(e))
            api_test_status = False

        finally:
            return api_test_status


    def Quick_Capture(self):
        '''
        Tests the QuickCapture API and logs its response (status, duration)
        :return: True or False
        '''

        api_test_status = False
        try:
            status = "FAILED"
            start_time = self.lib.get_time_stamp()
            path = self.dut.validator.QuickCapture("img")
            end_time = self.lib.get_time_stamp()
            if path:
                status = "PASSED"
                api_test_status = True

            self.lib.report_api_status(start_time, end_time, "QuickCapture", status, ss_required=True)

        except Exception as e:
            self.logger.Error("Exception raised in Quick_Capture function : " + str(e))
            api_test_status = False
            
        finally:
            return api_test_status


def main():
    testobj = api_test()
    testobj.run_test(testobj.script_name, testobj.apis)


if __name__ == '__main__':
    main()
