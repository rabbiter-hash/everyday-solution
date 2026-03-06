# Perfect Cube Count

Given two integers, determine how many perfect cubes exist in the range between and including the two numbers.

- The lower number is not garanteed to be the first argument.
- A number is a perfect cube if there exists an integer (`n`) where `n * n * n = number`. For example, 27 is a perfect cube because `3 * 3 * 3 = 27`.

## 一、题解和思路

### 1.1、题解

- 输入的两个数，不保证第一个参数是更小的数；
- 完美立方数为：2x2x2=8，这个2是完美立方数；
- 只需要统计两个参数区间的完美立方数个数；

### 1.2、思路

#### 1.2.1、确定区间顺序

题目明确说“lower number”不一定是第一个参数，所以先找到区间的最小值和最大值：

```text
low = min(a, b)
high = max(a, b)
```

#### 1.2.2、找到区间内立方数的范围

- 对于一个完美立方数 `n`，落在 `[low, high]`内，必须满足：

  ```tex
  n * n * n >= low
  n * n * n <= high
  ```

  比如[10, 30]，3 x 3 x 3 = 27，27 > 10， 27 < 30；

- 所以可以用 `整数开立方` 来求最小和最大`n`：

  ```tex
  min_n = ceil(cube_root(low))
  max_n = floor(cube_root(high))
  ```

  - cube_root(x)表示 x 的立方根；
  - ceil()：向上取整，确保 n的3次方>= low
  - floor()： 向下取整，确保n的三次放 <= high

- 计算立方数数量

  - 区间内立方数的数量就是：

    ```tex
    count = max_n - min_n + 1
    ```

  - 如果`max_n < min_n`，说明区间内没有立方数，返回0

#### 1.1.3、示例

##### 1.1.3.1、示例1

- 输入：`a = 1, b = 27`；
- cube_root(1) = 1， cube_root(27) = 3 
- min_n = 1，max_n = 3
- count = 3 - 1 + 1 = 3
- 对应立方数为： 1, 8, 27

##### 1.1.3.2、示例2

- 输入： `a = 10, b = 30`；
- cube_root(10) ≈ 2.154， cube_root(30) ≈ 3.107
- min_n = 3，（向上取整）；max_n = 3，向下取整；
- count = 3 - 3 + 1 = 1；
- 对应立方数为：27

### 1.4、负数的情况

- 负数没有平方根，但是有立方根

- 所以负数的立方根写法应该是：

  ```python
  def cbrt(x):
      return x ** ( 1/3 ) if x >= 0 else -(-x) ** ( 1/3 )
  ```

### 1.5、浮点精度问题

- 64 ** (1/3) = 3.9999999999999996，floor向下取整的结果为3

- -64 ** (1/3) = -3.9999999999999996，ceil向上取整的结果为-3

### 1.6、如果区间有负数

- **那么0也是完美平方数。**
- 如果区间`[-n³, n³]`那么立方数的个数一定是`2n+1`

### 1.7、负数精度

对于负数的立方根，要向上取整，必须用到绝对值`abs`。

## 二、Returns

1. `count_perfect_cubes(3, 30)` should return `2`.
2. `count_perfect_cubes(1, 30)` should return `3`.
3. `count_perfect_cubes(30, 0)` should return `4`.
4. `count_perfect_cubes(-64, 64)` should return `9`.
5. `count_perfect_cubes(9214, -8127)` should return `41`.

## 三、Python Solution(s)

### 3.1、遍历区间

- 找到区间low和high
- 遍历区间内的每个数字
- 判定是否是完美立方数

**如何判定？**

```python
round(n ** (1/3)) ** 3 == n
```

在数学上，n 的立方根就是 `(n ** ( 1/3 ))`，也就是 `n的3分之1次方`；

**代码：**

```python
def count_perfect_cubes(a, b):
    # 1、查找最大值和最小值
    low = min(a,b)
    high = max(a, b)

    # 2、统计量
    count = 0

    # 3、遍历区间
    for num in range(low, high + 1):
        print(num)
        # 取出每个数的立方根并取整
        # 处理负数的情况
        if num <= 0:
            cube_root = round(-abs(num ** (1 / 3)))
            if cube_root ** 3 == num:
                count += 1
        else:
            cube_root = round(num ** ( 1/3 ))
            print(cube_root)
            # 判定
            if cube_root ** 3 == num:
                count += 1

    return count

count_perfect_cubes(-64, 64)
```

**简化写法：**

```python
def count_perfect_cubes(a, b):
    # 1. 查找区间最大值和最小值
    low = min(a, b)
    high = max(a, b)

    # 2. 初始化统计量
    count = 0
    
    # 3. 开始遍历区间
    for num in range(low, high + 1):
        # 判定负数的情况
        if num < 0:
            # 计算负数的立方根
            cube_root = round(-abs( num ** (1/3)))
        else:
            cube_root = round(num ** (1/3))
            
        # 判定cube_root的立方根是否等于原num
        if cube_root ** 3 == num:
            count += 1
    # 4. 返回统计量
    return count
count_perfect_cubes(-64, 64)
```

### 3.2、整数枚举法（避免浮点数精度问题）

#### 3.2.1、原理和思路

1. 区间确定
   - 先确定`low 和high`
   - 完美立方数(n³)一定落在区间`[low, high]`
2. 整数枚举n
   - 所有完美立方数都可以写成`n³`，
   - 所以只需要枚举整数n，计算`n³`是否落在`[low, high]`
   - 关键是怎么处理`n从负数到正数`
3. 判断范围
   - 对于每个整数，如果`n³ < low` -> 太小 -> 往大走
   - 如果`n³ > high` -> 超出 -> 停止
4. 统计技术
   - 满足 `low <= n³ <= high`的整数n就是一个完美立方数

#### 3.2.2、代码

```python
def perfect_cube_count_int_enumerate(a, b):
    # 1. 提取最大值和最小值
    low = min(a, b)
    high = max(a, b)

    # 2. 以0为边界
    n = 0
    while n ** 3 > low:
        # 如果n 的三次方 > 最小值，那么n就要往负数走
        n -= 1
    while n ** 3 < low:
        # n的三次方小于low，那么n就要往上走
        n += 1

    # 3. 开始统计
    count = 0
    while n ** 3 <= high:
        count += 1
        n += 1
    return count


perfect_cube_count_int_enumerate(-64, 64)
```

#### 3.3.3、步骤和过程

##### 一、初始化区间

```python
low = min(a, b)
high = max(a, b)
```

##### 二、从n=0 开始找最小n

如果区间包含负数，需要从负数开始

```python
n = 0
while n ** 3 > low: # 对负数
    n -= 1
   
while n ** 3 < low: # 找到第一个n，使n³ >= low
    n += 1
```

此时的`n`是区间内最小的立方根整数。

##### 三、从最小n往上枚举，统计 n³ <= high

```python
count = 0
while n ** 3 <= high:
    count += 1
    n += 1
    
```

- 每次 n + 1，计算n³
- 超过high就停止
- count就是区间内的完美立方数个数

#### 3.3.4、关键点

- 初始化n=0；
- 先向负方向移动，找到第一个n³ >= low
- 再向正方向移动，直到n³ > high
- 全程整数运算，不需要浮点数
- 支持任意负数和整数区间



## 四、JavaScript Solution(s)

### 4.1、整数枚举法

```js
function countPerfectCubes(a, b) {
  // 1. 确定区间的最小值和最大值
  const low = Math.min(a, b);
  const high = Math.max(a, b);

  // 2. 从 n=0 开始，找到区间内第一个立方数 n³ >= low
  let n = 0;

  // 2a. 如果 low < 0，需要向负方向移动 n，直到 n³ <= low
  while (n ** 3 > low) {
    n -= 1;
  }

  // 2b. 调整 n，保证 n³ >= low
  while (n ** 3 < low) {
    n += 1;
  }

  // 3. 初始化计数器
  let count = 0;

  // 4. 从左边界 n 开始枚举，每次 n³ <= high 就计数
  while (n ** 3 <= high) {
    count += 1; // 统计一个完美立方数
    n += 1;     // 移动到下一个整数
  }

  // 5. 返回区间内完美立方数总数
  return count;
}

// 测试
console.log(countPerfectCubes(-64, 64)); // 输出 9
console.log(countPerfectCubes(0, 27));   // 输出 4 (0,1,8,27)
console.log(countPerfectCubes(-27, -1)); // 输出 3 (-27,-8,-1)
```

