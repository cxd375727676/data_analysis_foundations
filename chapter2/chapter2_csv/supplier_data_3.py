#筛选supplier_data.csv文件中成本大于600或供应商Z的数据
import csv
import sys
rpath=sys.argv[1]
wpath=sys.argv[2]
with open(rpath,"r") as rf:
    with open(wpath,"w") as wf:
        filereader=csv.reader(rf)
        filewriter=csv.writer(wf)
        header=next(filereader)       #filereader是一个迭代器，next进行一次迭代
        filewriter.writerow(header)
        for row_list in filereader:
            supplier=str(row_list[0]).strip()
            cost=str(row_list[3]).strip("$").replace(",","")
            if supplier=="Supplier Z" or float(cost)>600.00:
                filewriter.writerow(row_list)