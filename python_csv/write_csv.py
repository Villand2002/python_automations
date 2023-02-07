import csv
import datetime
from datetime import date,timedelta
import calendar

# a+ 読み取り、書き込み用にファイルを開き、存在しない場合は作成するために使用する. 
# 参考:https://stackoverflow.com/questions/44901806/python-error-message-io-unsupportedoperation-not-readable
# mode=xでも新規作成可能:https://note.nkmk.me/python-file-io-open-with/
# csvファイルの指定

file_path='C:\\Users\\st200\\downloads\\calender_csv'

# fileの新規作成の例
# with open(file_path, 'x') as f:
#     reader = csv.reader(f)
       
# foldername = "C:/Labo/python/csv-simpleschedule/"

inputdata = input("Please input year and month(eg:2020/1) >> ")



year, month = (x for x in inputdata.split('/'))
print(type(year)) 
print(type(month)) 
startdate = datetime.date(int(year), int(month), 1)
# lastdate =datetime.date(int(year), int(month), 1)
# filename = foldername + year + month + ".csv"

f= open(file_path, 'w')

startdate = datetime.date(int(year), int(month), 1)  

for i in range(40):
    if (startdate.strftime('%m') != month):
        break

    else:
        f.write(f"{startdate.strftime('%Y')}年{startdate.strftime('%m')}月{startdate.strftime('%d')}日,\n")
    startdate += datetime.timedelta(days=1)

# f.write(f"日付, 予定\n")
# f.write(f"{year}年{month}月1日, \n")

f.close()
    
        
# 参考:https://valed.press/programming-learning/input-output-csv-with-python/
# https://self-development.info/%E3%80%90python%E3%80%91open%E9%96%A2%E6%95%B0%E3%81%A8with%E6%96%87%E3%81%AB%E3%82%88%E3%82%8B%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E4%BD%9C%E6%88%90%E3%83%BB%E8%AA%AD%E3%81%BF%E8%BE%BC%E3%81%BF/