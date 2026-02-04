# -*- encoding: utf-8 -*- 
# @Time: 2026/2/3 14:52
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def get_sign(date_str: str) -> str:
    # 1. 处理输入的字符串
    _, month, day = map(int, date_str.split('-'))

    # 2. 通过月份和日期转成month_day，方便线性比较
    month_day = month * 100 + day

    # "Aries" Mar 21 - Apr 19
    if 321 <= month_day <= 419:
        return "Aries"
    # "Taurus" April 20 - May 20
    elif 420 <= month_day <= 520:
        return "Taurus"
    # "Gemini" May 21 - June 20
    elif 521 <= month_day <= 620:
        return "Gemini"
    # "Cancer" June 21 - July 22
    elif 621 <= month_day <= 722:
        return "Cancer"
    # "Leo" July 23 - August 22
    elif 723 <= month_day <= 822:
        return "Leo"
    # "Virgo" August 23 - September 22
    elif 823 <= month_day <= 922:
        return "Virgo"
    # "Libra" September 23 - October 22
    elif 923 <= month_day <= 1022:
        return "Libra"
    # "Scorpio" October 23 - November 21
    elif 1023 <= month_day <= 1121:
        return "Scorpio"
    # "Sagittarius"November 22 - December 21
    elif 1122 <= month_day <= 1221:
        return "Sagittarius"
    # "Capricorn" December 22 - January 19
    elif month_day >= 1222 or month_day <= 119:
        return "Capricorn"
    # "Aquarius"January 20 - February 18
    elif 120 <= month_day <= 218:
        return "Aquarius"
    else:
        return "Pisces"


print(get_sign("2026-01-31"))

def get_sign_map(date_str: str) -> str:
    _, month, day = map(int, date_str.split("-"))
    month_day = month * 100 + day

    # 因为Capricorn跨年，所以分成两段：1. Dec 22 - Dec 31，也就是1222 - 1231
    # 2. 第二段为：Jan 1 - Jan 19，也就是101 - 119
    ranges = [
        ((321, 419), "Aries"),
        ((420, 520), "Taurus"),
        ((521, 620), "Gemini"),
        ((621, 722), "Cancer"),
        ((723, 822), "Leo"),
        ((823, 922), "Virgo"),
        ((923, 1022), "Libra"),
        ((1023, 1121), "Scorpio"),
        ((1122, 1221), "Sagittarius"),
        ((1222, 1231), "Capricorn"),
        ((101, 119), "Capricorn"),
        ((120, 218), "Aquarius"),
        ((219, 320), "Pisces"),
    ]

    for start, end, zodiac in ranges:
        if start <= month_day <= end:
            return zodiac


def get_sign_tuple(date_str: str) -> str:
    _, month, day = map(int, date_str.split("-"))
    month_day = (month, day)

    if (3, 21) <= month_day <= (4, 19):
        return "Aries"
    elif (4, 20) <= month_day <= (5, 20):
        return "Taurus"
    elif (5, 21) <= month_day <= (6, 20):
        return "Gemini"
    elif (6, 21) <= month_day <= (7, 22):
        return "Cancer"
    elif (7, 23) <= month_day <= (8, 22):
        return "Leo"
    elif (8, 23) <= month_day <= (9, 22):
        return "Virgo"
    elif (9, 23) <= month_day <= (10, 22):
        return "Libra"
    elif (10, 23) <= month_day <= (11, 21):
        return "Scorpio"
    elif (11, 22) <= month_day <= (12, 21):
        return "Sagittarius"
    elif month_day >= (12, 22) or month_day <= (1, 19):
        return "Capricorn"
    elif (1, 20) <= month_day <= (2, 18):
        return "Aquarius"
    else:
        return "Pisces"