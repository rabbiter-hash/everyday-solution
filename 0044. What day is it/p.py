# -*- encoding: utf-8 -*- 
# @Time: 2026/4/7 10:33
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)


""" =====================================================
    *** 第一种解法：使用datetime库
    毫秒 -> 秒 -> utc时间 -> weekday
===================================================== """
def get_day_of_week(timestamp):
    from datetime import datetime
    # 1. 微妙转秒
    second = timestamp // 1000

    # 2. 转UTC时间，忽略时区
    dt = datetime.utcfromtimestamp(second)
    # print(dt) # 2026-04-06 16:17:29

    # 3. 映射日期
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[dt.weekday()]

print(get_day_of_week(1775492249000))

""" =====================================================
    *** 第二种解法：使用datetime库
    毫秒 -> 秒 -> utc时间 -> strftime
===================================================== """
def get_day_of_week_strftime(timestamp):
    from datetime import datetime
    return datetime.utcfromtimestamp(timestamp // 1000).strftime("%A")

print(get_day_of_week_strftime(1775492249000))

""" =====================================================
    *** 第三种解法：不使用库的解决办法
        # 1. 关键事实：
            - Unix 时间起点：1970-01-01 是星期四（Thursday）
            - 一天 = 86400 秒 = 86400000 毫秒
        # 2. 解题步骤
            - 毫秒 -> 多少天
                days = milliseconds // 86400000
            - 用星期循环，一周 7 天
                (day_index + 起点偏移) % 7
            - 起点偏移量：
                定义数组（从 Sunday 开始）：
                days_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                1970-01-01 是 Thursday
                在这个数组里 index = 4
            - 最终公式
                index = (days + 4) % 7
===================================================== """


def get_day_of_week_normal(timestamp):
    # 时间戳（毫秒） -> 天数
    # 一天 = 86400 秒 = 86400 * 1000 毫秒
    days = timestamp // (86400 * 1000)

    print(days)  # 从 Unix 起点到现在的总天数

    # 1970-01-01 是星期四（在数组中 index = 4），需要做偏移
    days_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    # 对 7 取模，得到星期索引
    return days_list[(days + 4) % 7]


get_day_of_week_normal(1775492249000)