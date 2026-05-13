# Character Frequency

Given a string, return an object (JavaScript) or dictionary (Python) mapping each character to the number of times it appears.

## 一、题解和思路

### 1.1、题解

从输入的字符串，返回每个字符的出现次数的字典形式。

### 1.2、思路

- 初始化结果存储对象（字典）

- 使用对象存储计算字符出现的次数

## 二、Returns

1. `get_frequency("test")` should return `{"t": 2, "e": 1, "s": 1}`.
2. `get_frequency("mississippi")` should return `{"m": 1, "i": 4, "s": 4, "p": 2}`.
3. `get_frequency("hello world")` should return `{"h": 1, "e": 1, "l": 3, "o": 2, " ": 1, "w": 1, "r": 1, "d": 1}`.
4. `get_frequency("She sells seashells by the seashore.")` should return `{"S": 1, "h": 4, "e": 7, " ": 5, "s": 7, "l": 4, "a": 2, "b": 1, "y": 1, "t": 1, "o": 1, "r": 1, ".": 1}`.
5. `get_frequency("The quick brown fox jumps over the lazy dog.")` should return `{"T": 1, "h": 2, "e": 3, " ": 8, "q": 1, "u": 2, "i": 1, "c": 1, "k": 1, "b": 1, "r": 2, "o": 4, "w": 1, "n": 1, "f": 1, "x": 1, "j": 1, "m": 1, "p": 1, "s": 1, "v": 1, "t": 1, "l": 1, "a": 1, "z": 1, "y": 1, "d": 1, "g": 1, ".": 1}`.

## 三、Python Solution(s)

### 3.1、字典计算

```python
def get_frequency(s):
    # 1. 结果存储
    freq = {}

    # 2. 遍历
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    return freq
```

### 3.2、Counter

```python
def get_frequency_counter(s):
    from collections import Counter
    return dict(Counter(s))
```

## 四、JavaScript Solution(s)

### 3.2、对象存储遍历

```js
function getFrequency(s){
    // 1. 结果集
    let freq = {};

    // 2. 遍历
    for(let char of s){
        freq[char] = (freq[char] || 0) + 1;
    }

    return freq;
}

```

### 3.3、函数式

```js
function getFrequencyWithMap(s){
    // 1. 结果存储对象
    const result = {};
    // 2. 展开字符串
    const chars = [...s];

    // 3. 遍历
    for(let char of chars){
        result[char] = chars.filter(c => c === char).length;
    }
    console.log(result);
}
```