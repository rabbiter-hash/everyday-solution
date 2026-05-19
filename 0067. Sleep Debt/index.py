# -*- encoding: utf-8 -*- 
# @Time: 2026/5/19 16:58
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def sleep_debt(hours_slept, target_hours):
    # 1. 变量设定
    # 1.1、过去几天的睡觉小数总和
    past_total = sum(hours_slept)
    # 1.2、过去几天的天数
    n = len(hours_slept)
    # 1.3、总共需要睡觉的小时数，包含今天
    need_total = target_hours * (n + 1)

    # 2. 判定
    # 如果过去睡觉的总数已经超过需要的小时数，按照题目意思返回0
    if past_total >= need_total:
        return 0

    return need_total - past_total

print(sleep_debt([6, 6, 6, 6, 6, 6], 8))
