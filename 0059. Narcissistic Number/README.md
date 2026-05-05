# Narcissistic Number

Given a positive integer, determine whether it is a narcissistic number.

- A number is narcissistic if the sum of each of its digits raised to the power of the total number of digits equals the number itself.

For example, 153 has 3 digits, and 13 + 53 + 33 = 153, so it is narcissistic.

## 一、题解和思路

### 1.1、题解

输入一个数字，判断它是否为自幂数。

> 自幂数，英文叫narcissistic number，也译作：阿姆斯特朗数。是指：一个n位数，其各位数上的数字的n次方之和等于它本身。
>
> - 所有一位数，都是自幂数，也就是1,2,3,4,5,6,7,8,9；
> - 两位数：不存在自幂数；
> - 三位数：153，370,371,407
> - 四位数：1634,8208,9474
>
> 在十进制下，这种数只有有限个（共 88 个），最大的一个是一个 39 位数。

### 1.2、思路

- 检验数据输入是否合法；
- `str(n)`转成字符串才能循环
- 遍历每一位
- 每位做`digit ** 位数`，也就是`len(str(n))`
- 累加后判断是否等于原数

## 二、Returns

1. `is_narcissistic(153)` should return `True`.
2. `is_narcissistic(154)` should return `False`.
3. `is_narcissistic(371)` should return `True`.
4. `is_narcissistic(512)` should return `False`.
5. `is_narcissistic(9)` should return `True`.
6. `is_narcissistic(11)` should return `False`.
7. `is_narcissistic(9474)` should return `True`.
8. `is_narcissistic(6549)` should return `False`.

## 三、Python Solution(s)

### 3.1、循环解法

```python
def is_narcissistic(n):
    # 1. 判定输入的合法性
    if not isinstance(n, int):
        raise TypeError("N must be an integer!")

    # 2. 预存储相加结果
    total = 0
    # 3. 输入数字的位数，用于幂计算
    power = len(str(n))

    # 4. 循环
    for digit in str(n):
        total += int(digit) ** power

    if total == n:
        return True
    return False

is_narcissistic(153)
```

### 3.2、Pythonic

```python
def is_narcissistic_pythonic(n):
    digits_to_str_list = str(n)
    power = len(digits_to_str_list)

    return n == sum(
        int(d)**power for d in digits_to_str_list
    )
```

## 四、JavaScript Solution(s)

### 4.1、循环解法

```js
function isNarcissistic(n) {
    // 1. 判定数据输入的合法性
    if(!Number.isInteger(n)){
        throw new TypeError("输入必须是整数！");
    }

    // 2. 将数字转成字符串
    const str = String(n);
    console.log(str);

    const power = str.length;
    // 3. 初始化计量结果
    let total = 0;

    // 4. 循环
    for(let i = 0; i < str.length; i++){
        // 定义数字
        const digit = Number(str[i]);
        console.log(digit);

        // 累加和
        total += Math.pow(digit, power);
        console.log(total);
    }
    console.log(total);

    // 5. 判定是否相等
    if(total === n){
        return true;
    }

    return false;
}

// isNarcissistic(153)
```

### 4.1、Idiomatic

```js
function isNarcissisticIdiomatic(n){
    const digits = String(n).split("");
    console.log(digits);
    const power = digits.length;

    return n === digits.reduce(
        (acc, num) => acc + Math.pow(num, power), 0
    );
}

isNarcissisticIdiomatic(153)
```