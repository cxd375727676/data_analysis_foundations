#从数据库suppliers表中选出cost>1000的记录，写入csv文件
import csv
import MySQLdb
import sys
output_path=sys.argv[1]
con=MySQLdb.connect(host="localhost",port=3306,db="my_suppliers",user="root",passwd="")
c=con.cursor()
filewriter=csv.writer(open(output_path,"w",newline=""),delimiter=",")
header=["Supplier Name", "Invoice Number", "Part Number", "Cost", "Purchase Date"]
filewriter.writerow(header)

c.execute("select * from suppliers where cost>700.0;")
rows=c.fetchall()
for row in rows:
    filewriter.writerow(row)