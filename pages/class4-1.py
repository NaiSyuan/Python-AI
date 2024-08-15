# Dictionary
# dict is use key-value pair to store data, and key is unique, value is not(can be duplicated)
# dict is no ordered, and can not be accessed by index
# key of dict can be a don't change type like string, int, float, bool
# value of dict can be any type
# key-value of dict is use : to separate key and value,like this -> key : value
# key-value of dict is use , to separate every key-value pair, like this -> {key1 : value1, key2 : value2}

# get key of dict
book = {"title": "Python Crash Course", "author": "Eric Matthes", "price": 10.00}
print(book.keys())  # prints ["title", "author", "price"]
for key in book.keys():
    print(key)  # prints "title", "author", "price"


# get value of dict
print(book.values())  # prints [Eric Matthes,10.0]
for value in book.values():
    print(value)  # prints Eric Matthes, 10.0


# get key-value of dict
print(book.items())
# prints [("title", 10.0), ("author", Eric Matthes), ("price", 10.0)]
for key, value in book.items():
    print(key, value)  # prints "title 10.0", "author Eric Matthes", "price 10.0"


# add/update key-value of dict
book["title"] = "JavaScript Crash Course"
print(book)
# prints {"title": "JavaScript Crash Course", "author": "Eric Matthes", "price": 10.0}
book["author"] = "John Doe"
print(book)
# prints {"title": "JavaScript Crash Course", "author": "John Doe", "price": 10.0}

# check if key exist in dict
# in can't be used to check if value exist in dict
# compare with list and dict , "in" can be used to check 'element in list' or 'value in dict'
print("title" in book)  # prints True
print("name" in book)  # prints False


# delete key-value of dict
# if key not exist, it will 回傳預設值
# if key exist, it will 刪除並回傳value
print(book.pop("title"))  # prints "JavaScript Crash Course"
print(book.pop("name", "not found"))  # not exist, prints not found
# print(book.pop("name"))  # not exist,and no default value, prints KeyError: 'name'
# # 如果資料不存在，也沒有預設值，就會報錯

# 比較複雜的dict
d = {"a": [1, 2, 3], "b": {"c": 4, "d": 5}}
print(d["a"])  # prints [1, 2, 3]
print(d["a"][0])  # prints 1
print(d["b"])  # prints {"c": 4, "d": 5}
print(d["b"]["c"])  # prints 4
# 成績登記系統
grade = {
    "小名": {"國文": [90, 80, 70], "數學": [80, 70, 60], "英文": [70, 60, 50]},
    "大名": {"國文": [95, 85, 75], "數學": [85, 75, 65], "英文": [75, 65, 55]},
    "中名": {"國文": [100, 90, 80], "數學": [90, 80, 70], "英文": [80, 70, 60]},
}

# 取得成績
print(grade["小名"]["國文"])  # prints [90, 80, 70]
# 取大名的國文第一次成績
print(grade["大名"]["國文"][0])  # prints 95
# 取中名的英文第二次成績
print(grade["中名"]["英文"][1])  # prints 70


# print average of 國文's grade
for name, subject in grade.items():
    # get 國文的成績
    chinese = subject["國文"]  # 取得國文中的成績
    # 計算平均值
    avg = sum(chinese) / len(chinese)
    print(f"{name} average: {avg:.2f}")  # :.2f 可以指定小數點後幾位


# 印出每一位同學的總平均值
for name, subject in grade.items():
    total = 0
    for score in subject.values():
        total += sum(score)
    avg = total / (len(subject) * 3)
    print(f"{name} average: {avg:.2f}")


# 整理全校科目的平均成績
# 建立一個字典，存放每一個科目的平均成績
grade_avg = {"國文": [], "英文": [], "數學": []}
for subjects in grade.values():
    # subjects = {"國文": [90, 80, 70], "數學": [80, 70, 60], "英文": [70, 60, 50]}
    # 逐一取得每一位同學的成績
    for sub, score in subjects.items():
        # score = [90, 80, 70]、[80, 70, 60]、[70, 60, 50]
        grade_avg[sub] += score

print(grade_avg)

# dict 取長度，取的是key的數量
print(len(grade_avg))  # 3
