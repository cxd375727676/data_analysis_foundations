#将sales_2013中的january_2013工作表保留姓名、日期【index=1，4】写入另外的工作簿中
import sys
from xlrd import open_workbook
from xlwt import Workbook
input_file=sys.argv[1]
output_file=sys.argv[2]
my_columns_index=[1,4]
output_workbook=Workbook() #准备写入工作簿
output_worksheet=output_workbook.add_sheet("jan_2013_output") #为写入的工作簿添加工作表
with open_workbook(input_file) as workbook:
    worksheet=workbook.sheet_by_name("january_2013") #读取工作簿的一张工作表
   #创建data列表，存储结果【以行为单位，列表的列表】
    data=[]
    for row_index in range(worksheet.nrows):
        row_list=[]
        for column_index in my_columns_index:
            row_list.append(worksheet.cell_value(row_index,column_index))
        data.append(row_list)

for i,row_list in enumerate(data):
    for j, element in enumerate(row_list):
        output_worksheet.write(i,j, element) #写入单元格
output_workbook.save(output_file)