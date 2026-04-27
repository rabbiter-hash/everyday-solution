# -*- encoding: utf-8 -*- 
# @Time: 2026/4/27 17:35
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def get_word_score(word):
    # 1. 映射硬编码
    letter_values = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
        'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
        'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22,
        'W': 23, 'X': 24, 'Y': 25, 'Z': 26
    }

    # 2. 累加初始化
    total = 0

    # 3. 循环累加
    for ch in word:
        # 将每个单次转大写
        ch = ch.upper()
        if ch in letter_values:
            total += letter_values[ch]

    return total

# 2. 使用函数
def get_word_score_by_ord(word):
    # 1. 初始化累加值
    total = 0

    # 2. 循环
    for ch in word.upper():
        if "A" <= ch <= "Z":
            total += ord(ch) - ord("A") + 1
    return total
get_word_score_by_ord("hi")

# 3. Pythonic
def get_word_score_pythonic(word):
    return sum(
        ord(ch) - 64
        for ch in word.upper()
        if "A" <= ch <= "Z"
    )