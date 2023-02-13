import pandas as pd
df=pd.read_csv("C:\\Users\\st200\\OneDrive - Kyushu University\\個人学習\\python\\train.csv")
# 最初の5行を出力
df.head()
# print(df.head) 確認用

# df中の列名を取得
print(df.columns)

# nan値をdropする
df=df.dropna()

print(df)

print(df["Embarked"])


# dummy変数に変換
print(pd.get_dummies(df["Embarked"])
)