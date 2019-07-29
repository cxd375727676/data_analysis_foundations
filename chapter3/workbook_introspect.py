import sys
import os
import glob
from xlrd import open_workbook
filespath=sys.argv[1]
workbook_counter=0

for filepath in glob.glob(os.path.join(filespath, "*.xlsx")):
    with open_workbook(filepath) as workbook:
        print("\nWorkbook:", os.path.basename(filepath))
        print("Number of worksheets:", workbook.nsheets)
        for worksheet in workbook.sheets():
            print("Worksheet Name:",worksheet.name,"\tRows:",worksheet.nrows,"\tColumns:",worksheet.ncols)
        workbook_counter+=1
print("Number of Workbooks:",workbook_counter)