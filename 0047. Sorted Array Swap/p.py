# -*- encoding: utf-8 -*- 
# @Time: 2026/4/15 13:43
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)


def sort_and_swap(arr):
    # 1. 先排序原数组
    sorted_arr = sorted(arr)
    # print(len(sorted_arr)) # 12
    # 2. 循环并且原地交换
    for i in range(len(arr)):
        # index： 0 - 11
        if i % 3 == 0 and i > 0:
            # 原地交换
            # 将当前索引i的值替换成替换成它前一个元素的值
            sorted_arr[i], sorted_arr[i - 1] = sorted_arr[i - 1], sorted_arr[i]
    return sorted_arr

sort_and_swap([12, 5, 8, 1, 3, 10, 2, 7, 6, 4, 9, 11])