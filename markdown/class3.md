## 1. `Streamlit` 簡介

Streamlit 是一個開源的 Python 庫，專為建立互動式 Web 應用程式而設計。它的主要特點是簡單易用，開發者可以快速將 Python 腳本轉化為可視化的 Web 應用。

---

## 2. 建立欄位元件與按鈕

### 基本概念

在 Streamlit 中，欄位（Column）可以用來將頁面劃分為多個垂直的區塊。每個欄位都可以容納不同的元件，如按鈕、文字框等。透過 `st.columns()` 函數可以輕鬆地建立欄位。

### 基本範例

```python
import streamlit as st

st.title("欄位元件")
col1, col2, col3 = st.columns(3)  # 建立3個等寬的欄位
col1.button("按鈕1", key="btn1")  # 在第一個欄位中建立一個按鈕，並且將它的key設為btn1
col2.button("按鈕2", key="btn2")  # 在第二個欄位中建立一個按鈕，並且將它的key設為btn2
col3.button("按鈕3", key="btn3")  # 在第三個欄位中建立一個按鈕，並且將它的key設為btn3
```

### 設定欄位比例

可以通過設置比例來調整欄位的寬度。例如，1:2:1 表示第二個欄位是第一和第三個欄位的兩倍寬。

```python
col1, col2, col3 = st.columns([1, 2, 1])  # 建立3個欄位，每個欄位比例為1:2:1
col1.button("按鈕4", key="btn4")  # 在第一個欄位中建立按鈕
col2.button("按鈕5", key="btn5")  # 在第二個欄位中建立按鈕
col3.button("按鈕6", key="btn6")  # 在第三個欄位中建立按鈕
```

### 使用 `with` 來操作欄位

在使用 `st.columns()` 函數時，可以搭配 `with` 語句來更方便地將元件加入特定的欄位中。

```python
col1, col2, col3 = st.columns([1, 2, 3])  # 建立3個欄位，比例為1:2:3
with col1:
    if st.button("按鈕7", key="btn7"):
        st.snow()  # 如果按下按鈕，會有下雪效果
    st.write("this is the col1")
with col2:
    st.button("按鈕8", key="btn8")
    st.write("this is the col2")
with col3:
    st.button("按鈕9", key="btn9")
    st.write("this is the col3")
```

### 使用迴圈動態生成欄位與按鈕

當需要在多個欄位中生成相似的元件時，可以使用 `for` 迴圈來簡化程式碼。

```python
cols = st.columns(4)  # 建立4個欄位
for col in range(len(cols)):
    with cols[col]:
        st.button(f"按鈕{col+1}", key=f"btn{col+10}")  # 動態生成按鈕
```

---

## 3. 文字輸入元件

### 基本概念

在 Streamlit 中，可以使用 `st.text_input()` 函數來建立文字輸入框。這個函數允許用戶輸入文字並進行後續的操作。

### 範例

```python
st.title("文字輸入元件")
text = st.text_input("請輸入文字", value="這是預設文字")
st.markdown(f"您輸入的文字是：{text}")
```

在這個範例中，`st.text_input` 函數創建了一個文字輸入框，並且將預設值設為「這是預設文字」。輸入後的文字會顯示在下方。

---

## 4. 使用 `session_state` 保存狀態

### 基本概念

`st.session_state` 是一個可以跨多次執行保存變數值的特性。在 Streamlit 中，每次使用者互動都會觸發應用程式的重新運行，因此 `session_state` 尤其重要，用於在按下按鈕後保持某些值。

### 範例

```python
st.title("session_state")
if "ans" not in st.session_state:
    st.session_state.ans = 1

if st.button("add 1", key="state2"):
    st.session_state.ans += 1

st.write(f"ans = {st.session_state.ans}")
```

在這裡，`st.session_state` 用來保存 `ans` 的狀態，按下按鈕後，`ans` 會自動加 1。

---

## 5. `st.rerun()` 重跑程式

在某些情況下，按下按鈕後頁面可能不會自動刷新。此時可以使用 `st.rerun()` 來強制重新執行整個程式。

```python
if st.button("refresh the screen", key="refresh"):
    st.rerun()  # 重新運行程式
```

---

## 6. 邏輯運算符與循環結構

在程式設計中，邏輯運算符（如 `+`, `-`, `*`, `/`）和循環結構（如 `while`, `for`）是非常基本的概念。

### operators priority

```
1. () parentheses
2. ** power
3. +(positive)、-(negative)
4. * / // % multiplication、division、integer division、modulo
5. + - addition、subtraction
6. == != < > <= >= comparison
7. not and or logical
8. = += -= *= /= //= %= **= Arithmetic operators
```

### 邏輯運算範例

```python
a = 1
a += 1  # a = a + 1
print(a)  # 2
a -= 1  # a = a - 1
print(a)  # 1
```

### `while` 迴圈與 `break` 範例

```python
i = 0
while i < 10:
    print(i)
    if i == 5:
        break  # 強制跳出循環
    i += 1
```

---

## 7. 隨機數與遊戲範例

### `random` 模組

`random` 模組提供了生成隨機數的功能，常用於各種隨機選擇的場景中。

### 範例：猜數字遊戲

```python
import random

min = 1
max = 100
num = random.randint(min, max)

while True:
    try:
        user_input = int(input(f"請輸入{min}到{max}的數字:"))
    except ValueError:
        print("請輸入有效的整數!")
        continue
    if user_input == num:
        print("恭喜你，正確！")
        break
    elif user_input > num:
        print("太大了!")
    elif user_input < num:
        print("太小了!")
```

這是一個簡單的猜數字遊戲，玩家需要在範圍內猜測數字，程式會提示數字太大或太小，直到猜對為止。

---
