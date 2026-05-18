# Bingo Range

Given a bingo letter, return the number range associated with that letter.

| Letter | Number Range |
| :----: | :----------: |
| `"B"`  |     1-15     |
| `"I"`  |    16-30     |
| `"N"`  |    31-45     |
| `"G"`  |    46-60     |
| `"O"`  |    61-75     |

Return an array with all numbers in the range from smallest to largest.

## 一、题解和思路

### 1.1、题解

输入一个字符，返回相应设定范围值的列表。

### 1.2、思路

- 做一个对象（字典）mapping，存储相应的规则和值；对象的值必须用`""`包裹；
- 遍历对象（字典），与输入进行比较
- 获取该值的区间
- 用`split`将其拆分为数组；这时得到的数组元素是字符串；
- 用数组元素的整数形式作为遍历的区间
- 存储数值数组并返回。

## 二、Returns

1. `get_bingo_range("B")` should return `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]`.
2. `get_bingo_range("I")` should return `[16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]`.
3. `get_bingo_range("N")` should return `[31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]`.
4. `get_bingo_range("G")` should return `[46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]`.
5. `get_bingo_range("O")` should return `[61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]`.

## 三、Python Solution(s)

### 3.1、常规解法

```python
def get_bingo_range(letter):
    # 1. 判定输入合法性
    if not letter in ["B", "I", "N", "G", "O"]:
        return []

    # 2. 结构化存储规则
    mapping = {
        "B": "1-15",
        "I": "16-30",
        "N": "31-45",
        "G": "46-60",
        "O": "61-75"
    }

    # 3. 提取区间
    start, end = map(int, mapping[letter].split("-"))

    print(start, end)
    print(type(start), type(end))
    print(list(range(start, end + 1)))

    return list(range(start, end + 1))
get_bingo_range("B")
```

### 3.2、Pythonic

```python
def get_bingo_range_pythonic(letter):
    mapping = {
        "B": (1, 15),
        "I": (16, 30),
        "N": (31, 45),
        "G": (46, 60),
        "O": (61, 75)
    }

    start, end = mapping[letter]

    return list(range(start, end + 1))
```

## 四、JavaScript Solution(s)

### 4.1、常规解法

```js
function getBingoRange(letter){
    // 1. 结构化
    const mapping = {
        B: "1-15",
        I: "16-30",
        N: "31-45",
        G: "46-60",
        O: "61-75"
    };
    // 2. 解构赋值，取到区间的起始和结束位置
    const [start, end] = (mapping[letter].split("-"))
        .map(Number);

    // 3. 初始化结果存储
    const result = [];

    // 4. 循环
    for(let i = start; i <= end; i++){
        result.push(i);
    }

    return result;
}

```

### 4.2、Idiomatic

```js
function getBingRangeIdiomatic(letter){
    const [start, end] = {
            B: [1, 15],
            I: [16, 30],
            N: [31, 45],
            G: [46, 60],
            O: [61, 75]
          }[letter];

  return Array.from(
    { length: end - start + 1 },
    (_, i) => start + i
  );
}
```

