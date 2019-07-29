import sqlite3
import csv
import sys
read_path=sys.argv[1]
con=sqlite3.connect("Supplier.db") 
create_table="CREATE TABLE IF NOT EXISTS Suppliers\
        (Supplier_Name VARCHAR(20),\
         Invoice_Number VARCHAR(20),\
         Part_Number VARCHAR(20),\
         Cost FLOAT,\
         Purchase_Date DATE);"         
con.execute(create_table)
con.commit()

file_reader=csv.reader(open(read_path,"r"),delimiter=",")
header=next(file_reader,None)
data=[]
for row in file_reader:
    data.append(row)
statement="INSERT INTO Suppliers VALUES(?,?,?,?,?)"
con.executemany(statement,data)
con.commit()

cursor=con.execute("SELECT * FROM Suppliers")
rows=cursor.fetchall()
for row in rows:
    print(row)