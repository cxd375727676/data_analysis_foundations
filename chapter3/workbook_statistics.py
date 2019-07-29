#分层次计算销售的总量和平均值
import glob
import sys
import os
from xlrd import open_workbook
from xlwt import Workbook
files_path=sys.argv[1]
output_path=sys.argv[2]
output_workbook=Workbook()
output_worksheet=output_workbook.add_sheet("all_data_statistics")
data=[]
for file_path in glob.glob(os.path.join(files_path,"*.xlsx")):
    with open_workbook(file_path) as workbook:
        book_sum=0.0
        book_number=0
        data_workbook=[["Workbook: "+os.path.basename(file_path), "total sales", "average sales"]]
        for worksheet in workbook.sheets():
            sheet_number=worksheet.nrows-1
            sheet_sum=0.0
            for row_index in range(1,worksheet.nrows):
                sheet_sum+=float(str(worksheet.cell_value(row_index,3)).strip("$").replace(",",""))
            book_sum+=sheet_sum
            book_number+=sheet_number
            data_workbook.append(["Worksheet: "+worksheet.name, sheet_sum,  round(sheet_sum/sheet_number,2)])
        data_workbook.append(["book-level", book_sum, round(book_sum/book_number,2)])
        data.extend(data_workbook)

for i, row_list in enumerate(data):
    for j, element in enumerate(row_list):
        output_worksheet.write(i,j,element)
output_workbook.save(output_path)