# -*- encoding: utf-8 -*- 
# @Time: 2026/7/16 11:51
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def chunk_array(arr, size):
    # 1. 初始化结果集
    results = []

    # 2. 遍历
    for i in range(0, len(arr), size):
        # 左闭右开，步长为size
        results.append(arr[i:i+size])

    print(results)
    return results

chunk_array([1, 2, 3, 4, 5, 6], 3)

def chunk_array_pythonic(arr, size):
    return [arr[i:i+size] for i in range(0, len(arr), size)]
    # return list(arr[i:i+size] for i in range(0, len(arr), size))