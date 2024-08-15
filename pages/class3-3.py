# Arithmetic operators

a = 1
a += 1  # a = a + 1
print(a)  # 2
a -= 1  # a = a - 1
print(a)  # 1
a *= 2  # a = a * 2
print(a)  # 2
a /= 2  # a = a / 2
print(a)  # 1.0
a //= 2  # a = a // 2
print(a)  # 0.0
a %= 2  # a = a % 2
print(a)  # 0.0
a **= 2  # a = a ** 2
print(a)  # 1.0


# operators priority
# 1. () parentheses
# 2. ** power
# 3. +(positive)、-(negative)
# 4. * / // % multiplication、division、integer division、modulo
# 5. + - addition、subtraction
# 6. == != < > <= >= comparison
# 7. not and or logical
# 8. = += -= *= /= //= %= **= Arithmetic operators


# while loop
# while can be used to repeat a block of code until a condition is met
# 條件式為True 會一直重複執行迴圈
# 條件式為 Flause 會立刻退出迴圈
i = 0
while i < 10:
    print(i)
    i += 1  # i = i + 1

# break
# break 可以強制跳出循環
# 先判斷break屬於哪一個迴圈，然後跳出該迴圈
i = 0
while i < 10:
    print(i)

    for j in range(10):
        print(j)

    if i == 5:
        break  # this 'break' is belongs to while loop
    print(i)
    i += 1  # i = i + 1

for i in range(10):
    print(i)
    if i == 5:
        break
    print(i)


import random

# 設定範圍的方式與range()一樣
print(random.randrange(7))  # 0~6
print(random.randint(1, 6))  # 1~6
print(random.randrange(1, 6, 2))  # 1~6 step 2
# random.randint()的設定方式一定要設定開始與結束值
# 且結束的數字會包含在內
print(random.randint(1, 6))
