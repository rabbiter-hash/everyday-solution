# Earth Day Cleanup Crew

Today is Earth Day. Given an array of items you cleaned up, return your total cleanup score based on the rules below.

Given items will be one of:

|      Item       | Base Value |
| :-------------: | :--------: |
|   `"bottle"`    |     10     |
|     `"can"`     |     6      |
|     `"bag"`     |     8      |
|    `"tire"`     |     35     |
|    `"straw"`    |     4      |
|  `"cardboard"`  |     3      |
|  `"newspaper"`  |     3      |
|    `"shoe"`     |     12     |
| `"electronics"` |     25     |
|   `"battery"`   |     18     |
|  `"mattress"`   |     38     |

A Rare item is represented as `["rare", value]`. For example, `["rare", 80]`. Rare items do not get a streak bonus.

- Streak bonus: If the same item appears consecutively, it gets increasing bonus points.
  - First consecutive occurrence: base value
  - Second: base value + 1
  - Third: base value + 2
  - etc.
- Fifth Item Multiplier: Every fifth item collected gets a multiplier.
  - Fifth item: *2
  - Tenth item: *3
  - etc.
- Apply the multiplier after calculating any bonuses.

## 一、题解和思路

### 1.1、题解

清理相应的物体得相应的分值，rare另算，其中数值就是分数；第二个规则是如果同一个物体出现第二次，分值+1，出现第三次，分值+2；第五个item（物体）的分值乘以2，第十个物体乘以3：

- 判断基础分
- 判断是否 streak（连续相同） → 加 bonus
- 判断是不是 rare（rare 不参与 streak）
- 判断是不是第5 / 10 / 15个 → 乘倍率
- 累加总分

| index | item   | streak | 分数计算 | multiplier | 最终 |
| ----- | ------ | ------ | -------- | ---------- | ---- |
| 1     | bottle | 0      | 10       | ×1         | 10   |
| 2     | bottle | 1      | 10+1     | ×1         | 11   |
| 3     | bottle | 2      | 10+2     | ×1         | 12   |
| 4     | can    | 0      | 6        | ×1         | 6    |
| 5     | can    | 1      | 6+1=7    | ×2         | 14   |

### 1.2、思路

1. 判断是不是rare，特殊处理：

   - 分数是 value
   - 不参与streak
   - 会打断streak

2. 如果是普通item，查基础分

3. 计算streak bouns

   - 如果当前item == 上一个item， streak += 1
   - 否则streak = 0

4. 判断 multiplier

   ```tex
   如果 index % 5 == 0
       multiplier = index / 5 + 1
   否则
       multiplier = 1
   ```

5. 最后累加：total += (base + streak) × multiplier

## 二、Returns

## 三、Python Solution(s)

### 3.1、常规解法

```python
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
```

## 四、JavaScript Solution(s)

### 4.1、常规解法

```js
function getCleanupScore(items) {
    // 1. 分值表
    const values = {
        bottle: 10,
        can: 6,
        bag: 8,
        tire: 35,
        straw: 4,
        cardboard: 3,
        newspaper: 3,
        shoe: 12,
        electronics: 25,
        battery: 18,
        mattress: 38
    };

    // 2. 初始化
    let total = 0;
    let prevItem = null;
    let streak = 0;

    // 3. 遍历
    for(let i = 0; i < items.length; i++){
        let item = items[i];
        let score;
        // console.log(item);

        // =====================
        // Step 1：判断 rare
        // =====================
        if (Array.isArray(item) && item[0] === "rare") {
            score = item[1];

            // 打断 streak
            prevItem = null;
            streak = 0;
        } else {
            // =====================
            // Step 2：基础分
            // =====================
            let base = values[item];

            // =====================
            // Step 3：streak
            // =====================
            if (item === prevItem) {
                streak++;
            } else {
                streak = 0;
            }

            score = base + streak;

            prevItem = item;
        }
        // =====================
        // Step 4：multiplier
        // =====================
        let index = i + 1; // 转成从1开始

        let multiplier = 1;
        if (index % 5 === 0) {
            multiplier = Math.floor(index / 5) + 1;
        }

        // =====================
        // Step 5：累加
        // =====================
        total += score * multiplier;
    }
    return total;
}

getCleanupScore(["bottle", "straw", "shoe", "battery"])
```

