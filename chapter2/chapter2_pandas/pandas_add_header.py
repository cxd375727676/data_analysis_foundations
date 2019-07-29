#添加列标题
import pandas as pd
import sys
rpath=sys.argv[1]
wpath=sys.argv[2]

head_row=["Supplier Name", "Invoice Number", "Part Number", "Cost", "Purchase Date"]
dataframe=pd.read_csv(rpath,header=None, names=head_row)
dataframe.to_csv(wpath,index=False)