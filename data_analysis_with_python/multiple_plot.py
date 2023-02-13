import matplotlib.pyplot as plt #モジュールのインポート
import pandas as pd
# グラフにしたいcsvの相対パスを指定.
path="C:\\Users\\st200\\OneDrive - Kyushu University\\学校用\\実験\\4回\\リングオシレータ。実験課題2\\4.7μF\\scope_20230119_141320.csv"

df=pd.read_csv(path)
# print(df.columns)
# columnsでリスト形式であるためこのような指定も可能

# plt.title("test_of_scatter") #タイトル
# plt.xlabel("X--Trace 1::[CH1]") #x軸のラベル
# plt.ylabel("Y--Trace 1::[CH1]") #y軸のラベル

# plt.grid() #グリッド線を引くためのもの

# plt.plot(df[df.columns[0]],df[df.columns[1]],marker = "o", color = "red")


Figure = plt.figure() #全体のグラフを作成

ax1 = Figure.add_subplot(1,2,1) #1つ目のAxを作成
ax2 = Figure.add_subplot(1,2,2) #2つ目のAxを作成

ax1.set_xlabel("X--Trace 1::[CH1]") #x軸のラベル
ax2.set_ylabel("Y--Trace 1::[CH1]") #y軸のラベル

ax2.set_xlabel(df.columns[3]) #x軸のラベル

ax1.legend()
ax2.legend()

ax1.plot(df[df.columns[0]],df[df.columns[1]],marker = "o", color = "red",label="1") #1つ目のAxにデータのプロット
ax2.plot(df[df.columns[3]],df[df.columns[4]],marker = "o", color = "blue",label="2") #2つ目のAxにデータのプロット


plt.show()