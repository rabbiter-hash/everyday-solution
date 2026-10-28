# Integer Sequence

Given a positive integer, return a string with all of the integers from `1` up to, and including, the given number, in numerical order.

For example, given `5`, return `"12345"`.

## 一、题解和思路

### 1.1、题解

输入一个正整数，输出它前面的所有连续自然数（不包括0）组成的字符串。

### 1.2、思路

#### 1.2.1、循环

注意`边界`。

## 二、Returns

1. `sequence(5)` should return `"12345"`.
2. `sequence(10)` should return `"12345678910"`.
3. `sequence(1)` should return `"1"`.
4. `sequence(27)` should return `"123456789101112131415161718192021222324252627"`.

## 三、Python Solution(s)

### 3.1、循环

```python
def sequence(n):
    # 1. 存储结果
    result = ''

    # 2. 开始循环，python要注意边界
    for i in range(n):
        result += str(i + 1)

    print(result)
    return result

sequence(5)
```

## 四、JavaScript Solution(s)

### 4.1、循环

```js
function sequence(n) {
    // 1. 存储结果集
    let result = '';

    // 2. 开始循环
    for (let i = 1; i <= n; i++){
        console.log(i);
        result += String(i);
    }

    console.log(result);
    return result;
}
```

