# -*- encoding: utf-8 -*- 
# @Time: 2026/3/5 9:57
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

""" =====================================================
    *** 第一种解法：遍历求解
===================================================== """
def perfect_cube_count(a, b):
    # 1、查找最大值和最小值
    low = min(a, b)
    high = max(a, b)

    # 2、统计量
    count = 0

    # 3. 遍历，根据立方根公示求解
    for num in range(low, high + 1):
        # 判定负数的情况
        if num < 0:
            cube_root = round(-abs(num * (1 / 3)))
        else:
            cube_root = round(num * ( 1 / 3))

        # 反向求解当前数n是否等于num，如果等于，就让统计量+1
        if cube_root ** 3 == num:
            count += 1
    return count

print(abs(-64 ** (1/3)))

""" =====================================================
    *** 第二种解法：算法味的写法
===================================================== """
def perfect_cube_count_x(a, b):
    import math
    # 1. 提取最大值和最小值
    low = min(a, b)
    high = max(a, b)

    # 2. 求立方根
    min_n = math.ceil(abs(low) ** (1/3))
    max_n = math.floor(abs(high) ** (1/3))

    if low < 0:
        min_n = -min_n

    return max_n - min_n + 1

""" =====================================================
    *** 第三种解法：整数枚举法
===================================================== """
def perfect_cube_count_int_enumerate(a, b):
    # 1. 提取最大值和最小值
    low = min(a, b)
    high = max(a, b)

    # 2. 以0为边界
    n = 0
    while n ** 3 > low:
        # 如果n 的三次方 > 最小值，那么n就要往负数走
        n -= 1
    while n ** 3 < low:
        # n的三次方小于low，那么n就要往上走
        n += 1

    # 3. 开始统计
    count = 0
    while n ** 3 <= high:
        count += 1
        n += 1
    return count


perfect_cube_count_int_enumerate(-64, 64)