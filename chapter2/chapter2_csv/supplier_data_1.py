#利用基础python读写supplier_data.csv文件
import sys

rpath=sys.argv[1]
wpath=sys.argv[2]

with open(rpath,"r") as rf:
    with open(wpath,"w") as wf:
        header=rf.readline()       #文件头，字符串形式
        header=header.strip(" ,\n\r")      #删除两端空格、制表符、换行符、逗号
        header_list=header.split(",")   #以逗号拆分为列表
        print(header_list)              #打印文件头列表
        #确保文件头列表每个元素是字符串形式，并将该列表元素用逗号连接形成字符串，末尾加上换行符
        newheader=",".join(map(str,header_list)) + "\n"
        #写入wf文件
        wf.write(newheader)
        
        for row in rf:# 文件头已经迭代过，从下一行起循环
            row=row.strip(" ,\n\r")
            row_list=row.split(",")
            print(row_list)
            wf.write(",".join(map(str,row_list)) + "\n")