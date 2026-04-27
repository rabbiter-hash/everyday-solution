# Word Score

Given a word, return its score using a standard letter-value table:

| Letter | Value |
| :----: | :---: |
|   A    |   1   |
|   B    |   2   |
|  ...   |  ...  |
|   Z    |  26   |

- Upper and lowercase letters have the same value.

## 一、题解和思路

### 1.1、题解

字母A-Z分别代表分值1-26，输入一个字符串，计算每个字母所代表分值的和（累加）；

### 1.2、思路

- 建立字母和分值映射表，字母是大写；
- 循环输入的字符串的字母
- 将其全部转成大写
- 在循环内累加

## 二、Returns

- `get_word_score("hi")` should return `17`.
- `get_word_score("hello")` should return `52`.
- `get_word_score("hippopotamus")` should return `169`.
- `get_word_score("freeCodeCamp")` should return `94`.

## 三、Python Solution(s)

### 3.1、映射硬编码

```python
def get_word_score(word):
    # 1. 映射硬编码
    letter_values = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
        'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
        'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22,
        'W': 23, 'X': 24, 'Y': 25, 'Z': 26
    }

    # 2. 累加初始化
    total = 0

    # 3. 循环累加
    for ch in word:
        # 将每个单次转大写
        ch = ch.upper()
        if ch in letter_values:
            total += letter_values[ch]

    return total
```

### 3.2、函数ord

```python
def get_word_score_by_ord(word):
    # 1. 初始化累加值
    total = 0

    # 2. 循环
    for ch in word.upper():
        if "A" <= ch <= "Z":
            total += ord(ch) - ord("A") + 1
    return total
get_word_score_by_ord("hi")
```

### 3.3、Pythonic

```python
def get_word_score_pythonic(word):
    return sum(
        ord(ch) - 64
        for ch in word.upper()
        if "A" <= ch <= "Z"
    )
```

## 四、JavaScript Solution(s)

### 4.1、映射硬编码

```js
function getWordScore(word){
    // 1. 映射值
    const letterValues = {
          A: 1,
          B: 2,
          C: 3,
          D: 4,
          E: 5,
          F: 6,
          G: 7,
          H: 8,
          I: 9,
          J: 10,
          K: 11,
          L: 12,
          M: 13,
          N: 14,
          O: 15,
          P: 16,
          Q: 17,
          R: 18,
          S: 19,
          T: 20,
          U: 21,
          V: 22,
          W: 23,
          X: 24,
          Y: 25,
          Z: 26
        };

    // 2. 初始化累加值
    let total = 0;

    // 3. 循环
    for(let ch of word){
        ch = ch.toUpperCase();
        total += letterValues[ch];
    }
    return total;
}
getWordScore("hi");
```

### 4.2、函数charCodeAt()

```js
function getWordScoreUseCharCodeAt(word){
    // 1. 初始化累加值
    let total = 0;

    // 2. 循环
    for (let ch of word.toUpperCase()){
        // 只处理A-Z
        if(ch >= "A" && ch <= "Z"){
            total += ch.charCodeAt(0) - 64;
        }
    }
    return total;

}
```

### 4.3、Idiomatic

```js
function getWordScoreIdiomatic(word){
    return [...word.toUpperCase()]
        .filter(ch => ch >= "A" && ch <= "Z")
        .reduce((acc, ch) => acc + ch.charCodeAt(0) - 64, 0);
}
```

