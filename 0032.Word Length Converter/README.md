# Word Length Converter

Given a string of words, return a new string where each word is replaced by its length.

- Words in the given string will be separated by a single space
- Keep the spaces in the returned string.

For example, given `"hello world"`, return `"5 5"`.

## 一、题解和思路

### 1.1、题解

- 输入字符串
- 有多个单词，单词之间用空格分割
- 把每个单词替换成该单词的长度，并保留空格

### 1.2、思路

- 把字符串拆分成单词数组

- 把每个单词变成“长度”，历数组，把每个单词替换为它的长度

- 把数字数组拼回字符串

- ```tex
  原字符串
     ↓
  按空格分割
     ↓
  得到单词数组
     ↓
  遍历数组 → 每项变长度
     ↓
  得到长度数组
     ↓
  用空格拼接
     ↓
  最终字符串
  ```

## 二、Returns

1. `convert_words("hello world")` should return `"5 5"`.
2. `convert_words("Thanks and happy coding")` should return `"6 3 5 6"`.
3. `convert_words("The quick brown fox jumps over the lazy dog")` should return `"3 5 5 3 5 4 3 4 3"`.
4. `convert_words("Lorem ipsum dolor sit amet consectetur adipiscing elit donec ut ligula vehicula iaculis orci vel semper nisl")` should return `"5 5 5 3 4 11 10 4 5 2 6 8 7 4 3 6 4"`.

## 三、Python Solution(s)

### 3.1、循环遍历法

```python
def convert_words_with_for(s):
    # 1. 判定输入是否合法
    if not isinstance(s, str):
        raise TypeError('s must be a string')

    # 2. 将字符串串转成列表
    words_lis = s.split(" ")

    # 3. 初始化长度存放的数组
    words_length_lis = []

    # 4. 遍历
    for word in words_lis:
        words_length_lis.append(str(len(word)))

    print(words_length_lis)
    # 5. 返回
    return " ".join(words_length_lis)

convert_words_with_for("hello world")
```

### 3.2、列表推导式

```python
def convert_words_one(s):
    return " ".join([str(len(word)) for word in s.split(" ")])
```

### 3.3、函数式

```python
def convert_words_with_map(s):
    return " ".join(map(lambda w: str(len(w)), s.split(" ")))
```



## 四、JavaScript Solution(s)

### 4.1、循环

```js
function convertWords(str) {
    const words = str.split(" ");   // 拆分单词
    const result = [];              // 存放长度

    for (let i = 0; i < words.length; i++) {
        result.push(String(words[i].length));
    }

    return result.join(" ");        // 拼接字符串
}
```

### 4.2、map映射

```js
function convertWordsWithMap(str) {
    return str
        .split(" ")
        .map(word => String(word.length))
        .join(" ");
}
```

### 4.3、map映射，但是更简洁

```js
function convertWordsWithMapSimple(str) {
    return str
        .split(" ")
        .map(wrod => word.length)
        .join(" ");
}
```

