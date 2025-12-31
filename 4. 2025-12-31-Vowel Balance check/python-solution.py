# -*- encoding: utf-8 -*- 
# @Time: 2025/12/31 13:54
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python-solution.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def is_balanced(s):
    vowels = set('aeiouAEIOU')
    if s == "":
        return False

    left = s[:len(s)//2]
    print(left)
    right = s[-(len(s)//2):]
    print(right)

    left_count = sum(1 for c in left if c in vowels)
    # 上面表达式等价于
    """
    left_count = 0
    for c in left:
        print(c)
        if c in vowels:
            left_count += 1
    """
    right_count = sum(1 for c in right if c in vowels)
    """
    # 上方代码等价于
    right_count = 0
    for c in right:
        print(c)
        if c in vowels:
            right_count += 1
    """
    return left_count == right_count


if __name__ == '__main__':
    s = 'abcdefg'
    print(is_balanced(s))
