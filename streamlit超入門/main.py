# main.pyを作業フォルダ内に作る
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

# ターミナル内で作業フォルダに移動し streamlit run main.pyを実行

st.title('streamlit超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

# dfを書き出すときはst.write/st.dataframeどちらも同じものが書けるが、dataframeの方が引数を設定できる
st.write(df)
st.dataframe(df, width=100, height=100)
st.dataframe(df.style.highlight_max(axis=0))

# .tableを使っても表示できるが、ソートはできない。
st.table(df.style.highlight_max(axis=0))

# streamlitのサイトのAPI reference>Display dataに色々載っている


# 見出し
# マークダウン
# バックコーテーションは３つで背景グレー＋コピー
""""
# 章
## 節
### 項



```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

# 折れ線グラフを書くst.line_cart(df)
df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a', 'b', 'c']
)
df
st.line_chart(df)

# エリアチャート（折れ線で下が塗られてるやつ）
st.area_chart(df)

# 棒グラフ
st.bar_chart(df)

# マッピング
df = pd.DataFrame(
    np.random.rand(100,2)/[50, 50]+ [35.69, 139.70],
    columns=['lat', 'lon']
)
df
st.map(df)

# 画像の表示
# st.wirteでタイトル
# img = で　画像ファイルの指定
# st.image で画像の書き出し
# use_column_widthでカラムの横幅いっぱいに使う＝True
st.write('Haruka Hirose')
img = Image.open('Hirose_family_Colour_Print255.jpg')
st.image(img, caption='2022年ロンドンにて',  use_column_width=True)

# 動的な変化：インタラクティブウィジット
# チェックボックスを使用 .checkbox
if st.checkbox('画像を表示する'):
    img = Image.open('Hirose_family_Colour_Print255.jpg')
    st.image(img, caption='2022年ロンドンにて',  use_column_width=True)

# セレクトボックス .selectbox
# セレクトボックスの中身はリスト型で表示：数字の1~10の場合は list(range(1,11))
option = st.selectbox(
    'あなたが好きな色を教えてください。',
    ['red', 'blue', 'yellow', 'green', 'white', 'black', 'purple', 'pink', 'orange']
)
'あながた好きな色は、', option, 'です。'
# '〇〇〇', 'option', '〇〇' ,忘れずに

# テキスト入力
st.write('インタラクティブ ウィジット')
text = st.text_input('あなたの趣味を教えてください')
'あなたの趣味：', text, 'です。'

# スライダー
condition = st.slider('あなたの今の調子は？', 0,100,50)
'コンディション：', condition, 'です。'


# サイドバー st.sideber. 以下コメントアウト済み
# text2 = st.sidebar.text_input('あなたの出身地を教えてください')
# condition2 = st.sidebar.slider('あなたの予算は？', 0,100,50)

# 'あなたの出身地：', text2, 'です。'
# '予算：', condition2, 'です。'

# 2カラムレイアウト
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示ボタン')
if button:
    right_column.write('ここは右カラム')

# アコーディオン .expander
espander = st.expander('問い合わせ')
espander.write('問い合わせ内容を書く')


#プログレスバーの表示　import time
st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!'


