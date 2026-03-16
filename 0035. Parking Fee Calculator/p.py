# -*- encoding: utf-8 -*- 
# @Time: 2026/3/14 16:14
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

import math
""" =====================================================
    *** 第一种解法：常规解法
===================================================== """
def calculate_parking_fee(park_time, pickup_time):
    # 1. 转换为分钟
    entry_h, entry_m = map(int, park_time.split(":"))
    exit_h, exit_m = map(int, pickup_time.split(":"))

    entry_minutes = entry_h * 60 + entry_m
    exit_minutes = exit_h * 60 + exit_m

    # 2. 判断是否过夜并计算停车时长
    overnight = False

    if exit_minutes < entry_minutes:
        overnight = True
        duration = (24 * 60 - entry_minutes) + exit_minutes
    else:
        duration = exit_minutes - entry_minutes

    # 3. 向上取整计算小时数
    hours = math.ceil(duration / 60)

    # 4. 计算费用
    cost = hours * 3

    # 5. 过夜费
    if overnight:
        cost += 10

    # 6. 最低收费
    cost = max(cost, 5)

    return f"${cost}"
calculate_parking_fee("09:00", "11:00")

