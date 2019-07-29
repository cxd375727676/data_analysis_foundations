#连接多个工作簿、工作表
import glob
import sys
import os
from xlrd import open_workbook
from xlwt import Workbook
files_path=sys.argv[1]
output_path=sys.argv[2]
output_workbook=Workbook()
output_worksheet=output_workbook.add_sheet("all_data_concat")
data=[]
first_sheet=True
for file_path in glob.glob(os.path.join(files_path,"*.xlsx")):
    with open_workbook(file_path) as workbook:
        for worksheet in workbook.sheets():
            if first_sheet:
                header=worksheet.row_values(0)
                data.append(header)
                first_sheet=False
            for row_index in range(1,worksheet.nrows):
                data.append(worksheet.row_values(row_index))

for i, row_list in enumerate(data):
    for j, element in enumerate(row_list):
        output_worksheet.write(i,j,element)
output_workbook.save(output_path)