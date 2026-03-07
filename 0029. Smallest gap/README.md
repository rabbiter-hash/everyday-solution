# Smallest Gap

Given a string, return the substring between the two identical characters that have the smallest number of characters between them (smallest gap).

- There will always be at least one pair of matching characters.
- The returned substring should exclude the matching characters.
- If two or more gaps are the same length, return the characters from the first one.

For example, given `"ABCDAC"`, return `"DA"`.

- Only `"A"` and `"C"` repeat in the string.
- The number of characters between the two `"A"` characters is 3, and between the `"C"` characters is 2.
- So return the string between the two `"C"` characters.

## 一、题解和思路

### 1.1、题解

- 输入：一个字符串，如`ABCDAC`
- 目标：找出字符串中重复出现的字符，并计算它们之间的字符串（不包含自己）。重复出现的字符，指在字符串中最少出现两次的字符；
- 间隔长度：指两个相同字符串之间的字符数（不包含重复字符本身），例如"ABCDAC"中：
  - 字符A出现两次，位置分别是0和4，它们之间的字符是"BCD"，间隔长度为3；
  - 字符C出现两次，位置分别是2和5，它们之间的字符是"DA"，间隔长度为2；
- 最小间隔：找出间隔长度最小的重复字符，然后返回这两个字符之间的子串。如果有多组，返回最短的那一组；
  - 上例中：A的间隔长度为3
  - C的间隔长度为2
  - 所以应该返回"DA"（两个C之间的内容）
- 如果有多个最小间隔相同，只返回第一个出现的

### 1.2、思路

- 遍历字符串
- 记录每个字符上一次出现的位置
- 如果字符再次出现，计算间隔：gap = 当前索引 - 上一次索引 - 1
- 如果这个gap比当前最小gap小，更新minGap和result
- 继续遍历，直至结束

## 二、Returns

1. `smallest_gap("ABCDAC")` should return `"DA"`.
2. `smallest_gap("racecar")` should return `"e"`.
3. `smallest_gap("A{5e^SD*F4i!o#q6e&rkf(po8|we9+kr-2!3}=4")` should return `"#q6e&rkf(p"`.
4. `smallest_gap("Hello World")` should return `""`.
5. `smallest_gap("The quick brown fox jumps over the lazy dog.")` should return `"fox"`.

## 三、Python Solution(s)

### 3.1、暴力解法，遍历字符串

#### 3.1.1、思路

- 遍历每个字符
- 向后找相同字符
- 计算间隔
- 记录最小值
- 返回结果

#### 3.1.2、代码

```python
def smallest_gap(s):
    # 1. 判定数据的合法性
    if not isinstance(s, str):
        raise TypeError('S must be a string')

    # 2. 初始化最小gap
    min_gap = float('inf') # 创建一个无穷大的浮点数，将它赋值给min_gap

    # 3. 初始化结果变量
    result = ""

    # 4. 开始循环遍历
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            # 如果出现了，就计算gap
            if s[i] == s[j]:
                gap = j - i - 1
                if gap < min_gap:
                    min_gap = gap
                    result = s[i+1:j]
    print(result)
    return result

smallest_gap("ABCDAC")
```

### 3.2、哈希表最优解

#### 3.2.1、思路

只需记录字符上一次出现的位置

如果字符串多次出现

```tex
A....A....A
```

最小gap一定在相邻两个A之间。所以，只需记得最近一次位置。

#### 3.2.2、步骤

- 遍历字符串
- 用字典记录字符出现的位置
- 如果字符串出现过：
  - 计算gap
  - 更新最小gap
- 更新字符位置

#### 3.3.3、代码

```python
def smallest_gap_with_hash_table(s):
    # 1. 判定数据的合法性
    if not isinstance(s, str):
        raise TypeError('S must be a string')

    # 2. 初始化哈希表和最小gap以及结果
    last_pos = {}  # 哈希表：记录字符最近一次出现的位置
    min_gap = float('inf')  # 初始化为正无穷，保证第一次gap一定能更新
    result = ""

    # 3. 遍历字符串
    for i, char in enumerate(s):

        """
        ======== 循环过程示例 (字符串: "ABCDAC") ========

        初始状态:
        last_pos = {}
        min_gap = ∞
        result = ""

        -----------------------------------------
        第1次循环
        i = 0
        char = 'A'

        'A' 不在 last_pos 中
        不计算 gap

        更新哈希表:
        last_pos['A'] = 0

        last_pos = {'A': 0}

        -----------------------------------------
        第2次循环
        i = 1
        char = 'B'

        'B' 不在 last_pos 中

        更新哈希表:
        last_pos['B'] = 1

        last_pos = {'A':0, 'B':1}

        -----------------------------------------
        第3次循环
        i = 2
        char = 'C'

        'C' 不在 last_pos 中

        更新哈希表:
        last_pos['C'] = 2

        last_pos = {'A':0, 'B':1, 'C':2}

        -----------------------------------------
        第4次循环
        i = 3
        char = 'D'

        'D' 不在 last_pos 中

        更新哈希表:
        last_pos['D'] = 3

        last_pos = {'A':0, 'B':1, 'C':2, 'D':3}

        -----------------------------------------
        第5次循环 (关键)
        i = 4
        char = 'A'

        'A' 已经在 last_pos 中
        上一次位置 = 0

        计算 gap:
        gap = 4 - 0 - 1 = 3

        中间字符串:
        s[1:4] = "BCD"

        因为:
        3 < ∞

        更新:
        min_gap = 3
        result = "BCD"

        更新字符最新位置:
        last_pos['A'] = 4

        last_pos = {'A':4, 'B':1, 'C':2, 'D':3}

        -----------------------------------------
        第6次循环
        i = 5
        char = 'C'

        'C' 在 last_pos 中
        上一次位置 = 2

        计算 gap:
        gap = 5 - 2 - 1 = 2

        中间字符串:
        s[3:5] = "DA"

        因为:
        2 < 3

        更新:
        min_gap = 2
        result = "DA"

        更新字符位置:
        last_pos['C'] = 5

        last_pos = {'A':4, 'B':1, 'C':5, 'D':3}

        -----------------------------------------
        循环结束

        最终:
        result = "DA"
        """

        if char in last_pos:
            gap = i - last_pos[char] - 1
            if gap < min_gap:
                min_gap = gap
                result = s[last_pos[char] + 1:i]

        # 更新字符最近出现的位置
        last_pos[char] = i

    print(result)
    print(last_pos)

    return result

smallest_gap_with_hash_table("ABCDAC")
```

#### 3.3.4、哈希表

哈希表是一种内存中的数据结构。

哈希表 ≠ Json

```js
// JSON - 是字符串，用于数据交换
let jsonStr = '{"name": "Alice", "age": 25}';

// 解析后变成内存中的对象（哈希表实现）
let obj = JSON.parse(jsonStr); // 这才是哈希表
```

## 四、JavaScript Solution(s)

### 4.1、暴力解法，遍历字符串

```js
function smallestGap(str) {
    // 1. 判定数据输入的合法性
    if(typeof str !== "string") {
        throw new Error("输入必须是字符串！");
    }

    // 2. 初始化最小gap和结果
    let minGap = Infinity;
    let result = "";

    // 3. 暴力循环
    for (let i = 0; i < str.length; i++) {
        for (let j = i + 1; j < str.length; j++){
            if(str[i] === str[j]){
                // 计算最小gap
                let gap = j - i - 1;
                // 判定gap是否小于minGap，小于就将更新minGap
                if(gap < minGap){
                    minGap = gap;
                    // 计算结果
                    result = str.slice(i + 1, j);
                }
            }
        }
    }
    console.log(result);
    return result;
}

// smallestGap("ABCDAC");
```

### 4.2、哈希表解法

```js
function smallestGapWithHashTable(str){
    // 1. 判定数据输入是否合法
    if(typeof str !== "string"){
        throw new Error("输入必须是字符串！");
    }

    // 2. 初始化哈希表、最小gap和结果
    let lastPos = {};
    let minGap = Infinity;
    let result = "";

    // 3. 开始循环
    for(let i = 0; i < str.length; i++){
        // 初始化char
        let char = str[i];
        // 判定char是否在哈希表中
        if(char in lastPos){
            // 如果在，我们就要计算最小gap
            let gap = i - lastPos[char] - 1; // 当前索引-在哈希表中的记录的索引值 - 1
            // 判定是否小于最小gap
            if(gap < minGap){
                // 更新minGap
                minGap = gap;
                // 拿到最小gap后，就可以取出结果了
                result = str.slice(lastPos[char] + 1, i); //
            }
        }
        // 更新哈希表
        lastPos[char] = i;
    }
    console.log(result);
    return result;
}
smallestGapWithHashTable("ABCDAC");
```

