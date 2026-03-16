# Parking Fee Calculator

Given two strings representing the time you parked your car and the time you picked it up, calculate the parking fee.

- The given strings will be in the format `"HH:MM"` using a 24-hour clock. So `"14:00"` is 2pm for example.
- The first string will be the time you parked your car, and the second will be the time you picked it up.
- If the pickup time is earlier than the entry time, it means the parking spanned past midnight into the next day.

Fee rules:

- Each hour parked costs $3.
- Partial hours are rounded up to the next full hour.
- If the parking spans overnight (past midnight), an additional $10 overnight fee is applied.
- There is a minimum fee of $5 (only used if the total would be less than $5).

Return the total cost in the format `"$cost"`, `"$5"` for example.

## 一、题解和思路

### 1.1、题解

- 通过车辆入场时间和出场时间计算停车费
- 如果出场时间比入场时间更早，说明这个车有过夜；
- 每小时3美元
- 不到一小时的，按一小时算
- 如果是过夜车辆，除了按正常的计费，还要额外+10美元
- 有最小收费为5美元，比如只停半小时，按一小时算，那么就是5美元、

### 1.2、思路

1. 比较入场时间和出厂时间，分两种情况：
   - 入场时间小于出场时间，按题目计费
   - 入场时间大于出场时间，那就要用 `24 - 入场时间 + 离场时间` * 3 + 10
2. 小于1小时，按1小时算，最低停车费5
3. 大于1小时，就按每小时3算
4. 小技巧：必须用分钟计算

## 二、Returns



## 三、Python Solution(s)

## 四、JavaScript Solution(s)

