# 猜數字遊戲
import random

min = 1
max = 100

num = random.randint(min, max)

while True:
    # try 是一個關鍵字，主要用於錯誤處理。它讓我們能夠在程式執行過程中，預先設定一個「試驗區」，當這個區塊內的程式碼發生錯誤時，我們可以採取特定的行動，
    # try 區塊： 放置可能產生錯誤的程式碼。
    # except 區塊： 如果 try 區塊內的程式碼發生錯誤，就會跳到 except 區塊執行。
    # try 跟except 是一對的，最少要有一個try，一個except，同一個try也可以有很多except。
    try:
        user_input = int(input(f"請輸入{min}到{max}的數字:"))
    except ValueError:  # 如果輸入不是數字
        print("請輸入有效的整數!")
        continue  # 跳過這次迴圈，直接進入下一次
    if min <= user_input <= max:
        if user_input > num:
            max = user_input
        elif user_input < num:
            min = user_input

    if user_input == num:
        print("恭喜你，正確！")
        break

    elif user_input > num:
        print("太大了!")

    elif user_input < num:
        print("太小了!")
