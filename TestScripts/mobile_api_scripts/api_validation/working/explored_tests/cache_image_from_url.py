# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author                :   Arathy P S
# Date                  :   30-01-2019
# Script Version        :   1.0
# Modification details  :
# APIs covered          :   "CacheImageFromUrl"
# Test Scenario         :   1. Valid url, Valid image name
#                           2. Invalid url, Valid image name
#                           3. Invalid parameter Empty string as image name
#                           4. Valid url, Lengthy image name
#                           5. Invalid parameter image name with special character
#                           6. Invalid parameter URL without file extension
#                           7. Invalid parameter Empty string as URL
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
    apis = 'CacheImageFromUrl'
    script_name = os.path.basename(__file__)

    def run_api_test(self):
        test_result = True
        test_params = self.config.cache_image_from_url_params

        try:            
            for key, value in test_params.items():
                self.logger.Log(" ----- Test Scenario - {} -----".format(value[0]))
                start_time = self.lib.gettimestamp()
                cached = self.dut.validator.CacheImageFromUrl(value[1], value[2])
                end_time = self.lib.gettimestamp()
                if cached == value[3]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False
                self.lib.report_api_status(start_time, end_time, "CacheImageFromUrl", status, ss_required=True)
                self.lib.report("CacheImageFromUrl: {}".format(value[0]), status, ss_required=False)

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
