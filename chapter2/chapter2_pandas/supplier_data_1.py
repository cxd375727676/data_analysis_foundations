#pandas数据框读写数据
import pandas as pd
import sys
rpath=sys.argv[1]
wpath=sys.argv[2]
dataframe=pd.read_csv(rpath)
print(dataframe)
dataframe.to_csv(wpath,index=False)