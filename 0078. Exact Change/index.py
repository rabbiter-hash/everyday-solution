# -*- encoding: utf-8 -*- 
# @Time: 2026/7/11 11:28
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def exact_change(amount):
    # 统计初始化
    count = 0

    # 1. 枚举quarter（25美分）
    for q in range(amount // 25 + 1):
        remaining_after_q = amount - q * 25
        # 2. 枚举dimes （10美分）
        for d in range(remaining_after_q // 10 + 1):
            remaining_after_d = remaining_after_q - d * 10
            # 3. 枚举nickles （5美分）
            for n in range(remaining_after_d // 5 + 1):
                # 剩下的用cents（1美分）补齐
                count += 1

    print(count)
    return count

exact_change(5)