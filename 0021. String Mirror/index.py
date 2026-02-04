# -*- encoding: utf-8 -*- 
# @Time: 2026/2/4 9:38
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

""" =====================================================
    *** 第一种解法：转成列表再原地翻转再拼接
===================================================== """
def mirror(s: str) -> str:
    # 1. 判定数据类型
    if not isinstance(s, str):
        raise TypeError('s is not a string')

    # 2. 拆解字符串
    str_list = list(s)
    # str_list = [item for item in s]
    # 3. 拷贝列表
    str_list_copy = str_list[:]

    # 4. 翻转拷贝列表
    str_list_copy.reverse()

    # 5. 扩展列表
    str_list.extend(str_list_copy)
    print(str_list)
    return ''.join(str_list)

mirror("freeCodeCamp")

""" =====================================================
    *** 第二种解法：使用字符串切片
===================================================== """
def mirror_with_slice(s: str) -> str:
    # 1. 判定数据
    if not isinstance(s, str):
        raise TypeError('s is not a string')

    # 2. 字符串切片
    return s + s[::-1]

""" =====================================================
    *** 第三种解法：转成列表再原地翻转再拼接
===================================================== """
def mirror_with_reversed(s: str) -> str:
    if not isinstance(s, str):
        raise TypeError('s is not a string')
    # print(list(reversed(s)))
    return s + "".join(reversed(s))
mirror_with_reversed("freeCodeCamp")

""" =====================================================
    *** 第四种解法：简化第一种方法的解法
===================================================== """
def simple_mirror(s: str) -> str:
    # 1. 判定数据类型是否合法
    if not isinstance(s, str):
        raise TypeError('s is not a string')
    # 2.
    chars = list(s)
    return "".join(chars + chars[::-1])