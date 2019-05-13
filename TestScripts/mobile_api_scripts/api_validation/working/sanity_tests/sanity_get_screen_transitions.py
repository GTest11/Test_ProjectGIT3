# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :   07-Jan-2019
# Script Version    :   1.0
# APIs covered      :   'GetScreenTransitions',
# Test Scenario     :
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import os
import sys
import time
sys.path.append('../')

from library.api_test_base import apiTestBase

try:
    from System.Collections.Generic import List
except Exception as e:
    print e
    sys.exit(0)

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class api_test(apiTestBase):

    # the class which handles the script intention.
    # this overrides base class run_api_test()

    apis = ( 'GetScreenTransitions',
         )
    script_name = os.path.basename(__file__)


    def hpa_init(self, type='coordinates'):
        inputParam = None
        tap_data_list = None
        lstInputParam = None
        try:

            inputParam = self.mob_lib.HighPrecisionValidationService.MotionParams()
            tap_data = self.mob_lib.Models.TapData()
            if type == 'coordinates':
                tap_data.x_Cord = self.config.C_TAP_PLAYBACK[0]
                tap_data.y_Cord = self.config.C_TAP_PLAYBACK[1]
            else:   # 'element'
                elm_type,type = self.lib.choose_elm_type(self.config.navbar_trending)
                tap_data.type = elm_type
                tap_data.value = self.config.navbar_trending[type]

            tap_data_list = List[self.mob_lib.Models.TapData]()
            tap_data_list.Add(tap_data)
            lstInputParam = List[self.mob_lib.HighPrecisionValidationService.MotionParams]()
            inputParam.x_cord = self.config.HPA_X
            inputParam.y_cord = self.config.HPA_Y
            inputParam.width = self.config.HPA_W
            inputParam.height = self.config.HPA_H
            inputParam.sensitivity = self.config.HPA_SENS
            lstInputParam.Add(inputParam)
        except Exception as e:
            self.logger.Error("Exception in hpa_params(): " + str(e))
            tap_data_list = None
            lstInputParam = None

        finally:
            return lstInputParam, tap_data_list


    def run_api_test(self):
        '''
        Executes the test script

        :return: True or False
        '''

        api_test_status = True
        types = ('coordinates', 'element')
        try:
            for type in types:
                lstInputParam, tap_data_list = self.hpa_init(type)
                start_time = self.lib.gettimestamp()
                response = self.dut.validator.GetScreenTransitions(self.dut, self.config.HPA_DUR, lstInputParam, tap_data_list)
                end_time = self.lib.gettimestamp()

                # if response is not None and response.MotionData is not None:
                if response.MotionData:
                    for i in response.MotionData:
                        self.logger.Log("HPA Duration for Screen transition " + str(i.Duration))
                    status = "PASSED"
                else:
                    api_test_status = False
                    status = "FAILED"
                    self.logger.Log("Unable to Launch DetectMotionExecutor")

                self.lib.report_api_status(start_time, end_time, 'GetScreenTransitions-{}'.format(type), status, ss_required=True)
                time.sleep(1)

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
