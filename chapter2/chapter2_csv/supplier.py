#利用csv模块读取supplier.csv文件，解决数据嵌入逗号的问题
import csv
import sys
rpath=sys.argv[1]
wpath=sys.argv[2]

with open(rpath,"r") as rf:
    with open(wpath,"w") as wf:
        filereader=csv.reader(rf,delimiter=",")
        filewriter=csv.writer(wf,delimiter=",")
        for row in filereader:
            print(row)
            filewriter.writerow(row)