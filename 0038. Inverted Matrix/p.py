# -*- encoding: utf-8 -*- 
# @Time: 2026/3/19 16:29
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

""" =====================================================
    *** 第一种解法：常规遍历法，将值替换
===================================================== """
def invert_matrix(matrix: list) -> list:
    # 1. 先找到两个值
    values = set()
    for row in matrix:
        values.update(row)

    v1, v2 = values
    print(v1, v2) # 顺序是不确定的
    # 2. 构建新矩阵并遍历
    result = []
    for row in matrix:
        # 取出矩阵中的每个列表元素，也就是行row
        # print(row)
        new_row = []
        for cell in row:
            if cell == v1:
                new_row.append(v2)
            else:
                new_row.append(v1)
        result.append(new_row)
    print(result)
    return result
invert_matrix([["a", "b"], ["a", "a"]])