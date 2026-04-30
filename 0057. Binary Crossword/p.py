# -*- encoding: utf-8 -*- 
# @Time: 2026/4/30 14:29
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)


def is_in_crossword(char):

    # 1. 定义矩阵
    grid = [
        [0, 1, 0, 0, 0, 0, 0, 1],
        [0, 1, 1, 0, 1, 1, 1, 1],
        [0, 1, 0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 0]
    ]

    # 2. 使用format + ord取得字母的八位二进制
    target = format(ord(char), "08b")

    print(target)
    print(type(target)) # str

    # 3. 先循环二维矩阵的行
    for row in grid:
        # print(row) # list
        row_str = "".join(map(str, row))
        if row_str == target or row_str[::-1] == target:
            return True

    # 4. 循环取每一列的值
    for col in range(len(grid[0])):
        # 要先固定列的值
        # 定义列上的字符串
        col_str = ""
        for row in range(len(grid)):
            col_str += str(grid[row][col])
            # 取值
            # grid[0][0],grid[1][0],grid[2][0]....
        # 取完所有值再进行比较
        if(col_str == target or col_str[::-1] == target):
            return True
    return False
print(is_in_crossword("Q"))

