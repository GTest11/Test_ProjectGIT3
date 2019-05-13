# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :
# Date              :   03-10-2018
# FE Version        :   FE 5.1.0.3
# APIs covered      :   "SetActiveFrameSource", "GetScreenshot", "UploadScreenshot"
#                       "QuickCapture", "QuickCaptureEx","CaptureImage"
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import os
import sys
import time

sys.path.append('../')
import library.common_functions as lib
import mobile_config.test_params as params

dut = lib.dut
msl = lib.msl


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
apis_in_the_script = ("SetActiveFrameSource", "GetScreenshot", "UploadScreenshot"
                      "QuickCapture", "QuickCaptureEx","CaptureImage"
                      )
config = lib.set_config()


def log_script_info():
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    lib.log_info("Script Name: {}".format(os.path.basename(__file__)))
    lib.log_info("Validating APIs - {}".format(apis_in_the_script))
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def upload_screenshot():
    start_time = lib.gettimestamp()
    img = dut.GetScreenshot()
    end_time = lib.gettimestamp()
    if img:
        status = lib.constants.STATUS[0]
    else:
        status = lib.constants.STATUS[1]

    lib.report("API: GetScreenshot", status)
    lib.report("API: Time taken by GetScreenshot".format(str(lib.getAPIduration(start_time,end_time))),
               status, image_required=False
               )
    if not img:
        return False

    start_time = lib.gettimestamp()
    ret = dut.validator.UploadScreenshot("test", img)
    end_time = lib.gettimestamp()
    if ret:
        status = lib.constants.STATUS[0]
        ret = True
    else:
        status = lib.constants.STATUS[1]
        ret = False

    lib.report("API: UploadScreenshot", status)
    lib.report("API: Time taken by UploadScreenshot".format(str(lib.getAPIduration(start_time, end_time))),
               status, image_required=True
               )
    return ret


def test_api():
    api_test_status = True
    try:
        apis = ("GetScreenshot",
                "QuickCapture",
                "QuickCaptureEx",
                "CaptureImage"
                )
        api_call = {
            "GetScreenshot" : dut.GetScreenshot(),
            "QuickCapture" : dut.validator.QuickCapture("img"),
            "QuickCaptureEx" : dut.validator.QuickCaptureEx("test", "jpeg"),
            "CaptureImage": dut.validator.CaptureImage(*config.CAPTUREIMG_INFO)
        }

        sources = params.video_sources #["f3b91a95", "21435", "aa455", "not_exists"]
        for source in sources:
            lib.log_info("*** Video Source changing to {} ***".format(source))
            dut.validator.SetActiveFrameSource(source)
            time.sleep(2)
            for api in apis:
                ret = None
                start_time = lib.gettimestamp()
                ret = api_call[api]
                end_time = lib.gettimestamp()
                lib.log_info("api returned - {}".format(ret))
                if ret:
                    status = lib.constants.STATUS[0]
                else:
                    status = lib.constants.STATUS[1]
                    api_test_status = False


                lib.report("API: {}".format(api), status)
                lib.report("API: Time taken by {} - {}".format(api, str(lib.getAPIduration(start_time, end_time))),
                           status, image_required=True
                           )
                if api == "GetScreenshot":
                    api_test_status = upload_screenshot()


    except Exception as e:
        lib.log_error(
            "Exception raised in test_api function : " + str(e))
        api_test_status = False
    finally:
        return api_test_status


def main():
    script_status = False
    try:
        if not config:
            lib.report("Invalid Config", "FAILED")
            return False

        'updating the Test Script details'
        lib.update_tc_details()
        log_script_info()

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
