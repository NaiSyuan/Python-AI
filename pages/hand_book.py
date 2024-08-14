import streamlit as st
import os

folderPath = "markdown"  # 設定資料夾路徑
files = os.listdir(folderPath)  # 取得資料夾內所有檔案
# 這時候資料夾可能包含其他種類檔案，因此需要判斷檔案是否為.md檔案
print(files)
files_name = []  # 新增一個空的list，用來存放.md檔案
for f in files:  # 逐一檢查所有檔案，看看是否以.md結尾
    if f.endswith(".md"):  # 如果是.md檔
        files_name.append(f)  # 將檔案名稱加入list中


for f in files_name:  # 逐一讀取所有的.md檔案
    # 用with open()讀取檔案內容並存到file變數裡面，讀取模式為r，檔案編碼為utf-8
    # 用with 就可以避免忘記關閉檔案的問題
    with open(f"{folderPath}/{f}", "r", encoding="utf-8") as file:
        # 開啟檔案後可以做很多事情，這裡我們指讀取檔案內容

        # 如果不使用with，則需要先開啟檔案，然後讀取內容，最後關閉檔案
        # flie = open (f"{folderPath}/{f}", "r", encoding="utf-8")
        # content = file.read()
        # flie.close()

        content = file.read()
    with st.expander(f[:-3]):  # 使用expender可以展開內容，同時標題去掉最後三個字(.md)
        st.markdown(content)  # 將檔案內容顯示在網頁上
