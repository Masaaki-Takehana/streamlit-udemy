import streamlit as st
from PIL import Image
import time

st.title("Streamlit超入門")

# st.write("プログレスバーの表示")
# "Start"
# latest_interation = st.empty()
# bar = st.progress(0)
# for i in range(100):
#     latest_interation.text(f"Interation {i+1}")
#     bar.progress(i + 1)
#     time.sleep(0.01)

opsion = st.selectbox(
    "好きな数字",
    list(range(1,11))
)
"あなたが選んだ数字は", opsion, "です"

left_column, right_column = st.columns(2)
button = left_column.button ("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラムです")

expander1 = st.expander("問い合わせ1")
expander1.write("問い合わせ1の回答")
expander2 = st.expander("問い合わせ2")
expander2.write("問い合わせ2の回答")
expander3 = st.expander("問い合わせ3")
expander3.write("問い合わせ3の回答")

st.write("DateFrame")

# df = pd.DataFrame({
#     '1列目' : [1, 2, 3, 4],
#     '2列目' : [10, 20, 30, 40]
# })
# st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

'''python
import streamlit as st
import numpy as np
import pandas as pd
'''

"""
# dfLine = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=["a", "b", "c"]
# )
# st.line_chart(dfLine)


# dfLatLon = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=["lat", "lon"]
# )
# st.map(dfLatLon)

st.write("Display Image")

img = Image.open("image/topimg.png")
st.image(img, caption="top img", use_column_width=True)