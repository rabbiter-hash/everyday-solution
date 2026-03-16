# Evenly Divisible

Given two integers, determine if you can evenly divide the first one by the second one.

## 一、题解和思路

### 1.1、题解

- 输入两个整数a, b，查看是否a 能被 b整除；
- 其中a是被除数，b是除数
- 也就是a除以b余数要为0
- 一个重要边界：被除数不能为0，也就是b不能为0，否则会报错。

### 1.2、思路

- 直接被除数 % 除数

## 二、Returns

1. `is_evenly_divisible(4, 2)` should return `True`.
2. `is_evenly_divisible(7, 3)` should return `False`.
3. `is_evenly_divisible(5, 10)` should return `False`.
4. `is_evenly_divisible(48, 6)` should return `True`.
5. `is_evenly_divisible(3186, 9)` should return `True`.
6. `is_evenly_divisible(4192, 11)` should return `False`.

## 三、Python Solution(s)

### 3.1、取模法

```python
def is_evenly_divisible(a, b):
    # 1. 判定数据合法性
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('a and b must be integers')
    # 2. 除数不能是0,
    if b == 0:
        return False

    # 3. 直接返回
    return a % b == 0
```

## 四、JavaScript Solution(s)

### 4.1、取模法

```js
function isEvenlyDivisible(a, b){
    // 1. 判定数据合法性
    if(!Number.isInteger(a) || !Number.isInteger(b)){
        throw new Error("A and B must be integers!");
    }
    // 2. b(divisor)不能是0
    if(b === 0){
        return false;
    }

    // 3. return
    return a % b === 0;
}
```

