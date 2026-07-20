# -*- encoding: utf-8 -*- 
# @Time: 2026/7/18 11:31
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def days_until_birthday(today, birthday):
    from datetime import datetime, date, timedelta

    # 1. 解析今天
    today = datetime.strptime(today, "%Y-%m-%d").date()
    print(today)
    year = today.year

    # 2. 解析生日
    month, day = map(int, birthday.split("/"))
    print(month, day)

    # 3. 尝试构造今年的生日
    try:
        this_year_birthday = date(year, month, day)
    except ValueError:
        # 如果是 2/29 且今年不是闰年，则今年没有这个日期
        # 直接跳到下一年
        this_year_birthday = None

    if this_year_birthday:
        if this_year_birthday > today:
            next_birthday = this_year_birthday
        else:
            # 今天 >= 今年生日，找明年的
            try:
                next_birthday = date(year + 1, month, day)
            except ValueError:
                # 明年也不是闰年，继续往后找
                next_year = year + 1
                while True:
                    try:
                        next_birthday = date(next_year, month, day)
                        break
                    except ValueError:
                        next_year += 1
    else:
        # 今年没有这个生日（2/29 非闰年），直接找下一个闰年的 2/29
        next_year = year + 1
        while True:
            try:
                next_birthday = date(next_year, month, day)
                break
            except ValueError:
                next_year += 1

    # 计算天数差
    delta = next_birthday - today
    return delta.days


days_until_birthday("2026-07-16", "9/7")