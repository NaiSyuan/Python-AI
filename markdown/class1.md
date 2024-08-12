### Python 程式技巧筆記

---

#### 註解 (Comments)

- **單行註解 (Single-line comments)**: 使用 `#` 開頭的註解，會忽略該行後面的內容。  

  ```python
  # 這是單行註解
  ```
  
- **多行註解 (Multi-line comments)**: 使用 `\"\"\"` 或 `'''` 將多行註解包裹起來。  

  ```python
  \"\"\"
  這是多行註解
  \"\"\"
  ```

#### 基本資料型態 (Basic Data Types)

- **整數 (Integer)**: `int`  

  ```python
  print(1)  # int這是整數
  ```

- **浮點數 (Float)**: `float`  

    ```python
    print(1.0)  # float這是浮點數
    ```

- **字串 (String)**: `str`  

  ```python
  print("1")  # str這是字串
  ```

- **布林值 (Boolean)**: `bool`  

  ```python
  print(True)  # bool這是布林值
  print(False)  # bool這是布林值
  ```

#### 變數 (Variables)

- **變數的使用**: 使用 `=` 來指定變數的值。  

  ```python
  a = 10  # 新增變數a，將"="右邊的10存入左邊的a
  print(a)  # 在終端機中顯示存在a的值
  ```

#### 運算子 (Operators)

- **數學運算子**:  

  ```python
  print(1 + 2)  # 加法
  print(1 - 2)  # 減法
  print(1 * 2)  # 乘法
  print(1 / 2)  # 除法
  print(1 // 1)  # 整除(取商)
  print(1 % 2)  # 取餘數
  print(1**2)  # 平方
  print(1**0.5)  # 平方根
  ```

- **優先順序**:  
  1. `()` 括號
  2. `**` 次方
  3. `* / // %` 乘、除、整除(取商)、取餘數
  4. `+ -` 加、減

- **字串運算**:  

  ```python
  print("hello" + "world")  # 字串加法
  print("hello" * 3)  # 字串重複三次
  ```

#### 字串格式化 (String Formatting)

- **f-string**:  

  ```python
  name = "apple"
  age = 18
  print(f"My name is {name} and I am {age} years old.")
  ```

#### 字串處理 (String Manipulation)

- **取字串的長度**:  

  ```python
  print(len("hello"))  # len()是一個函數，可以計算字串的長度
  ```

- **取得資料型態**:  

  ```python
  print(type("hello"))  # type()是一個函數，可以取得資料物件的型態
  ```

- **型態轉換 (Type Casting)**:  

  ```python
  print(int(1.0))  # 將float轉換成int
  print(float("123"))  # 將str轉換成float
  print(str(123))  # 將int轉換成str
  print(bool(0))  # 將int轉換成bool (False)
  print(bool(1))  # 將int轉換成bool (True)
  ```

#### 使用者輸入 (User Input)

- **input() 函數**: 讀取使用者的輸入，輸入的內容為字串。  

  ```python
  a = input("請輸入你的名字：")
  print(int(a) + 100)  # 將字串轉換成int，然後加100
  ```

#### 計算圓面積 (Calculating Circle Area)

- **範例**: 根據使用者輸入的半徑計算圓的面積。  

  ```python
  d = float(input("請輸入半徑："))
  print(f"圓面積{3.14 * d**2}")
  ```

---

### Markdown 標題 (Markdown Headings)

- **標題語法**: `#` 用來定義標題，`#` 的數量決定標題層級。  

  ```markdown
  # 這是大標題
  ## 這是第二大標題
  ### 這是第三大標題
  #### 這是第四大標題
  ##### 這是第五大標題
  ###### 這是第六大標題
  ```

- **範例**:  

  ```markdown
  # 這是大標題

  ## 這是第二大標題

  ---
  
  ```python 
  print("Hello world")
  ```

### 這是第三大標題

#### 這是第四大標題

##### 這是第五大標題

###### 這是第六大標題

  ```

  ### Streamlit 程式技巧筆記

---

#### 顯示文字內容 (Displaying Text)

- **`st.title()`**: 用於顯示頁面的標題，通常用來作為頁面中最主要的標題。  
  ```python
  st.title("這是標題")
  ```

- **`st.write()`**: 一個強大的函數，可以顯示多種格式的內容，包括字串、數字、Markdown、數據框等。  

  ```python
  st.write("這是一個用 `st.write` 顯示的字串，可以處理多種格式，例如：數字、文字、Markdown、數據框等。")
  ```

- **`st.text()`**: 用於顯示純文字內容，不支持任何格式化。  

  ```python
  st.text("這是一個用 `st.text` 顯示的純文字字串，只能顯示純文字，不支持其他格式。")
  ```

- **`st.markdown()`**: 用於顯示支持 Markdown 語法的內容，可以進行文字格式化、添加連結和代碼塊等。  

  ```python
  st.markdown(
      \"\"\"
      這是一個用 `st.markdown` 顯示的字串，可以處理 Markdown 語法。
      例如：
      * **粗體文字**
      * *斜體文字*
      * [連結](https://www.example.com)
      * 代碼塊：
      ```python
      print("Hello, Streamlit!")
      ```
      \"\"\"
  )
  ```

---

這些筆記幫助你理解在 Streamlit 中如何顯示不同類型的文字內容，並根據需求選擇合適的函數。

---

這些筆記涵蓋了程式中的主要技巧和概念，適合用作學習或回顧時的參考。
