#pandas读取所有工作表，汇总销售额大于2000的结果到另一张工作表
import pandas as pd
import sys
input_file=sys.argv[1]
output_file=sys.argv[2]
dataframe=pd.read_excel(input_file,sheetname=None,index_col=None)
output_list=[]     #筛选的数据框组成的列表
for worksheet_name,data in dataframe.items():
    output_list.append(data[data["Sale Amount"].astype(float) >2000.0])

#连接筛选后的数据框列表
filter_output=pd.concat(output_list, axis=0, ignore_index=True)
#声称存储对象
writer=pd.ExcelWriter(output_file)
#写入filter_output
filter_output.to_excel(writer,sheet_name="sale>2000" ,index=False)
writer.save()