# Word Compressor

Given a string, return a compressed version of the string using the following rules:

- The first occurrence of a word remains unchanged.
- Subsequent occurrences are replaced with the position of the first occurrence, where the first word is at position 1.
- Words are separated by a single space.

For example, given `"practice makes perfect and perfect practice makes perfect"`, return `"practice makes perfect and 3 1 2 3"`.

## 一、题解和思路

### 1.1、题解

给出一个字符串，字符串中每个单次第一次出现需要标号方便后续替换。

### 1.2、思路

要做的只有一件事：记录每个单词第一次出现的位置。第一次出现 —— 输出单次本身；再次出现 —— 输出“第一次出现的位置”

实现：

以`practice makes perfect and perfect practice makes perfect`进行说明：

**第一步：**拆分字符串成：`["practice","makes","perfect","and","perfect","practice","makes","perfect"]`；

**第二步：**准备两个东西：

- 哈希表（字典）：word_index = {}
- 结果数组：result = []

**第三步：**开始遍历

第**1**个词：practice（位置1）

- 不存在 -> 存入哈希表 -> `practice: 1`；

- 输出原词：result: ["practice"]

第**2**个词：makes（位置2）

- 不存在 -> 更新哈希表 -> `makes: 2`；
-  输出为：result: ["practice", "makes"]；

第**3**个词：perfect（位置3）

- 不存在 -> 更新哈希表 -> `perfect: 3`
- 输出： result: ["practice", "makes", "perfect"]；

第**4**个词：and（位置4）

- 不存在 -> 更新哈希表 -> `and: 4`
- 输出：result: ["practice", "makes", "perfect", "and"]；

第**5**个词：perfect

- 已存在 → 查 map = 3
  result: `["practice", "makes", "perfect", "and", 3]`

第**6**个词：practice

- 已存在 → 1
   result: `[..., 1]`

第**7**个词：makes

- 已存在 → 2
  result: `[..., 2]`

第**8**个词：perfect

- 已存在 → 3
   result: `[..., 3]`

## 二、Returns

1. `compress("practice makes perfect and perfect practice makes perfect")` should return `"practice makes perfect and 3 1 2 3"`.
2. `compress("hello hello hello")` should return `"hello 1 1"`.
3. `compress("the cat sat on the mat on which the cat sat")` should return `"the cat sat on 1 mat 4 which 1 2 3"`.
4. `compress("the more you know the more you realize you don't know")` should return `"the more you know 1 2 3 realize 3 don't 4"`.
5. `compress("lorem ipsum dolor sit per elit donec sit nostra libero per donec ligula sit gravida at elit vitae a elit sodales donec en donec at dolor nam ligula dignissim risus at ligula per nam ipsum ipsum gravida en elit per ipsum ligula en gravida per sodales sit at nam lorem sit per libero en ipsum elit sit sodales sit risus elit risus ipsum elit at gravida vitae en dignissim nam sit vitae sollicitudin per nostra per sit libero")` should return `"lorem ipsum dolor sit per elit donec 4 nostra libero 5 7 ligula 4 gravida at 6 vitae a 6 sodales 7 en 7 16 3 nam 13 dignissim risus 16 13 5 27 2 2 15 23 6 5 2 13 23 15 5 21 4 16 27 1 4 5 10 23 2 6 4 21 4 30 6 30 2 6 16 15 18 23 29 27 4 18 sollicitudin 5 9 5 4 10"`.

## 三、Python Solution(s)

### 3.1、清晰、常规解法

```python
def compress(s):
    # 1. 将字符串单词转成数组
    words_arr = s.split()

    # 2. 存储结果集
    ## 2.1、哈希表存储每个单词第一次出现的位置
    word_map = {}
    ## 2.2、结果集存储最终结果
    result = []

    # 3. 循环遍历
    for i,word in enumerate(words_arr):
        # 需要要判定是否在哈希表中
        if not word in word_map:
            # 不存在就要创建哈希表，注意+1的问题
            word_map[word] = i + 1
            # 将word追加到列表
            result.append(word)
        else:
            # 否则就是已经存在哈希表中了，直接append当前word在哈希表中的位置数值
            result.append(str(word_map[word]))

    return " ".join(result)

compress("the cat sat on the mat on which the cat sat")
```

### 3.2、Pythonic

```python
def compress_pythonic(s):
    seen = {}

    return " ".join(
        seen.setdefault(word, i+1) if word in seen else word
        for i, word in enumerate(s.split())
    )
```

## 四、JavaScript Solution(s)

### 4.1、清晰常规解法

```js

function compress(str){
    // 1. 将字符串拆分成数组
    const wordsArr = str.split(/\s+/g);

    // 2. 存储结果集
    // 2.1、字符串第一次出现位置的映射
    let wordsIndexMap = {};
    // 2.2、结果集
    let results = [];

    // 3. 循环遍历
    wordsArr.forEach((word, inx) => {
        // 判定word是否在映射表中
        if(!(word in wordsIndexMap)){
            // 不存在就追加
            /*
            * 也可以使用
            * 1. if(wordsIndexMap.hasOwnProperty(word))
            * 2. if(Object.hasOwn(wordsIndexMap, word))
            * */
            wordsIndexMap[word] = inx + 1;
            // 将word追加到结果集
            results.push(word);
        } else {
            // 如果word在哈希表中，就追加哈希表中对应字段的值
            results.push(wordsIndexMap[word]);
        }
    });
    // console.log(results);
    return results.join(" ");
}

compress("the cat sat on the mat on which the cat sat");
```

### 4.2、Idiomatic JavaScript

```js
function compressIdiomatic(str){
    const seen = new Map();

    return str
        .split(/\s+/g)
        .map((word, i) => {
            if(seen.has(word)) return seen.get(word);
            seen.set(word, i + 1);
            return word;
        }).join(" ");
}
```

