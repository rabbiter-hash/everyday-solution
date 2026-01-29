# -*- encoding: utf-8 -*- 
# @Time: 2026/1/29 11:20
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)


def flatten(arr: list) -> list:
    if not isinstance(arr, list):
        raise ValueError('arr must be list')

    # 1. 栈
    stack = arr.copy() # 拷贝原数组
    result = []

    # 2. 开始迭代
    while(len(stack) > 0):
        # 从栈顶取出
        top = stack.pop()
        # 判定top是否是列表
        if isinstance(top, list):
            # 是的话就要遍历，或者extend
            stack.extend(top)
        else:
            result.append(top)

    # 3. LIFO
    return result[::-1]


print(flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(list(flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9]])))
print(flatten([["red", ["blue", ["green", ["yellow", ["purple"]]]]], "orange", ["pink", ["brown"]]]))
print(list(flatten([["red", ["blue", ["green", ["yellow", ["purple"]]]]], "orange", ["pink", ["brown"]]])))