import os
import sys
from fe_auto_config.fe_variables import fe_var
from febatch_executor.report_consolidator import summarize_report
script_dir = fe_var.script_dir
scripts = os.listdir(script_dir)

# adding script path to the system path
sys.path.insert(0, script_dir)

class batch_executor(object):
    def run_batch(self):
        if not scripts:
            print "script path not valid"

        for script in scripts:
            if script is not ( not "__init__.py" and os.path.isfile(script) and not script.endswith(".pyc")):
                print "script", script
                script = script.replace(".py", "")
                print script
                try:
                    fescript = __import__(script)
                    fescript.main()
                except Exception as e:
                    print "import failed"
            else:
                print "not a valid script"


def main():
    # for batch execution
    batch_exec = batch_executor()
    batch_exec.run_batch()
    # generate report summary
    rpt = summarize_report()
    rpt.create_summary_report()


if __name__ == "__main__":
    main()
