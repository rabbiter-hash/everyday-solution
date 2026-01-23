# -*- encoding: utf-8 -*- 
# @Time: 2026/1/23 14:26
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def vowel_case(s: str) -> str:
    """ 注释 #=============================================
                *** 元音字母转大写
                    辅音字母转小写
                :return str
              ============================================= # """
    if not isinstance(s, str):
        return '不是字符串，拜拜！'

    vowels = set('aeiouAEIOU')
    result = []
    for char in s:
        if char in vowels:
            result.append(char.upper())
        elif char.isalpha():
            result.append(char.lower())
        else:
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    print(vowel_case('"HELLO, world!"'))