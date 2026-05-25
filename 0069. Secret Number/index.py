# -*- encoding: utf-8 -*- 
# @Time: 2026/5/25 13:40
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def guess_number(secret, guess):
    # 1. 常规判断法
    if guess < secret:
        return "higher"
    elif guess > secret:
        return "lower"
    else:
        return "you got it!"


def guess_number_pythonic(secret, guess):
    return (
        "higher" if guess < secret
        else "lower" if guess > secret
        else "you got it!"
    )