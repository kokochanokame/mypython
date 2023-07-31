import streamlit as st
import time

st.title('streamlit　超入門')

st.write('インタラクティブなウィジェット')
'Start!!'

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f'Interation {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!'

col1, col2 = st.columns(2)
button = col1.button('ここを押してみ')
if button:
    col2.write('happy hallo')

expander = st.expander('お問い合わせ')
expander.write('ここに回答の内容が入ります')    
