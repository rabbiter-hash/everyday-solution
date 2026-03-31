# Wake-Up Alarm

Given a string representing the time you set your alarm and a string representing the time you actually woke up, determine if you woke up early, on time, or late.

- Both times will be given in `"HH:MM"` 24-hour format.

Return:

- `"early"` if you woke up before your alarm time.
- `"on time"` if you woke up at your alarm time, or within the 10 minute snooze window after the alarm time.
- `"late"` if you woke up more than 10 minutes after your alarm time.

Both times are on the same day.

## 一、题解和思路

### 1.1、题解

- 接收两个参数，一个是闹钟（alarm_time），另外一个是醒的时间（wake_time）
- 如果wake_time比alarm_time，早，就返回"early"
- 如果wake_time正好与alarm_time相等，或者在闹钟响了后打盹10分钟内，都应该返回"On time"
- 如果wake_time比alarm_time大于10分钟，就返回"late"

### 1.2、思路

在不用时间库的前提下，需要比较字符串：

- 分割字符串
  - 比较小时部分
  - 比较分钟部分
- 根据条件返回相应的字符串

## 二、Returns

- `alarm_check("07:00", "06:45")` should return `"early"`.
- `alarm_check("06:30", "06:30")` should return `"on time"`.
- `alarm_check("08:10", "08:15")` should return `"on time"`.
- `alarm_check("09:30", "09:45")` should return `"late"`.
- `alarm_check("08:15", "08:25")` should return `"on time"`.
- `alarm_check("05:45", "05:56")` should return `"late"`.
- `alarm_check("04:30", "04:00")` should return `"early"`.

## 三、Python Solution(s)

### 3.1、常规解法用if...else判定

```python
# -*- encoding: utf-8 -*- 
# @Time: 2026/3/31 17:31
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

""" =====================================================
    *** 第一种解法：常规解法
===================================================== """
def alarm_check(alarm_time, wake_time):
    # 1. 先拆分时间字符串
    alarm_time_hour = int(alarm_time.split(':')[0])
    alarm_time_minute = int(alarm_time.split(':')[1])

    wake_time_hour = int(wake_time.split(':')[0])
    wake_time_minute = int(wake_time.split(':')[1])

    # 2. 比较小时
    if wake_time_hour < alarm_time_hour:
        # 如果起床时间的小时小于闹钟时间的小时，那么一定是早起
        return "early"
    elif wake_time_hour == alarm_time_hour:
        # 同小时，比较分钟
        if wake_time_minute < alarm_time_minute:
            return "early"
        elif wake_time_minute <= alarm_time_minute + 10:
            # 闹钟偏后十分钟
            return "on time"
        else:
            return "late"
    else:
        # wake_time_hour > alarm_time_hour
        # 计算超过闹钟多少分钟
        minutes_late = (wake_time_hour - alarm_time_hour) * 60 + (wake_time_minute - alarm_time_minute)
        if minutes_late <= 10:
            return "on time"
        else:
            return "late"

```



## 四、JavaScript Solution(s)

### 4.1、常规解法

```js
/* ==========================================
    第一种解法：循环遍历
 ========================================== */
function alarmCheck(alarmTime, wakeTime) {
    // 提取小时和分钟
    let alarmHour = parseInt(alarmTime.slice(0, 2));
    let alarmMinute = parseInt(alarmTime.slice(3, 5));

    let wakeHour = parseInt(wakeTime.slice(0, 2));
    let wakeMinute = parseInt(wakeTime.slice(3, 5));

    // 先比较小时
    if (wakeHour < alarmHour) {
        return "early";
    } else if (wakeHour === alarmHour) {
        // 同小时，比较分钟
        if (wakeMinute < alarmMinute) {
            return "early";
        } else if (wakeMinute <= alarmMinute + 10) {
            return "on time";
        } else {
            return "late";
        }
    } else {
        // wakeHour > alarmHour
        let minutesLate = (wakeHour - alarmHour) * 60 + (wakeMinute - alarmMinute);
        if (minutesLate <= 10) {
            return "on time";
        } else {
            return "late";
        }
    }
}
```

