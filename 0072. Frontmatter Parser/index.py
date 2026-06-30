# -*- encoding: utf-8 -*- 
# @Time: 2026/6/26 10:46
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def parse_frontmatter(s):
    # 结果存储
    results = {}

    # 1. 去掉首尾，得到正确的字符串
    lines = s.split('\n')
    # 2. 去除首尾
    lines = lines[1:-1]

    # 3. 循环读取key和value
    for line in lines:
        key, value = line.split(":", 1) #按照第一个冒号分

        # 做空白处理
        value = value.strip()

        if value == "true":
            value = True
        elif value == "false":
            value = False
        else:
            # 有情况是浮点数的时候
            try:
                # 先将数字转成浮点数
                num = float(value)
                # 开始判定
                if num.is_integer():
                    value = int(value)
                else:
                    value = num
            except ValueError:
                pass

        # 将键值组成字典
        results[key] = value
    print(results)
    return results

parse_frontmatter("---\ntitle: My Post\ndraft: false\nviews: 100\n---")

