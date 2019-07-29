#将sales_2013中的january_2013工作表销售额大于1400的行筛选出来，写入另外的工作簿中
import sys
from xlrd import open_workbook
from xlwt import Workbook
input_file=sys.argv[1]
output_file=sys.argv[2]
output_workbook=Workbook() #准备写入工作簿
output_worksheet=output_workbook.add_sheet("jan_2013_output") #为写入的工作簿添加工作表
aim_col=3   #销售额列索引3
with open_workbook(input_file) as workbook:
    worksheet=workbook.sheet_by_name("january_2013") #读取工作簿的一张工作表
   #创建data列表，存储符合条件的行
    data=[worksheet.row_values(0)]           #标题行存入data列表
    for row_index in range(1,worksheet.nrows):
        if worksheet.cell_value(row_index, aim_col) > 1400.0:
            data.append(worksheet.row_values(row_index))
            
for i,row_list in enumerate(data):
    for j, element in enumerate(row_list):
        output_worksheet.write(i,j, element) #写入单元格
output_workbook.save(output_file)