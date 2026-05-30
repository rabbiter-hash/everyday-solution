# -*- encoding: utf-8 -*- 
# @Time: 2026/5/29 11:38
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def fizz_buzz_count(start, end):
    def fizz_buzz_count(start, end):
        fcount = 0
        bcount = 0

        for i in range(start, end + 1):
            # 注意，一定是if分支，这样才能满足题目条件中的
            # Numbers divisible by both 3 and 5 count as both a fizz and a buzz.
            # 如果是if..elif，就会被分走
            if i % 3 == 0:
                fcount += 1

            if i % 5 == 0:
                bcount += 1

        return {"fizz": fcount, "buzz": bcount}

def fizz_buzz_count_pythonic(start, end):
    return {
        "fizz": sum(1 for i in range(start, end + 1) if i % 3 == 0),
        "buzz": sum(1 for i in range(start, end + 1) if i % 5 == 0)
    }
