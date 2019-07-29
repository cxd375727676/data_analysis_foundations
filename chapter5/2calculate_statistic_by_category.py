import csv
import sys
from datetime import date, datetime

def date_diff(date1,date2):
    """给定两个日期字符串%m/%d/%Y，返回相差的整数天数（int型）"""
    diff=datetime.strptime(date1,"%m/%d/%Y")-datetime.strptime(date2,"%m/%d/%Y")
    diff=str(diff).split()[0]   #以空格分割字符串，取days的部分（天数）
    diff=int(diff)
    return diff

input_file=sys.argv[1]
output_file=sys.argv[2]

dict={}     #嵌套的字典
pre_name="hehe"
pre_service="hehe"
pre_service_date="hehe"
first_row=True

#今天的日期用下面的语句，但是书中的“今天”是2015年10月11日
#today=date.today().strftime("%m/%d/%Y")    
today="10/11/2015"

with open(input_file,"r",newline="") as input_csv_file:
    filereader=csv.reader(input_csv_file)
    header=next(filereader)
    for row in filereader:
        #读入当前行的姓名、业务及购买日期
        c_name=row[0]
        c_service=row[1]
        c_service_date=row[3]
        
        #构造字典，初始化
        if c_name not in dict.keys():
            dict[c_name]={}
        if c_service not in dict[c_name].keys():
            dict[c_name][c_service]=0
        
        #判断顾客是否已经切换，如果切换了，则将上一个顾客最后一次购买服务迄今的时间段加上去；
           #注意读入第一个记录时，顾客姓名总是从hehe切换为读入值，但是不存在上一个客户，无需计算
        #如果没有切换，则将当前业务购买日期到上次购买业务的日期这一时间段加上去
        if c_name!=pre_name:
            if first_row:
                first_row=False
            else:
                dict[pre_name][pre_service]+=date_diff(today,pre_service_date)
        else:
            dict[pre_name][pre_service]+=date_diff(c_service_date,pre_service_date)
            
        pre_name=c_name
        pre_service=c_service
        pre_service_date=c_service_date

#将dict信息输出为csv文件
header=["customer Name", "Category", "Total Time (in Days)"]
with open(output_file,"w",newline="") as output_csv_file:
    filewriter=csv.writer(output_csv_file)
    filewriter.writerow(header)
    for name,package in dict.items():
    #若将信息按姓名首字母排序输出，则可以改为
     #for name,package in sorted(dict.items(),key=lambda x:x[0]):
        for service,days in package.items():
            print(name,service,days)
            rowlist=[name,service,days]
            filewriter.writerow(rowlist)