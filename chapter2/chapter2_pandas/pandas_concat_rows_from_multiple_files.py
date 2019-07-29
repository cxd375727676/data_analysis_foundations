#合并三张表
import pandas as pd
import glob
import os
import sys
rpath=sys.argv[1]
wpath=sys.argv[2]
dataframes=[]

for file_path in glob.glob(os.path.join(rpath, "sales_*")):
    dataframe=pd.read_csv(file_path)
    dataframes.append(dataframe)
concat_dataframe=pd.concat(dataframes,axis=0)
concat_dataframe.to_csv(wpath, index=False)