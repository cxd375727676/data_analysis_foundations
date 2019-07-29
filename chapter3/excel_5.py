#读取sales_2013中的所有工作表，将销售额大于2000的行筛选出来，写入另外的工作簿（表）中
import sys
from xlrd import open_workbook
from xlwt import Workbook
input_file=sys.argv[1]
output_file=sys.argv[2]
output_workbook=Workbook() #准备写入工作簿
output_worksheet=output_workbook.add_sheet("results_fit_all_sheets") #为写入的工作簿添加工作表
with open_workbook(input_file) as workbook:
   #创建data列表，存储符合条件的行
    data=[]           #标题行存入data列表
    active_first_sheet=True
    for worksheet in workbook.sheets():
        #对第一张表加入标题行
        if active_first_sheet:
            data.append(worksheet.row_values(0))
            active_first_sheet=False
            
        for row_index in range(1,worksheet.nrows):
            if worksheet.cell_value(row_index, 3) > 2000:
                data.append(worksheet.row_values(row_index))
            
for i,row_list in enumerate(data):
    for j, element in enumerate(row_list):
        output_worksheet.write(i,j, element) #写入单元格
output_workbook.save(output_file)