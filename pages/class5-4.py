import streamlit as st
import openai
from utils import load_openai_api, encode_image

openai.api_key = load_openai_api()  # 載入openai api key

st.title("AI圖片分析")

uploaded_file = st.file_uploader("上傳圖片", type=["png", "jpg", "jpeg"])  # 上傳圖片

if uploaded_file:
    st.image(uploaded_file, caption="已上傳的圖片", width=300)  # 顯示圖片

    with open("temp_image.jpg", "wb") as f:  # 將圖片寫入檔案
        f.write(uploaded_file.getbuffer())  # 將圖片寫入檔案

    base64_image = encode_image("temp_image.jpg")  # 將檔案編碼為base64
    prompt = st.chat_input("請輸入想要對話的訊息")  # 顯示對話框
    st.write(prompt)
    if prompt:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # 使用的模型
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt,
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            },
                        },
                    ],
                },
            ],
        )
        assistant_messsage = response.choices[0].message.content
        st.write(assistant_messsage)
