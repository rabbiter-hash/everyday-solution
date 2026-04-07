# What Day Is It?

Given a Unix timestamp in milliseconds, return the day of the week.

Valid return days are:

- `"Sunday"`
- `"Monday"`
- `"Tuesday"`
- `"Wednesday"`
- `"Thursday"`
- `"Friday"`
- `"Saturday"`

Be sure to ignore time zones.

## 一、题解和思路

### 1.1、题解

给出一个milliseconds级的Unix时间戳，判定它是星期几。忽略时区。

### 1.2、思路

#### 1.2.1、使用封装的库

- Python是datetime
- Js是Date

### 1.2.2、原生解法

- 一天的时间为`24 * 60 * 60`秒，转成微秒为：`24 * 60 * 60 * 1000`

- 时间戳换算成天，微秒数timestamp / 一天的微秒数；可以得到整数天；

- 时间戳起始天数为`1970-01-01 星期四`；

- 所以当前天数应该偏离；如果映射星期四为第一天，那就不需要偏离；

- 建立映射：

  ```python
  days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  ```

- 直接返回

## 二、Returns

1. `get_day_of_week(1775492249000)` should return `"Monday"`.
2. `get_day_of_week(1766246400000)` should return `"Saturday"`.
3. `get_day_of_week(33791256000000)` should return `"Tuesday"`.
4. `get_day_of_week(1773576000000)` should return `"Sunday"`.
5. `get_day_of_week(0)` should return `"Thursday"`.

## 三、Python Solution(s)

### 3.1、解法一：常规解法、不用库

```bash
def get_day_of_week_normal(timestamp):
    # 时间戳（毫秒） -> 天数
    # 一天 = 86400 秒 = 86400 * 1000 毫秒
    days = timestamp // (86400 * 1000)

    print(days)  # 从 Unix 起点到现在的总天数

    # 1970-01-01 是星期四（在数组中 index = 4），需要做偏移
    days_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    # 对 7 取模，得到星期索引
    return days_list[(days + 4) % 7]


get_day_of_week_normal(1775492249000)
```

### 3.2、datetime库

思路：毫秒 -> 秒 -> utc时间 -> weekday

```python
def get_day_of_week(timestamp):
    from datetime import datetime
    # 1. 微妙转秒
    second = timestamp // 1000

    # 2. 转UTC时间，忽略时区
    dt = datetime.utcfromtimestamp(second)
    # print(dt) # 2026-04-06 16:17:29

    # 3. 映射日期
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[dt.weekday()]

print(get_day_of_week(1775492249000))
```

### 3.3、datetime简洁

```python
def get_day_of_week_strftime(timestamp):
    from datetime import datetime
    return datetime.utcfromtimestamp(timestamp // 1000).strftime("%A")

print(get_day_of_week_strftime(1775492249000))
```

## 四、JavaScript Solution(s)

### 4.1、常规解法

```js
function getDayOfWeek(timestamp) {
    // 1. 一天的毫秒数
    const ONE_DAY = 24 * 60 * 60 * 1000;

    // 2. 计算经过的天数，并向下取整
    const days = Math.floor(timestamp / ONE_DAY);

    // 3. 映射日期
    const daysLists = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

    return daysLists[(days + 1) % 7];

}
getDayOfWeek(1775492249000)
```

### 4.2、使用Date内置对象

```js
function getDayOfWeekDate(timestamp){
    // 1. 获取date，单位是毫秒
    const date = new Date(timestamp); // 得到的日期
    console.log(date.getUTCDay());
    const daysList = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

    // 2. 利用getUTCDay()获取
    return daysList[date.getUTCDay()];

}
getDayOfWeekDate(1775492249000)
```

