### 比較運算子

- `==`：判斷是否相等
  - `print(1 == 1)`  # True
  - `print(1 == 2)`  # False
- `!=`：判斷是否不相等
  - `print(1 != 1)`  # False
  - `print(1 != 2)`  # True
- `<`：判斷是否小於
  - `print(1 < 2)`  # True
- `>`：判斷是否大於
  - `print(1 > 2)`  # False
- `<=`：判斷是否小於或等於
  - `print(1 <= 2)`  # True
- `>=`：判斷是否大於或等於
  - `print(1 >= 2)`  # False

### 邏輯運算子

- `and` 運算子
  - `print(True and True)`  # True
  - `print(True and False)`  # False
  - `print(False and True)`  # False
  - `print(False and False)`  # False
- `or` 運算子
  - `print(True or True)`  # True
  - `print(True or False)`  # True
  - `print(False or True)`  # True
  - `print(False or False)`  # False
- `not` 運算子
  - `print(not True)`  # False
  - `print(not False)`  # True

### 運算子優先順序

1. `()` 括號
2. `**` 次方
3. `+` (正數)、`-` (負數)
4. `*` `/` `//` `%` 乘、除、整除(取商)、取餘數
5. `+` `-` 加、減
6. `==` `!=` `<` `>` `<=` `>=` 比較運算子
7. `not` `and` `or` 邏輯運算子

### 密碼門檢查

```python
while True:
    password = input("請輸入密碼：")
    if password == "123456":
        print("密碼正確")
        break
    elif password == "12345678":
        print("歡迎XXX")
        break
    elif password == "123456789":
        print("歡迎OOO")
        break
    else:
        print("密碼錯誤")
```

### 連續使用 `if` 與使用 `if-elif-else` 的差別

- `elif` 可以排除前面已經判斷過的條件，縮短代碼，節省時間。如果使用多個 `if` 判斷，每個 `if` 條件都會被執行，會降低效率。如果每個條件都是獨立事件，則應分別使用 `if` 來判斷。

```python
password = input("請輸入密碼：")
if password == "123456":
    print("密碼正確")
else:
    print("密碼錯誤")
```

### Streamlit 使用

- `st.number_input()`
  - 用來取得數字輸入
  - `number = st.number_input("Please input a number", step=1, min_value=0, max_value=100)`
- `st.markdown()`
  - 用來顯示 Markdown 文本
  - `st.markdown(f"The number is ：{number}")`

- 顯示分數等級

  ```python
  score = st.number_input("Please input the score", step=1, min_value=0, max_value=100)
  if score > 90:
      st.markdown("A")
  elif score > 80:
      st.markdown("B")
  elif score > 70:
      st.markdown("C")
  elif score > 60:
      st.markdown("D")
  else:
      st.markdown("F")
  ```

- `st.button()`
  - 用來創建和顯示按鈕
  - `st.button("Click me", key="clickme")`
  - `if st.button("Click me", key="balloonssnow"):`
    - `st.balloons()`
    - `st.snow()`

### `for` 迴圈

- 基本用法

  ```python
  for i in range(10):
      print(i)
  ```

- 指定範圍

  ```python
  for i in range(2, 10):
      print(i)
  ```

- 指定間隔

  ```python
  for i in range(2, 11, 3):
      print(i)
  ```

### `list` 操作

- `append`：將元素加入列表末尾

  ```python
  L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  L.append(11)
  print(L)
  ```

- 移除元素
  - `remove`：移除指定元素

    ```python
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3]
    L.remove(3)
    ```

  - `pop`：移除指定索引的元素

    ```python
    L = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    L.pop(0)  # 移除第一個元素
    L.pop(-1)  # 移除最後一個元素
    L.pop()  # 移除最後一個元素
    ```

### 金字塔和箭頭金字塔示範

- 數字金字塔

  ```python
  number = st.number_input("Please input a number", step=1, min_value=1, max_value=9)
  for i in range(0, number + 1):
      st.markdown(f"{i}" * i)
  ```

- 箭頭金字塔

  ```python
  a = st.number_input("Enter a number:", min_value=1, step=1)
  output = ""
  for i in range(1, a + 1):
      output += " " * (a - i) + "*" * ((i - 1) * 2) + "*\n"
  for i in range(a):
      output += " " * (a - 1) + "*\n"
  st.markdown(f"```\n箭頭金字塔 \n{output}```")
  ```

### `list` 的基本操作

- 新增和讀取元素

  ```python
  L = [1, 2, 3, "a", "b", "c"]
  print(L[0])  # 第一個元素
  ```

- 讀取長度

  ```python
  print(len(L))  # 長度為6
  ```

- 走訪元素

  ```python
  for i in L:
      print(i)
  ```

### `call by value` 和 `call by reference`

- `call by value`

  ```python
  a = 1
  b = a
  b = 2
  print(a, b)  # 1, 2
  ```

- `call by reference`

  ```python
  a = [1, 2, 3]
  b = a
  b[0] = 2
  print(a, b)  # [2, 2, 3], [2, 2, 3]

  a = [1, 2, 3]
  b = a.copy()
  b[0] = 2
  print(a, b)  # [1, 2, 3], [2, 2, 3]
  ```
