#选择供应商和成本列(列指标0、3)
import pandas as pd
import sys
rpath=sys.argv[1]
wpath=sys.argv[2]

dataframe=pd.read_csv(rpath)
dataframe_column_by_index=dataframe.iloc[:,[0,3]]
dataframe_column_by_index.to_csv(wpath,index=False)