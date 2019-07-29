#计算每张表销售额这一列的总数和平均数
import pandas as pd
import glob
import os
import sys
rpath=sys.argv[1]
wpath=sys.argv[2]
dataframes=[]

for file_path in glob.glob(os.path.join(rpath, "sales_*")):
    dataframe=pd.read_csv(file_path)
    sales_list=[float(str(value).strip("$").replace(",","")) \
                for value in dataframe.loc[:, "Sale Amount"]]
    total_sales=sum(sales_list)
    average_sales=float(total_sales/len(sales_list))
    """total_sales=pd.DataFrame([float(str(value).strip("$").replace(",","")) \
                for value in dataframe.loc[:, "Sale Amount"]]).sum()
    average_sales=pd.DataFrame([float(str(value).strip("$").replace(",","")) \
                for value in dataframe.loc[:, "Sale Amount"]]).mean()"""
    data_dict={"file_name": [os.path.basename(file_path)],
               "total_sales": [total_sales],
               "average_sales": [average_sales]}
    dataframe=pd.DataFrame(data_dict)
    dataframes.append(dataframe)

concat_dataframe=pd.concat(dataframes,axis=0)
concat_dataframe.to_csv(wpath,index=False)