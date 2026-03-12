# -*- encoding: utf-8 -*- 
# @Time: 2026/3/12 14:52
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

""" =====================================================
    *** 第一种解法：循环遍历
===================================================== """
def is_valid_domino_chain_with_for(dominoes):
    # 1. 判定数据的合法性
    # 1.1。 输入必须是数组
    if not isinstance(dominoes, list):
        raise TypeError("dominoes must be a list")
    # 1.2. 判定数字是否在1-6之间
    for domino in dominoes:
        if not isinstance(domino, list):
            raise TypeError("domino must be a list")
        # 检查内层数组的长度
        if(len(domino) != 2):
            raise ValueError("domino must have 2 elements")
        for d in domino:
            if not isinstance(d, int) or not (1 <= d <= 6):
                raise ValueError("domino must be an integer between 1 and 6")
    # 2. 空数组和一个元素的二维数组应该return True，因为没有违反规则
    if len(dominoes) <= 1:
        return True

    # 3. 循环
    for i in range(len(dominoes) - 1):
        if(dominoes[i][1] != dominoes[i+1][0]):
            return False

    return True

# print(is_valid_domino_chain_with_for([[1, 3], [3, 6], [6, 5]]))

""" =====================================================
    *** 第二种解法：循环遍历 + 手动取变量
===================================================== """
def is_valid_domino_chain_mannual_var(dominoes):
    # 1. 判定数据的合法性
    # 1.1. 输入必须是数组
    if not isinstance(dominoes, list):
        raise TypeError("dominoes must be a list")
    # 1.2. 内层数组判定，长度，和值的合法性
    for domino in dominoes:
        if not isinstance(domino, list):
            raise TypeError("domino must be a list")
        # 判定内层数组的长度
        if(len(domino) != 2):
            raise ValueError("domino must have 2 elements")

        # 内层数组的元素值必须在1-6之间
        for d in domino:
            if not isinstance(d, int) or not (1 <= d <= 6):
                raise ValueError("domino must be an integer between 1 and 6")

    # 2. 特殊情况，空数组和一个元素的二维数组应该返回True，因为没有违反规则
    if len(dominoes) <= 1:
        return True

    # 3. 循环 + 手动取变量
    for i in range(len(dominoes) - 1):
        # 必须-1，以防超出边界
        current = dominoes[i]
        next = dominoes[i+1]

        right = current[1]
        left = next[0]
        if(right != left):
            return False

    return True

""" =====================================================
    *** 第三种解法：循环遍历 + zip
===================================================== """
def is_valid_domino_chain_with_zip(dominoes):
    # 1. 判定数据的合法性
    # 1.1. 输入必须是数组
    if not isinstance(dominoes, list):
        raise TypeError("dominoes must be a list")
    # 1.2. 内层数组判定，长度，和值的合法性
    for domino in dominoes:
        if not isinstance(domino, list):
            raise TypeError("domino must be a list")
        # 判定内层数组的长度
        if (len(domino) != 2):
            raise ValueError("domino must have 2 elements")

        # 内层数组的元素值必须在1-6之间
        for d in domino:
            if not isinstance(d, int) or not (1 <= d <= 6):
                raise ValueError("domino must be an integer between 1 and 6")

    # 2. 特殊情况，空数组和一个元素的二维数组应该返回True，因为没有违反规则
    if len(dominoes) <= 1:
        return True

    # 3. 循环遍历 + zip
    for a, b in zip(dominoes, dominoes[1:]):
        print(a, b)
        if(a[1] != b[0]):
            return False
    return True

# is_valid_domino_chain_with_zip([[1, 3], [3, 6], [6, 5]])
""" =====================================================
    *** 第四种解法：使用all函数
===================================================== """
def is_valid_domino_chain_with_all(dominoes):
    return all(a[1] == b[0] for a, b in zip(dominoes, dominoes[1:]))