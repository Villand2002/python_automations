import csv
import datetime
from datetime import date,timedelta
import calendar



nihongo = ['日', '月', '火', '水', '木', '金', '土']

# データを入力
inputdata = input("Please input year and month(eg:2020/01) >> ")
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
        f.write(f",{startdate.strftime('%Y')}年{startdate.strftime('%m')}月{startdate.strftime('%d')}日({nihongo[int(startdate.strftime('%w'))]}),{startdate.strftime('%Y')}年{startdate.strftime('%m')}月{startdate.strftime('%d')}日({nihongo[int(startdate.strftime('%w'))]})\n")
    # 日付を加算
    startdate += datetime.timedelta(days=1)

# ファイルを閉じる
f.close()


# 参考:https://opty-life.com/study/program/python/python-lecture-23/