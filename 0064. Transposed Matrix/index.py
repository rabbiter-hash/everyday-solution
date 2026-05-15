# -*- encoding: utf-8 -*- 
# @Time: 2026/5/15 10:57
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def transpose(matrix):
    # 1. 空矩阵处理
    if not matrix:
        return []

    # 2. 获取矩阵的行和列，假设列的长度是一样的
    len_row = len(matrix)
    len_col = len(matrix[0])

    # 3. 初始化一个矩阵
    transposed = [[0] * len_row for _ in range(len_col)]

    print(transposed)

    # 4. 遍历
    for i in range(len_row):
        for j in range(len_col):
            transposed[j][i] = matrix[i][j]

    print(transposed)
    return transposed

transpose([
    [1, 2, 3],
    [4, 5, 6]])

def transpose_pythonic(matrix):
    return [list(row) for row in zip(*matrix)]
