#利用loc函数选择符合条件的行
import sys
import pandas as pd
rpath=sys.argv[1]
wpath=sys.argv[2]
dataframe=pd.read_csv(rpath)
dataframe["Cost"]=dataframe["Cost"].str.strip("$").astype(float)
conditional_dataframe=dataframe.loc[(dataframe["Cost"]>600.0) | (dataframe["Supplier Name"].str.contains("Z")) , :]
conditional_dataframe.to_csv(wpath,index=False)