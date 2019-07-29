#筛选supplier_data.csv文件中Invoice以001-打头的数据,正则表达式匹配
import csv
import sys
import re
rpath=sys.argv[1]
wpath=sys.argv[2]
pattern=re.compile(r"^001-.*" ,re.I)
with open(rpath,"r") as rf:
    with open(wpath,"w") as wf:
        filereader=csv.reader(rf)
        filewriter=csv.writer(wf)
        header=next(filereader)       #filereader是一个迭代器，next进行一次迭代
        filewriter.writerow(header)
        for row_list in filereader:
            invoice_number=str(row_list[1]).strip()
            if pattern.search(invoice_number):
                filewriter.writerow(row_list)