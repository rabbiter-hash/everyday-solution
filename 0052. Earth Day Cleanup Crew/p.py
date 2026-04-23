# -*- encoding: utf-8 -*- 
# @Time: 2026/4/23 16:09
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def get_cleanup_score(items):
    # 1. 分值表，映射表
    values = {
        "bottle": 10,
        "can": 6,
        "bag": 8,
        "tire": 35,
        "straw": 4,
        "cardboard": 3,
        "newspaper": 3,
        "shoe": 12,
        "electronics": 25,
        "battery": 18,
        "mattress": 38
    }

    # 2. 初始化总和、上一个item已经streak
    total = 0  # 总分
    prev_item = None  # 上一个 item
    streak = 0  # 连续次数（注意：从0开始）

    # 3. 遍历（index 从1开始很关键）
    for i, item in enumerate(items, start=1):
        # =====================
        # Step 1：判断是否 rare
        # =====================
        if isinstance(item, list) and item[0] == "rare":
            score = item[1]

            # rare 打断streak
            prev_item = None
            streak = 0

        else:
            # =====================
            # Step 2：基础分
            # =====================
            base = values[item]

            # =====================
            # Step 3：streak 处理
            # =====================
            if item == prev_item:
                streak += 1
            else:
                streak = 0
            score = base + streak

            # 更新prev
            prev_item = item

        # =====================
        # Step 4：multiplier
        # =====================
        if i % 5 == 0:
            multiplier = i // 5 + 1
        else:
            multiplier = 1

        # =====================
        # Step 5：累加
        # =====================
        total += score * multiplier
    return total

get_cleanup_score(["bottle", "straw", "shoe", "battery"])

