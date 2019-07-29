#将supplier_data.csv文件中的数据导入mysql数据库
import csv
import MySQLdb
import sys
from datetime import datetime,date
read_path=sys.argv[1]

con=MySQLdb.connect(host="localhost",port=3306,db="my_suppliers",
                     user="root",passwd="")
c=con.cursor()      #建立游标对象，用于处理sql语句返回结果
file_reader=csv.reader(open(read_path,"r",newline=""))
header=next(file_reader)
for row in file_reader:
    #对于每行创建一个列表data记录结果，注意格式化日期符合mysql数据库格式
    #日期在第5列，列索引4
    data=[]
    for column_index in range(len(header)):
        if column_index<4:
            data.append(str(row[column_index]).lstrip("$").replace(",","").strip())
        else:
            a_date=str(row[column_index]) #获取csv文件中日期的字符串形式(月/日/年)
            a_date=datetime.strptime(a_date, "%m/%d/%Y") #利用上述字符串生成日期的datetime对象
            a_date=datetime.date(a_date)   #截取日期部分，生成date对象
            a_date=a_date.strftime("%Y-%m-%d") #利用date对象格式化输出为mysql接受的日期字符串
            data.append(a_date)
    c.execute("insert into Suppliers values(%s,%s,%s,%s,%s);",data)
con.commit()
#查询
c.execute("select * from Suppliers")
rows=c.fetchall()
for row in rows:
    print(row)