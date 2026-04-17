# -*- encoding: utf-8 -*- 
# @Time: 2026/4/17 14:17
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)


def get_initials(name):
    # 1. 判定输入是否合法
    if not isinstance(name, str):
        raise TypeError('name must be a string')

    # 2. 以空格拆分字符串
    name_words = name.split()

    # 3. 初始化存储结果
    names_initials = []
    for name_word in name_words:
        names_initials.append(name_word[0].upper())

    return ".".join(names_initials) + "."

    # 一句话代码
    return ".".join(word[0].uppper() for word in name.split("")) + "."
