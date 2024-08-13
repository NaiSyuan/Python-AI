# 新增list
L = []  # 這是一個空的list
print(L)

L = [1, 2, 3, 4, 5]  # 這是一個list，其中包含5個元素
print(L)

L = [1, 2, 3, "a", "b", "c"]  # 這是一個list，其中包含6個元素
print(L)

L = [1, 2, 3, [4, 5, 6], [7, 8, 9]]  # 這是一個list，其中包含5個元素
print(L)

L = [1, True, "a", 2.33]  # 這是一個list，其中包含4個元素
print(L)


# list 讀取元素, 元素的index從0開始
L = [1, 2, 3, "a", "b", "c"]  # 這是一個list，其中包含6個元素
print(L[0])  # 取出第一個元素
print(L[1])  # 取出第二個元素
print(L[2])  # 取出第三個元素
print(L[3])  # 取出第四個元素
print(L[4])  # 取出第五個元素
print(L[5])  # 取出第六個元素

# list 讀取長度，也就是list中有幾個元素，不是index的最大值
L = [1, 2, 3, "a", "b", "c"]
print(len(L))  # 長度為6

# list 走訪元素
# 可以透過取得index的方式來找到list中的的資料
# 也可以直接把list 當作一個範圍來取得資料
# 這兩種方式都可以，一情境判斷是否會用到index來決定要用哪一種方式
L = [1, 2, 3, "a", "b", "c"]
for i in L:  # in 後面放的是一個有範圍的元素
    print(i)

for i in range(len(L)):
    print(L[i])

for i in range(0, len(L), 2):
    print(L[i])


# 跟range 一樣用法，只是符號不同
# 取index 0 到最後，每次取2個元素，所以是[1,3,"b"]
print(L[::2])
# 取出第1到第3個元素，不包含第4個元素，所以是[2,3,"a"]
print(L[1:4])
# 取出第1到第3個元素，不包含第4個元素，每次取2個元素，所以是[2,"a"]
print(L[1:4:2])


# call by value
a = 1
b = a  # 複製a的內容到b
b = 2
print(a, b)

# call by reference
a = [1, 2, 3]
b = a  # 把a跟b指向同一個記憶體位址，所以改變b的內容，也會改變a的內容，同理a也是
b[0] = 2
print(a, b)


print("---")
a = [1, 2, 3]
b = a.copy()  # 複製a的內容到b，a和b指向不同記憶體位址
b[0] = 2
print(a, b)
