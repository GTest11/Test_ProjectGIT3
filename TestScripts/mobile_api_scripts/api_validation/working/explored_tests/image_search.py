# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            : Shameena HA
# Date              :   28-11-2018
# Script Version    : 1.0
# APIs covered      :   "ImageSearch"
# Test Scenario: "Valid parameters, expected region (small) and algoritham: SqdiffNormed",
#                 "Valid parameters, max region and algoritham: CcorrNormed",
#                 "Valid parameters, max region and algoritham: default_CcoeffNormed",
#                 "Valid parameters, percentMatchThreshold boundary condition: 0",
#                 "Valid parameters, multiple occurance of pattern",
#                 "Valid parameters, but checkpoint not available on the screen"
#                 "Invalid parameters, Checkpoint does not exist",
#                 "Valid parameters, OCR Checkpoint",
#
# '''''''''''''''''''''''''''TEST CASE DETAILS' - END '''''''''''''''''''''''''''''''''

import os
import sys
import time
sys.path.append('../')

from library.api_test_base import apiTestBase

class api_test(apiTestBase):
    # the class which handles the script intention.
    # this overrides base class run_api_test()

    # class variables
    apis = ('ImageSearch',)
    script_name = os.path.basename(__file__)


    def run_api_test(self):
        test_result = True
        params = self.config.image_search_params
        w, h = self.lib.get_image_resolution()
        try:
            for param in params.keys():
                self.logger.Log("--- Scenario: {} ---".format(params[param][0]))

                if param != 0:
                    api_param = list(params[param][-1])
                    api_param[3], api_param[4] = w, h
                    params[param][-1] = tuple(api_param)

                if param == 6:
                    if not self.dut.Tap(*self.config.C_TAP_PLAYBACK):
                        self.lib.report("Failed to start the playback", "FAILED", ss_required=True)
                        test_result = False
                        continue

                start_time = self.lib.gettimestamp()
                response = self.dut.validator.ImageSearch(*params[param][-1])
                end_time = self.lib.gettimestamp()
                self.logger.Log("response.OpStatus {}".format(response.OpStatus))
                self.logger.Log("response.MatchPercentage {}".format(response.MatchPercentage))
                try:
                    self.logger.Log("response.MatchRegion {}".format(response.MatchRegion))
                except Exception as e:
                    print e
                if response.OpStatus == params[param][1]:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    test_result = False
                self.lib.report_api_status(start_time, end_time, "ImageSearch", status, ss_required=True)
                self.lib.report("ImageSearch: {}".format(params[param][0]), status, ss_required=False)
                time.sleep(5) # wait between next scenario test

        except Exception as e:
            self.logger.Error("Error in run_api_test() " + str(e))
            test_result = False

        finally:
            self.test_result = test_result


def main():
    testobj = api_test()
    testobj.run_test(testobj.script_name, testobj.apis)


if __name__ == '__main__':
    main()
