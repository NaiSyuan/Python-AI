import streamlit as st

# 初始化清單，如果在 session_state 中沒有 'L'，則設置為空列表
if "L" not in st.session_state:
    st.session_state.L = []

st.title("點餐機")

# 建立2個欄位
cols = st.columns(2)
with cols[0]:
    name = st.text_input("請輸入餐點名稱")

with cols[1]:
    if st.button("新增餐點", key="add"):
        if name:  # 確保名稱不為空
            st.session_state.L.append(name)  # 直接將名稱新增到清單中

# 顯示目前的餐點清單，每個餐點旁邊有一個刪除按鈕
st.write("目前的餐點清單：")
for index, item in enumerate(st.session_state.L):
    cols = st.columns([3, 1])  # 建立一個有比例的欄位，讓刪除按鈕與文字保持對齊
    cols[0].write(item)  # 顯示餐點名稱
    if cols[1].button(f"刪除", key=f"delete_{index}"):  # 刪除按鈕的 key 使用索引
        st.session_state.L.pop(index)  # 根據索引從清單中移除該餐點
        st.rerun()  # 刷新頁面以更新顯示
