# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Script name       :   orientation.py
# Author            :
# Date              :   22-April-2019
# Script Version    :   1.0
# APIs covered      :   "GetOrientation", "ChangeOrientation", "SetOrientation"
# Test Scenario     :   Launch the APP, call the GetOrientation API to get the current orientation
#                       Call the ChangeOrientation API to change the current orientation. Take the
#                       Image resolution before and after ChangeOrientation API call. If the Image resolution changed,
#                       commit the API Status as PASS.
#                       Call SetOrientation API to change the orientation. compare the image resolution to commit the
#                       API Status.
#                       Finally Close the APP and stop the appium driver.
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import sys, os, time

#importing user defined functions
sys.path.append('../')

from library.api_test_base import ApiTestBase


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class api_test(ApiTestBase):

    # the class which handles the script intention.
    # this overrides base class run_api_test()

    apis = ("GetOrientation", "ChangeOrientation", "SetOrientation")
    script_name = os.path.basename(__file__)
    

    def run_api_test(self):
        '''
        Executes the test script

        :return:
        '''

        api_test_status = False
        try:
            orientation_before_change = self.get_orientation()
            resolution_before_change = self.lib.get_image_resolution()
            self.dut.CommitStepResult("Image Resolution on " + str(orientation_before_change), str(resolution_before_change))

            if not self.lib.play_back_from_search_result():
                self.lib.report("Tap on video", "FAILED", ss_required=True)
            else:
                time.sleep(10)   # delay for playback
            
            orientation_after_change = self.change_orientation()
            resolution_after_change = self.lib.get_image_resolution()
            
            if orientation_after_change and resolution_after_change:
                self.dut.CommitStepResult("Image Resolution on " + str(orientation_after_change), str(resolution_after_change))
                self.logger.Log("Orientation after ChangeOrientation: " + str(orientation_after_change))
                change_verified = self.resolution_changed(resolution_before_change, resolution_after_change)
                if not change_verified:
                    self.dut.CommitStepResult("API: ChangeOrientation API", "FAILED")
                    self.dut.CommitStepResult("API: Reason", "No change in orientation after the API call")
                else:
                    self.dut.CommitStepResult("API: ChangeOrientation API", "PASSED")
    
                set_verified = self.verify_set_orientation()

                if orientation_before_change and change_verified and set_verified:
                    api_test_status = True

            else:
                self.dut.CommitStepResult("API - ChangeOrientation or GetOrientation", "Failed")

            
        except Exception as e:
            self.logger.Error("Exception raised in main function : " + str(e))
            api_test_status = False

        finally:
            self.test_result = api_test_status
            self.dut.SetOrientation("Portrait")


    # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    # @Function Name	: resolution_changed
    # @Description		: Function to compare the resolutions
    # @Input arguments	: before    :   Resolution before change orientation
    #                   : after     :   Resolution after change orientation
    # @Output values	: Bool
    # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def resolution_changed(self, before, after):
        return before[0] == after[1] and before[1] == after[0]
        # if before[0] == after[1] and before[1] == after[0]:
        #     return True
        # return False


    # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    # @Function Name	: get_orientation
    # @Description		: Function to call GetOrientation API
    # @Input arguments	: None
    # @Output values	: string    :   orientation
    # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def get_orientation(self):
        orientation = None
        try:
            start_time = self.lib.get_time_stamp()
            orientation = self.dut.GetOrientation()
            end_time = self.lib.get_time_stamp()
            if orientation in ["PORTRAIT", "LANDSCAPE"]:
                status = "PASSED"
            else:
                orientation = None
                status = "FAILED"
            self.lib.report_api_status(start_time, end_time, "GetOrientation", status)
        except Exception as e:
            orientation = None
            self.logger.Error("Exception in get_orientation Function" + str(e))
        finally:
            return orientation


    # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    # @Function Name	: change_orientation
    # @Description		: Function to call ChangeOrientation API
    # @Input arguments	: None
    # @Output values	: string    :   orientation
    # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def change_orientation(self):
        orientation = None
        try:
            start_time = self.lib.get_time_stamp()
            changed = self.dut.ChangeOrientation()
            end_time = self.lib.get_time_stamp()
            if changed:
                status = "PASSED"
            else:
                status = "FAILED"
            self.lib.report("API: ChangeOrientation", status, ss_required=True)
            self.lib.report_api_status(start_time, end_time, "ChangeOrientation", status)
            orientation = self.dut.GetOrientation()
        except Exception as e:
            orientation = None
            self.logger.Error("Exception in change_orientation Function" + str(e))
        finally:
            return orientation


    # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    # @Function Name	: verify_set_orientation
    # @Description		: Invokes SetOrientation API and veriies if it works poperly
    # @Input arguments	: None
    # @Output values	: Bool : Returns True if it was able to set a different orientation successfully
    # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def verify_set_orientation(self):
        toggled = False
        status = "FAILED"
        try:
            orient = self.dut.GetOrientation()
            resolution_before_set = self.lib.get_image_resolution()
            if orient is not None:
                new_orient = "PORTRAIT" if orient == "LANDSCAPE" else "LANDSCAPE"
                self.logger.Log("Setting orientation to {}".format(new_orient))
            else:
                return toggled
            start_time = self.lib.get_time_stamp()
            set_changed = self.dut.SetOrientation(new_orient)
            end_time = self.lib.get_time_stamp()
        
            resolution_after_set = self.lib.get_image_resolution()
            if resolution_before_set and resolution_after_set:
                resolution_changed = self.resolution_changed(resolution_before_set, resolution_after_set)
            else:
                self.logger.Error("Error in retrieving resolution")
                return toggled
            if set_changed and resolution_changed:
                status = "PASSED"
                toggled = True
            else:
                status = "FAILED"

            self.lib.report("API: SetOrientation", status, ss_required=True)
            self.lib.report_api_status(start_time, end_time, "SetOrientation", status)
            self.dut.CommitStepResult("API: ChangeOrientation API", status)

        except Exception as e:
            toggled = False
            self.logger.Error("Exception in set_orientation Function" + str(e))
            
        finally:
            return toggled


def main():
    testobj = api_test()
    testobj.run_test(testobj.script_name, testobj.apis)


if __name__ == '__main__':
    main()
