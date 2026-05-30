# -*- encoding: utf-8 -*- 
# @Time: 2026/5/26 15:12
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def sum_of_differences(arr):
    # 1. 判断数据的合法性
    if not isinstance(arr, list):
        raise TypeError('arr must be a list')

    # 2. 初始化加和
    total = 0

    # 3. 循环比那里
    for i in range(len(arr) - 1):
        # 边界问题，一定要-1，不然会出现超出边界的问题
        total += arr[i + 1] - arr[i]
    print(total)
    return total

sum_of_differences([1, 3, 4])

def sum_of_differences_telescoping_method(arr):
    if not isinstance(arr,list):
        raise TypeError('arr must be a list')

    if len(arr) < 2:
        return 0

    return arr[-1] - arr[0]