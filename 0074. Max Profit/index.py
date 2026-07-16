# -*- encoding: utf-8 -*- 
# @Time: 2026/7/3 11:33
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def get_max_profit(prices, budget):
    # 1. 初始化最大利润
    max_profit = 0
    # 2. 初始化有多少填
    max_days = len(prices)

    # 3. 开始遍历
    for i in range(max_days - 1):
        # 买入价格要在最后一天之前的一天，这样才能计算
        for j in range(i + 1, max_days):
            # 卖出的价格一定要比买入晚
            # 买入价格
            buy_price = prices[i]
            sell_price = prices[j]

            # 判定买入价格
            if(sell_price > buy_price):
                # 只有当买入价格大于卖出价格的时候，才有利可图
                # 计算可买股数
                shares = budget // buy_price

                # 计算总利润
                profit = shares * (sell_price - buy_price)

                # 更新max_profit
                if(profit > max_profit):
                    max_profit = profit
    # 向下取整，并保留两位小数
    results = int(max_profit * 100) / 100
    return f"{results:.2f}"


get_max_profit([5, 6], 50)
get_max_profit([8, 2, 5, 10], 20)