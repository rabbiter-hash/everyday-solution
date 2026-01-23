# -*- encoding: utf-8 -*- 
# @Time: 2026/1/16 17:50
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

import math
def is_integer_hypotenuse(a, b):
    # 直接开平方
    c = math.sqrt(a**2 + b**2)
    return c.is_integer()

print(is_integer_hypotenuse(780, 1040))