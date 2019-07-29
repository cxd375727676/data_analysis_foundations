import sys
from xlrd import open_workbook
from xlwt import Workbook
input_file=sys.argv[1]
output_file=sys.argv[2]
output_workbook=Workbook() #准备写入工作簿
output_worksheet=output_workbook.add_sheet("jan_2013_output") #为写入的工作簿添加工作表

with open_workbook(input_file) as workbook:
    worksheet=workbook.sheet_by_name("january_2013") #读取工作簿的一张工作表
    for row_index in range(worksheet.nrows):
        for column_index in range(worksheet.ncols):
            output_worksheet.write(row_index,column_index, worksheet.cell_value(row_index,column_index)) #写入单元格
output_workbook.save(output_file)