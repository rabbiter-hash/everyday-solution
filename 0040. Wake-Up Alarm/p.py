# -*- encoding: utf-8 -*- 
# @Time: 2026/3/31 17:31
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

""" =====================================================
    *** 第一种解法：常规解法
===================================================== """
def alarm_check(alarm_time, wake_time):
    # 1. 先拆分时间字符串
    alarm_time_hour = int(alarm_time.split(':')[0])
    alarm_time_minute = int(alarm_time.split(':')[1])

    wake_time_hour = int(wake_time.split(':')[0])
    wake_time_minute = int(wake_time.split(':')[1])

    # 2. 比较小时
    if wake_time_hour < alarm_time_hour:
        # 如果起床时间的小时小于闹钟时间的小时，那么一定是早起
        return "early"
    elif wake_time_hour == alarm_time_hour:
        # 同小时，比较分钟
        if wake_time_minute < alarm_time_minute:
            return "early"
        elif wake_time_minute <= alarm_time_minute + 10:
            # 闹钟偏后十分钟
            return "on time"
        else:
            return "late"
    else:
        # wake_time_hour > alarm_time_hour
        # 计算超过闹钟多少分钟
        minutes_late = (wake_time_hour - alarm_time_hour) * 60 + (wake_time_minute - alarm_time_minute)
        if minutes_late <= 10:
            return "on time"
        else:
            return "late"
