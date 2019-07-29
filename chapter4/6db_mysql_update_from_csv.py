#利用csv文件更新数据库
import csv
import MySQLdb
import sys

input_path=sys.argv[1]
con=MySQLdb.connect(host="localhost",port=3306,db="my_suppliers",user="root",passwd="")
c=con.cursor()

file_reader=csv.reader(open(input_path,"r",newline=""),delimiter=",")
header=next(file_reader,None)
for row in file_reader:
    print(row)
    c.execute("update Suppliers set cost=%s,purchase_date=%s where supplier_name=%s;", row)
    con.commit()

c.execute("select * from suppliers")
rows=c.fetchall()
for row in rows:
    print(row)