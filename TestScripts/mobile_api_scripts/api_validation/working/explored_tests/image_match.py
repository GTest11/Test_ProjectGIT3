# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author                :   Arathy P S
# Date                  :   30-01-2019
# Script Version        :   1.1
# Modification details  :   Extra scenarios added
# APIs covered          :   "ImageMatch"
# Test Scenario         :   "Valid parameters, RMSE algorithm"
#                             "Valid parameters, tolerance, boundary condition: 100"
#                             "Invalid parameter, image doesn't exist
#                             "Invalid parameters, tolerance: -12"
#                             "Invalid Parameters, tolerance invalid"
#                             "Valid parameters, tolerance boundary condition: 0"
#                             "Invalid parameters, wrong algorithm"
#                             "Invalid parameters, negative algorithm"
#
# '''''''''''''''''''''''''''TEST CASE DETAILS' - END '''''''''''''''''''''''''''''''''

try:
    import os
    import sys
    sys.path.append('../')
    from library.api_test_base import apiTestBase
except Exception as e:
    print ("Exception in Import " + str(e))
    sys.exit()


class api_test(apiTestBase):
    # the class which handles the script intention.
    # this overrides base class run_api_test()
    # class variables
    apis = 'ImageMatch'
    script_name = os.path.basename(__file__)

    def run_api_test(self):
        test_result = True
        cur_dut = self.lib.get_dut_name()
        self.logger.Log("Currently selected DUT : "+str(cur_dut))
        try:
            if cur_dut in self.config.c_capture_image_non_playback_region:
                x,y,w,h = self.config.c_capture_image_non_playback_region[cur_dut]
                cap_img_ref_region = (x, y, w, h, "ref", self.config.CAP_IMG_DEFAULT_QUALITY, self.config.overwrite_file)
                cap_img_test_region = (x, y, w, h, "test", self.config.CAP_IMG_DEFAULT_QUALITY, self.config.overwrite_file)
            else:
                self.lib.report(
                    "Coordinates for capture image is not available in Config. Hence skipping the test",
                    "FAILED", ss_required=True
                    )
                test_result = False
                return test_result

            test_params = self.config.image_match_params
            for key, value in test_params.items():
                captured_1 = self.dut.validator.CaptureImage(*cap_img_ref_region)
                captured_2 = self.dut.validator.CaptureImage(*cap_img_test_region)
                if not (captured_1 or captured_2):
                    self.lib.report("Failed to capture image", "FAILED", ss_required=True)
                    test_result = False
                    continue

                self.logger.Log(" ----- Test Scenario - {} -----".format(value[0]))
                start_time = self.lib.gettimestamp()
                match_found = self.dut.validator.ImageMatch(*value[2])
                end_time = self.lib.gettimestamp()
                self.logger.Log("Image Match - {}".format(match_found))
                if match_found == value[1]:
                    status = "PASSED"
                else:
                    test_result = False
                    status = "FAILED"
                self.lib.report_api_status(start_time, end_time, "ImageMatch", status, ss_required=True)
                self.lib.report("ImageMatch: {}".format(value[0]), status, ss_required=False)

            self.logger.Log(" ----- Test Scenario - Image from CacheImageFromUrl ----- ")
            cached_1 = self.dut.validator.CacheImageFromUrl(self.config.CACHE_VALID_URL, "cache_refImg")
            cached_2 = self.dut.validator.CacheImageFromUrl(self.config.CACHE_VALID_URL, "cache_testImg")
            if not (cached_1 or cached_2):
                    self.lib.report("Failed to capture image", "FAILED", ss_required=True)
                    test_result = False
                    return test_result

            start_time = self.lib.gettimestamp()
            match_found = self.dut.validator.ImageMatch("cache_refImg", "cache_testImg", self.config.RMSE_ALGORITHM,
                                                         self.config.DEFAULT_STR_TOLERANCE)
            end_time = self.lib.gettimestamp()
            if not match_found:
                status = "FAILED"
                test_result = False
            else:
                status = "PASSED"
            self.lib.report_api_status(start_time, end_time, "ImageMatch", status, ss_required=True)
            self.lib.report("ImageMatch: Images supplied from CacheImageFromUrl", status, ss_required=False)

            #----------------Issue in QuickCapture FAL-4207 -----------------------------------------------#
            # self.logger.Log(" ----- Test Scenario - Image from QuickCapture ----- ")
            # self.dut.validator.QuickCapture("Quick_refImg")
            # self.dut.validator.QuickCapture("Quick_testImg")
            # start_time = self.lib.gettimestamp()
            # status_quick = self.dut.validator.ImageMatch("Quick_refImg", "Quick_testImg", self.config.RMSE_ALGORITHM,
            #                                              self.config.DEFAULT_STR_TOLERANCE)
            # end_time = self.lib.gettimestamp()
            # if not status_quick:
            #     status = "FAILED"
            #     test_result = False
            # else:
            #     status = "PASSED"
            # self.lib.report_api_status(start_time, end_time, "ImageMatch", status, ss_required=True)
        #    self.lib.report("ImageMatch: Images supplied from QuickCapture", status, ss_required=False)

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
