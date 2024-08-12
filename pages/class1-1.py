"""
這是多行註解
"""

"""
# 這是單行註解

print("hello")  # print是在終端機中顯示文字的指令
# ctrl + ? 可以快速註解文字/反註解，不一定要匡滿


# 基本型態
print(1)  # int這是整數
print(1.0)  # float這是浮點數
print(1.234567890)  # float這是浮點數
print("1")  # str這是字串"string","56454"
print(True)  # bool這是布林值
print(False)  # bool這是布林值


b = max(1, 2, 3)
print(max(1, 2, 3))
print(b)

# 變數
a = 10  # 新增變數a，將"="右邊的10存入左邊的a
print(a)  # 在終端機中顯示存在a的值

a = "apple"  # 新增變數a，將"="右邊的"apple"存入左邊的a
print(a)  # 在終端機中顯示存在a的值

# 運算子
print(1 + 2)  # 加法
print(1 - 2)  # 減法
print(1 * 2)  # 乘法
print(1 / 2)  # 除法
print(1 // 1)  # 整除(取商)
print(1 % 2)  # 取餘數
# 次方
print(1**2)  # 平方
print(1**0.5)  # 平方根

# 優先順序
# 1. () 括號
# 2. ** 次方
# 3. * / // % 乘 除 整除(取商) 取餘數
# 4. + - 加 減

# 字串運算，+、*
print("hello" + "world")  # 字串加法
print("hello" * 3)  # 字串重複三次

# 字串格式化
name = "apple"
age = 18
print(f"My name is {name} and I am {age} years old.")  # 字串格式化f-string
# 可以將變數或其他型態的資料放到f裡面的{}中，這樣就可以在字串中顯示

# 取字串的長度
print(len("hello"))  # len()是一個函數，可以計算字串的長度

# 取得資料物件的型態
print(type("hello"))  # type()是一個函數，可以取得資料物件的型態
print(type(1))  # <class 'int'>
print(type(1.0))  # <class 'float'>
print(type(1.234567890))  # <class 'float'>
print(type("1"))  # <class 'str'>
print(type(True))  # <class 'bool'>
print(type(False))  # <class 'bool'>

# 型態轉換
print(int(1.0))  # 將float轉換成int
print(float("123"))  # 將int轉換成float
print(str(123))  # 將int轉換成str
print(bool(0))  # 將int轉換成bool
print(bool(1))  # 如果內容為有，則將其轉換成True
print(bool("hello"))  # 如果字為有，則將其轉換成True
print(bool(""))  # 如果字串為無，則將其轉換成False
# print(int("hello"))  # 如果字串內容不是字元，則無法轉換成int


a = input("請輸入你的名字：")  # input()是一個函數，可以讀取輸入的內容
type(a)  # 取得資料物件的型態
print(type(a))  # <class 'str'>，證明透過input()取得的內容是字串
print(int(a) + 100)  # 將字串轉換成int，然後加100
print(a)


# 向使用者尋問半徑，依此半徑計算園面積，並將結果輸出至螢幕
d = float(input("請輸入半徑："))  # input()是一個函數，可以讀取輸入的內容
print(f"圓面積{3.14 * d**2}")  # 將半徑轉換成圓周率，並將結果輸出至螢幕
"""
