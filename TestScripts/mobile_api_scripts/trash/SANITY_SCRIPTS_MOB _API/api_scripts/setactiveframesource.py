# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :   Rohith P V
# Date              :   05-10-2018
# Script Version    :   1.1
# Modification details: Fixed review comments, date 17/10/2018
# APIs covered      :   "SetActiveFrameSource", "GetScreenshot", "UploadScreenshot"
#                       "QuickCapture", "QuickCaptureEx"
# Test Scenario     :   Launches youtube application -> Change the active framesource using SetActiveFrameSource API -> Validate the framesource change 
#                        by the images taken using GetScreenshot -> UploadScreenshot -> QuickCapture -> QuickCaptureEx APIs
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


import os
import sys
import time

sys.path.append('../')
import library.common_functions as lib
import mobile_config.test_params as params

# dut = lib.dut
# msl = lib.msl


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
apis_in_the_script = ("SetActiveFrameSource", "GetScreenshot", "UploadScreenshot",
                       "QuickCapture", "QuickCaptureEx"
                      )
config = lib.set_config()

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# @Function Name	: screenshot()
# @Description		: Tests the GetScreenshot and UploadScreenshot APIs and logs its response (status, duration)
# @Input arguments	: Null
# @Output values	: Bool
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def screenshot():
    api_test_status = False
    try:
        status_Get = "FAILED"
        start_time = lib.gettimestamp()
        img = lib.dut.GetScreenshot()
        end_time = lib.gettimestamp()
        if img:
            status_Get = "PASSED"
            ret_get = True

        lib.report("API: GetScreenshot", status_Get)
        lib.report_elapsed_time(start_time,end_time, "GetScreenshot")

        #ret = False
        status_Upload = "FAILED"
        start_time = lib.gettimestamp()
        ret = lib.dut.validator.UploadScreenshot("test", img)
        end_time = lib.gettimestamp()
        if ret:
            status_Upload = "PASSED"
            ret_upload = True

        lib.report("API: UploadScreenshot", status_Upload)
        lib.report_elapsed_time(start_time, end_time, "UploadScreenshot")

        if ret_get & ret_upload:
            api_test_status = True

    except Exception as e:
        lib.log_error(
            "Exception raised in screenshot function : " + str(e))

    finally:
        return api_test_status

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# @Function Name	: QuickCapture_Ex()
# @Description		: Tests the QuickCaptureEx API for different image formats and logs its response (status, duration)
# @Input arguments	: Null
# @Output values	: Bool
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def QuickCapture_Ex():
    api_test_status = False
    try:
        formats = {"JPG","PNG","BMP"}
        for fmt in formats:
            status = "FAILED"
            start_time = lib.gettimestamp()
            path = lib.dut.validator.QuickCaptureEx("test_{}_image".format(fmt), fmt)
            end_time = lib.gettimestamp()

            if path:
                status = "PASSED"

            lib.report("API: QuickCaptureEx in {} format".format(fmt), status)
            lib.report_elapsed_time(start_time, end_time, "QuickCaptureEx {} format".format(fmt))

        if status == "PASSED":
            api_test_status = True

    except Exception as e:
        lib.log_error(
            "Exception raised in QuickCapture_Ex function : " + str(e))

    finally:
        return api_test_status

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# @Function Name	: screenshot()
# @Description		: Tests the QuickCapture API and logs its response (status, duration)
# @Input arguments	: Null
# @Output values	: Bool
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def Quick_Capture():
    api_test_status = False
    try:
        status = "FAILED"
        start_time = lib.gettimestamp()
        path = lib.dut.validator.QuickCapture("img")
        end_time = lib.gettimestamp()
        lib.report_elapsed_time(start_time, end_time, "QuickCapture")
        if path:
            status = "PASSED"
        lib.report("API: QuickCapture", status)

        if status == "PASSED":
            api_test_status = True

    except Exception as e:
        lib.log_error(
            "Exception raised in Quick_Capture function : " + str(e))

    finally:
        return api_test_status
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# @Function Name	: test_api()
# @Description		: Tests the SetActiveFrameSource, QuickCapture and QuickCaptureEx APIs and logs its response (status, duration)
# @Input arguments	: Null
# @Output values	: Bool
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def test_api():
    api_test_status = False
    try:
        apis = ["GetScreenshot","QuickCapture","QuickCaptureEx"]
        sources = params.video_sources  # ["f3b91a95", "21435", "aa455", "not_exists"]
        for source in sources:
            api_test_status = False
            status = "FAILED"
            lib.log_info("*** Video Source changing to {} ***".format(source))
            start_time = lib.gettimestamp()
            if lib.dut.validator.SetActiveFrameSource(source):
                end_time = lib.gettimestamp()
                status = "PASSED"
                lib.report_elapsed_time(start_time, end_time, "SetActiveFrameSource")
                lib.report("API: {}".format("SetActiveFrameSource"), status)
                time.sleep(2)
                for api in apis:
                    # ret_screenshot, ret_QuickCaptureEx, ret_QuickCapture = None
                    if (api == "GetScreenshot"):
                        ret_screenshot = screenshot()
                    elif (api == "QuickCaptureEx"):
                        ret_QuickCaptureEx = QuickCapture_Ex()
                    else:
                        ret_QuickCapture = Quick_Capture()
            else:
                end_time = lib.gettimestamp()
                lib.report("API: SetActiveFrameSource", status)
                lib.report_elapsed_time(start_time, end_time, "SetActiveFrameSource")

        if ret_screenshot & ret_QuickCaptureEx & ret_QuickCapture:
            api_test_status = True

    except Exception as e:
        lib.log_error(
            "Exception raised in test_api function : " + str(e))
        api_test_status = False
    finally:
        return api_test_status


def main():
    driver = False
    script_status = False
    try:
        if not config:
            lib.report("Invalid Config", "FAILED")
            return False

        'updating the Test Script details'
        lib.update_tc_details()
        lib.log_script_info(os.path.basename(__file__), apis_in_the_script)

        'launching application'
        if lib.start_run(home=config.app_home):
            driver = True
            script_status = test_api()
        else:
            lib.report("Script Status", "FAILED", image_required=True)

    except Exception as e:
        lib.log_error("Exception raised in main function : " + str(e))
        script_status = False

    finally:
        if driver:
            lib.stop_run()
        lib.CommitScriptResult(script_status)
        lib.log_info("-- Execution End --")


if __name__ == "__main__":
    main()
