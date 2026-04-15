# -*- encoding: utf-8 -*- 
# @Time: 2026/4/14 15:03
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)


def get_last_letter(s):
    import re
    # 1. 数据类型判定
    if not isinstance(s, str):
        raise TypeError('s must be a string')

    # 2. 提取字母
    letters = re.findall(r'[a-zA-Z]', s)

    if not letters:
        return ''

    # 3. 用小写取出字符串中最大的字符
    max_char = max(ch.lower() for ch in letters)

    # 3.遍历列表，找到第一个与最大字符串相等的字符
    for char in letters:
        if char.lower() == max_char:
            return char


print(get_last_letter("!#$ er@R asd fT.,> 2t0e9"))