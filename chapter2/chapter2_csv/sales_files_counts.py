# 文件数、行列数计数
import csv
import glob
import os
import sys
files_path=sys.argv[1]
files_counter=0
for file_path in glob.glob(os.path.join(files_path, "sales_*")):
    files_counter+=1
    with open(file_path,"r") as file:
        filereader=csv.reader(file)
        header=next(filereader)
        row_counter=1
        for row in filereader:
            row_counter+=1
    print("{0}: \t{1} rows \t{2} columns".format(os.path.basename(file_path),
          row_counter, len(header)))
print("Number of files: "+str(files_counter))