# -*- encoding: utf-8 -*- 
# @Time: 2026/4/16 13:51
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def do_math(s):
    import re
    # 1. 找出数字
    nums = list(map(int, re.findall(r'\d+', s)))

    # 2. 找出间隔
    gaps = re.split(r'\d+', s)

    # 3. 计算每两个数字之间的间隔长度
    gap_lengths = [len(gaps[i]) for i in range(1, len(gaps) -1)]

    # 4. 初始化结果为第一个数字
    result = nums[0]

    # 5. 循环遍历
    for i in range(1, len(nums)):
        if(gap_lengths[i-1] % 2 == 0):
            result += nums[i]
        else:
            result -= nums[i]
    return result
do_math("3ab10c8")

