# -*- encoding: utf-8 -*- 
# @Time: 2026/10/28 11:17
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def validate(email):
    # 1. 判定@在email中的数量，要有且只有一个
    if(email.count('@') != 1):
        return False
    # 2. 通过@进行分割字符串
    local_part, domain_part = email.split('@')
    # 2.1、如果local_part或者domain_part为空，就返回False
    if(not local_part or not domain_part):
        return False
    # 3. 对local_part进行判定
    ## 3.1、local_part不能以.开始或者结束
    if(local_part.startswith('.')):
        return False
    if(local_part[-1] == '.'):
        return False
    ## 3.2、local_part不能连续出现两个..
    # 不能包含连续的..
    if ('..' in local_part):
        return False
    ## 3.3、local_part必须包含题目要求的字符
    for char in local_part:
        is_letter = char.isalpha()
        is_digit = char.isdigit()
        is_symbol = char in ['-', '_', '.']
        if(not is_letter and not is_digit and not is_symbol):
            return False
    # 4. 对domain_part进行判定
    ## 4.1、题目要求domain_part需要一个.，但是不能有两个连续的
    if('.' not in domain_part or '..' in domain_part):
        return False
    ## 4.2、找到最后一个.并进行分割
    dot_split_suffix = domain_part.split('.')[-1]
    ## 4.3、后缀的长度不能低于2
    if(len(dot_split_suffix) < 2):
        return False
    ## 4.4、后缀必须是字母
    for char in dot_split_suffix:
        if(not char.isalpha()):
            return False
    return True

validate("hell.-w.rld@example.com")