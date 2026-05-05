# -*- encoding: utf-8 -*- 
# @Time: 2026/5/5 14:00
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)


def is_narcissistic(n):
    # 1. 判定输入的合法性
    if not isinstance(n, int):
        raise TypeError("N must be an integer!")

    # 2. 预存储相加结果
    total = 0
    # 3. 输入数字的位数，用于幂计算
    power = len(str(n))

    # 4. 循环
    for digit in str(n):
        total += int(digit) ** power

    if total == n:
        return True
    return False

is_narcissistic(153)

def is_narcissistic_pythonic(n):
    digits_to_str_list = str(n)
    power = len(digits_to_str_list)

    return n == sum(
        int(d)**power for d in digits_to_str_list
    )