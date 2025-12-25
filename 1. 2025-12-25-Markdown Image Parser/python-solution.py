# -*- encoding: utf-8 -*- 
# @Time: 2025/12/25 14:36
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python-solution.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

import re

def markdown_image_parser(markdown: str) -> str:
    # 顺序处理方法
    results = []
    # 1. 正则规则
    pattern = r'!\[([^\]]+)\]\(([^)]+)\)'
    """
        正则解释：
        1. 核心规则，使用()捕获组
        # !\[：匹配 ![
        # ([^\]]+)：第 1 个捕获组 → Cute cat
        # \]：匹配 ]
        # \(：匹配 (
        # ([^)]+)：第 2 个捕获组 → cat.png
        # \)：匹配 )
        2. 需要注意的是\[和圆括号内[的关系。
    """
    # 2. 判定
    if not markdown:
        return ''
    # 3. 开始匹配
    g = re.match(pattern, markdown)
    if not g:
        return ''

    # 4. 存储结果
    for item in g.groups():
        results.append(item)

    # 5. 返回结果
    return f'<img src="{results[1]}" alt="{results[0]}">'

def markdown_image_parser_short(markdown: str) -> str:
    # 更简洁版
    pattern = r'!\[([^\]]+)\]\(([^)]+)\)'
    m = re.search(pattern, markdown)

    if not m:
        return ''

    alt, src = m.groups()
    return f'<img src="{src}" alt="{alt}">'