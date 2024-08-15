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
files_name.sort()  # 排序

for f in files_name:  # 逐一讀取所有的.md檔案
    # 用with open()讀取檔案內容並存到file變數裡面，讀取模式為r，檔案編碼為utf-8
    # 用with 就可以避免忘記關閉檔案的問題
    with open(f"{folderPath}/{f}", "r", encoding="utf-8") as file:
        # 開啟檔案後可以做很多事情，這裡我們指讀取檔案內容

        # 如果不使用with，則需要先開啟檔案，然後讀取內容，最後關閉檔案
        # flie = open (f"{folderPath}/{f}", "r", encoding="utf-8")
        # content = file.read()
        # flie.close()

        # "r"（檔案開啟模式）：
        # "r" 是 open() 函數的參數之一，用來指定檔案的開啟模式。
        # "r" 代表「讀取模式」（read mode），表示你只想讀取檔案的內容，而不會對檔案進行寫入或修改。
        # 如果檔案不存在，使用 "r" 模式會導致 FileNotFoundError 錯誤。
        # 其他檔案開啟模式還包括 "w"（寫入模式）、"a"（追加模式）、"b"（二進位模式），等等。

        # read()（檔案讀取方法）：
        # read() 是檔案物件的方法，用來從已開啟的檔案中讀取內容。
        # read() 會讀取檔案中的所有內容，並將其返回為一個字串。如果檔案很大，這可能會消耗大量記憶體。
        # 除了 read()，還有其他的讀取方法，例如 readline() 用來逐行讀取，readlines() 用來讀取檔案的所有行並返回一個列表。

        # 當你使用 "r" 模式打開檔案後，你可以使用 read() 方法來讀取檔案的內容。

        content = file.read()  # 讀取檔案內容
    with st.expander(f[:-3]):  # 使用expender可以展開內容，同時標題去掉最後三個字(.md)
        st.markdown(content)  # 將檔案內容顯示在網頁上
