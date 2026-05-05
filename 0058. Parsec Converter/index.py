# -*- encoding: utf-8 -*- 
# @Time: 2026/5/5 11:31
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)


def convert_parsecs(parsecs):
    # 1. 判定数据的合法性
    if not isinstance(parsecs, int):
        raise TypeError("parsecs must be a number")

    # 2. 直接返回
    # return parsecs * 3 if parsecs % 2 == 0 else parsecs * 2

    # 更简洁
    return parsecs * (3 if parsecs % 2 == 0 else 2)
