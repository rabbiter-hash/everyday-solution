# -*- encoding: utf-8 -*- 
# @Time: 2026/5/18 15:44
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)


def get_bingo_range(letter):
    # 1. 判定输入合法性
    if not letter in ["B", "I", "N", "G", "O"]:
        return []

    # 2. 结构化存储规则
    mapping = {
        "B": "1-15",
        "I": "16-30",
        "N": "31-45",
        "G": "46-60",
        "O": "61-75"
    }

    # 3. 提取区间
    start, end = map(int, mapping[letter].split("-"))

    print(start, end)
    print(type(start), type(end))
    print(list(range(start, end + 1)))

    return list(range(start, end + 1))
get_bingo_range("B")

def get_bingo_range_pythonic(letter):
    mapping = {
        "B": (1, 15),
        "I": (16, 30),
        "N": (31, 45),
        "G": (46, 60),
        "O": (61, 75)
    }

    start, end = mapping[letter]

    return list(range(start, end + 1))