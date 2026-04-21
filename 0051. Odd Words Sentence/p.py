# -*- encoding: utf-8 -*- 
# @Time: 2026/4/21 16:23
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def get_odd_words(s):
    # 1. 拆分输入的字符串
    words_lis = s.split()

    # print(words_lis)

    # 2. 结果数组
    results = []

    # 3. 循环遍历
    for ch in words_lis:
        if len(ch) % 2 != 0:
            results.append(ch)

    return " ".join(results)
get_odd_words("This is a super good test")

def get_odd_words_one(s):
    return " ".join([word for word in s.split() if len(word) % 2 != 0])