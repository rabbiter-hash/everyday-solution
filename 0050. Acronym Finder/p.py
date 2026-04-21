# -*- encoding: utf-8 -*- 
# @Time: 2026/4/20 15:43
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)


def find_org(acronym):
    # 1. 将所有的organizations存储成列表
    organizations = [
        "National Avocado Storage Authority",
        "Cats Infiltration Agency",
        "Fluffy Beanbag Inspectors",
        "Department Of Jelly",
        "Wild Honey Organization",
        "Eating Pancakes Administration"
    ]

    # 2. 循环遍历并拼接organizations的简写
    for org in organizations:
        # 3. 初始化拼接
        initials = ""

        # 4. 提取org中的单词并提取首字母进行拼接
        all_words = org.split(" ")

        # 5. 每次循环取每个单词的首字母大写进行拼接
        for word in all_words:
            initials += word[0].upper()
        if(initials == acronym):
            return org
    return None

find_org("NASA")