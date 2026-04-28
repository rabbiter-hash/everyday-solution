# -*- encoding: utf-8 -*- 
# @Time: 2026/4/28 15:10
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def get_number_words(n):
    # 1. 首先编码20以下的
    words = [
        "zero", "one", "two", "three", "four", "five", "six", "seven",
        "eight", "nine", "ten", "eleven", "twelve", "thirteen",
        "fourteen", "fifteen", "sixteen", "seventeen",
        "eighteen", "nineteen"
    ]
    # print(len(words))  20

    # 2. 编码数字整数位
    tens = [
        "", "", "twenty", "thirty", "forty", "fifty", "sixty",
        "seventy", "eighty", "ninety"
    ]

    # 3. 判定输入的n
    if n < 20:
        return words[n]

    # 4. 判定是否整除
    ten = n // 10 # 整除获得十位数
    one = n % 10 # 取模取得个位数

    if one == 0:
        # 说明是整数
        return tens[ten]

    return tens[ten] + "-" + words[one]

print(get_number_words(21))