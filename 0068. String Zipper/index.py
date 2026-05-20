# -*- encoding: utf-8 -*- 
# @Time: 2026/5/20 17:53
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def zip_strings(a, b):
    # 1. Python可以直接交替结果
    result = ''.join(ach + bch for ach, bch in zip(a, b))
    print(result)
    # 2. 获取最短的那个字符串
    min_len = min(len(a), len(b))

    # 3. 切片取有多余的字符串
    result += a[min_len:] + b[min_len:]

    return result
zip_strings("python", "javascript")
