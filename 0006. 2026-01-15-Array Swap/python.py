# -*- encoding: utf-8 -*- 
# @Time: 2026/1/15 17:12
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

""" 注释 #=============================================
    *** 将长度为2的列表进行翻转，有如下几种方法：
    1. 解包赋值法（tuple unpacking）
    2. 列表切片翻转
    3. 索引显示返回
    ============================================= # """
def array_swap_with_tuple_unpacking_first(arr: list) -> list:
    # 1. 要求的是长度为2的列表进行翻转
    if len(arr) != 2:
        return
    # 2. 解包赋值
    a,b = arr
    return [b, a]

def array_swap_with_tuple_unpacking_second(arr: list) -> list:
    if len(arr) != 2:
        return
    arr[0], arr[1] = arr[1], arr[0]
    return arr


def array_swap_with_list_slice_reversed_first(arr: list) -> list:
    # 1. 要求的是给长度为2的列表进行翻转
    if len(arr) != 2:
        return
    return arr[::-1]

def array_swap_with_list_slice_reversed_second(arr: list) -> list:
    return list(reversed(arr))


def array_swap_with_index(arr: list) -> list:
    if len(arr) != 2:
        return
    return [arr[1], arr[0]]


