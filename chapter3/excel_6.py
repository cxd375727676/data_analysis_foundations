#读取sales_2013中的所有工作表，将Customer Name和Sale Amount列筛选出来，写入另外的工作簿（表）中
import sys
from xlrd import open_workbook
from xlwt import Workbook
input_file=sys.argv[1]
output_file=sys.argv[2]
my_columns=["Customer Name", "Sale Amount"]
output_workbook=Workbook() #准备写入工作簿
output_worksheet=output_workbook.add_sheet("results_fit_all_sheets") #为写入的工作簿添加工作表
with open_workbook(input_file) as workbook:
   #创建data列表，存储符合条件的行
    data=[my_columns]           #标题行存入data列表
    active_first_sheet=True
    for worksheet in workbook.sheets():
        if active_first_sheet:
            header=worksheet.row_values(0)
            select_column_index=[]
            for column_index in range(len(header)):
                if header[column_index] in my_columns:
                    select_column_index.append(column_index)
            active_first_sheet=False
    
        for row_index in range(1,worksheet.nrows):
            row_list=[]
            for column_index in select_column_index:
                row_list.append(worksheet.cell_value(row_index,column_index))
            data.append(row_list)      
            
for i,row_list in enumerate(data):
    for j, element in enumerate(row_list):
        output_worksheet.write(i,j, element) #写入单元格
output_workbook.save(output_file)