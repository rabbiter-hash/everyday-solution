# Digital Detox

Given an array of your login logs, determine whether you have met your digital detox goal.

Each log is a string in the format `"YYYY-MM-DD HH:mm:ss"`.

You have met your digital detox goal if both of the following statements are true:

- You logged in no more than once within any four-hour period.
- You logged in no more than 2 times on any single day.

## 一、Python Solution(s)

### 1.1、Returns

- `digital_detox(["2026-02-01 08:00:00", "2026-02-01 12:30:00"])` should return `True`.
- `digital_detox(["2026-02-01 04:00:00", "2026-02-01 07:30:00"])` should return `False`.
- `digital_detox(["2026-01-31 08:21:30", "2026-01-31 14:30:00", "2026-02-01 08:00:00", "2026-02-01 12:30:00"])` should return `True`.
- `digital_detox(["2026-01-31 10:40:21", "2026-01-31 15:19:41", "2026-01-31 21:49:50", "2026-02-01 09:30:00"])` should return `False`.
- `digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 09:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"])` should return `True`.
- `digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 01:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"])` should return `False`.

### 1.2、思路

- 解析时间字符窜，将把 `"YYYY-MM-DD HH:mm:ss"` 转成 **时间对象 / 时间戳**.
  - 字符串不好算时间差
  - 时间戳可以直接相减
- 排序：时间从早到晚进行排序
- 事件检查。在一次遍历中，相邻两次登录是否 < 4小时；每的登录次数是否 > 2

### 1.3、解法

#### 1.3.1、相邻比较

```python
# -*- encoding: utf-8 -*- 
# @Time: 2026/2/2 8:44
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

from datetime import datetime, timedelta

def digital_detox(logs: list) -> bool:
    # 1. 判定是否数组
    if not isinstance(logs, list):
        raise TypeError('logs is not a list')

    # 2. 转换成时间对象
    times = [datetime.strptime(log, "%Y-%m-%d %H:%M:%S") for log in logs]
    print(id(times))
    # 排序时间对象
    times.sort()
    # print(times)
    print(id(times))

    # 3. 空字典，用于统计键值对
    day_count = {}
    four_hours = timedelta(hours=4) # 这里一定要输入hours=4，不然会是days=4

    # 4. 遍历时间对象数组
    for i, t in enumerate(times):
        # 对排序后的时间对象，比较两个相邻时间
        if(i > 0) and t - times[i-1] < four_hours:
            return False

        # 日期对象
        day = t.date()
        print(day)
        # 字典day_count初始是没有键值对的，所以应该使用get(day, 0)
        # +1的意思是，如果该day_count有了键后，就给它的值+1
        day_count[day] = day_count.get(day, 0) + 1
        if day_count[day] > 2:
            return False
    return True


digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 09:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"])

```



## 二、JavaScript Solution(s)

### 2.1、Returns

- `digitalDetox(["2026-02-01 08:00:00", "2026-02-01 12:30:00"])` should return `true`.
- `digitalDetox(["2026-02-01 04:00:00", "2026-02-01 07:30:00"])` should return `false`.
- `digitalDetox(["2026-01-31 08:21:30", "2026-01-31 14:30:00", "2026-02-01 08:00:00", "2026-02-01 12:30:00"])` should return `true`.
- `digitalDetox(["2026-01-31 10:40:21", "2026-01-31 15:19:41", "2026-01-31 21:49:50", "2026-02-01 09:30:00"])` should return `false`.
- `digitalDetox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 09:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"])` should return `true`.
- `digitalDetox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 01:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"])` should return `false`.

### 2.2、思路

1. map将字符串转成时间对象
2. 排序时间对象
3. 定义对象和条件
4. 遍历时间对象数组进行相邻判定

### 2.3、解法

#### 2.3.1、相邻比较

```javascript

function digitalDetox(logs){
    // 1. 判定数据输入类型
    if(!Array.isArray(logs)){
        throw new TypeError("输入的不是数组！");
    }

    // 2. 输入处理
    const times = logs
        .map( t => new Date(t))
        .sort((a, b) => a - b);
    console.log(times);

    const dayCounts = {}
    const FOUR_HOURS = 4 * 60 * 60 * 1000; // 毫秒级4天
    console.log(FOUR_HOURS);

    // 3. 循环遍历，注意边界
    for(let i = 0; i < times.length; i++){
        console.log(i + "=>>" + times[i]); // 确定循环边界
        if(i > 0 && times[i] - times[i-1] < FOUR_HOURS){
            return false;
        }

        // 统计次数
        const day = times[i].toLocaleDateString("en-US");
        // 也可以使用 但是toISOString() 是 UTC 时间，如果是中国时区，可能会导致错一天
        // 所以做日志统计的时候，最好以服务器时间的时区进行统计
        // const day = times[i].toISOString().slice(0, 10);
        console.log(day);
        console.log("查看：", dayCounts);
        // 给字典添加值
        dayCounts[day] = (dayCounts[day] || 0) + 1; // 初始的时候是没有值的，所以取0，然后通过循环进行加值

        if(dayCounts[day] > 2){
            return false;
        }
    }

    return true;
}

console.log(digitalDetox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 09:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"]))
```





