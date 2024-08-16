import streamlit as st
import openai
from utils import load_openai_api  # 載入自定義函式

# API 應用程式介面->透過key可以使用這個公司提供的特定服務
openai.api_key = load_openai_api()  # 載入openai api key

if "history" not in st.session_state:
    st.session_state.history = []  # 初始化對話記錄
if "system_message" not in st.session_state:
    st.session_state.system_message = "使用繁體中文回應後續訊息"  # 初始化系統訊息

cols = st.columns([4, 2, 1])  # 分割兩個列

with cols[0]:
    st.session_state.system_message = st.text_input(
        "系統訊息", st.session_state.system_message
    )  # 可以自訂系統訊息

with cols[1]:
    st.session_state.model = st.selectbox(
        "AI模型",
        [
            "gpt-4o-mini",
            "gpt-4o-2024-08-06",
        ],
    )  # 選擇AI模型

with cols[2]:
    if st.button("清除對話記錄"):
        st.session_state.history = []  # 清除對話紀錄
        st.rerun()


for message in st.session_state.history:  # 顯示對話記錄
    if message["role"] == "user":
        st.chat_message("user", avatar="🍳").write(message["content"])
    else:
        st.chat_message("assistant", avatar="✨").write(message["content"])


prompt = st.chat_input("請輸入想要對話的訊息")  # 顯示對話框
if prompt:
    st.session_state.history.append(
        {"role": "user", "content": prompt}
    )  # 將用戶輸入的訊息加入對話記錄
    response = openai.chat.completions.create(
        model=st.session_state.model,  # 使用的模型
        temperature=0.7,  # 溫度參數，設定回應的創意程度，值越大回應越有變化
        messages=[{"role": "system", "content": st.session_state.system_message}]
        + st.session_state.history,
    )
    assistant_messsage = response.choices[0].message.content
    st.session_state.history.append(
        {"role": "assistant", "content": assistant_messsage}
    )
    st.rerun()
