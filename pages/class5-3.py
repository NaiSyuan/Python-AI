import streamlit as st
import openai
from utils import load_openai_api  # 載入自定義函式

openai.api_key = load_openai_api()  # 載入openai api key
prompt_text = st.text_area("prompt", "A cute baby sea otter")  # 輸入提示詞
if st.button("開始生成圖片"):  # 按鈕
    generatedImage = openai.images.generate(  # 生成圖片
        model="dall-e-3",  # 選擇模型
        prompt=prompt_text,  # 輸入提示詞
        n=1,  # 生成幾張圖片，目前openai只能生成一張
        size="1024x1024",  # 設定圖片大小
    )

    image_url = generatedImage.data[0].url  # 取得圖片的url
    st.image(image_url)  # 顯示圖片
