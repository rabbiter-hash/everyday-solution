# Zodiac Finder

Given a date string in the format `"YYYY-MM-DD"`, return the zodiac sign for that date using the following chart:

|        Date Range         |   Zodiac Sign   |
| :-----------------------: | :-------------: |
|    March 21 - April 19    |    `"Aries"`    |
|     April 20 - May 20     |   `"Taurus"`    |
|     May 21 - June 20      |   `"Gemini"`    |
|     June 21 - July 22     |   `"Cancer"`    |
|    July 23 - August 22    |     `"Leo"`     |
| August 23 - September 22  |    `"Virgo"`    |
| September 23 - October 22 |    `"Libra"`    |
| October 23 - November 21  |   `"Scorpio"`   |
| November 22 - December 21 | `"Sagittarius"` |
| December 22 - January 19  |  `"Capricorn"`  |
| January 20 - February 18  |  `"Aquarius"`   |
|  February 19 - March 20   |   `"Pisces"`    |

- Zodiac signs are based only on the month and day, you can ignore the year.

## 一、Returns

- `get_sign("2026-01-31")` should return `"Aquarius"`.
- `get_sign("2001-06-10")` should return `"Gemini"`.
- `get_sign("1985-09-07")` should return `"Virgo"`.
- `get_sign("2023-03-19")` should return `"Pisces"`.
- `get_sign("2045-11-05")` should return `"Scorpio"`.
- `get_sign("1985-12-06")` should return `"Sagittarius"`.
- `get_sign("2025-12-30")` should return `"Capricorn"`.
- `get_sign("2018-10-08")` should return `"Libra"`.
- `get_sign("1958-05-04")` should return `"Taurus"`.

## 二、解法和思路

### 2.1、问题本质

1. 不关心年份，只关心月和日
2. 闰年也完全不重要，所以可以忽略闰年判定

### 2.2、思路

确定和多区间，通过判定区间，直接return相应的`zodiac`。

### 2.3、疑问

`December 22 - January 19`这是一个跨年区间，不能单纯的用`12.22 <= start and end <= 1.19`处理。

## 三、Python Solution(s)

### 3.1、把日期映射成一个可比较的整数——线性解法

比如：

```python
md = month * 100 + day
# 那么
# 3月21日 -> 321
# 12月25日 -> 1225
# 1月10日 -> 110
```

这样可以不用`datetime`，不怕跨年（用or判断）

代码：

```python
# -*- encoding: utf-8 -*- 
# @Time: 2026/2/3 14:52
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def get_sign(date_str: str) -> str:
    # 1. 处理输入的字符串
    _, month, day = map(int, date_str.split('-'))

    # 2. 通过月份和日期转成month_day，方便线性比较
    month_day = month * 100 + day

    # "Aries" Mar 21 - Apr 19
    if 321 <= month_day <= 419:
        return "Aries"
    # "Taurus" April 20 - May 20
    elif 420 <= month_day <= 520:
        return "Taurus"
    # "Gemini" May 21 - June 20
    elif 521 <= month_day <= 620:
        return "Gemini"
    # "Cancer" June 21 - July 22
    elif 621 <= month_day <= 722:
        return "Cancer"
    # "Leo" July 23 - August 22
    elif 723 <= month_day <= 822:
        return "Leo"
    # "Virgo" August 23 - September 22
    elif 823 <= month_day <= 922:
        return "Virgo"
    # "Libra" September 23 - October 22
    elif 923 <= month_day <= 1022:
        return "Libra"
    # "Scorpio" October 23 - November 21
    elif 1023 <= month_day <= 1121:
        return "Scorpio"
    # "Sagittarius"November 22 - December 21
    elif 1122 <= month_day <= 1221:
        return "Sagittarius"
    # "Capricorn" December 22 - January 19
    elif month_day >= 1222 or month_day <= 119:
        return "Capricorn"
    # "Aquarius"January 20 - February 18
    elif 120 <= month_day <= 218:
        return "Aquarius"
    else:
        return "Pisces"


print(get_sign("2026-01-31"))

```

### 3.2、映射——区间映射表

```python
def get_sign_map(date_str: str) -> str:
    _, month, day = map(int, date_str.split("-"))
    month_day = month * 100 + day

    # 因为Capricorn跨年，所以分成两段：1. Dec 22 - Dec 31，也就是1222 - 1231
    # 2. 第二段为：Jan 1 - Jan 19，也就是101 - 119
    ranges = [
        ((321, 419), "Aries"),
        ((420, 520), "Taurus"),
        ((521, 620), "Gemini"),
        ((621, 722), "Cancer"),
        ((723, 822), "Leo"),
        ((823, 922), "Virgo"),
        ((923, 1022), "Libra"),
        ((1023, 1121), "Scorpio"),
        ((1122, 1221), "Sagittarius"),
        ((1222, 1231), "Capricorn"),
        ((101, 119), "Capricorn"),
        ((120, 218), "Aquarius"),
        ((219, 320), "Pisces"),
    ]

    for start, end, zodiac in ranges:
        if start <= month_day <= end:
            return zodiac
```

此处跨年的区间，要做两个映射。

### 3.3、元组比较

```python
def get_sign_tuple(date_str: str) -> str:
    _, month, day = map(int, date_str.split("-"))
    month_day = (month, day)

    if (3, 21) <= month_day <= (4, 19):
        return "Aries"
    elif (4, 20) <= month_day <= (5, 20):
        return "Taurus"
    elif (5, 21) <= month_day <= (6, 20):
        return "Gemini"
    elif (6, 21) <= month_day <= (7, 22):
        return "Cancer"
    elif (7, 23) <= month_day <= (8, 22):
        return "Leo"
    elif (8, 23) <= month_day <= (9, 22):
        return "Virgo"
    elif (9, 23) <= month_day <= (10, 22):
        return "Libra"
    elif (10, 23) <= month_day <= (11, 21):
        return "Scorpio"
    elif (11, 22) <= month_day <= (12, 21):
        return "Sagittarius"
    elif month_day >= (12, 22) or month_day <= (1, 19):
        return "Capricorn"
    elif (1, 20) <= month_day <= (2, 18):
        return "Aquarius"
    else:
        return "Pisces"
```

## 四、JavaScript Solution(s)

```js
function zodiacFinder(date) {
  const [, monthStr, dayStr] = date.split("-");
  const month = Number(monthStr);
  const day = Number(dayStr);

  if ((month === 3 && day >= 21) || (month === 4 && day <= 19)) return "Aries";
  if ((month === 4 && day >= 20) || (month === 5 && day <= 20)) return "Taurus";
  if ((month === 5 && day >= 21) || (month === 6 && day <= 20)) return "Gemini";
  if ((month === 6 && day >= 21) || (month === 7 && day <= 22)) return "Cancer";
  if ((month === 7 && day >= 23) || (month === 8 && day <= 22)) return "Leo";
  if ((month === 8 && day >= 23) || (month === 9 && day <= 22)) return "Virgo";
  if ((month === 9 && day >= 23) || (month === 10 && day <= 22)) return "Libra";
  if ((month === 10 && day >= 23) || (month === 11 && day <= 21)) return "Scorpio";
  if ((month === 11 && day >= 22) || (month === 12 && day <= 21)) return "Sagittarius";
  if ((month === 12 && day >= 22) || (month === 1 && day <= 19)) return "Capricorn";
  if ((month === 1 && day >= 20) || (month === 2 && day <= 18)) return "Aquarius";
  return "Pisces"; // 剩下的就是 2/19 - 3/20
}

```

