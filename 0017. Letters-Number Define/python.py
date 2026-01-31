# -*- encoding: utf-8 -*- 
# @Time: 2026/1/31 11:14
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

import re
def separate_letters_and_numbers(s: str) -> str:
    # 1.判定数据格式
    if not isinstance(s, str) or not s:
        raise ValueError('s must be a string')
    # 2. 结果集初始化
    result = [s[0]]
    print("初始化结果集为：", result)

    # 3. 从第二个元素开始遍历比较
    for i in range(1, len(s)):
        # 取出前一个元素和当前元素
        prev_ele = s[i-1]
        curr_ele = s[i]
        print(prev_ele, curr_ele, sep=" | ")

        # 判定前一个元素和当前元素是否为字母
        prev_is_letter = prev_ele.isalpha()
        curr_is_letter = curr_ele.isalpha()

        # 如果不等，则说明有一个是数字，一个是字母
        if(prev_is_letter != curr_is_letter):
            result.append("-")
        result.append(curr_ele)
    return "".join(result)
print(separate_letters_and_numbers("a1b2c3d4"))


def separate_letters_and_numbers_test(s: str) -> str:
    if not isinstance(s, str) or not s:
        raise ValueError('s must be a string')

    # 2. 结果集
    result = [s[0]]

    # 3. 遍历
    for i in range(1, len(s)):
        if(s[i-1].isalpha() != s[i].isalpha()):
            result.append("-")

        result.append(s[i])
    return "".join(result)


from functools import reduce
def separate_letters_and_numbers_with_reduce(s: str) -> str:
    if not isinstance(s, str) or not s:
        raise ValueError('s must be a string')

    return reduce(
        lambda acc, c: acc + ("-" if acc and acc[-1].isalpha() != c.isalpha() else "") + c,
        s,
        ''
    )