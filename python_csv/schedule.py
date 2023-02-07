import csv
import datetime
from datetime import date,timedelta
import calendar



# データを入力
inputdata = input("Please input year and month(eg:2020/01/01) >> ")

# /で区切ってそれぞれをデータとして取得する.
year, month = (x for x in inputdata.split('/'))

# csvの作成場所
file_path=f'C:\\Users\\st200\\downloads\\{year}_{month}.csv'


# with open(file_path,"x") as f:
f= open(file_path, 'x')

# goodle calendarの書式に合わせて設定
f.write(f"Subject,Start Date,End Date\n")

startdate = datetime.date(int(year), int(month), 1)  

for i in range(40):
    # 月が替わったらやめる.
    if (startdate.strftime('%m') != month):
        break
    else:
        # csvに書き込む
        f.write(f",{startdate.strftime('%m')}/{startdate.strftime('%d')}/{startdate.strftime('%Y')},{startdate.strftime('%m')}/{startdate.strftime('%d')}/{startdate.strftime('%Y')}\n")
    # 日付を加算
    startdate += datetime.timedelta(days=1)

# ファイルを閉じる
f.close()


# 参考:https://opty-life.com/study/program/python/python-lecture-23/
# https://non-dimension.com/python-googlecalendarapi/