import csv
import sqlite3
import sys
#记录更新信息的csv文件路径
read_path=sys.argv[1]

#创建SQlite3内存数据库,建立数据表结构
con=sqlite3.connect(":memory:") #":memory:"内存数据库，也可保存在磁盘上
query="CREATE TABLE sales\
        (customer VARCHAR(20),\
         product VARCHAR(40),\
         amount FLOAT,\
         date DATE);"           #varchar(20)变长字符串，最大字符数20
con.execute(query)              #执行创建表的操作
con.commit()                    #对数据库的任何更改都需要保存

#插入数据
#四个记录，每个记录（行）都是四元数组
data=[("Richard Lucas","Notepad",2.50,"2014-01-02"),
      ("Jenny Kim","Binder",4.15,"2014-01-15"),
      ("Svetlana Crow", "Printer", 155.75, "2014-02-03"),
      ("Stephen Randolph","Computer", 679.40, "2014-02-20")] 
#打印原始信息
for tuple in data:
    print(tuple)
#?是占位符，con.executemany对data中每个元组执行命令，?被元组替换
statement="INSERT INTO sales VALUES(?,?,?,?)"
con.executemany(statement,data)
con.commit()

#利用csv文件对数据库进行更新
file_reader=csv.reader(open(read_path,"r"),delimiter=",")
header=next(file_reader,None)
data=[]
for row in file_reader:
    data.append(row)
con.executemany("UPDATE sales SET amount=?,date=? WHERE customer=?",data)
con.commit()
#查询sales表,建立光标对象
cursor=con.execute("SELECT * FROM sales")
rows=cursor.fetchall() #取出查询结果所有行存入rows，rows是一个元组列表
#打印查询结果
for row in rows:
    print(row)