#计算sales_files文件夹中每个文件的销售总量和平均量
import csv
import sys
import os
import glob
output_header=["file name","total sales","average sales"]
rpath=sys.argv[1]
wpath=sys.argv[2]
with open(wpath,"w",newline="") as wf:
    writefile=csv.writer(wf)
    writefile.writerow(output_header)
    for file_path in glob.glob(os.path.join(rpath,"sales_*")):
        
        with open(file_path,"r",newline="") as rf:
            readfile=csv.reader(rf)
            header=next(readfile)
            sales_counter=0
            sales_sum=0.0
            for row in readfile:
                sales_counter+=1
                sales_sum+=float(str(row[3]).strip("$").replace(",",""))
        average_sales="{0:.2f}".format(sales_sum/sales_counter)
        output_result=[os.path.basename(file_path), sales_sum, average_sales]
        writefile.writerow(output_result)