# -*- encoding: utf-8 -*- 
# @Time: 2026/4/29 15:53
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def parse_url_query(url):
    # 1. 初始化结果
    result = {}

    # 2. 用 ? 分割取后面部分
    query = url.split("?")[1]

    # 3. 用 & 分割参数
    params = query.split("&")

    # 4. 遍历参数
    for param in params:
        key, value = param.split("=")
        result[key] = value

    return result

parse_url_query("https://example.com/search?name=Alice&age=30")

def parse_url_query_pythonic(url):
    # 1. 先取到参数
    query = url.split("?")[1]
    print(query)

    return {
        key:value
        for key, value in (
            param.split("=")
            for param in query.split("&")
        )
    }
parse_url_query_pythonic("https://example.com/search?name=Alice&age=30")