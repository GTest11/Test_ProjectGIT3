# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Script name       :   GetScreenTransitions.py
# Author            :
# Date              :   17-10-2018
# Script Version    :   1.0
# APIs covered      :   GetScreenTransitions
# Test Scenario     :   Launch the app, call GetScreenTransitions API. If response data obtained,
#                       update the script status as Pass
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
try:
    import os
    import sys
    sys.path.append('../')
    import library.common_functions as lib
    import mobile_config.test_params as params
except Exception as e:
    print ("Exception in Import " + str(e))
    sys.exit()

apis_in_the_script = "GetScreenTransitions"
config = lib.set_config()
file_name = os.path.basename(__file__)

"""
``````````````````````````````````````````````````````````````````````````
Function Name	  	: hpa_init
Description		    : Function to initialize HPA
Input arguments	    : null
Output values		: null
``````````````````````````````````````````````````````````````````````````
"""


def hpa_init():
    global inputParam
    global tap_data_list
    global lstInputParam
    try:
        from System.Collections.Generic import List
        inputParam = lib.fe_mob_lib.HighPrecisionValidationService.MotionParams()
        tap_data = lib.fe_mob_lib.Models.TapData()
        tap_data.type = lib.fe_mob_lib.Constants.ElementType.XPath
        tap_data_list = List[lib.fe_mob_lib.Models.TapData]()
        tap_data.x_Cord = 250
        tap_data.y_Cord = 250
        tap_data_list.Add(tap_data)
        lstInputParam = List[lib.fe_mob_lib.HighPrecisionValidationService.MotionParams]()
    except Exception as e:
        lib.log_info("Exception in hpa_params(): " + str(e))

"""
``````````````````````````````````````````````````````````````````````````
Function Name	  	: hpa_param
Description		    : Function to initialize HPA API params
Input arguments	    : null
Output values		: null
``````````````````````````````````````````````````````````````````````````
"""


def hpa_param():
    try:
        hpa_init()
        inputParam.x_cord = params.HPA_X
        inputParam.y_cord = params.HPA_Y
        inputParam.width = params.HPA_W
        inputParam.height = params.HPA_H
        inputParam.sensitivity = params.HPA_SENS
        lstInputParam.Add(inputParam)
    except Exception as e:
        lib.log_info("Exception in hpa_params(): " + str(e))

"""
``````````````````````````````````````````````````````````````````````````
Function Name	  	: test_api
Description		    : Function to test the APIs
Input arguments	    : null
Output values		: bool  :   script execution status
``````````````````````````````````````````````````````````````````````````
"""


def test_api():
    script_status = False
    try:
        hpa_param()
        start_time = lib.gettimestamp()
        response = lib.dut.validator.GetScreenTransitions(lib.dut, params.HPA_DUR, lstInputParam, tap_data_list)
        end_time = lib.gettimestamp()
        if response is not None and response.MotionData is not None:
            for i in response.MotionData:
                lib.log_info("HPA Duration for Screen transition " + str(i.Duration))
                lib.dut.CommitStepResult("HPA Duration for Screen transition ", str(i.Duration))
            status = "PASSED"
            script_status = True
        else:
            status = "FAILED"
            lib.log_info("Unable to Launch DetectMotionExecutor")
            lib.dut.CommitStepResult("HPA Duration for Screen transition ", "FAILED")
        lib.report_elapsed_time(start_time, end_time, "GetScreenTransitions")
        lib.report("GetScreenTransitions API", status, image_required=True)
    except Exception as e:
        script_status = False
        lib.log_error("Exception raised in test_api() function : " + str(e))
    finally:
        return script_status

"""
``````````````````````````````````````````````````````````````````````````
Function Name	  	: main
Description		    : main function
Input arguments	    : null
Output values		: null
``````````````````````````````````````````````````````````````````````````
"""


def main():
    script_status = False
    try:
        if not config:
            lib.report("Invalid Config", "FAILED")
            return False

        'updating the Test Script details'
        lib.update_tc_details()
        lib.log_script_info(file_name, apis_in_the_script)

        'launching application'
        if lib.start_run(home=config.app_home):
            script_status = test_api()
        else:
            lib.report("Script Status", "FAILED", image_required=True)

    except Exception as e:
        lib.log_error("Exception raised in main function : " + str(e))
        script_status = False
    finally:
        lib.stop_run()
        lib.CommitScriptResult(script_status)
        lib.log_info("-- Execution End --")

if __name__ == "__main__":
    main()
