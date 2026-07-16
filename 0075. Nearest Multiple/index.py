# -*- encoding: utf-8 -*- 
# @Time: 2026/7/8 11:56
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def round_to_nearest_multiple(num, multiple):
    # 1. 先取出商
    quotient = num // multiple
    # 2. 余数
    remainder = num % multiple

    # 3. 比较
    if remainder < multiple / 2:
        return quotient * multiple
    else:
        return (quotient + 1) * multiple


round_to_nearest_multiple(5, 3)