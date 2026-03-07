# -*- encoding: utf-8 -*- 
# @Time: 2026/3/7 9:26
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

""" =====================================================
    *** 第一种解法：暴力遍历二维数组 + 四个方向判定
===================================================== """

def navigate_trail(map):
    # 1. 判定数据输入是否合法
    if not isinstance(map, list):
        raise TypeError('Map must be a list!')
    # 2. 把地图路径变成二维数组同时获取尺寸
    grid = [list(row) for row in map]
    rows = len(grid)
    cols = len(grid[0])
    print(grid)
    print(rows, cols, sep = " | ")
    # 3. 遍历二维数组，找到C的位置
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'C':
                start_r, start_c = r, c
                # print(start_r, start_c) # 0 1，第一行第二列；
    # 4. 定义相对C位置的四个方向
    directions = [
        (0, 1, "R"), # 右
        (1, 0, "D"), # 下
        (0, -1, "L"), # 左
        (-1, 0, "U"), # 上
    ]
    # 5. 准备当前移动的结果变量
    path = ""
    r, c = start_r, start_c

    # 6. 记录访问过的位置
    visited = set()
    visited.add((r, c))

    # 7. 开始循环，走路径
    while grid[r][c] != 'G':
        # 如果当前的位置不是G，就向当前位置的四个位置移动
        # 8. 检查四个方向
        for dr, dc, move in directions:
            # 它会走四个方向，直到遇到G
            nr = r + dr # 新行的坐标
            nc = c + dc # 新列的坐标

            # 9. 判定是否合法
            # 条件判定：1. 不能超出行列的边界；
            # 2. 当前坐标grid[nr][nc]必须是可移动的方向，也就是T和G
            # 3. 不能是访问过的坐标，也就是不能回退
            if(
                0 <= nr < rows and
                0 <= nc < cols and
                grid[nr][nc] in ("T", "G") and
                (nr, nc) not in visited
            ):
                # 10. 开始移动
                # 记录移动的位置
                path += move
                # 更新当前坐标和位置
                r, c = nr, nc
                # 添加到移动过的集合
                visited.add((r, c))
                break # break很重要，路径只有一条，找到就走
    # print(path)
    return path

# navigate_trail(["-CT--", "--T--", "--TT-", "---T-", "---G-"])

""" =====================================================
    *** 第一种解法：暴力遍历二维数组 + 不回到前一步
===================================================== """
def navigate_trail_not_prev(map):
    # 1. 判定数据格式是否合法
    if not isinstance(map, list):
        raise TypeError('Map must be a list!')

    # 2. 将map转成二维数组
    grid = [list(row) for row in map]
    rows = len(grid)
    cols = len(grid[0])
    print(grid, rows, cols, sep = "|")

    # 3. 找到C所在的位置，并初始化当前位置
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'C':
                r0, c0 = r, c
    # 4. 初始化位置
    r, c = r0, c0
    # 上一步初始化为None
    prev_step = None
    # 路径
    path = ""

    # 5.
    while grid[r][c] != "G":
        # 如果当前位置点不是G，就要比较相邻的四个点
        neighbors = [
            (r, c + 1, "R"), # 行不变，列+1，就是往右
            (r, c - 1, "L"), # 行不变，列-1，就是向左
            (r + 1, c, "D"), # 列不变，行+1，向下
            (r - 1, c, "U"), # 列不变，行+1，向上
        ]
        # 根据相邻的点确定新点
        for nr, nc, move_direction in neighbors:
            if(
                0 <= nr < rows and
                0 <= nc < cols and
                grid[nr][nc] in ("T", "G") and
                (nr, nc) != prev_step
            ):
                path += move_direction
                # 将前一步追加到prev
                prev_step = (r, c)
                # 更新当前点的坐标
                r, c = nr, nc
                break # beak是必须的，找到G就退出，跳出当前条件层的循环
    # print(path)
    return path
navigate_trail_not_prev(["-CT--", "--T--", "--TT-", "---T-", "---G-"])