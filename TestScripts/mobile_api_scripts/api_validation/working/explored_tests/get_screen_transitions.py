# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :   Arathy P.S.
# Date              :   06-02-2019
# Script Version    :   1.0
# APIs covered      :   'GetScreenTransitions',
# Test Scenario     :
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

try:
    import os
    import sys
    import re
    sys.path.append('../')
    from library.api_test_base import apiTestBase
    from System.Collections.Generic import List
    import time
except Exception as e:
    print ("Exception in Import " + str(e))
    sys.exit()


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

class api_test(apiTestBase):
    # the class which handles the script intention.
    # this overrides base class run_api_test()
    # class variables
    apis = 'GetScreenTransitions'
    script_name = os.path.basename(__file__)

    def hpa_init(self, type='coordinates', type_value=(0, 0), coordinates=(0, 0, 0, 0)):
        tap_data_list = None
        lstInputParam = None
        try:
            inputParam = self.mob_lib.HighPrecisionValidationService.MotionParams()
            tap_data = self.mob_lib.Models.TapData()
            if type == 'coordinates':
                tap_data.x_Cord = type_value[0]
                tap_data.y_Cord = type_value[1]
            else:   # 'element'
                tap_data.type = self.mob_lib.Constants.ElementType.Id
                tap_data.value = type_value[0]

            tap_data_list = List[self.mob_lib.Models.TapData]()
            tap_data_list.Add(tap_data)
            lstInputParam = List[self.mob_lib.HighPrecisionValidationService.MotionParams]()
            inputParam.x_cord = coordinates[0]
            inputParam.y_cord = coordinates[1]
            inputParam.width = coordinates[2]
            inputParam.height = coordinates[3]
            inputParam.sensitivity = self.config.HPA_SENS
            lstInputParam.Add(inputParam)
        except Exception as ex:
            self.logger.Error("Exception in hpa_init(): " + str(ex))
            tap_data_list = None
            lstInputParam = None
        finally:
            return lstInputParam, tap_data_list

    def run_api_test(self):
        api_test_status = True
        try:
            test_params = self.config.get_screen_transitions
            for key, value in test_params.items():
                self.logger.Log(" ----- Test Scenario - {} -----".format(value[0]))
                lstInputParam, tap_data_list = self.hpa_init(value[1], value[2], value[4])
                start_time = self.lib.gettimestamp()
                response = self.dut.validator.GetScreenTransitions(self.dut, value[3], lstInputParam, tap_data_list)
                end_time = self.lib.gettimestamp()
                if response.ErrorData is not None:
                    status = "PASSED"
                elif response is None:
                    status = "PASSED"
                elif response.MotionData is None:
                    status = "PASSED"
                else:
                    api_test_status = False
                    status = "FAILED"
                self.lib.report_api_status(start_time, end_time, 'GetScreenTransitions', status, ss_required=True)
        except Exception as e:
            self.logger.Error("Error in run_api_test() " + str(e))
            api_test_status = False

        finally:
            self.test_result = api_test_status


def main():
    try:
        test_obj = api_test()
        test_obj.run_test(test_obj.script_name, test_obj.apis)
    except Exception as e:
        print "Exception from main function" + str(e)

if __name__ == '__main__':
    main()
