# -*- encoding: utf-8 -*- 
# @Time: 2026/3/10 11:20
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

""" =====================================================
    *** 第一种解法：遍历相加
===================================================== """
def sum_array(numbers):
    # 1. 判定数据的合法性
    if not isinstance(numbers, list):
        raise TypeError('numbers is not a list')

    # 2. 初始化计数器
    total = 0

    # 3. 遍历数组的每个元素
    for i in numbers:
        if not isinstance(i, (int, float)):
            # 如果不是数字，就跳过当前轮
            continue
        total += i
    print(total)
    return total
sum_array([1, 2, 3, 4, 5])

def sum_array_pythonic(numbers):
    # 将上面版本优化成
    if not isinstance(numbers, list):
        raise TypeError('numbers is not a list')
    return sum(i for i in numbers if isinstance(i, (int, float)))

""" =====================================================
    *** 第二种解法：reduce()函数
===================================================== """
from functools import reduce
def sum_array_with_reduce(numbers):
    # 1. 判定数据是否合法
    if not isinstance(numbers, list):
        raise TypeError('numbers is not a list')

    # 2. 直接用reduce返回
    return reduce(lambda acc, x: acc + x if isinstance(x, (int, float)) else acc, numbers, 0)
    # ====================
        # acc: 累加器
        # x： 当前元素
        # 逻辑：
            # 如果 x 是整数或浮点数 → acc + x（累加）
            # 否则 → acc 不变（跳过非数字）
    # ====================#