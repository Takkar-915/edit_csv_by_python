import pandas as pd

#各購買頻度ごとの顧客数を求める関数を定義
def count_customer_per_purchase_flequency(num):
    count = (df['purchase_flequency'] == num).sum()
    return count

#csvファイルのパスを指定
filepath = 'records.csv'

df = pd.read_csv(filepath,encoding="UTF-8")
df = pd.DataFrame(df)

#新たに作成した列を保持するデータフレーム
df_after = pd.DataFrame()

#各購買頻度ごとの顧客数を保持するリストを定義
total_of_customer_per_purchase_flequency = []

#汎用性は低いが、最大購買頻度が23だと分かっている状況なので…len()にすればよかった…
for i in range(1,24):
    ans = count_customer_per_purchase_flequency(i)
    total_of_customer_per_purchase_flequency.append(ans)

#分かりずらいけどassignの=の左がcsvの列名になる
df_after = df_after.assign(total_of_customer_per_purchase_flequency = total_of_customer_per_purchase_flequency)

#購買頻度を保持するリスト
flequency = []

for i in range(1,24):
    flequency.append(i)

#分かりずらいけどassignの=の左がcsvの列名になる
df_after = df_after.assign(flequency = flequency)

#うまくいってるか確認
print(df_after)


#以下、df_afterをcsvファイルとして保存する
df_after.to_csv('processed_file.csv',encoding='UTF-8')