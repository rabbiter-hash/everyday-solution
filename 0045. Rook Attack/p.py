# -*- encoding: utf-8 -*- 
# @Time: 2026/4/11 10:19
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

""" =====================================================
    *** 第一种解法：标准解法
     - 1. 拆解坐标
        "A1" -> 列="A" -> 行="1"

     - 2. 如果行相同 -> 在同一行 -> 可攻击 -> True
     - 3. 如果列相同 -> 在同一列 -> 可攻击 -> True
===================================================== """
def rook_attack(rook1, rook2):
    # 1. 判定数据是否合法
    if not isinstance(rook1, str) \
        or not isinstance(rook2, str) \
        or (len(rook1) != 2 or len(rook2) != 2):
        raise TypeError("The Inputs must str and all length should be 2")

    # 2. 拆解字符串
    col1, row1 = rook1[0], rook1[1]
    col2, row2 = rook2[0], rook2[1]

    return col1 == col2 or row1 == row2

""" =====================================================
    *** 第二种解法：一行代码
===================================================== """
def rook_attack_single(rook1, rook2):
    return rook1[0] == rook2[0] or rook1[1] == rook2[1]

""" =====================================================
    *** 第三种解法：用zip
===================================================== """
def rook_attack_zip(rook1, rook2):
    return any(a == b for a, b in zip(rook1, rook2))
    # 相当于
    # for a, b in zip(rook1, rook2):
    #     if a == b:
    #         return True
    # return Flase