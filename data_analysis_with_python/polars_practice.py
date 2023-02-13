import polars as pl
# polarsのインストール
# テスト
url = "https://raw.githubusercontent.com/pparkitn/imagehost/master/ACA_date.csv"
df=pl.read_csv(url)
print(df.head())