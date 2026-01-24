# -*- encoding: utf-8 -*- 
# @Time: 2026/1/24 15:35
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

""" =============================================
    # 第一种解法：常规解法，使用if...elif...else解决
    ============================================= """
def get_bingo_letters_normal(n: int) -> str:
    """
    Returns the bingo letters with given an integer n
    :param n:
    :return: bingo letters
    """
    # 1. 判定是否是数字
    if(not isinstance(n ,int) or (n < 1) or (n > 75)):
        return "输入必须是数字且在1-75之间!"
    if( 1 <= n <= 15 ):
        return "B"
    elif( 16 <= n <= 30 ):
        return "I"
    elif( 31 <= n <= 45 ):
        return "N"
    elif( 45 <= n <= 60 ):
        return "G"
    else:
        return "O"

""" =============================================
    # 第二种解法：常规解法，使用数学中的等差法返回列表项
    ============================================= """
def get_bingo_letters_list(n: int) -> str:
    """
        Returns the bingo letters with given an integer n
        Use list[x] to get the bingo letters
    :param n:
    :return: bingo letters
    """
    if(not isinstance(n ,int) or (n < 1) or (n > 75)):
        return "输入必须是数字，且在1-75之间！"

    letters = ["B", "I", "N", "G", "O"]
    # return letters[ int((n - 1) / 15)] # 使用int向下取整
    return letters[ (n-1) // 15 ] # 整除

""" =============================================
    # 第三种解法：映射解法，
        将范围和字母做成字典映射
        从范围去匹配当前n的值再返回当前范围的字母
    ============================================= """
def get_bingo_letters_range_map(n: int) -> str:
    if(not isinstance(n, int) or (n < 1) or (n > 75)):
        return "invalid"

    # 映射表
    mapping = {
        range(1, 16): "B",
        range(16, 31): "I",
        range(31, 46): "N",
        range(46, 61): "G",
        range(61, 76): "O",
    }
    for r, letter in mapping.items():
        print(r, letter, sep=" | ")
        if n in r:
            return letter

""" =============================================
    # 第四种解法：配置驱动映射解法，
        类似解法3
    ============================================= """
BING_RULES = [
    (1, 15, "B"),
    (16, 30, "I"),
    (31, 45, "N"),
    (46, 60, "G"),
    (61, 75, "O"),
]
def get_bingo_letters_driver_map(n: int) -> str:
    if(not isinstance(n, int) or (n < 1) or (n > 75)):
        return "invalid"

    for start, end, letter in BING_RULES:
        print(start, end, letter, sep=" | ")
        if start <= n <= end:
            return letter


