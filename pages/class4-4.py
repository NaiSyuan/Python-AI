# def
# 新增一個函數要用def 開頭，後面接著函數名稱，再接著小括號，最後加上冒號。
# 小括號裡面可以放入傳入的參數也可以不放


def hello():
    print("Hello, world!")


for i in range(10):
    hello()


# 有傳入參數的函數
# 這個參數有一個參數name，當呼叫這個函數時，可以傳入一筆資料給name
def hello(name):
    print(f"Hello, {name}!")


hello("world")
hello("vegeterian")

for i in range(10):
    hello(i)

# 有return回傳值的函數
# 這個函數會為傳一個值，當呼叫這個函數時，可以把回傳的值存起來
# 在指令當中只要執行return，就會回傳值，並結束函數


def add(a, b):
    return a + b


print(add(1, 2))
print(add("Hello,", "World"))

sum = add(1, 2)
print(sum)


# 有多個回傳值的函數
# 這個函數會回傳兩個值，當呼叫這個函數時，可以存起來兩個值
def add_sub(a, b):
    return a + b, a - b


sum, sub = add_sub(1, 2)
print(f"sum = {sum}, sub = {sub}")


# 多個return
def add_sub2(a, b):
    if a > b:
        return a + b
    else:
        return a - b


print(add_sub2(5, 6))
print(add_sub2(6, 5))


# 預設參數
# 可以再函樹的參數中，設定預設值，當呼叫這個函數時，如果沒有傳入值，就會使用預設值
# 多個參數時，有預設值的參數要放在沒有預設值的後面
def hello(name, message="Hello!"):
    print(f"{message}, {name}")


hello("Alice")
hello("Bob", "Hi!")


# 限制傳入的參數型態
# 可以再函數的參數中，設定傳入的參數型態，當呼叫這個函數時，可以提示使用者要傳入的參數型態
# 變數: 型態= 預設值
# -> 型態  代表回傳值的型態
def add(a: int, b: int = 0) -> int:
    return a + b


print(add(1, 2))
print(add("Hello,", "World"))
