# -*- encoding: utf-8 -*- 
# @Time: 2026/1/27 14:23
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

import datetime

def odd_or_even_day(timestamp: int) -> str:
    """
    说明：输入毫秒级的时间戳，计算UTC时区的日期的日是奇数还是偶数
    :param timestamp: 毫秒级
    :return: str
    """
    dt = datetime.datetime.fromtimestamp(timestamp / 1000, datetime.UTC)
    # 本来可以使用utffromtimestamp(timestamp/1000)，但是即将弃用
    day = dt.day
    return "even" if day % 2 == 0 else "odd"


print(odd_or_even_day(6739456780000))