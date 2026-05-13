# -*- encoding: utf-8 -*- 
# @Time: 2026/5/13 10:53
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)


def get_frequency(s):
    # 1. 结果存储
    freq = {}

    # 2. 遍历
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    return freq


def get_frequency_counter(s):
    from collections import Counter
    return dict(Counter(s))
