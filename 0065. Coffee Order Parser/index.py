# -*- encoding: utf-8 -*- 
# @Time: 2026/5/16 11:05
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def format_coffee_order(order):
    # 1. 先将输入转成小写
    order = order.lower()

    # 2. 将菜品和价格做成结构化数据（dict）
    mapping = {
        "cold brew": 4.50,
        "oat latte": 5.00,
        "cappuccino": 4.75,
        "espresso": 3.00,
        "vanilla syrup": 0.75,
        "caramel drizzle": 0.60,
        "extra shot": 0.50,
        "oat milk": 0.75,
        "cream": 0.75,
    }

    # 3. 初始化存储
    items = []
    total = 0

    # 4. 循环遍历
    for item, price in mapping.items():
        if item in order:
            items.append(item)
            total += price
    print(items)
    print(f"{total:.2f}")

    return " + ".join(items) + ": " + "$" + f"{total:.2f}"


format_coffee_order("I'd like an oat latte with vanilla syrup and an extra shot please.")

format_coffee_order("Just an espresso please.")

format_coffee_order("I'll take an oat latte with cream and an extra shot, and some vanilla syrup and caramel drizzle.")


