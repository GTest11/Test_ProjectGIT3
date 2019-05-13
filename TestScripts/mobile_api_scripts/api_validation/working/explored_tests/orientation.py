# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author                :   Arathy P S
# Date                  :   26-11-2018
# Script Version        :   1.0
# Modification details  :
# APIs covered          :   "GetOrientation", "ChangeOrientation", "SetOrientation"
# Test Scenario         :
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
    apis = ('GetOrientation', 'ChangeOrientation', 'SetOrientation')
    script_name = os.path.basename(__file__)

    def set_orientation(self, orientation, comp_text, message, no_change_required=True):
        '''
        To set orientation

        :param orientation: the orientation to be set by the API
        :param comp_text: The text to be compared against the API return value
        :param no_change_required: If this set to True, orientation before and after setting orientation are compared
        If required only to set orientation and verify the status, update this variable to False
        :return: True or False
        '''

        before = None
        if no_change_required:
            before = self.dut.GetOrientation()
        start_time  = self.lib.gettimestamp()
        self.dut.SetOrientation(orientation)
        end_time = self.lib.gettimestamp()
        get = self.dut.GetOrientation()
        if not no_change_required:
            before = get
        if get == comp_text == before:
            status = "PASSED"
            test_result = True
        else:
            status = "FAILED"
            test_result = False
        self.lib.report_api_status(start_time, end_time, "SetOrientation", status, ss_required=True)
        self.lib.report(message, status, ss_required=False)
        return test_result


    def run_api_test(self):
        test_result = True
        try:
            self.logger.Log("----- Test Scenario 1: GetOrientation on portrait mode after SetOrientation API -----")
            set = self.set_orientation(
                "Portrait", "PORTRAIT",
                "GetOrientation after SetOrientation('Portrait')", no_change_required=False
            )
            if not set:
                test_result = False

            self.logger.Log("----- Scenario 2: SetOrientation from portrait to portrait -----")
            set = self.set_orientation(
                "Portrait", "PORTRAIT",
                "SetOrientation from Portrait to Portrait", no_change_required=True
            )
            if not set:
                test_result = False

            self.logger.Log("----- Scenario 3: GetOrientation on Landscape mode after SetOrientation API -----")
            set = self.set_orientation(
                "Landscape", "LANDSCAPE",
                "GetOrientation after SetOrientation('Landscape')", no_change_required=False
            )
            if not set:
                test_result = False

            self.logger.Log("----- Scenario 4: SetOrientation from landscape to landscape -----")
            set = self.set_orientation(
                "Landscape", "LANDSCAPE",
                "SetOrientation from Landscape to Landscape", no_change_required=True
            )
            if not set:
                test_result = False

            self.logger.Log("----- Scenario 5: GetOrientation after ChangeOrientation -----")
            orientation_bfr_change = self.dut.GetOrientation()
            start_time = self.lib.gettimestamp()
            self.dut.ChangeOrientation()
            end_time = self.lib.gettimestamp()
            orientation_aft_change = self.dut.GetOrientation()
            if orientation_bfr_change == orientation_aft_change:
                status = "FAILED"
                test_result = False
            else:
                status = "PASSED"
            self.lib.report_api_status(start_time, end_time, "ChangeOrientation", status, ss_required=True)
            self.lib.report("GetOrientation after ChangeOrientation", status, ss_required=False)

            self.logger.Log("----- Scenario 6: Orientation API calls after media play back -----")
            if self.dut.Tap(*self.config.C_TAP_PLAYBACK):
                set_status = self.dut.SetOrientation("Portrait")
                orientation_before = self.dut.GetOrientation()
                change_status = self.dut.ChangeOrientation()
                orientation_after = self.dut.GetOrientation()
                if not ((orientation_after != orientation_before) & (set_status & change_status)):
                    status = "FAILED"
                    test_result = False
                else:
                    status = "PASSED"
                self.lib.report("Orientation API calls after media play back", status, True)
            else:
                self.logger.Error("Failed to tap on video, hence skipping this scenario")
                test_result = False

            self.logger.Log("----- Scenario 7: Invalid orientation for SetOrientation -----")
            status_invalid = self.dut.SetOrientation("test")
            if status_invalid:
                status = "FAILED"
                test_result = False
            else:
                status = "PASSED"
            self.lib.report("Invalid orientation for SetOrientation", status, True)

        except Exception as run_e:
            self.logger.Error("Exception in run_api_test" + str(run_e))
            test_result = False

        finally:
            self.test_result = test_result


def main():
    try:
        test_obj = api_test()
        test_obj.run_test(test_obj.script_name, test_obj.apis)

    except Exception as e:
        print "Exception from main function" + str(e)


if __name__ == '__main__':
    main()
