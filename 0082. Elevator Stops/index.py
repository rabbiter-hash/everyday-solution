# -*- encoding: utf-8 -*- 
# @Time: 2026/7/20 13:56
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def elevator_stops(current_floor, stops):

    # 1. 去重要停靠的楼层
    stops = list(set(stops))
    print(stops)

    # 2. 分离向上和向下的请求
    above = sorted([f for f in stops if f > current_floor])
    below = sorted([f for f in stops if f < current_floor], reverse=True)
    print(above, below)
    # 3. 如果没有上下请求
    if not above and not below:
        return []
    # 如果有向下没有向上
    if not above:
        return below
    # 如果有向上没有向下
    if not below:
        return above

    # 4. 找最近的向下和向上请求
    nearest_up = above[0] # 升序排列，所以是第一个
    nearest_down = below[0] # 降序排列，所以是第一个

    # 5. # 决定先上还是先下
    # 如果向下更近或距离相等，先下
    dist_up = nearest_up - current_floor
    dist_down = current_floor - nearest_down

    if dist_down <= dist_up:
        # 先向下
        return below + above
    else:
        return above + below
elevator_stops(5, [2, 8, 3, 9])
