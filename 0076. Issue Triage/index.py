# -*- encoding: utf-8 -*- 
# @Time: 2026/7/9 11:57
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def triage_issue(ms, message):
    # 1. 七天的毫秒数
    seven_days_millsecs = 7 * 24 * 60 * 60 * 1000

    # 2. 开始判断
    if ms < seven_days_millsecs:
        # 如果 ms 小于七天，无条件返回 leave it
        return "leave it"
    elif ms >= seven_days_millsecs and "bump" in message.lower():
        return "close it"
    else:
        return "bump it"



def triage_issue_if(ms, message):
    # 用单if实现
    # 1. 七天的毫秒数
    seven_days_millsecs = 7 * 24 * 60 * 60 * 1000

    # 2. 判定
    if ms < seven_days_millsecs:
        return "leave it"

    if ms >= seven_days_millsecs and "bump" in message.lower():
        return "close it"

    return "bump it"