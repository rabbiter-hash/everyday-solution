# -*- encoding: utf-8 -*- 
# @Time: 2026/4/3 14:38
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)


def get_browser_history(commands):
    # 1. 初始化历史记录列表
    history = []

    # 2. 当前索引
    current_index = -1

    # 3. 循环
    for command in commands:
        # 判定是否为Back
        if command == "Back":
            if current_index > 0:
                current_index -= 1
        elif command == "Forward":
            if current_index < len(history) - 1:
                current_index += 1
        else:
            # 是URL
            history = history[:current_index + 1]
            # 追加到列表
            history.append(command)
            # 更新索引
            current_index += 1
    print([history, current_index])

get_browser_history(["a.com", "b.com", "Back", "Forward"])