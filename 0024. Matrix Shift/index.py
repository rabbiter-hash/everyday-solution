# -*- encoding: utf-8 -*- 
# @Time: 2026/2/28 10:40
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

""" =====================================================
    *** 第一种解法：常规解法
        展开 -> 移动 -> 还原
===================================================== """
def shift_matrix(matrix, shift):
    # 1. 首先判定输入是否合法
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a list')
    if not isinstance(shift, int):
        raise TypeError('shift must be an integer')

    # 2. 数组信息
    # 行数
    rows = len(matrix)
    # 列数
    cols = len(matrix[0])
    print(rows, cols, sep = " | ")
    # 总长度
    n = rows * cols

    # 3. 处理shift，防止长度过长越界
    shift = shift % n # 取模运算符可以防止越界

    # 4. 展开数组
    flat = []
    for row in matrix:
        flat.extend(row)
    # print(flat)

    # 5. 右移shift位
    if shift != 0:
        flat = flat[-shift:] + flat[:-shift]

    # 6. 还原数组
    result = []
    for i in range(rows):
        # 根据原数组的行数，确定要切分数组的起始位置和结束位置
        start = i * cols
        end = start + cols
        result.append(flat[start:end])
    print(result)
    return result
# shift_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], -1)

