#利用startswith函数选择001打头的的行
import sys
import pandas as pd
rpath=sys.argv[1]
wpath=sys.argv[2]
dataframe=pd.read_csv(rpath)
conditional_dataframe=dataframe.loc[dataframe["Invoice Number"].str.startswith("001-")  , :]
conditional_dataframe.to_csv(wpath,index=False)