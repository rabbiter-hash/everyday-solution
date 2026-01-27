# Odd or Even Day

Given a timestamp (number of milliseconds since the Unix epoch), return:

- `"odd"` if the day of the month for that timestamp is odd.
- `"even"` if the day of the month for that timestamp is even.

For example, given `1769472000000`, a timestamp for January 27th, 2026, return `"odd"` because the day number (`27`) is an odd number.

## 概述：

`Timestamp`分为`秒级（10位）`、`毫秒级（13位）`、`微秒级（16位）`、`纳秒级（17位+）`，题目要求毫秒级计算。

python函数`datetime.datetime.fromtimestamp(ts, datetime.UTC)`，以前可以用`datetime.datetime.utcfromtimestamp(ts)`

- fromtimestamp：使用本地时区
- utcfromtimestamp：使用UTC，即将弃用，改为fromtimestamp(ts, datetime.UTC)

## 一、Python Solution(s)

### 1.1、常规解法

```python
import datetime
def odd_or_even_day(timestamp: int) -> str:
    """
    说明：输入毫秒级的时间戳，计算UTC时区的日期的日是奇数还是偶数
    :param timestamp: 毫秒级
    :return: str
    """
    dt = datetime.datetime.fromtimestamp(timestamp / 1000, datetime.UTC)
    # 本来可以使用utffromtimestamp(timestamp/1000)，但是即将弃用
    day = dt.day
    return "even" if day % 2 == 0 else "odd"


print(odd_or_even_day(6739456780000))
```



## 二、JavaScript Solutuon(s)

### 2.1、常规解法

```js
function oddOrEvenDay(timestamp){
    // 1. 获取当前时间戳的具体日期
    const dt = new Date(timestamp);
    console.log(dt);
    // 2. 获取日
    const currentTimeStampDay = dt.getUTCDate(); // 注意是UTCDate，不是UTCDay
    console.log(currentTimeStampDay);
    
    // 3. 返回
    return (currentTimeStampDay % 2 === 0) ? "odd" : "even";
}
```

