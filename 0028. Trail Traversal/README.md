# Trail Traversal

Given an array of strings representing your trail map, return a string of the moves needed to get to your goal.

The given strings will contain the values:

- `"C"`: Your current location
- `"G"`: Your goal
- `"T"`: Traversable parts of the trail
- `"-"`: Untraversable parts of the map

Return a string with the moves needed to follow the trail from your location to your goal where:

- `"R"` is a move right
- `"D"` is a move down
- `"L"` is a move left
- `"U"` is a move up
- There will always be a single continuous trail, without any branching, from your current location to your goal.
- Each trail location will have a maximum of two traversable locations touching it.

For example, given:

```js
[
  "-CT--",
  "--T--",
  "--TT-",
  "---T-",
  "---G-"
]
```

Return `"RDDRDD"`.

## 一、题解和思路

### 1.1、题解

给定一个数组，数组中的每个item都是路劲字符串。

- 要从C（current）走到G（goal）
- C的位置不确定，要遍历所有可能出现C的位置
- 确定C后，根据T走到G
- 返回约定字符窜

### 1.2、思路

- 找到C的位置，c在(row, col)

- 每一步检查四个方向：

  ```tex
  右(r, c + 1)
  下(r + 1, c)
  左(r, c - 1)
  上(r - 1, c)
  ```

  如果是T或者G，就走过去

- 记录方向，右（R），下（D），左（L），上（U）
- 防止回头，走过的点要标记visited，不然会来回走，用set
- 不是迷宫，迷宫通常要回溯，这里只有一条路径。所以算法上只能一直走，走到下一个T直到G结束。

## 二、Returns

1. `navigateTrail(["-CT--", "--T--", "--TT-", "---T-", "---G-"])` should return `"RDDRDD"`.
2. `navigateTrail(["-----", "--TTG", "--T--", "--T--", "CTT--"])` should return `"RRUUURR"`.
3. `navigateTrail(["-C----", "TT----", "T-----", "TTTTT-", "----G-"])` should return `"DLDDRRRRD"`.
4. `navigateTrail(["--------", "-CTTT---", "----T---", "---GT---", "--------"])` should return `"RRRDDL"`.
5.  `navigateTrail(["TTTTTTT-", "T-----T-", "T-----T-", "TTTT--TG", "---C----"])` should return `"ULLLUUURRRRRRDDDR"`.

## 三、Python Solution(s)

### 3.1、解法一，二维数组 + 方向判定

#### 3.1.1、思路

- 找到起点C，遍历二维数组，得到C的坐标

- 循环走路径，只有一条路径，没有分叉，所以逻辑就是：

  ```tex
  while 当前不是G：
  	查看四个方向
  ```

  检查左右上下四个方向，如果是T或G就走过去

- 记录当前步数的方向RDLU；

- 防止回头，因为每个点最多连接两个点，所以必须避免走回刚刚来的位置。最常见就是用set

#### 3.1.2、图解

```tex
1 找到 C

2 while 没到 G

3 检查四个方向
    右
    下
    左
    上

4 如果是 T 或 G 且没访问过
    移动
    记录方向

5 重复
```

#### 3.1.3、栈

- 二维数组遍历
- 坐标移动
- 方向判定
- 防止回头

#### 3.1.4、代码

```python
# -*- encoding: utf-8 -*- 
# @Time: 2026/3/7 9:26
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

""" =====================================================
    *** 第一种解法：暴力遍历
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

navigate_trail(["-CT--", "--T--", "--TT-", "---T-", "---G-"])
```

### 3.2、解法二，二维数组 + 上一步判定

#### 3.2.1、思路

记录“上一步的位置”，因为：

当前点只有两个邻居：一个是刚刚来的位置，一个是下一步，所以，只要**不走回上一步**就一定是正确的方向。

#### 3.2.2、步骤

- 找到C

  ```python
  for r in range(len(map)):
      for c in range(len(map[0])):
          if map[r][c] == "C":
              # 初始化c的位置
              r0, c0 = r, c
  ```

- 记录当前位置和上一步位置

  ```python
  r, c = r0, c0
  prev_step = None
  path = ""
  ```

- 不间断找下一个位置

  ```python
  # 检查四个方向
  neighbors = [
      (r, c + 1, "R"),
      (r + 1, c, "D"),
      (r, c - , "L"),
      (r - , c, "U")
  ]
  ```

  然后找是T或者G不是prev的点。

#### 3.2.3、代码

```python
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
                break # beak是必须的，找到G就退出
    # print(path)
    return path
navigate_trail_not_prev(["-CT--", "--T--", "--TT-", "---T-", "---G-"])
```



## 四、Javascript Solution(s)

```js

function navigateTrail(map){
    // 1. 判定是否是数组
    if(!Array.isArray(map)){
        throw new Error("输入必须是数组！");
    }

    // 2. 转成二维数组
    const grid = map.map(item => item.split(""));
    console.log(grid);
    // rows
    const rows = grid.length;
    const cols = grid[0].length;

    let r0, c0;
    // 3. 找到c的位置
    for(let r=0; r < rows; r++){
        for(let c = 0; c < cols; c++){
            if(grid[r][c] === "C"){
                r0 = r;
                c0 = c;
            }
        }
    }
    let r = r0;
    let c = c0;

    let prevStep = null;
    let path = "";

    // 4. 开始循环
    while(grid[r][c] !== "G"){

        // 相邻坐标
        const neighbors = [
            [r, c + 1, "R"],
            [r + 1, c, "D"],
            [r, c - 1, "L"],
            [r - 1, c, "U"]
        ];

        // 循环
        for (let [nr, nc, moveDirection] of neighbors){
            if(
                nr >= 0 &&
                nr < rows &&
                nc >= 0 &&
                nc < cols &&
                ["T", "G"].includes(grid[nr][nc]) &&
                (prevStep === null || !(nr === prevStep[0] && nc === prevStep[1]))
            ) {
                path += moveDirection;
                // 更新前一步的数值
                prevStep = [r, c];
                // 更新当前坐标
                r = nr;
                c = nc;
                break; // 必须满足条件才退出循环
            }
        }
    }
    return path;
}

console.log(navigateTrail(["-CT--", "--T--", "--TT-", "---T-", "---G-"]))
```

