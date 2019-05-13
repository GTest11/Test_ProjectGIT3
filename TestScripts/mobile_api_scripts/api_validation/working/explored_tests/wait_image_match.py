# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author                :   Arathy P S
# Date                  :   30-11-2018
# Script Version        :   1.0
# Modification details  :
# APIs covered          :   "WaitImageMatch"
# Test Scenario         :   "InValid parameter, non existing reference image"
#                         "Valid parameters RMSE algorithm"
#                         "Valid parameters, PIXEL_BASED algorithm"
#                         "Valid parameters, Test region is larger than reference image"
#                         "In Valid parameters, wrong algorithm"
#                         "Valid parameters, tolerance, boundary condition: 0"
#                         "InValid parameters, tolerance, invalid value: '-12'
#                         "InValid parameters, tolerance, out of range: '200'
#                         "InValid parameters, waitGap greater than timeToWait
#                         "Valid parameters, whole HD frame comparison"
#                         "Valid parameters,ref image and test region from two different
#                         "Valid parameters, tolerance, boundary condition: 100"
#                         "Valid parameters, timeToWait, large value"
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
    apis = 'WaitImageMatch'
    script_name = os.path.basename(__file__)

    def run_api_test(self):
        test_result = True
        test_params = self.config.wait_image_match_params
        w, h = self.lib.get_image_resolution()

        try:
            for key, value in test_params.items():
                if key == 9:
                    param_lst = list(test_params[key][2])
                    param_lst[3], param_lst[4] = w, h
                    test_params[key][2] = tuple(param_lst)
                if not self.dut.validator.CaptureImage(self.config.C_WAIT_IMG_MATCH[0], self.config.C_WAIT_IMG_MATCH[1],
                                                       self.config.C_WAIT_IMG_MATCH[2], self.config.C_WAIT_IMG_MATCH[3],
                                                       self.config.img_wait_im_match,
                                                       self.config.CAP_IMG_DEFAULT_QUALITY, 0):
                    self.logger.Log("CaptureImage API Failed")
                    test_result = False
                    continue

                self.logger.Log(" ----- Test Scenario - {} -----".format(value[0]))
                start_time = self.lib.gettimestamp()
                match_found = self.dut.validator.WaitImageMatch(*value[2])
                end_time = self.lib.gettimestamp()
                self.logger.Log("Image Match - {}".format(match_found))
                if match_found == value[1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False
                self.lib.report_api_status(start_time, end_time, "WaitImageMatch", status, ss_required=True)
                self.lib.report("WaitImageMatch: {}".format(value[0]), status, ss_required=False)

        except Exception as run_e:
            self.logger.Error("Exception in run_api_test " + str(run_e))
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
