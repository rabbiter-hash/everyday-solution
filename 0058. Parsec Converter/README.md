# Parsec Converter

In a distant galaxy, parsecs are used to measure both time and distance. Given an integer number of parsecs, return its equivalent in time or distance.

- If the given integer is odd, it represents time. If it's even, it represents distance.

Use these conversion rates:

| Parsecs | Time/Distance |
| :-----: | :-----------: |
|    1    |    2 hours    |
|    2    | 6 light years |

Return the converted value as an integer.

## 一、题解和思路

### 1.1、题解

输入一个整数，如果是奇数（odd）就用`Time`计算，返回相应的值，即：`parsecs * 2`；如果是偶数（even），就用`distance`计算，返回相应的值，即：`parsecs * 6 // 2`；

### 1.2、思路

判定输入是奇数还是偶数，如果是奇数，`return parsecs * 2`，如果是偶数，`return parsecs * 6 // 2`；

## 二、Returns

1. `convertParsecs(1)` should return `2`.
2. `convertParsecs(2)` should return `6`.
3. `convertParsecs(31)` should return `62`.
4. `convertParsecs(88)` should return `264`.
5. `convertParsecs(17)` should return `34`.
6. `convertParsecs(14)` should return `42`.

## 三、Python Solution(s)

```python
def convert_parsecs(parsecs):
    # 1. 判定数据的合法性
    if not isinstance(parsecs, int):
        raise TypeError("parsecs must be a number")

    # 2. 直接返回
    # return parsecs * 3 if parsecs % 2 == 0 else parsecs * 2

    # 更简洁
    return parsecs * (3 if parsecs % 2 == 0 else 2)
```

## 四、JavaScript Solution(s)

```js
function convertParsecs(parsecs){
    // 1. 判定数据输入的合法性
    if(!Number.isInteger(parsecs)){
        throw new Error("输入必须是整数！");
    }

    // 2. 返回
    return parsecs % 2 === 0 ? parsecs * (6 / 2) : parsecs * 2;
    // 更简洁
    // return parsecs * (parsecs % 2 === 0 ? 3 : 2);
}
```

