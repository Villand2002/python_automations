import csv
import datetime
from datetime import date,timedelta
import calendar
import time
# osとsys は標準ライブラリ
# https://qiita.com/jp0003menegi/items/fbf407af7d294c09481a
import os
# pip install keyboard
# 参考:https://kuku81kuku81.hatenablog.com/entry/2022/06/19_python_endofprocessingbykeyinput
# https://kuku81kuku81.hatenablog.com/entry/2022/06/07_python_keyinputjudgement
import keyboard

import sys

# csvの作成場所
file_path=f'C:\\Users\\st200\\downloads\\schedule.csv'


# with open(file_path,"x") as f:
f= open(file_path, 'x')

# goodle calendarの書式に合わせて設定
f.write("Subject,Start Date,End Date\n")

for i in range(40):
    # データを入力
    print("入力終了の時はxを入れてください.")
    Subject=input("予定は何でしょうか:")
    startdata = input("予定の日にちは?(例:2020/01/01) >> ")
    enddata = input("予定はいつ終了しますか?(例:2020/01/01) >> ")
    # /で区切ってそれぞれをデータとして取得する.
    startyear, startmonth,startdate = (x for x in startdata.split('/'))
    endyear, endmonth,enddate = (x for x in enddata.split('/'))
    startdate = datetime.date(int(startyear), int(startmonth), int(startdate))  
    enddate = datetime.date(int(endyear), int(endmonth), int(enddate))  
   
    
    # csvに書き込む
    f.write(f"{Subject},{startdate.strftime('%m')}/{startdate.strftime('%d')}/{startdate.strftime('%Y')},{enddate.strftime('%m')}/{enddate.strftime('%d')}/{enddate.strftime('%Y')}\n")   

f.close()


# 参考:https://opty-life.com/study/program/python/python-lecture-23/
# https://non-dimension.com/python-googlecalendarapi/s