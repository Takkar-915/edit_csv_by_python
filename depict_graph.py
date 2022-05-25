import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import japanize_matplotlib

filepath = 'processed_file.csv'
df = pd.read_csv(filepath,encoding='UTF-8')

x_name = 'flequency'
y_name = 'total_of_customer_per_purchase_flequency'

#フォントサイズの指定
plt.rcParams['font.size'] = 10

#棒グラフの作成
fig = plt.figure(dpi = 100)

plt.bar(df[x_name], df[y_name], 0.6, color='c', label=y_name)

for i,j in enumerate(np.array(df[y_name])):
    print(i+1,j)
    plt.text(i+1, j, str(int(j)), ha='center', va='bottom', color='k')

plt.xlabel('購買頻度')
plt.ylabel('累積顧客数')

ax = plt.gca()
ax.set_facecolor('white')
x_min, x_max = ax.get_xlim()

#デフォルトのメモリ表記を取得
y_ticklabels = ax.get_yticklabels()

#目盛りを表示する間隔
tick_spacing = 1000

#x軸の目盛りの表示間隔
ax.xaxis.set_major_locator(ticker.MultipleLocator(1)) 

#凡例の表示位置の指定
ax.legend(loc='upper right')

#横線のみ表示。
plt.grid(which='both', axis='y', color='k', alpha=0.5, linestyle='dotted', linewidth=1)

#サブプロット間の正しい感覚を自動的に維持。
plt.tight_layout()

plt.xlim(0,23)
plt.ylim(0,)

#グラフを表示
plt.show()