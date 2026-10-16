# -*- encoding: utf-8 -*- 
# @Time: 2026/10/16 9:55
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: idx.py.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def strip_tags(html):
    # 1. 初始化结果集，采用列表吧，比较好拼接
    result_lis = []

    # 2. 初始化状态标识
    status = False

    # 3. 开始循环并赋予状态
    for ch in html:
        if ch == '<':
            status = True
        elif ch == '>':
            status = False
        # 当not status的时候，就追加列表
        elif not status:
            result_lis.append(ch)

    print(result_lis)
    print("".join(result_lis))
    return "".join(result_lis)
strip_tags('<a href="#">Click here</a>')