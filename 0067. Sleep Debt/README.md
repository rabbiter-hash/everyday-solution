# Sleep Debt

Given an array of hours slept each night leading up to today, and a target number of hours per night, return how many hours of sleep you need tonight to eliminate your sleep debt.

- Include tonight's hours in the total time needed to catch up.
- If you've slept enough to cover tonight's target or more, return `0`.

## 一、题解和思路

### 1.1、题解

输入一个数组，表示过去几天每晚的睡眠小时数，以及一个目标每晚睡眠小时数。

需要计算出：**为了还清之前的睡眠债务，今晚需要睡多少小时**

计算时，**今晚的睡眠小时数要算在还债的总时间中**。

如果过去的睡眠已经足够覆盖今晚的目标甚至更多，那么就返回 0。

### 1.2、思路

1. 计算`total_needed = target x (days_past + 1)`
2. 计算`past_total = sum(hours_slept)`
3. 如果`past_total >= total_needed` -> 返回0；
4. 否则返回`total_needed - past_total`；

## 二、Returns

1. `sleep_debt([6, 6, 6, 6, 6, 6], 8)` should return `20`.
2. `sleep_debt([6, 7, 8, 4, 8, 6], 7)` should return `10`.
3. `sleep_debt([10, 10, 9, 10, 9, 11], 9)` should return `4`.
4. `sleep_debt([8, 7, 6, 7, 6, 8], 6)` should return `0`.
5. `sleep_debt([8, 9, 10, 9, 10, 7], 7)` should return `0`.

## 三、Python Solution(s)

### 3.1、常规解法

```python
def sleep_debt(hours_slept, target_hours):
    # 1. 变量设定
    # 1.1、过去几天的睡觉小数总和
    past_total = sum(hours_slept)
    # 1.2、过去几天的天数
    n = len(hours_slept)
    # 1.3、总共需要睡觉的小时数，包含今天
    need_total = target_hours * (n + 1)

    # 2. 判定
    # 如果过去睡觉的总数已经超过需要的小时数，按照题目意思返回0
    if past_total >= need_total:
        return 0

    return need_total - past_total

print(sleep_debt([6, 6, 6, 6, 6, 6], 8))
```

## 四、JavaScript Solution(s)

### 4.1、常规解法

```js

function sleptDebt(hoursSlept, targetHours){
    // 1. 变量设定
    // 1.1、过去几天睡觉总和
    const pastTotal = hoursSlept.reduce((acc, cur) => acc + cur, 0);
    console.log(pastTotal);
    // 1.2、过去几天的天数
    const n = hoursSlept.length;
    // 1.3、根据targetHours计算需要睡觉的总小时数，包含今天
    const needTotal = targetHours * (n + 1);

    // 2. 开始判定
    if(pastTotal >= needTotal) {
        return 0;
    }

    return needTotal - pastTotal;
}

console.log(sleptDebt([6, 6, 6, 6, 6, 6], 8));
```

