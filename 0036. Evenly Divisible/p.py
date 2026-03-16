# -*- encoding: utf-8 -*- 
# @Time: 2026/3/16 15:48
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)


""" =====================================================
    *** 第一种解法：取模法
===================================================== """
def is_evenly_divisible(a, b):
    # 1. 判定数据合法性
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('a and b must be integers')
    # 2. 除数不能是0,
    if b == 0:
        return False

    # 3. 直接返回
    return a % b == 0

""" =====================================================
    *** 第二种解法：除法 + 乘法验证法
===================================================== """
def is_evenly_divisible_with_divi(a, b):
    if b == 0:
        return False

    return (a // b) * b == a

""" =====================================================
    *** 第三种解法：用divmod()
===================================================== """
def is_evenly_divisible_divmod(a, b):
    if b == 0:
        return False

    _, reminder = divmod(a, b)
    if reminder != 0:
        return False
    return True

