# -*- encoding: utf-8 -*- 
# @Time: 2026/2/26 14:32
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)


""" =====================================================
    *** 第一种解法：使用str.isalpha()和str.isdigit()方法进行判定
===================================================== """
def count_letters_and_numbers_with_str_method(s):
    # 1. 判定是否是字符串
    if not isinstance(s, str):
        raise ValueError("输入的不是字符窜！")
    # 2. 判定字符串长度
    if len(s) == 0:
        raise ValueError("不能是空字符串！")

    # 3. 定义统计量
    letter_count = 0
    number_count = 0

    # 4. 开始遍历
    for char in s:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            number_count += 1

    letter_word = "letter" if letter_count == 1 else "letters"
    number_word = "number" if number_count == 1 else "numbers"

    return f"The string has {letter_count} {letter_word} and {number_count} {number_word}."

# print(count_letters_and_numbers_with_str_method("helloworld123"))

""" =====================================================
    *** 第二种解法：双sum写法，基于解法一，但更严谨，isalpha()匹配的是unicode字符
===================================================== """
import string
def count_letters_and_numbers_with_two_sums(s: str) -> str:
    # 1. 输入必须是非空字符串
    if not isinstance(s, str) or len(s) == 0:
        raise ValueError("输入必须是非空字符串！")

    # 2. 列表推导式进行统计
    letter_count = sum(c in string.ascii_letters for c in s)
    # string.ascii_letters只包含英文字母
    number_count = sum(c.isdigit() for c in s)

    return (f"The string has {letter_count} "
            f"{'letter' if letter_count == 1 else 'letters'} "
            f"and {number_count} "
            f"{'number' if number_count == 1 else 'numbers'}.")
print(count_letters_and_numbers_with_two_sums("helloworld123"))

""" =====================================================
    *** 第三种解法：单次遍历 + 双计数（性能最优）
===================================================== """
def count_letters_and_numbers_with_for_and_two_counts(s: str) -> str:
    # 1. 输入必须是非空字符
    if not isinstance(s, str) or len(s) == 0:
        raise ValueError("输入必须是非空字符！")

    # 2. 双计数
    letter_count = number_count = 0

    # 3. 遍历
    for char in s:
        if char in string.ascii_letters:
            letter_count += 1
        elif char.isdigit():
            number_count += 1

    # 4. 返回
    return (
        f"The string has {letter_count} "
        f"{'letter' if letter_count == 1 else 'letters'} "
        f"and {number_count} "
        f"{'number' if number_count == 1 else 'numbers'}."
    )

print(count_letters_and_numbers_with_for_and_two_counts("helloworld123"))

