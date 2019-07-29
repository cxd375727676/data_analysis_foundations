#利用pandas模块读写supplier_data.csv文件
import sys
import pandas as pd

rpath=sys.argv[1]
wpath=sys.argv[2]
dataframe=pd.read_csv(rpath)
print(dataframe)
dataframe.to_csv(wpath,index=False)