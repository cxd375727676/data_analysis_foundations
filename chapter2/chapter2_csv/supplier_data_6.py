#利用列标题名进行筛选
import csv
import sys
rpath=sys.argv[1]
wpath=sys.argv[2]
select_columns=["Purchase Date","Invoice Number"]
with open(rpath,"r") as rf:
    with open(wpath,"w") as wf:
        filereader=csv.reader(rf)
        filewriter=csv.writer(wf)
        header=next(filereader)
        select_columns_index=[]
        for index in range(len(header)):
            if header[index] in select_columns:
                select_columns_index.append(index)
        #注意select_header与select_columns的区别，前者能与列输出顺序保持一致
        select_header=[header[index] for index in select_columns_index]
        filewriter.writerow(select_header)    
        for row_list in filereader:
            select_row_list=[]
            for index in select_columns_index:
                select_row_list.append(row_list[index])
            filewriter.writerow(select_row_list)