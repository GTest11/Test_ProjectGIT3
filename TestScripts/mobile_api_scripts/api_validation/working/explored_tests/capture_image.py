# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author                :   Arathy P S
# Date                  :   26-11-2018
# Script Version        :   1.0
# Modification details  :
# APIs covered          :   "CaptureImage"
# Test Scenario         :   1. Valid parameters: overWriteAction: 1 (OverWrite action set to Error)
#                           2. Valid parameters: overWriteAction: 0 (overwrites the existing file)"
#                           3. Valid parameters: overWriteAction: 2 (creates a new file)"
#                           4. InValid parameters: overWriteAction: 5
#                           5. Valid parameters: jpegQuality: 100
#                           6. Valid parameters: jpegQuality: 0
#                           7. InValid parameters: jpegQuality: -10
#                           8. InValid parameters: jpegQuality: 200
#                           9. InValid parameters: lengthy image name
#                           10. Valid parameters: another co ordinate
#                           11. Valid parameters: whole frame
#                           12. Invalid parameters: overWriteAction: -1
#                           13. Invalid parameters: Empty string as image name
#                           14. Invalid parameters: Negative value for parameters
#                           15. Invalid parameters: Image name with special characters
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
    apis = 'CaptureImage'
    script_name = os.path.basename(__file__)

    def run_api_test(self):
        test_result = True
        test_params = self.config.capture_image_params
        w, h = self.lib.get_image_resolution()
        try:
            param_lst = list(test_params[10][2])
            param_lst[2], param_lst[3] = w, h
            test_params[10][2] = tuple(param_lst)
            for key, value in test_params.items():
                self.logger.Log(" ----- Test Scenario - {} -----".format(value[0]))
                if key == 0:
                    self.dut.validator.CaptureImage(*value[2])
                start_time = self.lib.gettimestamp()
                im_path = self.dut.validator.CaptureImage(*value[2])
                end_time = self.lib.gettimestamp()
                if im_path:  # if image path returned by the API
                    captured = True
                else:
                    captured = False
                if captured == value[1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False
                self.lib.report_api_status(start_time, end_time, "CaptureImage", status, ss_required=True)
                self.lib.report("CaptureImage: {}".format(value[0]), status)
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
