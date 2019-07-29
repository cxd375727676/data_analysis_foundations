# 选出文件中的供应商和成本这两列，对应索引0，3
import csv
import sys
rpath=sys.argv[1]
wpath=sys.argv[2]
select_columns=[0,3]
with open(rpath,"r") as rf:
    with open(wpath,"w") as wf:
        filereader=csv.reader(rf)
        filewriter=csv.writer(wf)
        for row_list in filereader:
            select_row_list=[]
            for index in select_columns:
                select_row_list.append(row_list[index])
            filewriter.writerow(select_row_list)