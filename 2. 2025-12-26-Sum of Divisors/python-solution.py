# -*- encoding: utf-8 -*- 
# @Time: 2025/12/26 15:51
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python-solution.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def sum_divisors(n:int) -> int:
    """
    直观解法
    """
    sum = 0
    if n <= 0:
        return 'Positive Integer is needed!'
    for i in range(1, n + 1):
        if(n % i == 0):
            # print(i)
            sum += i
            # print(sum)
    return sum

import math
def sum_divisors_sqrt(n:int) -> int:
    """
        因数是成对出现的：
        如果 i 是因数，那么 n // i 也是因数。
    """
    sum = 0
    if n <= 0:
        return 'Positive Integer is needed!'
    for i in range(1, int(math.sqrt(n)) + 1):
        print(i)
        print(math.sqrt(n))
        if(n % i == 0):
            sum += i
            if(i != n//i):  # 避免平方数重复加
                sum += n//i
    return sum

print(math.sqrt(4))