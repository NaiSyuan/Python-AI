import streamlit as st


# 先定義一個函數，可以接受一個1-9的數字，返回其金字塔，並且在呼叫函數時，可以使用參數，顯示在streamlit的畫面上，下一次的要顯示數字要下一行
# 數字金字塔
number = st.number_input("Please input a number", step=1, min_value=1, max_value=9)

for i in range(0, number + 1):
    st.markdown(f"{i}" * i)


# 箭頭金字塔(箭頭型金字塔)

# 輸入數字
a = st.number_input("Enter a number:", min_value=1, step=1)

# 儲存結果
output = ""

# 產生結果
for i in range(1, a + 1):
    output += " " * (a - i) + "*" * ((i - 1) * 2) + "*\n"

for i in range(a):
    output += " " * (a - 1) + "*\n"

st.markdown(f"```\n箭頭金字塔 \n{output}```")
