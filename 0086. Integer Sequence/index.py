# -*- encoding: utf-8 -*- 
# @Time: 2026/10/28 9:35
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def sequence(n):
    # 1. 存储结果
    result = ''

    # 2. 开始循环，python要注意边界
    for i in range(n):
        result += str(i + 1)

    print(result)
    return result

sequence(5)

# 2. 一句话解决
def sequence_use_join(n):
    return "".join(str(i) for i in range(1, n+1))

