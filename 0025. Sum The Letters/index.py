# -*- encoding: utf-8 -*- 
# @Time: 2026/3/2 15:14
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)
import re


""" =====================================================
    *** 第一种解法：常规解法
        映射 -> 替换 -> 求值
===================================================== """
def sum_letters_with_chr(s):
    # 1. 判定是否符合要求
    if not isinstance(s, str) or len(s) == 0:
        return 0
    # 2. 映射
    mapping = {chr(i+97):i+1 for i in range(26)}
    print(mapping)

    # 3. 处理s中的特殊字符
    s = re.sub(r'[^a-zA-Z]', '', s)

    # 4. 开始循环
    total = 0
    for c in s.lower():
        if c in mapping:
            total += mapping[c]
    return total
print(sum_letters_with_chr('abc'))

""" =====================================================
    *** 第二种解法：ord函数
===================================================== """

def sum_letters_with_ord(s):
    # 1. 判定是否为字符串
    if not isinstance(s, str) or len(s) == 0:
        raise ValueError('Empty string')
    if not s:
        return 0

    # 累加器
    total = 0

    # 2. 处理字符串中的特殊字符，因为只需要字母，可以用排除
    # s = re.sub(r'[^a-zA-Z]', '', s)

    # 3. 累加
    for char in s:
        if char.isalpha():
            total += ord(char.lower()) - ord('a') + 1

    # # 累加也可以换成一句话代码
    # total = sum(ord(c.lower()) - ord('a') + 1 for c in s)
    return total

print(sum_letters_with_ord("The quick brown fox jumps over the lazy dog."))

""" =====================================================
    *** 第三种解法：生成器式一句话
===================================================== """
def sum_letters_with_generator(s):
    return sum(ord(c.lower()) - ord('a') + 1 for c in s if c.islpah())