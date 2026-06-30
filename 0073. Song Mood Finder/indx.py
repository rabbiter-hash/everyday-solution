# -*- encoding: utf-8 -*- 
# @Time: 2026/6/30 11:37
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: indx.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def get_mood(genre, bpm):
    # 键是 genre，值是一个列表，包含 (BPM范围, mood) 的元组
    mood_map = {
        "classical": [
            (60, 109, "focus"),
            (110, 180, "happy")
        ],
        "electronic": [
            (60, 89, "focus"),
            (90, 134, "happy"),
            (135, 180, "hype")
        ],
        "pop": [
            (60, 180, "happy")
        ],
        "rock": [
            (60, 129, "happy"),
            (130, 180, "hype")
        ]
    }

    # 1. 首先判定genere是否在字典中
    if not genre in mood_map:
        return None

    # 2. 遍历genre的所有规则
    for low, high, mood in mood_map[genre]:
        # 判定bpm的范围
        if low <= bpm <= high:
            return mood

    return None


get_mood("rock", 111)