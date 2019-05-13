# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author                :   Arathy P S
# Date                  :   30-01-2019
# Script Version        :   1.0
# Modification details  :
# APIs covered          :   "DynamicImageCompare"
# Test Scenario         :   "Valid parameters"
#                           "Valid: tolerance, boundary condition [100]"
#                           "Valid: tolerance, boundary condition [0]"
#                           "InValid referenceImageName"
#                           "Invalid parameter, coordinate out of boundary"
#                           "Invalid case, Use image from CaptureImage API as refImage"
# '''''''''''''''''''''''''''TEST CASE DETAILS' - END '''''''''''''''''''''''''''''''''

try:
    import os
    import sys
    import time
    sys.path.append('../')
    from library.api_test_base import apiTestBase
except Exception as e:
    print ("Exception in Import " + str(e))
    sys.exit()


class api_test(apiTestBase):
    # the class which handles the script intention.
    # this overrides base class run_api_test()
    apis = ("DynamicImageCompare",)
    script_name = os.path.basename(__file__)

    def run_api_test(self):
        test_result = True
        test_params = self.config.dynamic_image_compare_params
        w, h = self.lib.get_image_resolution()
        try:
            if not self.dut.validator.CacheImageFromUrl(
                    self.config.CACHE_VALID_URL_FOR_DYNAMIC_COMPARE,
                    self.config.dyn_img):
                self.lib.report("CacheImageFromUrl", "FAILED", ss_required=True)
                test_result = False
                return False

            for key, value in test_params.items():
                time.sleep(5)
                self.logger.Log(" ----- Test Scenario - {} -----".format(value[0]))
                if key == 4:
                    param_lst = list(test_params[4][2])
                    param_lst[3], param_lst[4] = w, h
                    test_params[4][2] = tuple(param_lst)
                elif key == 5:
                    self.dut.validator.CaptureImage(self.config.C_DYN_IMG_COMP[0], self.config.C_DYN_IMG_COMP[1],
                                                    self.config.C_DYN_IMG_COMP[2], self.config.C_DYN_IMG_COMP[3],
                                                    self.config.dyn_img, self.config.CAP_IMG_DEFAULT_QUALITY, 2)
                start_time = self.lib.gettimestamp()
                compared = self.dut.validator.DynamicImageCompare(*value[2])
                end_time = self.lib.gettimestamp()

                if compared == value[1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False

                self.lib.report_api_status(start_time, end_time, "DynamicImageCompare", status, ss_required=True)
                self.lib.report("DynamicImageCompare: {}".format(value[0]), status)

        except Exception as ex:
            self.logger.Error("Error in run_api_test() " + str(ex))
            test_result = False

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
