# Max Profit

Given an array of daily stock prices and a budget (in dollars), calculate the maximum profit you could make by buying and selling the stock over the given period.

- You may only sell after you buy.
- You can only buy whole shares.
- Return the maximum possible profit as a string, rounded down to the nearest cent and formatted to two decimal places.

## 一、题解和思路

### 1.1、题解

给出一个数组，它包含每日股价（daily stock prices），给定预算，计算在当前时期内， 能获得的最大利润。

- 必须先买后卖
- 必须买整股（whole shares）
- 返回的值保留两位数。

### 1.2、思路

- 初始化最大利润
- 遍历所有的可能买入日（i从0到n-2）
- 遍历所有可能的卖出日（j从i+1到n-1）
- 确保卖出价 > 买入价（否则亏损，不考虑）
- 计算可买股数`Math.floor(budget / buyPrice)`
- 计算总利润=`股数 x (卖出价 - 买入价)`
- 更新最大利润
- 最后结果向下取整，格式化为两位小数

## 二、Returns

1. `getMaxProfit([5, 6], 50)` should return `"10.00"`.
2. `getMaxProfit([8, 2, 5, 10], 20)` should return `"80.00"`.
3. `getMaxProfit([4, 5, 3, 6], 20)` should return `"18.00"`.
4. `getMaxProfit([54.40, 51.22, 53.99, 50.28, 53.01, 52.84], 200)` should return `"8.31"`.
5. `getMaxProfit([15.38, 15.01, 14.99, 14.62, 14.28], 80)` should return `"0.00"`.
6. `getMaxProfit([121.45, 126.82, 122.91, 124.65, 128.83, 128.83, 127.33], 1230.25)` should return `"73.80"`.

## 三、Python Solution(s)

## 四、JavaScript Solution(s)

