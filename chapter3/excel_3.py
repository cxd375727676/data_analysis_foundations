#将sales_2013中的january_2013工作表客户姓名以J打头的行筛选出来，写入另外的工作簿中
import sys
import re
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
input_file=sys.argv[1]
output_file=sys.argv[2]
pattern=re.compile(r"^J.*")
output_workbook=Workbook() #准备写入工作簿
output_worksheet=output_workbook.add_sheet("jan_2013_output") #为写入的工作簿添加工作表
with open_workbook(input_file) as workbook:
    worksheet=workbook.sheet_by_name("january_2013") #读取工作簿的一张工作表
   #创建data列表，存储符合条件的行
    data=[worksheet.row_values(0)]           #标题行存入data列表
    for row_index in range(1,worksheet.nrows):
        if pattern.search(worksheet.cell_value(row_index, 1)):
            data.append(worksheet.row_values(row_index))
            
for i,row_list in enumerate(data):
    for j, element in enumerate(row_list):
        output_worksheet.write(i,j, element) #写入单元格
output_workbook.save(output_file)