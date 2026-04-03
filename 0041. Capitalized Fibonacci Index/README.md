# Capitalized Fibonacci

Given a string, return a new string where each letter is capitalized if its index is a Fibonacci number, and lowercased otherwise.

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. The first 10 numbers in the sequence are `0`, `1`, `1`, `2`, `3`, `5`, `8`, `13`, `21`, `34`.

- The first character is at index `0`.
- If the index of non-letter characters is a Fibonacci number, leave it unchanged.

## 一、题解、思路、注意

### 1.1、题解

使用斐波那契数列的值作为查询索引，将字符串中对应的索引的值（字母）大写，其他的小写。

### 1.2、思路

- 计算字符串的最大长度
- 通过字符串的最大长度，算出斐波那契数列，并用集合存储；因为斐波那契数列为：[0, 1, 1, 2, 3, 5....]，中间会出现两个1，要去重；
- 通过循环字符串，找到字符索引是否存在于斐波那契数列，如果存在，就让当前索引的值大写，否则小写。

### 1.3、注意

- 索引从0开始，计算出字符串的长度后，要-1；

## 二、Returns

- `capitalize_fibonacci("hello world")` should return `"HELLo woRld"`.
- `capitalize_fibonacci("HELLO WORLD")` should return `"HELLo woRld"`.
- `capitalize_fibonacci("hello, world!")` should return `"HELLo, wOrld!"`.
- `capitalize_fibonacci("The quick brown fox jumped over the lazy dog.")` should return `"THE qUicK broWn fox jUmped over thE lazy dog."`.
- `capitalize_fibonacci("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin pulvinar ex nibh, vel ullamcorper ligula egestas quis. Integer tincidunt fringilla accumsan. Integer et metus placerat, gravida felis at, pellentesque nisl.")` should return `"LOREm ipSum dOlor sit amet, consecTetur adipiscing elit. proin pulvinar ex nibh, vel ullaMcorper ligula egestas quis. integer tincidunt fringillA accumsan. integer et metus placerat, gravida felis at, pellentesque nisl."`.

## 三、Python Solution(s)

### 3.1、底层解法

```python
def capitalize_fibonacci(s):
    # 1. 结果
    result = []

    # 2. 基础斐波那契
    a, b = 0, 1

    # 3. 循环
    for i, char in enumerate(s):
        # print(i, char)
        # 判定是否为字符，关键
        if char.isalpha():
            # 判定当前轮循环是否等于斐波那契数列数值
            if i == a:
                print(a)
                result.append(char.upper())
                # 添加之后，要更新斐波那契的值
                a, b = b, a + b
            else:
                # 如果不是斐波那契数列值，但是是字符，直接小写
                result.append(char.lower())
        else:
            result.append(char)
    print("".join(result))
    return "".join(result)

capitalize_fibonacci("HELLO WORLD")
capitalize_fibonacci("hello world")
```

#### 3.1.1、详解

- 时间复杂度：O(n)
- 空间复杂度：O(1)
- 解法不用存，流式（strem）解法
- 在线生成 Fibonacci + 单指针推进
- 但是有一个问题：它只会更新两次a，b的值，这与斐波那契数列有关，它有两个1，而index只有一个1.

### 3.2、常规解法

```python
def capitalize_fibonacci(s: str) -> str:
    # 1. 获取字符串的最大索引
    max_index = len(s) - 1

    # 2. 斐波那契数列的值
    fib_set = set()
    a, b = 0, 1

    while a <= max_index:
        #
        fib_set.add(a)
        a, b = b, a + b

    result = []
    # 3. 循环读取字符串，取出所以与当前集合中的索引进行比对
    for i, char in enumerate(s):
        # 判定i是否在集合中
        if i in fib_set:
            # 如果存在，就让当前char大写
            result.append(char.upper() if char.isalpha() else char)
        else:
            # 如果不存在，需要判定是否为大写，如果是大写就要转成小写
            result.append(char.lower() if char.isalpha() else char)

    print(result)
    return "".join(result)
capitalize_fibonacci("hello world")
```

#### 3.2.1、详解

- 非字母处理

  ```tex
  如果是字母：
      Fibonacci → 大写
      非 Fibonacci → 小写
  如果不是字母：
      完全不动（不管是不是 Fibonacci）
  ```

- 时间复杂度：O(n)

- 空间复杂度：O(n)

- 如果字符串超大（GB级）：set方案会爆内存；

## 四、JavaScript Solution(s)

