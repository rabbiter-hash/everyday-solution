# -*- encoding: utf-8 -*- 
# @Time: 2026/3/10 13:32
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

""" =====================================================
    *** 第一种解法：循环遍历加条件判定
===================================================== """
def insert_into_arr_with_for(arr, value, index):
    # 1. 判定数据的合法性
    if not isinstance(arr, list):
        raise TypeError('arr should be a list')
    if not isinstance(index, int):
        raise TypeError('index should be an integer')

    # 2. 初始化记录值
    result = []

    # 3. 遍历数组
    for i, v in enumerate(arr):
        print(i, v, sep= " | ")
        if i == index:
            # 假如到了指定的索引
            result.append(value)
        # 这里不用else，因为if只做条件判定，而下方的追加，是for循环的必要流程
        result.append(v)
    # 4. index 可能会出现大于 数组长度的情况，这时候只要追加到末尾
    if index >= len(arr):
        result.append(value)

    return result

print(insert_into_arr_with_for([2, 4, 8, 10], 6, 2))

""" =====================================================
    *** 第二种解法：切片
===================================================== """
def insert_into_arr_with_slice(arr, value, index):
    # 1. 判定数据的合法性
    if not isinstance(arr, list):
        raise TypeError('arr should be a list')
    if not isinstance(index, int):
        raise TypeError('index should be an integer')
    # 2. 利用列表切片，原则：左闭右开
    return arr[:index] + [value] + arr[index:]
print(insert_into_arr_with_slice([2, 4, 8, 10], 6, 2))

""" =====================================================
    *** 第三种解法：Python有一个方法insert就是原地插入的
===================================================== """
def insert_into_arr_with_insert(arr, value, index):
    # 1. 判定数据的合法性
    if not isinstance(arr, list):
        raise TypeError('arr should be a list')
    if not isinstance(index, int):
        raise TypeError('index should be an integer')

    # 2. 原地修改数组
    arr.insert(index, value)

    # 3. 赋值给new_arr
    new_arr = arr[:]

    return new_arr
    # 也可以先复制数组，用新数组去做insert()操作
print(insert_into_arr_with_insert([2, 4, 8, 10], 6, 2))