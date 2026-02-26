# -*- encoding: utf-8 -*- 
# @Time: 2026/2/26 8:59
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

""" =====================================================
    *** 第一种解法：列表循环
===================================================== """
def find_differences(arr):
    # 1. 判定是否为列表
    if not isinstance(arr, list) or len(arr) == 0:
        raise ValueError("必须是列表且长度大于0！")

    # 2. 开始循环
    result = []
    for i in range(len(arr) - 1):
        # len(arr) - 1 防止越界
        result.append(arr[i+1]-arr[i]) # 后一个元素减去前一个元素
    # 3. 在循环的时候，用的是len(arr) - 1，没有循环到最后一个值，最后一个补0
    result.append(0)

    # 4. 返回数值
    return result

""" =====================================================
    *** 第二种解法： 列表推导式
===================================================== """
def find_differeneces_with_one(arr):
    # 1. 最开始还是判定是否为数组
    if not isinstance(arr, list) or len(arr) == 0:
        raise ValueError("Arr must be list or empty")
    # 2. 列表推导式
    return [arr[i+1] - arr[i] for i in range(len(arr)-1)] + [0]

""" =====================================================
    *** 第三种解法： 使用zip
===================================================== """
def find_differences_with_zip(arr):
    if not isinstance(arr, list) or len(arr) == 0:
        raise ValueError("Arr must be list or empty22")

    return [b-a for a, b in zip(arr, arr[1:])] + [0]
