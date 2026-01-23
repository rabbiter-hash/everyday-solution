# -*- encoding: utf-8 -*- 
# @Time: 2026/1/21 11:57
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def to_consonant_case(s: str) -> str:
    vowels = set('aeiouAEIOU')
    print(vowels)
    result = []

    for char in s:
        if char == '-':
            result.append('_')
        elif char in vowels:
            result.append(char.lower())
        elif char.isalpha():
            result.append(char.upper())
        else:
            result.append(char)
    return ''.join(result)

print(to_consonant_case("-heloeee-"))