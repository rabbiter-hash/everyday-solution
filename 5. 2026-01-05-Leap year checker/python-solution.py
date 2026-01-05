# -*- encoding: utf-8 -*- 
# @Time: 2026/1/5 11:12
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python-solution.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def is_leap_year(year):
    """
    Checks if the given year is a leap year.
    :conditions:
        1. year is a positive integer;
        2. year can be divided by 4 but not 100;
        3. year can be divided by 400.
    :param year:
    :return: Boolean
    """
    # 1. year must be position integer
    if(not isinstance(year, int) or year <= 0):
        return False

    # 2. conditions
    if((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        return True
    else:
        return False

