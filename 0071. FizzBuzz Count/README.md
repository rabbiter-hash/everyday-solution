# FizzBuzz Count

Given a start and end number, count the number of fizz and buzz appearances in the range (inclusive).

- Numbers divisible by 3 count as a fizz.
- Numbers divisible by 5 count as a buzz.
- Numbers divisible by both 3 and 5 count as both a fizz and a buzz.

Return an object or dictionary with the counts in the format: `{ fizz, buzz }`.

## 一、题解和思路

### 1.1、题解

给出一个区间，区间内能被三整除的加入`fizz`统计，能被五整除的加入`buzz`，以字典（对象）方式返回。

### 1.2、思路

循环遍历区间内的数，加入到统计。需要注意的是，循环的数要包含给定区间的边界数值。

`Numbers divisible by both 3 and 5 count as both a fizz and a buzz.`，同时能被3和5整除的数，既要计入`fizz`也要计入`buzz`

也就是，循环遍历的时候，要走单分支`if`，而不能走`if..elif`。

## 二、Returns

1. `fizz_buzz_count(1, 11)` should return `{"fizz": 3, "buzz": 2}`.
2. `fizz_buzz_count(14, 41)` should return `{"fizz": 9, "buzz": 6}`.
3. `fizz_buzz_count(24, 100)` should return `{"fizz": 26, "buzz": 16}`.
4. `fizz_buzz_count(-635, -14)` should return `{"fizz": 207, "buzz": 125}`.
5. `fizz_buzz_count(-5432, 6789)` should return `{"fizz": 4074, "buzz": 2444}`.

## 三、Python Solution(s)

### 3.1、

## 四、 JavaScript Solution(s)

