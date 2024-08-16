import streamlit as st
from utils import set_background  # 從utils.py只匯入set_background函式

set_background("bgimage/ntutcdlogo.png", 10, "left bottom")
st.title("歡迎來到PythonAI")
