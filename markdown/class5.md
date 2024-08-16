### 區域變數與全域變數

在 Python 中，變數的作用範圍（Scope）決定了變數可以在哪些部分被訪問與修改。變數主要分為**全域變數**（Global Variables）與**區域變數**（Local Variables）。

#### 1. 全域變數（Global Variables）

- **定義**：在函數外部定義的變數，可以在整個程式內部被訪問。
- **存取**：全域變數可以在所有函數內被讀取，但不能直接修改，除非使用 `global` 關鍵字。

#### 2. 區域變數（Local Variables）

- **定義**：在函數內部定義的變數，僅在該函數內有效。
- **存取**：區域變數只能在其所在的函數內被訪問，無法在函數外部直接使用。

---

### 範例與說明

#### 範例 1：區域變數與全域變數的區別

```python
lenth = 5  # 全域變數
area = 3.14  # 全域變數

def calculate_square_area():
    area = lenth**2  # lenth 是全域變數，area 是區域變數
    print("面積是", area)  # 輸出 25

calculate_square_area()  # 呼叫函數
```

- **說明**：
  - `lenth` 是全域變數，函數內可以直接使用。
  - 在函數內定義的 `area` 是區域變數，與全域變數 `area` 沒有直接關聯。

#### 範例 2：函數內修改全域變數的錯誤

```python
lenth = 5

def calculate_square_area():
    area = lenth**2  # 正確
    length = length**2  # 錯誤，因為未定義 `length`

calculate_square_area()  # 錯誤：未定義的 `length`
```

- **說明**：
  - 嘗試修改未在函數內部定義的變數 `length` 會導致錯誤。

#### 範例 3：使用 `return` 回傳區域變數

```python
lenth = 5
area = 50

def calculate_square_area():
    area = lenth**2  # 定義區域變數
    return area  # 回傳區域變數的值

area = calculate_square_area()  # 將回傳值賦值給全域變數
print("面積是", area)  # 輸出 25
```

- **說明**：
  - 使用 `return` 將區域變數的值傳遞給全域變數，這樣可以修改全域變數的值。

#### 範例 4：使用 `global` 關鍵字修改全域變數

```python
lenth = 5
area = 50

def calculate_square_area():
    global area  # 宣告使用全域變數
    area = lenth**2  # 修改全域變數

calculate_square_area()
print("面積是", area)  # 輸出 25
```

- **說明**：
  - `global` 關鍵字允許在函數內直接修改全域變數。

---

### 其他程式技巧與範例

#### `hello` 函數：使用 `docstring` 註解

```python
def hello(name: str):
    """
    指令說明區\n
    這是一個多行指令說明區

    參數:\n
    name: str使用者名稱

    回傳:\n
    None

    範例:hello("Alice")
    """
    print(f"Hello, {name}!")
```

- **說明**：
  - `docstring` 提供了函數的說明、參數、回傳值與範例，有助於程式碼的可讀性與維護。

---

### Streamlit 應用範例

#### 1. 基本對話框與訊息處理

```python
import streamlit as st
import openai
from utils import load_openai_api  # 載入自定義函式

openai.api_key = load_openai_api()  # 載入 OpenAI API 金鑰

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
        temperature=0.7,  # 設定回應的創意程度
        messages=[{"role": "system", "content": st.session_state.system_message}]
        + st.session_state.history,
    )
    assistant_messsage = response.choices[0].message.content
    st.session_state.history.append(
        {"role": "assistant", "content": assistant_messsage}
    )
    st.rerun()
```

- **說明**：
  - 此程式範例展示了如何使用 Streamlit 建立一個簡單的對話應用程式，並處理用戶訊息與回應。

#### 2. 圖片生成與顯示

```python
import streamlit as st
import openai
from utils import load_openai_api  # 載入自定義函式

openai.api_key = load_openai_api()  # 載入 OpenAI API 金鑰

prompt_text = st.text_area("prompt", "A cute baby sea otter")  # 輸入提示詞
if st.button("開始生成圖片"):  # 按鈕
    generatedImage = openai.images.generate(  # 生成圖片
        model="dall-e-3",  # 選擇模型
        prompt=prompt_text,  # 輸入提示詞
        n=1,  # 生成幾張圖片，目前 OpenAI 只能生成一張
        size="1024x1024",  # 設定圖片大小
    )

    image_url = generatedImage.data[0].url  # 取得圖片的 URL
    st.image(image_url)  # 顯示圖片
```

- **說明**：
  - 此範例展示了如何使用 OpenAI API 生成圖片並在 Streamlit 中顯示。

#### 3. 圖片分析與處理

```python
import streamlit as st
import openai
from utils import load_openai_api, encode_image  # 載入自定義函式

openai.api_key = load_openai_api()  # 載入 OpenAI API 金鑰

st.title("AI圖片分析")

uploaded_file = st.file_uploader("上傳圖片", type=["png", "jpg", "jpeg"])  # 上傳圖片

if uploaded_file:
    st.image(uploaded_file, caption="已上傳的圖片", width=300)  # 顯示圖片

    with open("temp_image.jpg", "wb") as f:  # 將圖片寫入檔案
        f.write(uploaded_file.getbuffer())  # 將圖片寫入檔案

    base64_image = encode_image("temp_image.jpg")  # 將檔案編碼為 Base64
    prompt = st.chat_input("請輸入想要對話的訊息")  # 顯示對話框
    st.write(prompt)
    if prompt:
        response = openai.chat.completions

.create(
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
```

- **說明**：
  - 此範例展示了如何在 Streamlit 中上傳圖片，並將圖片轉換為 Base64 編碼後，與 OpenAI 模型進行互動。

---

### 小結

- 全域變數與區域變數的理解與運用是撰寫穩定、可讀程式的基礎。
- 在不同情境下選擇合適的變數範圍（Scope），可以避免不必要的錯誤並提高程式的可維護性。
- 善用 `global` 關鍵字與 `return` 回傳值，可以靈活管理全域變數與區域變數的互動。
- 透過範例理解 Streamlit 與 OpenAI API 的應用，能有效地將理論運用於實踐中。
