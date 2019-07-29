#删去csv文件的头尾（0、1、2、16、17、18）
import pandas as pd
import sys
rpath=sys.argv[1]
wpath=sys.argv[2]

dataframe=pd.read_csv(rpath, header=None)
dataframe=dataframe.drop([0,1,2,16,17,18])
dataframe.columns=dataframe.iloc[0]
dataframe=dataframe.drop(3)
dataframe.to_csv(wpath,index=False)