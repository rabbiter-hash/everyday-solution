# -*- encoding: utf-8 -*- 
# @Time: 2026/3/3 8:49
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

""" =====================================================
    *** 第一种解法：数据类型判定
        通过判定输入数组的每个元素的数据类型，碰到数组类型的就返回flase
===================================================== """

def is_flat(arr: list) -> bool:
    # 1. 判定数据类型
    if not isinstance(arr, list):
        raise TypeError('arr must be a list')

    # 2. 循环读取每个元素，如果有一个是数组类型，return false结束函数
    for item in arr:
        if isinstance(item, list):
            return False

    return True

""" =====================================================
    *** 第二种解法：用all判定
===================================================== """
def is_flat_use_all(arr: list) -> bool:
    # 1. 数据类型判定
    if not isinstance(arr, list):
        raise TypeError('arr must be a list')

    # 2. all函数
    return all(not isinstance(item, list) for item in arr)

""" =====================================================
    *** 第三种解法：用any判定，与all对偶
===================================================== """
def is_flat_us_all(arr: list) -> bool:
    if not isinstance(arr, list):
        raise TypeError('arr must be a list')
    return not any(isinstance(item, list) for item in arr)
    # any的意思是，只要有一个item为list，any就返回True
