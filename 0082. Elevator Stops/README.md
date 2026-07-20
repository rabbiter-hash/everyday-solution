# Elevator Stops

Given a number for the current floor of an elevator and an array of requested floors, return an array of the order the elevator should visit them to minimize number of floors traveled.

- If tied, go up first
- Floors with a request must be visited when the elevator first passes them

## 一、题解和思路

### 1.1、题解

给出电梯所在的楼层跟要停靠的楼层，返回楼梯停靠的顺序。

- 从当前楼层开始，先向最近的方向走；如果上下距离相等，先上；
- 沿该方向继续走，经过的所有请求楼层都要停；直到该方向没有更多请求；
- 再转向；

**"If tied, go up first"** 的意思是：

- 当向上和向下的**最近请求距离相等**时，优先向上

### 1.2、思路

- 去重所有请求楼层，得到一个集合；
- 以当前楼层为基准，分离上下请求楼层为数组并进行排序
  - 向上，升序排列；
  - 向下，降序排列；
- 用上下组中的第一个元素与当前楼层进行比较；
  - 如果求出的向下的数小于或者等于向上的数，那么优先向下；
  - 否则向上；

## 二、Returns

1. `elevator_stops(5, [2, 8, 3, 9])` should return `[3, 2, 8, 9]`.
2. `elevator_stops(6, [2, 10, 8, 3, 1, 9])` should return `[8, 9, 10, 3, 2, 1]`.
3. `elevator_stops(1, [4, 8, 3, 6, 9])` should return `[3, 4, 6, 8, 9]`.
4. `elevator_stops(12, [6, 10, 7, 3, 1, 4])` should return `[10, 7, 6, 4, 3, 1]`.
5. `elevator_stops(11, [2, 8, 23, 5, 12, 10, 6, 9, 19])` should return `[10, 9, 8, 6, 5, 2, 12, 19, 23]`.

## 三、Python Solution(s)

### 3.1、常规解法

```python
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

```

## 四、JavaScript Solution(s)

### 4.1、常规解法

```js
function elevatorStops(currentFloor, stops) {
    // 1. 去重所有要停靠的楼层
    const allStops = new Set(stops);
    console.log(allStops);

    // 2. 分离向上和向下请求
    const above = stops
        .filter(f => f > currentFloor)
        .sort((a, b) => a - b);
    console.log(above);
    const below = stops
        .filter(f => f < currentFloor)
        .sort((a, b) => b - a);
    console.log(below);

    // 3. 如果不存在上下请求
    if(above.length === 0 && below.length === 0) return null;
    if(above.length === 0) return below;
    if(below.length === 0) return above;

    // 4. 找出最近的向下和向上的请求以供比较
    const nearestUp = above[0]; // 升序排列，直接取第一个
    const nearestDown = below[0]; // 降序排列，直接取第一个
    // 5. 决定先下还是先上
    const distUp = nearestUp - currentFloor;
    const distDown = currentFloor - nearestDown;
    // 如果向下的距离小于或者等于向上的距离，优先向下
    if(distDown <= distUp) {
        return [...below, ...above];
    }
    return [...above, ...below];
}

elevatorStops(5, [2, 8, 3, 9]);
elevatorStops(6, [2, 10, 8, 3, 1, 9]);
elevatorStops(1, [4, 8, 3, 6, 9]);
elevatorStops(12, [6, 10, 7, 3, 1, 4]);
```