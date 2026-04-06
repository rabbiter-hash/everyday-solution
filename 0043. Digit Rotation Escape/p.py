# -*- encoding: utf-8 -*- 
# @Time: 2026/4/6 8:23
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

""" =====================================================
    *** 第一种解法：常规解法
===================================================== """
def get_rotation(n: int):
    # 1. 首先判定数字的合法性
    if not isinstance(n, int) or "0" in str(n) or n < 0:
        raise TypeError("n must be a positive integer and not contains 0")

    # 2. 将数字转成字符串并提取出长度
    str_n = str(n)
    len_n = len(str_n)

    # 3. 循环读取
    for i in range(len_n):
        # 旋转0次，就是str_n[0:] + str_n[:0]符合题意
        # 旋转1次，就是str_n[1:] + str_n[:1]
        # 边界问题，旋转range(len_n)包前不包后
        rotated_num = int(str_n[i:] + str_n[:i])
        # 判定当前被旋转的数字，是否能整除数字的长度
        if rotated_num % len_n == 0:
            return i
    return "none"
get_rotation(84138789345)
get_rotation(24681)


