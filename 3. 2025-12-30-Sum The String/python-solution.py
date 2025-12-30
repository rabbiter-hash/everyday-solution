# -*- encoding: utf-8 -*- 
# @Time: 2025/12/30 14:32
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python-solution.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

import re
def string_sum(s):
    # 1. 使用正则表达式，查找藏在字符串中的所有数字
    digits_results = re.findall(r'\d+', s)

    total = 0
    # 2. 实现累加
    for num in digits_results:
        total += int(num)

    # 3. 返回结果
    return total

def string_sum_one_line(s):
    # 1. re.findall(r'\d+', s) -> list
    # 2. int(num) for num in re.findall(r'\d+', s) -> int list
    # 3. sum(list) -> digit
    return sum(int(num) for num in re.findall(r'\d+', s))



