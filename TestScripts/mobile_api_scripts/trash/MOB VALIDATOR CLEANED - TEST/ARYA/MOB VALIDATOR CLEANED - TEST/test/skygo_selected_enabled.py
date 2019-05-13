# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID       :
# Author            :
# Date              :   05-10-2018
# FE Version        :   FE 5.1.0.3
# APIs covered      :   "IsEnabled", "IsSelected"
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import sys, os, time
sys.path.append('../')
import library.common_functions as lib

dut = lib.dut
msl = lib.fe_mob_lib


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
apis_in_the_script = ("IsEnabled", "IsSelected",
                      )
config = lib.set_config("skygo")

def log_script_info():
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    lib.log_info("Script Name: {}".format(os.path.basename(__file__)))
    lib.log_info("Validating APIs - {}".format(apis_in_the_script))
    lib.log_info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def test_api():
    api_test_status = True
    try:
        time.sleep(30)

        if not dut.IsElementPresent(msl.Constants.ElementType.Id, config.hamburger):
            lib.report("Hamburger not found", "FAILED", image_required=True)
            return False

        tapped = dut.TapElement(msl.Constants.ElementType.Id, config.hamburger)
        if not tapped:
            lib.report("failed to tap on Hamburger", "FAILED", image_required=True)
            return False

        lib.report("Tapped on Hamburger", "PASSED", image_required=True)
        if not dut.IsElementPresent(msl.Constants.ElementType.XPath, config.settings):
            lib.report("Settings not found", "FAILED", image_required=True)
            return False

        tapped = dut.TapElement(msl.Constants.ElementType.XPath, config.settings)
        if not tapped:
            lib.report("Failed to tap on Settings", "FAILED", image_required=True)
            return False
        lib.report("Tapped on Settings", "PASSED", image_required=True)

        if not dut.IsElementPresent(msl.Constants.ElementType.XPath, config.x_settings_network_pref):
            lib.report("Network Preferences not found", "FAILED", image_required=True)
            return False
        tapped = dut.TapElement(msl.Constants.ElementType.XPath, config.x_settings_network_pref)
        if not tapped:
            lib.report("Failed to tap on Network Preferences", "FAILED", image_required=True)
            return False

        start_time = lib.gettimestamp()
        enabled = dut.IsEnabled(msl.Constants.ElementType.Id, config.id_allow_streaming)
        end_time = lib.gettimestamp()
        if enabled:
            status = "PASSED"
        else:
            status = "FAILED"

        lib.report_elapsed_time(start_time, end_time, "IsEnabled", status)
        lib.report("API: IsEnabled", status, image_required=True)

        start_time = lib.gettimestamp()
        selected = dut.IsSelected(msl.Constants.ElementType.Id, config.id_allow_streaming)
        end_time = lib.gettimestamp()
        if not selected:
            lib.log_info("Allow Streaming Over Mobile Network not selected")
            tapped = dut.TapElement(msl.Constants.ElementType.Id, config.id_allow_streaming)
            if not tapped:
                lib.report("failed to tap on checkbox - Allow Streaming Over Mobile Network",
                           "FAILED", image_required=True
                           )
                return False
            start_time = lib.gettimestamp()
            selected = dut.IsSelected(msl.Constants.ElementType.Id, config.id_allow_streaming)
            end_time = lib.gettimestamp()

        if selected:
            status = "PASSED"
        else:
            status = "FAILED"

        lib.report_elapsed_time(start_time, end_time, "IsSelected", status)
        lib.report("API: IsSelected", status, image_required=True)


    except Exception as e:
        lib.log_error(
            "Exception raised in test_app_info function : " + str(e))
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
        if lib.start_run(msl.Constants.ElementType.Id, config.skygo_home):
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
