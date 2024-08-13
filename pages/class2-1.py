# 比較運算子
print(1 == 1)  # True
print(1 != 1)  # False
print(1 < 2)  # True
print(1 > 2)  # False
print(1 <= 2)  # True
print(1 >= 2)  # False
print(1 == 2)  # False
print(1 != 2)  # True

# 邏輯運算子
# and運算子
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# or運算子
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# not運算子
print(not True)  # False
print(not False)  # True


# 運算子優先順序
# 1. () 括號
# 2. ** 次方
# 3. +(正數)、-(負數)
# 4. * / // % 乘 除 整除(取商) 取餘數
# 5. + - 加 減
# 6. == != < > <= >= 比較運算子
# 7. not and or 邏輯運算子


# 密碼門檢查
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


### 連續使用 if 與使用 if-elif-else的差別
# elif 可以排除前面已經判斷過的條件，因此可以縮短代碼，並節省時間。如果使用多個 if 來判斷，則每個 if 條件都會被執行，這會降低效率。
# 但如果每個條件都是獨立的事件，則應分別使用 if 來判斷。

password = input("請輸入密碼：")
if password == "123456":
    print("密碼正確")
else:
    print("密碼錯誤")
