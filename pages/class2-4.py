# 數字金字塔
import streamlit as st


# 先定義一個函數，可以接受一個1-9的數字，返回其金字塔，並且在呼叫函數時，可以使用參數，顯示在streamlit的畫面上，下一次的要顯示數字要下一行

number = st.number_input("Please input a number", step=1, min_value=1, max_value=9)

for i in range(0, number + 1):
    st.markdown(f"{i}" * i)

# 箭頭金字塔(箭頭型金字塔)
number = st.number_input("Please input a number", step=1)
