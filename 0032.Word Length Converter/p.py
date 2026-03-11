# -*- encoding: utf-8 -*- 
# @Time: 2026/3/11 17:28
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

""" =====================================================
    *** 第一种解法：循环遍历
===================================================== """
def convert_words_with_for(s):
    # 1. 判定输入是否合法
    if not isinstance(s, str):
        raise TypeError('s must be a string')

    # 2. 将字符串串转成列表
    words_lis = s.split(" ")

    # 3. 初始化长度存放的数组
    words_length_lis = []

    # 4. 遍历
    for word in words_lis:
        words_length_lis.append(str(len(word)))

    print(words_length_lis)
    # 5. 返回
    return " ".join(words_length_lis)

convert_words_with_for("hello world")

""" =====================================================
    *** 第二种解法：列表推导式
===================================================== """
def convert_words_one(s):
    return " ".join([str(len(word)) for word in s.split(" ")])

""" =====================================================
    *** 第三种解法：函数式
===================================================== """
def convert_words_with_map(s):
    return " ".join(map(lambda w: str(len(w)), s.split(" ")))
