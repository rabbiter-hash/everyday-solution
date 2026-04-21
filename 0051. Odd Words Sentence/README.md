# Odd Words

Given a string of words, return only the words with an odd number of letters.

- Words in the given string will be separated by a single space.
- Return the words separated by a single space.

## 一、题解和思路

### 1.1、题解

取出字符串中奇数长度的单词，并重新组成句子返回。

### 1.2、思路

- 将输入通过空格拆成数组；
- 一个结果存储数组
- 遍历拆分后的数组，判定元素长度，如果是奇数长度，就追加到结果存储数组
- 通过拼接返回结果

## 二、Returns

1. `get_odd_words("This is a super good test")` should return `"a super"`.
2. `get_odd_words("one two three four")` should return `"one two three"`.
3. `get_odd_words("banana split sundae with rainbow sprinkles on top")` should return `"split rainbow sprinkles top"`.
4. `get_odd_words("The quick brown fox jumped over the lazy river")` should return `"The quick brown fox the river"`.

## 三、Python Solution(s)

### 3.1、常规解法

```python
def get_odd_words(s):
    # 1. 拆分输入的字符串
    words_lis = s.split()

    # print(words_lis)

    # 2. 结果数组
    results = []

    # 3. 循环遍历
    for ch in words_lis:
        if len(ch) % 2 != 0:
            results.append(ch)

    return " ".join(results)
get_odd_words("This is a super good test")
```

### 3.2、一句话版本

```python
def get_odd_words_one(s):
    return " ".join([word for word in s.split() if len(word) % 2 != 0])
```

### 3.3、底层解法

```python
def get_odd_words(s):
    result = ""
    word = ""

    for ch in s:
        if ch != " ":
            word += ch
        else:
            if len(word) % 2 != 0:
                if result:
                    result += " "
                result += word
            word = ""

    if len(word) % 2 != 0:
        if result:
            result += " "
        result += word

    return result
```



## 四、JavaScript Solution(s)

### 4.1、常规解法

```js
function getOddWords(s){
    // 1. 拆分成数组
    let wordsArr = s.split(/\s+/);

    console.log(wordsArr);

    // 2. 结果集
    let results = [];

    // 3. 循环遍历数组
    for(let word of wordsArr){
        if(word.length % 2 !== 0){
            results.push(word);
        }
    }
    console.log(results);
    return results.join(" ");
}

getOddWords("This is a super good test")
```

### 4.2、一句话版本

```js
```

