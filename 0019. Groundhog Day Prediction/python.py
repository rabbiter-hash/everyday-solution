# -*- encoding: utf-8 -*- 
# @Time: 2026/2/3 8:39
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def groundhog_day_prediction(appearance):
    # case-match，python3.10后
    match appearance:
        case True:
            return "Looks like we'll have six more weeks of winter."
        case False:
            return "It's going to be an early spring."
        case _:
            return "No prediction this year."

print(groundhog_day_prediction(''))