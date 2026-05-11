# -*- encoding: utf-8 -*- 
# @Time: 2026/5/11 14:52
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def get_oldest_person_compare(people):
    # 1. 定义一个数组，用于存储结果
    oldest_person = []

    # 2. 定义一个负无穷大的变量，用于存储最大年龄
    max_age = float('-inf')

    # 3. 循环
    for person in people:
        # 取出name和age
        name = person['name']
        age = person['age']
        # 开始比较，如果当前发现的年龄比max_age大
        if age > max_age:
            # 更新max_age
            max_age = age
            # 清空数组
            oldest_names = [name]
        elif age == max_age:
            # 如果相等，证明有另外一个人有最大年龄
            oldest_names.append(name)
        else:
            pass
    return oldest_names

print(get_oldest_person_compare([{ "name": "George", "age": 50 }, { "name": "Shirley", "age": 42 }, { "name": "Beth", "age": 48 }, { "name": "Holly", "age": 50 }, { "name": "Kevin", "age": 44 }, { "name": "Frank", "age": 47 }, { "name": "Zach", "age": 50 }, { "name": "Jennifer", "age": 43 }]))

def get_oldest_person_pythonic(people):
    if not people:
        return []

    # 找到最大年龄
    max_age = max(person['age'] for person in people)
    return [person['name'] for person in people if person['age'] == max_age]

print(get_oldest_person_pythonic([{ "name": "George", "age": 50 }, { "name": "Shirley", "age": 42 }, { "name": "Beth", "age": 48 }, { "name": "Holly", "age": 50 }, { "name": "Kevin", "age": 44 }, { "name": "Frank", "age": 47 }, { "name": "Zach", "age": 50 }, { "name": "Jennifer", "age": 43 }]))
