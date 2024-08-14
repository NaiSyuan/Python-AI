import streamlit as st

st.title("欄位元件")
col1, col2, col3 = st.columns(3)  # 建立3個欄位
col1.button("按鈕1", key="btn1")
# 在第一個欄位中建立一個按鈕，並且將它的key設為1(st.button("按鈕1") )
col2.button("按鈕2", key="btn2")  # 在第二個欄位中建立一個按鈕，並且將它的key設為2
col3.button("按鈕3", key="btn3")  # 在第三個欄位中建立一個按鈕，並且將它的key設為3

# 3columns :can use the proportion to setup the column ratio,and put the porportion into the column
col1, col2, col3 = st.columns([1, 2, 1])  # 建立3個欄位，每個欄位比例為1:2:1
col1.button("按鈕4", key="btn4")  # 在第一個欄位中建立一個按鈕，並且將它的key設為4
col2.button("按鈕5", key="btn5")  # 在第二個欄位中建立一個按鈕，並且將它的key設為5
col3.button("按鈕6", key="btn6")  # 在第三個欄位中建立一個按鈕，並且將它的key設為6

col1, col2, col3 = st.columns([1, 2, 3])  # built 3 columns, the proportion is 1:2:3
with col1:  # creat a button in the col1

    if st.button(
        "按鈕7", key="btn7"
    ):  # creat a button in the col1, and set its key to 7
        st.snow()
    st.write("this is the col1")  # write something in the col1

with col2:  # creat a button in the col2
    st.button("按鈕8", key="btn8")  # creat a button in the col2, and set its key to 8
    st.write("this is the col2")  # write something in the col2
with col3:  # creat a button in the col3
    st.button("按鈕9", key="btn9")  # creat a button in the col3, and set its key to 9
    st.write("this is the col3")  # write something in the col3


# much more columns

cols = st.columns(4)  # creat 4 columns, col[0]...col[3]

# If the four buttons are the same
for col in range(len(cols)):  # creat 4 buttons in the columns
    with cols[col]:
        st.button(f"按鈕{col+1}", key=f"btn{col+10}")
        # creat a button in the col[col], and set its key to col+10


cols = st.columns(4)  # creat 4 columns, col[0]...col[3]
with cols[0]:
    st.button("按鈕1", key="btn14")
    # creat a button in the col[0], and set its key to btn14
with cols[1]:
    st.button("按鈕2", key="btn15")
    # creat a button in the col[1], and set its key to btn15
with cols[2]:
    st.button("按鈕3", key="btn16")
    # creat a button in the col[2], and set its key to btn16
with cols[3]:
    st.button("按鈕4", key="btn17")
    # creat a button in the col[3], and set its key to btn17

st.markdown("---")
st.title("文字輸入元件")
# st.text_input's command format -> st.text_input(enter the label, value=default value)
text = st.text_input("請輸入文字", value="這是預設文字")
st.markdown(f"您輸入的文字是：{text}")

# Comparison of the effects of arranging components
st.markdown("---")
st.title("columns of the effect of arranging components")
# 2columns
col1, col2 = st.columns(2)
with col1:
    st.button("按鈕1", key="btn18")
    st.button("按鈕2", key="btn19")
    st.button("按鈕3", key="btn20")
with col2:
    st.write("這是col2")
    st.write("這是col2")
    st.write("這是col2")

st.markdown("---")


for i in range(3):
    col1, col2 = st.columns(2)
    with col1:
        st.button(f"按鈕{i+1}", key=f"btn{i+23}")
    with col2:
        if i == 0:
            st.write("hello")
        elif i == 1:
            st.write("hi")
        else:
            st.write("bye")


st.title("session_state")
ans = 1
if st.button("add 1", key="state1"):
    ans += 1  # add 1 to ans
st.write(f"ans = {ans}")

# session_state
if "ans" not in st.session_state:  # 如果session_state中沒有ans，就將ans設為1
    st.session_state.ans = 1

if st.button("add 1", key="state2"):  # 如果按鈕按下，就將ans加1
    st.session_state.ans += 1  # 將ans加1

st.write(f"ans = {st.session_state.ans}")  # 將ans寫入畫面


# Sometimes pressing the button may not reorganize the screen.
# In this case, you can use 'st.rerun' to reorganize the screen.
if st.button("refresh the screen", key="refresh"):
    # ... ...
    st.rerun()  # rerun the code
