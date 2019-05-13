'''
@desc: idea is to consolidate the fe ui automation reports with passed/failed status
        in a separate sheet.
'''


# imports
import os
import xlsxwriter
import datetime
import xlrd
from fe_auto_config.fe_variables import fe_var


class summarize_report(object):
    # declaration
    def create_summary_report(self):
        '''
        Creates summary report by reading all execution reports
        :return:
        '''

        report_dir = fe_var.report_dir

        time_stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        workbook = xlsxwriter.Workbook("FE_UI_AUTO_SUMMARY_REPORT_{}.xlsx".format(time_stamp))
        # font formats
        header_fmt = workbook.add_format(
            {
                'bold': True, 'border':2,
                'font_color': 'white', 'bg_color': 'gray',
                'align': 'center', 'valign': 'center'
            }
        )
        content_format = workbook.add_format({
            'border':2
        }
        )
        summary_report = workbook.add_worksheet("FE_Auto_Report_Summary")
        summary = ("SL No", "Script Id", "Script Name", "Script Status", "Date of Execution", "Report File Name")

        reports = os.listdir(report_dir)
        print reports
        #
        row_idx = 1
        col_idx = 1
        summary_report.write_row(row_idx, col_idx, summary, header_fmt)

        sl = 0

        for report in reports:
            print report
            script_id = None
            script_name = None
            script_status = None
            exec_date = None
            wb = None
            try:
                wb = xlrd.open_workbook(report_dir+report)
            except Exception as e:
                print "Could not open report. Make sure that all reports are closed before running the script" + str(e)
                exit()

            sheet = wb.sheet_by_name("Execution Report")
            for rowindex in range(sheet.nrows):
                for colindex, cell in enumerate(sheet.row(rowindex)):
                    if cell.value == "Script Id":
                        script_id = sheet.cell_value(rowindex, colindex+1)
                    if cell.value == "Script Name":
                        script_name = sheet.cell_value(rowindex, colindex+1)
                    if cell.value == "Date":
                        exec_date = sheet.cell_value(rowindex, colindex+1)
                    if cell.value == "Script Status":
                        script_status = sheet.cell_value(rowindex, colindex + 1)
            wb.release_resources()
            del wb
            sl += 1
            row_idx += 1
            data = (sl, script_id, script_name, script_status, exec_date) #, report, exec_date)
            summary_report.write_row(row_idx, col_idx, data, content_format)
            summary_report.write_url(row_idx, col_idx+5, report_dir+report, cell_format=content_format,
                  string=report, tip='Report Sheet')
            # print exec_date
            # summary_report.write_row(row_idx, col_idx+4, exec_date, content_format)

        workbook.close()
        print "Report Consolidation finished"


if __name__ == '__main__':
    sum_rpt = summarize_report()
    sum_rpt.create_summary_report()
