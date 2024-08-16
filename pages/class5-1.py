# def 區域變數與全域變數

lenth = 5
area = 3.14


def calculate_square_area():
    area = lenth**2  # lenth 是全域變數，area 是區域變數
    # length = length**2 這行會出錯，
    # 因為在函數內部length是區域變數，不能直接修改全域變數
    print("面積是", area)


calculate_square_area()  # 面積是 25
# print("長度是", area  )#錯誤


lenth = 10
calculate_square_area()  # 面積是 100
# print("面積是", area)  # 錯誤，因為area 是區域變數

lenth = 5
area = 3.14 * 10**2


def calculate_square_area():
    area = lenth**2  # lenth 是全域變數，area 是區域變數


calculate_square_area()
print("面積是", area)  # 面積是 314


lenth = 5
area = 3.14 * 10**2


def calculate_square_area():
    # ("面積是", area)  # 加了這行，錯誤，因為area此時是區域變數，尚未被賦值
    area = lenth**2  # lenth 是全域變數，area 是區域變數
    print("面積是", area)


calculate_square_area()


lenth = 5
area = 50


def calculate_square_area():
    area = lenth**2  # lenth 是全域變數，area 是區域變數
    return area  # 將區域變數丟到全域變數


area = calculate_square_area()
print("面積是", area)  # 面積是 100


lenth = 5
area = 50


def calculate_square_area():
    global area  # 使用global 將area 變數全域變數，可以在函數內修改全域變數的值
    area = lenth**2  # lenth 是全域變數，area 是區域變數


calculate_square_area()
print("面積是", area)  # 面積是 100


def hello(name: str):
    """
    指令說明區\n
    這是一個多行指令說明區

    參數:\n
    name: str使用者名稱

    回傳:\n
    None

    範例:hello("Alice")
    """
    print(f"Hello, {name}!")
