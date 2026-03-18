# -*- encoding: utf-8 -*- 
# @Time: 2026/3/18 15:11
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

""" =====================================================
    *** 第一种解法：常规遍历法
===================================================== """

def largest_number_normal_for(s: str) -> int or float:
    # 1. 判定用户输入
    if not isinstance(s, str):
        raise TypeError("Input must be a string!")

    # 2. 初始化统计
    nums = []
    current = ""

    # 3. 开始循环
    for i, ch in enumerate(s):
        # print(i, ch)
        # 因为是扫描字符串，所以要判定字符是否是数字跟小数点
        if ch.isdigit() or ch == ".":
            # 如果是数字且是小数点，我们就构建current
            current += ch  # 它会类似1 -> 5 -> :，现在还在构建的过程中，所以不能append
        elif ch == "-" and current == "":
            # 确定负数的情况，如果当前ch是-号，并且current为空，我们就构建负数
            current = "-"
        else:
            # if中的条件一定是要碰到数字跟小数点才会进行构建，else中我们要确定current是有值才能append
            if current and current != "-":
                nums.append(current)
                # 构建完后，将current重置
                current = ""
    # 4. 构建的时候如果最后一个字符不是特殊字符，那么current应该会有一个值存在
    if current and current != "-":
        nums.append(current)

    # 5. 求取最大值
    largest = max(nums, key=lambda x: float(x))

    # 6. 返回
    return float(largest) if "." in largest else int(largest)

largest_number_normal_for("4;15:60,26?52!0")


""" =====================================================
    *** 第二种解法：正则解法
===================================================== """
def largest_number_with_reg(s: str) -> int or float:
    import re
    # 1. pattern匹配正数、负数和小数
    pattern = re.compile(r"-?\d+\.?\d*")
    nums = re.findall(pattern, s)

    largest = max(nums, key=lambda x: float(x))
    return float(largest) if "." in largest else int(largest)
