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


class STC_02(feautotest):
    def run(self):
        try:
            sl = self.lib.goto_screen("scheduler")
            if not sl:
                self.report("Failed to navigate to Scheduler Window", "FAILED", logging.WARNING)
                self.script_status = False
                return False
            self.report("Navigated to Scheduler Window", "PASSED", logging.INFO)

            time.sleep(2)

            current_time = self.get_timestamp_formatted()
            print current_time
            job_name = config.fe_test_job_name.format(current_time)
            # trigger after 5 minutes
            if not self.lib.create_job(job_name,
                                       trigger_time=(0, 0, config.default_trigger_delay,0)
                                       ):
                self.report("Failed to create job", "FAILED", logging.WARNING)
                self.script_status = False
                return False

            self.report("Created a job - {}".format(job_name), "PASSED", logging.INFO, screenshot=True)

            if not self.lib.search_scheduler_job(current_time):
                self.report("Failed to get the search result", "FAILED", logging.WARNING, screenshot=True)
                self.script_status = False
                return False
            self.report("Search result obtained", "PASSED", logging.INFO, screenshot=True)

            self.logger.info("Waiting for the scheduled job to fire..")

            print "wait", (config.default_trigger_delay-1) * 60
            time.sleep((config.default_trigger_delay-1) * 60)

            status_changed = False
            status = None
            # reading ocr with an iterval of 5 seconds in one minute
            for i in range (0, 12):
                print "2"
                status = self.lib.get_text(region=config.c_job_status_list)
                print status
                if ("Ready" in status) or ("InProgress" in status):
                    status_changed = True
                    break
                else:
                    # to wait for the status to change before the next ocr read
                    time.sleep(5)

            if status_changed:
                self.report("Job Status changed to {}".format(status), "PASSED", logging.INFO, screenshot=True)
            else:
                self.report("Failed to change the job status - {}".format(status), "FAILED", logging.WARNING, screenshot=True)
                # self.script_status = False

            logging.info("Waiting for {} seconds for the run to complete".format(config.wait_until_schedule_execution))

            time.sleep(config.wait_until_schedule_execution)

            # going to reports tab
            rpt = self.lib.goto_screen("reports")
            if not rpt:
                self.report("Failed to navigate to Reports Window", "FAILED", logging.WARNING)
                self.script_status = False
                return False
            self.report("Navigated to Reports Window", "PASSED", logging.INFO)

            self.lib.sendkeys((config.tab, config.tab), interval=1)

            self.lib.sendkey(current_time)

            self.lib.sendkey(config.enter)
            time.sleep(2)   # to load the run report

            jobinreports = False
            job_in_reports = self.lib.get_text(config.c_job_in_report)
            if "fe_test" in job_in_reports or current_time in job_in_reports:
                jobinreports = True

            if jobinreports:
                self.report("Job executed and the report is available in Reports", "PASSED", logging.INFO, screenshot=True)
            else:
                self.report("Failed to find the job name in Reports", "FAILED", logging.WARNING, screenshot=True)
                self.script_status = False

            if not self.lib.expand_job():
                self.report("Could not open the reports", "FAILED", logging.WARNING, screenshot=True)
                self.script_status = False
                return False

            self.report("Opened the report", "PASSED", logging.INFO, screenshot=True)

            time.sleep(3)   # waiting to open the report
            read_result = self.lib.get_test_result()
            if not read_result:
                self.report("Failed to read the test result", "FAILED", logging.WARNING, screenshot=True)
                self.script_status = False
                # return False
            else:
                self.report("Test Result is {}".format(read_result), "PASSED", logging.INFO, screenshot=True)

            log_file = self.lib.export_report_to_txt_file(windowname='reports')
            if not log_file:
                self.report("Failed to save the Execution log", "FAILED", logging.WARNING, screenshot=True)
                self.script_status = False
                return False

            self.report("Execution log saved to {}".format(log_file), "PASSED", logging.INFO, screenshot=True)

            time.sleep(3)
            print "read"
            test_status = self.lib.read_test_status_from_log_file(log_file)
            print "log status", test_status
            if test_status in config.possible_test_results.upper():
                status = "PASSED"
                log = logging.INFO
            else:
                status = "FAILED"
                log = logging.WARNING
                self.script_status = False

            self.report("Scheduled Run Status is {}".format(test_status), status, log)
            self.report("Scheduled Run is happening and the Result is available in Reports", status, log)

        except Exception as e:
            self.logger.debug(str(e))


    def exit_test(self):
        try:
            if not self.lib.goto_screen("scheduler"):
                   return False

            # if not self.lib.delete_job():
            #     return False

        except Exception as e:
            logging.warning("Failed to delete the scheduled jobs")
            self.script_status = False
            return False
        finally:
            super(STC_02, self).exit_test()


def main():
    test_obj = STC_02()
    test_obj.run_test("STC_02", os.path.basename(__file__))
    test_obj.report_test_result()
    test_obj.exit_test()


if __name__ == "__main__":
    main()

# --------------------------------------------------------------------------------------
# Author: Shameena HA
# Date:
# --------------------------------------------------------------------------------------
