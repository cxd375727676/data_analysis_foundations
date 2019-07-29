#利用loc、isin函数选择符合条件的行：1/20/2014, 1/30/2014
import sys
import pandas as pd
rpath=sys.argv[1]
wpath=sys.argv[2]
dataframe=pd.read_csv(rpath)
important_dates=["1/20/2014", "1/30/2014"]
conditional_dataframe=dataframe.loc[dataframe["Purchase Date"].isin(important_dates) , :]
conditional_dataframe.to_csv(wpath,index=False)