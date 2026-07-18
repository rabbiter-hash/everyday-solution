# Exact Change

Given an integer amount in cents, return the number of distinct ways to make exact change using pennies (1 cent), nickels (5 cents), dimes (10 cents), and quarters (25 cents).

## 一、题解和思路

### 1.1、题解

用1美分、5美分、10美分和25美分进行找零，返回不同的方式。

### 1.2、思路

硬币面额固定且只有4种，可以用**嵌套循环**枚举所有可能的硬币数量。

## 二、Returns

1. `exact_change(3)` should return `1`.
2. `exact_change(9)` should return `2`.
3. `exact_change(17)` should return `6`.
4. `exact_change(39)` should return `24`.
5. `exact_change(61)` should return `73`.
6. `exact_change(99)` should return `213`.

## 三、Python Solution(s)

### 3.1、暴力枚举

```python
# -*- encoding: utf-8 -*- 
# @Time: 2026/7/11 11:28
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def exact_change(amount):
    # 统计初始化
    count = 0

    # 1. 枚举quarter（25美分）
    for q in range(amount // 25 + 1):
        remaining_after_q = amount - q * 25
        # 2. 枚举dimes （10美分）
        for d in range(remaining_after_q // 10 + 1):
            remaining_after_d = remaining_after_q - d * 10
            # 3. 枚举nickles （5美分）
            for n in range(remaining_after_d // 5 + 1):
                # 剩下的用cents（1美分）补齐
                count += 1

    print(count)
    return count

exact_change(5)
```

## 四、JavaScript Solution(s)

### 4.1、暴力枚举

```js

function exactChange(amount) {
    // 1. 初始化统计值
    let count = 0;

    // 2. 开始暴力枚举
    // 2.1、首先是quarter （25美分）
    for(let q = 0; q <= Math.floor(amount / 25 ); q++) {
        let remainingAfterQ = amount - q * 25;

        // 2.2、其次dimes
        for(let d = 0; d <= Math.floor(remainingAfterQ / 10); d++){
            let remainingAfterD = remainingAfterQ - d * 10;
            // nickel 可以从 0 到 remainingAfterD / 5
            // 剩下的全部用 pennies 补齐
            for (let n = 0; n <= Math.floor(remainingAfterD / 5); n++) {
                count++;
            }
        }
    }
    console.log(count);
    return count;
}

exactChange(9);
```

