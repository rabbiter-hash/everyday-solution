# Birthday Countdown

Given today's date and a birthday, return the number of days until the person's next birthday.

- Today's date is given as a string in `"YYYY-MM-DD"` format, with leading zeros, for example: `"2026-07-16"`.
- The birthday is given as a string in `"M/D"` format, without leading zeros, for example: `"9/7"`.
- If today is their birthday, return the number of days until their next birthday (not `0`).
- Leap years should be accounted for.

## 一、题解和思路

### 1.1、题解

- 输入：
  - today： 今天的日期，格式为`YYYY-MM-DD`，例如：`"2026-07-18"`
  - `birthday`：生日，格式为`"M/D"`，例如：`7/18`，表示7月18日；
- 输出：
  - 距离`下一个生日`还有多少天
  - 如果`今天就是生日`，则返回距离`明年`生日的天数（不能返回0）
- 需要考虑`闰年`（2月29天的情况）

### 1.2、思路

1. 解析输入
   - 从`today`提取年、月、日
   - 从`birthday`提取月、日
2. 构造今年的生日日期
   - 用今年的年份 + 生日的月、日，构造一个日期对象
3. 比较日期
   - 如果今天的日期`早于`今年的生日，说明下一个生日就是今年的这个日期；
   - 如果今天的日期`晚于或者等于`今年的生日（包括今天正好是生日），则下一个生日就是明年的同一天；
4. 特殊情况：闰年2月29日
   - 如果生日是2月29日，而今年不是闰年，则今年的生日不存在，需要特殊处理：
     - 如果今年不是闰年，则今年没有2月29日，应该将生日顺延到3月1日（但通常题目中会要求按实际日期计算，所以我们要判断年份是否为闰年，如果不是，则这个生日在今年不存在，直接跳到明年）
     - 更稳妥的做法：直接用日期库（如Python中的datetime）处理，它会自动处理无效日期；
5. 计算天数差
   - 用下一个生日的日期减去今天的日期，得到相差的天数并返回

## 二、Returns

1. `days_until_birthday("2026-07-16", "9/7")` should return `53`.
2. `days_until_birthday("2026-07-16", "3/22")` should return `249`.
3. `days_until_birthday("2026-07-16", "7/16")` should return `365`.
4. `days_until_birthday("2024-02-28", "3/1")` should return `2`.
5. `days_until_birthday("2023-04-24", "12/30")` should return `250`.
6. `days_until_birthday("2024-03-01", "2/29")` should return `1460`.
7. `days_until_birthday("2096-03-01", "2/29")` should return `2920`.

## 三、Python Solution(s)

### 3.1、常规解法

```python
# -*- encoding: utf-8 -*- 
# @Time: 2026/7/18 11:31
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def days_until_birthday(today, birthday):
    from datetime import datetime, date, timedelta

    # 1. 解析今天
    today = datetime.strptime(today, "%Y-%m-%d").date()
    print(today)
    year = today.year

    # 2. 解析生日
    month, day = map(int, birthday.split("/"))
    print(month, day)

    # 3. 尝试构造今年的生日
    try:
        this_year_birthday = date(year, month, day)
    except ValueError:
        # 如果是 2/29 且今年不是闰年，则今年没有这个日期
        # 直接跳到下一年
        this_year_birthday = None

    if this_year_birthday:
        if this_year_birthday > today:
            next_birthday = this_year_birthday
        else:
            # 今天 >= 今年生日，找明年的
            try:
                next_birthday = date(year + 1, month, day)
            except ValueError:
                # 明年也不是闰年，继续往后找
                next_year = year + 1
                while True:
                    try:
                        next_birthday = date(next_year, month, day)
                        break
                    except ValueError:
                        next_year += 1
    else:
        # 今年没有这个生日（2/29 非闰年），直接找下一个闰年的 2/29
        next_year = year + 1
        while True:
            try:
                next_birthday = date(next_year, month, day)
                break
            except ValueError:
                next_year += 1

    # 计算天数差
    delta = next_birthday - today
    return delta.days


days_until_birthday("2026-07-16", "9/7")
```

## 四、JavaScript Solution(s)

### 3.2、常规解法

```js
function daysUntilBirthday(today, birthday) {
    // 1. 解析今天的日期 (YYYY-MM-DD)
    const todayParts = today.split('-').map(Number);
    const todayDate = new Date(todayParts[0], todayParts[1] - 1, todayParts[2]);
    const year = todayDate.getFullYear();

    // 2. 解析生日 (M/D)
    const birthdayParts = birthday.split('/').map(Number);
    const month = birthdayParts[0];
    const day = birthdayParts[1];

    // 3. 辅助函数：查找下一个有效日期（处理2/29等特殊情况）
    function findNextValidDate(startYear, targetMonth, targetDay) {
        let year = startYear;
        while (true) {
            const testDate = new Date(year, targetMonth - 1, targetDay);
            // 检查日期是否有效（月份和日期是否匹配）
            if (testDate.getMonth() === targetMonth - 1 &&
                testDate.getDate() === targetDay) {
                return testDate;
            }
            year++;
        }
    }

    // 4. 构造今年的生日
    let nextBirthday;
    const thisYearBirthday = new Date(year, month - 1, day);
    const isValidThisYear = (thisYearBirthday.getMonth() === month - 1 &&
                             thisYearBirthday.getDate() === day);

    if (isValidThisYear) {
        // 今年生日存在
        const todayMidnight = new Date(year, todayDate.getMonth(), todayDate.getDate());
        const birthdayMidnight = new Date(year, month - 1, day);

        if (birthdayMidnight > todayMidnight) {
            // 今年的生日还没到
            nextBirthday = birthdayMidnight;
        } else {
            // 今天就是生日或者生日已过，找明年的
            nextBirthday = findNextValidDate(year + 1, month, day);
        }
    } else {
        // 今年没有这个生日（比如2/29在非闰年）
        nextBirthday = findNextValidDate(year + 1, month, day);
    }

    // 5. 计算天数差（向上取整，确保得到完整天数）
    const diffTime = nextBirthday.getTime() - todayDate.getTime();
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

    return diffDays;
}
```