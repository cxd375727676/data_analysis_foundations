#搜索项目
import csv
import glob
import os
import sys
from xlrd import open_workbook
item_numbers_file=sys.argv[1] #搜索条件文件路径
path_to_folder=sys.argv[2]    #文件夹所在路径
output_file=sys.argv[3]       #输出结果保存路径(写入csv文件)

#读取搜索条件文件，以列表形式存储
item_numbers_to_find=[]
with open(item_numbers_file,"r",newline="") as item_numbers_csv_file:
    filereader=csv.reader(item_numbers_csv_file)
    for row in filereader:
        item_numbers_to_find.append(row[0])

filewriter=csv.writer(open(output_file,"a",newline=""))
file_counter=0                 #文件夹包含文件总数
line_counter=0                 #所有文件包含的记录总数
count_of_item_numbers=0        #符合搜索条件的记录数

#读取文件夹中的文件，依不同格式类型处理
for input_file in glob.glob(os.path.join(path_to_folder,"*.*")):
    file_counter+=1
    #csv文件
    if input_file.split(".")[1]=="csv":
        with open(input_file, "r",newline="") as csv_in_file:
            filereader=csv.reader(csv_in_file)
            header=next(filereader)
            #将csv文件中每一行格式化存入列表(cost列需去掉美元符号及可能包含的逗号)
            #并将csv文件名加入列表末尾
            for row in filereader:
                line_counter+=1
                row_of_output=[]
                for c_index in range(len(header)):
                    row_of_output.append(str(row[c_index]).lstrip("$").replace(",","").strip())
                row_of_output.append(os.path.basename(input_file))
                 #搜索符合条件的行
                if row[0] in item_numbers_to_find:    #row[0]=row_of_output[0]
                     filewriter.writerow(row_of_output)
                     count_of_item_numbers+=1
    #excel文件            
    elif input_file.split(".")[1]=="xls" or input_file.split(".")[1]=="xlsx":
        workbook=open_workbook(input_file)
        for worksheet in workbook.sheets():
            try:
                header=worksheet.row_values(0)
            except IndexError:
                pass
            #将excel工作表每行格式化存入列表，并将工作簿名、表名加入列表末尾
            for row in range(1,worksheet.nrows):
                line_counter+=1
                row_of_output=[]
                for c_index in range(len(header)):
                   row_of_output.append(str(worksheet.cell_value(row,c_index)).strip()) 
                row_of_output.append(os.path.basename(input_file))
                row_of_output.append(worksheet.name)
                #搜索符合条件的行
                if  str(worksheet.cell_value(row,0)).split(".")[0].strip() in item_numbers_to_find:
                    filewriter.writerow(row_of_output)
                    count_of_item_numbers+=1

print("Number of files: "+str(file_counter))
print("Number of lines: "+str(line_counter))
print("Number of item numbers: "+str(count_of_item_numbers))