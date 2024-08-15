# 1. 字典 (Dictionary)

- **字典概述**:  
  - 字典（`dict`）是一種使用鍵值對（key-value pair）來存儲數據的數據結構。
  - 鍵（key）是唯一的，值（value）則可以重複。
  - 字典是無序的，不能通過索引訪問元素。
  - 鍵必須是不可變的數據類型（如字符串、整數、浮點數、布爾值），而值可以是任何數據類型。
  - 鍵值對的格式是：`key: value`，多個鍵值對之間用逗號 `,` 分隔。

- **獲取字典的鍵**:

  ```python
  book = {"title": "Python Crash Course", "author": "Eric Matthes", "price": 10.00}
  print(book.keys())  # 輸出: ["title", "author", "price"]

  for key in book.keys():
      print(key)  # 分別打印 "title", "author", "price"
  ```

- **獲取字典的值**:

  ```python
  print(book.values())  # 輸出: ["Python Crash Course", "Eric Matthes", 10.0]

  for value in book.values():
      print(value)  # 分別打印 "Python Crash Course", "Eric Matthes", 10.0
  ```

- **獲取字典的鍵值對**:

  ```python
  print(book.items())  # 輸出: [("title", "Python Crash Course"), ("author", "Eric Matthes"), ("price", 10.0)]

  for key, value in book.items():
      print(key, value)  # 分別打印 "title Python Crash Course", "author Eric Matthes", "price 10.0"
  ```

- **新增/更新字典中的鍵值對**:

  ```python
  book["title"] = "JavaScript Crash Course"
  print(book)  # 輸出: {"title": "JavaScript Crash Course", "author": "Eric Matthes", "price": 10.0}

  book["author"] = "John Doe"
  print(book)  # 輸出: {"title": "JavaScript Crash Course", "author": "John Doe", "price": 10.0}
  ```

- **檢查鍵是否存在於字典中**:

  ```python
  print("title" in book)  # 輸出: True
  print("name" in book)  # 輸出: False
  ```

- **刪除字典中的鍵值對**:

  ```python
  print(book.pop("title"))  # 輸出: "JavaScript Crash Course"
  print(book.pop("name", "not found"))  # 輸出: "not found" (若鍵不存在且無預設值，則報錯)
  ```

- **處理複雜字典結構**:

  ```python
  d = {"a": [1, 2, 3], "b": {"c": 4, "d": 5}}
  print(d["a"])  # 輸出: [1, 2, 3]
  print(d["a"][0])  # 輸出: 1
  print(d["b"])  # 輸出: {"c": 4, "d": 5}
  print(d["b"]["c"])  # 輸出: 4
  ```

- **成績登記系統範例**:
  - 建立成績字典並計算平均成績：

    ```python
    grade = {
        "小名": {"國文": [90, 80, 70], "數學": [80, 70, 60], "英文": [70, 60, 50]},
        "大名": {"國文": [95, 85, 75], "數學": [85, 75, 65], "英文": [75, 65, 55]},
        "中名": {"國文": [100, 90, 80], "數學": [90, 80, 70], "英文": [80, 70, 60]},
    }

    # 取得小名的國文成績
    print(grade["小名"]["國文"])  # 輸出: [90, 80, 70]

    # 計算每位學生的國文平均成績
    for name, subject in grade.items():
        chinese = subject["國文"]
        avg = sum(chinese) / len(chinese)
        print(f"{name} average: {avg:.2f}")  # :.2f 表示保留小數點後兩位
    ```

    - 計算全校科目的平均成績：

    ```python
    grade_avg = {"國文": [], "英文": [], "數學": []}

    for subjects in grade.values():
        for sub, score in subjects.items():
            grade_avg[sub] += score

    print(grade_avg)
    print(len(grade_avg))  # 輸出科目數量: 3
    ```

# 2. 購物商城範例 (Streamlit)

- **建立基本界面並加載圖片**:

  ```python
  import streamlit as st
  import time
  import os

  st.title("購物商城")
  image_folder = "image"
  image_files = os.listdir(image_folder)
  st.write(image_files)
  ```

- **商品顯示與購買邏輯**:

  ```python
  def display_products(cols):
      for i, (item_name, item_info) in enumerate(st.session_state.commodity.items()):
          with cols[i % len(cols)]:
              st.image(item_info["image"], use_column_width=True)
              st.subheader(item_name)
              st.write(f"價格: {item_info['price']}")
              st.write(f"庫存: {item_info['stock']}")

              if st.button(f"購買{item_name}", key=f"buy_{item_name}"):
                  if item_info["stock"] > 0:
                      st.session_state.commodity[item_name]["stock"] -= 1
                      st.success(f"購買{item_name}成功")
                      time.sleep(0.5)
                      st.rerun()
                  else:
                      st.error(f"購買{item_name}失敗")
  ```

- **庫存管理**:

  ```python
  def add_stock():
      st.title("新增商品庫存")
      product_name = st.selectbox("請選擇要補貨的商品", list(st.session_state.commodity.keys()))
      add = st.number_input("請輸入要新增的庫存數量", value=1, min_value=1, max_value=10, step=1)
      if st.button("新增庫存"):
          st.session_state.commodity[product_name]["stock"] += add
          st.success("新增庫存成功")
          time.sleep(0.5)
          st.rerun()
  ```

- **主函數組織**:

  ```python
  def main():
      st.title("Vegeterian 購物商城")
      columns = st.number_input("請輸入行數", value=1, min_value=1, max_value=10, step=1)
      cols = st.columns(columns)

      image_folder = "image"
      img_files = load_images(image_folder)
      initialize_commodity(image_folder, img_files)
      display_products(cols)
      add_stock()
      display_current_stock()

  if __name__ == "__main__":
      main()
  ```

# 3. 函數 (Function)

- **函數定義與參數傳遞**:

  ```python
  def hello():
      print("Hello, world!")

  for i in range(10):
      hello()
  ```

- **帶參數的函數**:

  ```python
  def hello(name):
      print(f"Hello, {name}!")

  hello("world")
  hello("vegeterian")

  for i in range(10):
      hello(i)
  ```

- **有回傳值的函數**:

  ```python
  def add(a, b):
      return a + b

  print(add(1, 2))
  sum = add(1, 2)
  print(sum)
  ```

- **多個回傳值**:

  ```python
  def add_sub(a, b):
      return a + b, a - b

  sum, sub = add_sub(1, 2)
  print(f"sum = {sum}, sub = {sub}")
  ```

- **預設參數與類型提示**:

  ```python
  def hello(name, message="Hello!"):
      print(f"{message}, {name}")

  hello("Alice")
  hello("Bob", "Hi!")

  def add(a: int, b: int = 0) -> int:
      return a + b

  print(add(1, 2))
  ```
