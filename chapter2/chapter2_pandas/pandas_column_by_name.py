#保留发票代码和购买日期
import pandas as pd
import sys
rpath=sys.argv[1]
wpath=sys.argv[2]

dataframe=pd.read_csv(rpath)
dataframe_column_by_name=dataframe.loc[:,["Invoice Number", "Purchase Date"]]
dataframe_column_by_name.to_csv(wpath,index=False)