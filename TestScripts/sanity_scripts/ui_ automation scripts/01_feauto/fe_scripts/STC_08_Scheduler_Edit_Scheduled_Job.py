# --------------------------------------------------------------------------------------
# TC Id: STC_08
# Module: Scheduler
# TC Summary:  To verify Delete Job functionality in scheduler
# TC Steps:    Creates multiple jobs as configured in the config file and
#               deletes all those jobs
#
# --------------------------------------------------------------------------------------

# imports
import time, datetime, os
import logging
from fe_auto_config.fe_variables import fe_var as config
from fe_auto_config.feauto import feautotest


class STC_08(feautotest):
    def create_jobs(self):

        # getting number of jobs to be created from Config file
        jobs = config.no_of_jobs

        sl = self.lib.goto_screen("scheduler")
        if not sl:
            self.report("Failed to navigate to Scheduler Window", "FAILED", logging.WARNING)
            self.script_status = False
            return False
        self.report("Navigated to Scheduler Window", "PASSED", logging.INFO)
        while(jobs):
            current_time = self.get_timestamp_formatted()
            print current_time
            job_name = config.fe_test_job_name.format(current_time)

            # trigger after 5 minutes
            if not self.lib.create_job(job_name, trigger_time=None):
                logging.warning("Failed to create job {}".format("FE_test_job_"+job_name))
                self.script_status = False
                return False

            self.report("Created a job - {}".format("FE_test_job_"+job_name), "PASSED", logging.INFO, screenshot=True)
            jobs -= 1
        return True


    def run(self):
        try:
            # creating multiple jobs in scheduler
            if not self.create_jobs():
                self.report("Failed to create multiple jobs", "FAILED", logging.WARNING, screenshot=True)
                self.script_status = False
                return False

            if not self.lib.search_scheduler_job(config.fe_job_name):
                self.report("Failed to get the search result", "FAILED", logging.WARNING, screenshot=True)
                self.script_status = False
                return False
            self.report("Search result obtained", "PASSED", logging.INFO, screenshot=True)
            self.report("Jobs are created and those are available in search result", "PASSED", logging.INFO, screenshot=True)

            time.sleep(1)   # min wait before delete
            for job in range(0, config.no_of_jobs):
                print "job", job
                if not self.lib.delete_job():
                    self.report("Failed to delete {} job".format(job), "FAILED", logging.WARNING, screenshot=True)
                    self.script_status = False
                    return False

                self.report("Deleted {} job".format(job), "PASSED", logging.WARNING, screenshot=True)
                time.sleep(3)   #wait between the deletions

        except Exception as e:
            self.logger.debug(str(e))


    def exit_test(self):
        try:
            if not self.script_status:
               self.lib.delete_job()

        except Exception as e:
            logging.warning("No jos found to be deleted")
        super(STC_08, self).exit_test()


def main():
    test_obj = STC_08()
    test_obj.run_test("STC_08", os.path.basename(__file__))
    test_obj.report_test_result()
    test_obj.exit_test()


if __name__ == "__main__":
    main()

# --------------------------------------------------------------------------------------
# Author: Shameena HA
# Date: 25/10/2018
# --------------------------------------------------------------------------------------
