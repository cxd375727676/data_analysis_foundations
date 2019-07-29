# 连接sales_files文件
import csv
import glob
import os
import sys
files_path=sys.argv[1]
write_path=sys.argv[2]

active=True
for file_path in glob.glob(os.path.join(files_path,"sales_*")):
    print(os.path.basename(file_path))
    with open(file_path, "r",newline="") as rf:
        with open(write_path,"a",newline="") as wf:
            filereader=csv.reader(rf)
            filewriter=csv.writer(wf)
            if active:
                for row in filereader:
                    filewriter.writerow(row)
                active=False
            else:
                header=next(filereader)
                for row in filereader:
                    filewriter.writerow(row)