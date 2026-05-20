# String Zipper

Given two strings, return a new string that interleaves their characters one at a time. If one string is longer, append the remaining characters at the end.

Begin with the first character of the first string.

## 一、题解和思路

### 1.1、题解

输入两个字符串`a和b`，输出一个新的字符串，从`a`的第一个字符开始，依次交替取`a`和`b`的字符，如果一个字符串比另一个长，则把剩下的字符串直接加到结果末尾；

### 1.2、思路

- 遍历索引
- 找到两个字符串长度的最小值`min_length`
- 用一个循环从`0`到`min_length - 1`，依次把`a[i]`和`b[i]`追加到结果
- 循环结束，把剩余的字符（如果有）直接加到结果末尾

## 二、Returns

1. `zip_strings("abc", "123")` should return `"a1b2c3"`.
2. `zip_strings("acegikmoqsuwy", "bdfhjlnprtvxz")` should return `"abcdefghijklmnopqrstuvwxyz"`.
3. `zip_strings("day", "night")` should return `"dnaiyght"`.
4. `zip_strings("python", "javascript")` should return `"pjyatvhaosncript"`.
5. `zip_strings("feCdCm", "reoeap")` should return `"freeCodeCamp"`.

## 三、Python Solution(s)

### 3.1、索引遍历

```python
def zip_strings(a, b):
    # 1. Python可以直接交替结果
    result = ''.join(ach + bch for ach, bch in zip(a, b))
    print(result)
    # 2. 获取最短的那个字符串
    min_len = min(len(a), len(b))

    # 3. 切片取有多余的字符串
    result += a[min_len:] + b[min_len:]

    return result
zip_strings("python", "javascript")
```

##  四、JavaScript Solution(s)

### 4.1、索引遍历

```js

function zipStrings(a, b){
    // 1. 结果集
    let result = '';

    // 2. 取最短长度
    let minLength = Math.min(a.length, b.length);

    // 3. 循环
    for(let i = 0; i < minLength; i++){
        result += a[i] + b[i];
    }
    console.log(result);

    // 4. 继续追加长度
    result += a.slice(minLength, ) + b.slice(minLength, );

    console.log(result);

    return result;
}

zipStrings("python", "javascript")
```