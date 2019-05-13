# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :   17-April-2019
# Script Version    :   1.0
# APIs covered      :   'GetScreenTransitions',
# Test Scenario     :
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import os
import sys
import time
sys.path.append('../')

from library.api_test_base import ApiTestBase

try:
    from System.Collections.Generic import List
except Exception as e:
    print e
    sys.exit(0)

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class api_test(ApiTestBase):

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

            inputParam = self.lib.mob_lib.HighPrecisionValidationService.MotionParams()
            tap_data = self.lib.mob_lib.Models.TapData()
            if type == 'coordinates':
                dev = self.lib.get_dut_name()
                coord = self.config.home_in_home_menu[dev]
                tap_data.x_Cord = coord[0]
                tap_data.y_Cord = coord[1]
            else:   # 'element'
                elm_type,type = self.lib.choose_elm_type(self.config.home_menu)
                tap_data.type = elm_type
                tap_data.value = self.config.home_menu[type]

            tap_data_list = List[self.lib.mob_lib.Models.TapData]()
            tap_data_list.Add(tap_data)
            lstInputParam = List[self.lib.mob_lib.HighPrecisionValidationService.MotionParams]()
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
        types = ('element', 'coordinates')
        try:
            for type in types:
                    lstInputParam, tap_data_list = self.hpa_init(type)
                    start_time = self.lib.get_time_stamp()
                    response = self.dut.validator.GetScreenTransitions(self.dut, self.config.HPA_DUR, lstInputParam, tap_data_list)
                    end_time = self.lib.get_time_stamp()

                    # if response is not None and response.MotionData is not None:
                    if response.MotionData:
                        for resp in response.MotionData:
                            self.logger.Log("HPA Duration for Screen transition " + str(resp.Duration))
                        status = "PASSED"
                    else:
                        api_test_status = False
                        status = "FAILED"
                        self.logger.Log("Unable to Launch DetectMotionExecutor")

                    self.lib.report_api_status(start_time, end_time, 'GetScreenTransitions-{}'.format(type), status, ss_required=True)
                    time.sleep(1)

                    if not self.dut.CloseApp():
                        self.logger.Log("Failed to close the application")
                        api_test_status = False
                        return

                    if not self.dut.LaunchApp():
                        self.logger.Log("Failed to launch the application")
                        api_test_status = False
                        return

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
