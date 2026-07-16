# Nearest Multiple

Given two integers, round the first to the nearest multiple of the second.

## 一、题解和思路

### 1.1、题解

找到第二个参数的某个倍数，使得这个倍数最接近第一个数。

### 1.2、思路

反向思路，用第一个参数`a`去除以第二个参数`b`，会得到商`quotient`；

看余数`remainder`

比较余数(remainder)与`b/2`的大小：

- 如果余数 < b/2，要向下取整（取较小的倍数）
- 如果余数 > b/2，要向上取整（取较大的倍数）

## 二、Returns

- `round_to_nearest_multiple(5, 3)` should return `6`.
- `round_to_nearest_multiple(17, 4)` should return `16`.
- `round_to_nearest_multiple(43, 5)` should return `45`.
- `round_to_nearest_multiple(38, 11)` should return `33`.
- `round_to_nearest_multiple(93, 12)` should return `96`.

## 三、Python Solution(s)

### 3.1、常规余数法

```python
# -*- encoding: utf-8 -*- 
# @Time: 2026/7/8 11:56
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def round_to_nearest_multiple(num, multiple):
    # 1. 先取出商
    quotient = num // multiple
    # 2. 余数
    remainder = num % multiple

    # 3. 比较
    if remainder < multiple / 2:
        return quotient * multiple
    else:
        return (quotient + 1) * multiple


round_to_nearest_multiple(5, 3)
```

## 四、JavaScript Solution(s)

### 4.1、常规余数法

```js
function roundToNearestMultiple(num, multiple) {
    // 1. 先算商
    const quotient = Math.floor( num / multiple );
    // 2. 余数
    const remainder = num % multiple;

    // 3. 比较
    if(remainder < multiple / 2){
        return quotient * multiple;
    } else {
        return (quotient + 1 ) * multiple;
    }
}
```

