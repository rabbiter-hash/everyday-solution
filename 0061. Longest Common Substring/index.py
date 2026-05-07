# -*- encoding: utf-8 -*- 
# @Time: 2026/5/7 14:30
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def get_longest_substring(s):
    """
    暴力枚举法
        # 1、枚举所有可能的子串
        # 2、对每个子串检查它在原字符串中出现了不止一次。
        # 3、记录最长的那个
    """
    # 1. 首先获取字符串的长度
    s_length = len(s)
    print(s_length)

    # 2. 初始化最长子串
    longest_substring = ""

    # 3. 开始循环枚举
    for i in range(s_length):
        for j in range(i + 1, s_length + 1):
            substring = s[i:j]

            # 剪枝：如果当前子串长度 <= 已找到的最长长度，跳过
            if len(substring) <= len(longest_substring):
                continue

            # 检查这个子串是否在后面再次出现
            if substring in s[i+1:]:
                longest_substring = substring

    print(longest_substring)
    return longest_substring
get_longest_substring("abracadabra")