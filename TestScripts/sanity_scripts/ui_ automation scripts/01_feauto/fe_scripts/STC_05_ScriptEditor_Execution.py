# --------------------------------------------------------------------------------------
# TC Id: STC_02
# Module: Scheduler
# TC Summary:  To verify that the job triggering, execution,
#              and report generation happening in the proper way
# TC Steps:     1) Login to the application.
#                 2) Navigate to scheduler tab.
#                 3) Create a job and observe the job behavior.
# Expected: 3)i. Job should get saved without any failure.
#             ii. The job may listed with scheduled status.
#             iii. One minute before the trigger time, status shall change to Ready.
#                   At trigger time status shall change to In Progress and attached scripts
#                   will get executed one by one. After executing the job, status will change
#                   to Completed if there is no other trigger associated with the job,
#                   otherwise status will be Scheduled also next run time may be displayed.
#             iv. After the completion of job execution reports should be available in Reports.
# --------------------------------------------------------------------------------------

# imports
import time, datetime, os
import logging
from fe_auto_config.fe_variables import fe_var as config
from fe_auto_config.feauto import feautotest


class STC_05(feautotest):
    def run(self):
        try:
            sl = self.lib.goto_screen("script_editor")
            if not sl:
                self.report("Failed to navigate to Scheduler Window", "FAILED", logging.WARNING)
                self.script_status = False
                return False
            self.report("Navigated to Scheduler Window", "PASSED", logging.INFO)

            time.sleep(2)

            if not self.lib.open_script(config.keys_to_open_script):
                self.report("Failed to open script", "FAILED", logging.WARNING, screenshot=True)
                self.script_status = False
                return False
            self.report("Opened the script to run", "PASSED", logging.INFO, screenshot=True)

            time.sleep(1)

            if not self.lib.start_local_execution():
                self.report("Failed to start the execution", "FAILED", logging.WARNING, screenshot=True)
                self.script_status = False
                return False
            self.report("Script execution started", "PASSED", logging.INFO, screenshot=True)

            time.sleep(config.wait_until_local_execution)

            # log_file = "D://01_Projects//0101_FE_AUTO//09_pyautoit//scripts//01_feauto//logs_ocrim//logs_18_37_32_451000.txt"
            log_file = self.lib.export_report_to_txt_file(windowname='script_editor')
            if not log_file:
                self.report("Failed to save the Execution log", "FAILED", logging.WARNING, screenshot=True)
                self.script_status = False
                return False

            self.report("Execution log saved to {}".format(log_file), "PASSED", logging.INFO, screenshot=True)

            time.sleep(3)
            print "read"
            test_status = self.lib.read_test_status_from_log_file(log_file)
            if test_status:
                status = "PASSED"
                log = logging.INFO
            else:
                status = "FAILED"
                log = logging.WARNING
                self.script_status = False

            self.report("Local Run Status is {}".format(test_status), status, log)
            self.report("Local Run is happening and the Result is available", status, log)

        except Exception as e:
            self.logger.debug(str(e))


    def exit_test(self):
        super(STC_05, self).exit_test()


def main():
    test_obj = STC_05()
    test_obj.run_test("STC_05", os.path.basename(__file__))
    test_obj.report_test_result()
    test_obj.exit_test()


if __name__ == "__main__":
    main()

# --------------------------------------------------------------------------------------
# Author: Shameena HA
# Date: 31/10/2018
# --------------------------------------------------------------------------------------
