import matplotlib.pyplot as plt
import csv
import pandas as pd


# グラフにしたいcsvの相対パスを指定.
path="C:\\Users\\st200\\OneDrive - Kyushu University\\学校用\\実験\\4回\\リングオシレータ。実験課題2\\4.7μF\\scope_20230119_141320.csv"

df=pd.read_csv(path)
# print(df.head())

# print(df.columns[0])
# columnsでリスト形式であるためこのような指定も可能

plt.title("test_of_scatter") #タイトル
plt.xlabel("X--Trace 1::[CH1]") #x軸のラベル
plt.ylabel("Y--Trace 1::[CH1]") #y軸のラベル

# plt.grid() グリッド線を引くためのもの

plt.plot(df[df.columns[0]],df[df.columns[1]],marker = "o", color = "red")


plt.show() #show関数を使うことで図が表示される


