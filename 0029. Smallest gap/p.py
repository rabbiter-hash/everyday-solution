# -*- encoding: utf-8 -*- 
# @Time: 2026/3/7 14:03
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

""" =====================================================
    *** 第一种解法：暴力遍历
===================================================== """
def smallest_gap(s):
    # 1. 判定数据的合法性
    if not isinstance(s, str):
        raise TypeError('S must be a string')

    # 2. 初始化最小gap
    min_gap = float('inf') # 创建一个无穷大的浮点数，将它赋值给min_gap

    # 3. 初始化结果变量
    result = ""

    # 4. 开始循环遍历
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            # 如果出现了，就计算gap
            if s[i] == s[j]:
                gap = j - i - 1
                if gap < min_gap:
                    min_gap = gap
                    result = s[i+1:j]
    print(result)
    return result

# smallest_gap("ABCDAC")

""" =====================================================
    *** 第二种解法：哈希表
===================================================== """
def smallest_gap_with_hash_table(s):
    # 1. 判定数据的合法性
    if not isinstance(s, str):
        raise TypeError('S must be a string')

    # 2. 初始化哈希表和最小gap以及结果
    last_pos = {}  # 哈希表：记录字符最近一次出现的位置
    min_gap = float('inf')  # 初始化为正无穷，保证第一次gap一定能更新
    result = ""

    # 3. 遍历字符串
    for i, char in enumerate(s):

        """
        ======== 循环过程示例 (字符串: "ABCDAC") ========

        初始状态:
        last_pos = {}
        min_gap = ∞
        result = ""

        -----------------------------------------
        第1次循环
        i = 0
        char = 'A'

        'A' 不在 last_pos 中
        不计算 gap

        更新哈希表:
        last_pos['A'] = 0

        last_pos = {'A': 0}

        -----------------------------------------
        第2次循环
        i = 1
        char = 'B'

        'B' 不在 last_pos 中

        更新哈希表:
        last_pos['B'] = 1

        last_pos = {'A':0, 'B':1}

        -----------------------------------------
        第3次循环
        i = 2
        char = 'C'

        'C' 不在 last_pos 中

        更新哈希表:
        last_pos['C'] = 2

        last_pos = {'A':0, 'B':1, 'C':2}

        -----------------------------------------
        第4次循环
        i = 3
        char = 'D'

        'D' 不在 last_pos 中

        更新哈希表:
        last_pos['D'] = 3

        last_pos = {'A':0, 'B':1, 'C':2, 'D':3}

        -----------------------------------------
        第5次循环 (关键)
        i = 4
        char = 'A'

        'A' 已经在 last_pos 中
        上一次位置 = 0

        计算 gap:
        gap = 4 - 0 - 1 = 3

        中间字符串:
        s[1:4] = "BCD"

        因为:
        3 < ∞

        更新:
        min_gap = 3
        result = "BCD"

        更新字符最新位置:
        last_pos['A'] = 4

        last_pos = {'A':4, 'B':1, 'C':2, 'D':3}

        -----------------------------------------
        第6次循环
        i = 5
        char = 'C'

        'C' 在 last_pos 中
        上一次位置 = 2

        计算 gap:
        gap = 5 - 2 - 1 = 2

        中间字符串:
        s[3:5] = "DA"

        因为:
        2 < 3

        更新:
        min_gap = 2
        result = "DA"

        更新字符位置:
        last_pos['C'] = 5

        last_pos = {'A':4, 'B':1, 'C':5, 'D':3}

        -----------------------------------------
        循环结束

        最终:
        result = "DA"
        """

        if char in last_pos:
            gap = i - last_pos[char] - 1
            if gap < min_gap:
                min_gap = gap
                result = s[last_pos[char] + 1:i]

        # 更新字符最近出现的位置
        last_pos[char] = i

    print(result)
    print(last_pos)

    return result

smallest_gap_with_hash_table("ABCDAC")


