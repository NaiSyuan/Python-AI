import streamlit as st
import os
import time

st.title("graph")
# st.image使用方式: st.image(圖片路徑, 寬度)(等比例縮放)
st.image("image/apple.png", width=500)


image_folder = "image"  # 設定資料夾路徑
image_files = os.listdir(image_folder)  # 取得資料夾內所有檔案

st.write(image_files)
st.text(image_files)
image_size = st.number_input(
    "請輸入圖片大小", min_value=50, max_value=1000, value=100, step=50
)


for image_file in image_files:
    st.image(f"{image_folder}/{image_file}", width=image_size)
# 顯示圖片，根據使用者輸入的大小調整寬度

for image_file in image_files:
    # 除了width，還有一個use_column_width = True 這個參數的作用是讓圖片自動調整其寬度以適應 Streamlit 應用的column寬度。
    # 這樣可以確保圖片在顯示時不會超出網頁的範圍
    st.image(f"{image_folder}/{image_file}", use_column_width=True)
    # 顯示圖片，並且使用column寬度

if st.button("購買"):
    st.success("購買成功")
    time.sleep(0.5)  # 延遲0.5秒讓使用者看到訊息
    st.rerun()  # 重新整理頁面

if st.button("購買"):
    st.error("購買失敗")
