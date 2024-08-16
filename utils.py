import base64
import streamlit as st


def encode_image(image_path):
    """
    將圖片編碼為 base64 字串。\n
    參數：
    - image_path (str)：圖片的檔案路徑。\n
    返回值：
    - str：編碼後的 base64 字串。
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def set_background(png_file, width=25, position="right bottom", opacity=1):
    """
    設定網頁背景圖片。
    參數：
    - png_file (str): 背景圖片的檔案路徑。
    - width (int, optional): 背景圖片的寬度百分比。\n
        預設為 25。
    - position (str, optional): 背景圖片的位置, 可以是 "right"、"left"、"center"、"top"、"bottom" 等。\n
        預設為 "right bottom"。
    - opacity (float, optional): 背景圖片的透明度。\n
        預設為 1。
    使用範例：\n
        set_background("/path/to/image.png", width=50, position="center", opacity=0.5)
    """
    bin_str = encode_image(png_file)
    page_bg_img = (
        f"""
    <style>
        .main {{
            background-image: url("data:image/png;base64,%s");
            background-size: {width}%% auto;  /* 設定寬度, 高度自動調整 */
            background-repeat: no-repeat;  /* 防止背景圖片重複 */
            background-attachment: local; /* 設定背景圖片隨著網頁一起捲動 */
            background-position: {position};  /* 靠右下角顯示 */
            opacity : {opacity}; /* 透明度 */
        }}
    
        /* 手機樣式 */
        @media only screen and (max-width: 600px) {{
            .main {{
                background-size: 20%% auto;  /* 手機上背景圖片寬度設為20%% */
                background-position: left bottom;  /* 靠左下角顯示 */
                background-attachment: fixed; /* 背景圖片固定 */
            }}
        }}
    </style>
    """
        % bin_str
    )
    st.markdown(page_bg_img, unsafe_allow_html=True)


def load_openai_api() -> str:
    """
    加載 OpenAI API 的 key
    Returns:
    - str: OpenAI API key
    Raises:
    - RuntimeError: 如果找不到 API key
    """
    openai_api_key = st.secrets.get("OPENAI_API_KEY")
    if not openai_api_key:
        st.error("找不到 OpenAI API key，請設置環境變數 OPENAI_API_KEY")
        st.stop()
    return openai_api_key
