# -*- encoding: utf-8 -*- 
# @Time: 2026/4/3 9:12
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def capitalize_fibonacci_normal(s:str) -> str:
    # 1. 结果
    result = []

    # 2. 基础斐波那契
    a, b = 0, 1

    # 2. 循环
    for i, char in enumerate(s):
        # 判定是否为字符，关键
        if char.isalpha():
            # 判定当前轮循环是否等于斐波那契数列数值
            if i == a:
                result.append(char.upper())
                # 添加之后，要更新斐波那契的值
                a, b = b, a + b
            else:
                # 如果不是斐波那契数列值，但是是字符，直接小写
                result.append(char.lower())
        else:
            result.append(char)

    return "".join(result)


def capitalize_fibonacci(s: str) -> str:
    # 1. 获取字符串的最大索引
    max_index = len(s) - 1

    # 2. 斐波那契数列的值
    fib_set = set()
    a, b = 0, 1

    while a <= max_index:
        #
        fib_set.add(a)
        a, b = b, a + b

    result = []
    # 3. 循环读取字符串，取出所以与当前集合中的索引进行比对
    for i, char in enumerate(s):
        # 判定i是否在集合中
        if i in fib_set:
            # 如果存在，就让当前char大写
            result.append(char.upper() if char.isalpha() else char)
        else:
            # 如果不存在，需要判定是否为大写，如果是大写就要转成小写
            result.append(char.lower() if char.isalpha() else char)

    print(result)
    return "".join(result)
capitalize_fibonacci("hello world")