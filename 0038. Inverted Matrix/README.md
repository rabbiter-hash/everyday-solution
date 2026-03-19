# Inverted Matrix

Given a matrix (an array of arrays) filled with two distinct values, return a new matrix where all occurrences of one value are swapped with the other.

For example, given:

```js
[
  ["a", "b"],
  ["a", "a"]
]
```

Return:

```js
[
  ["b", "a"],
  ["b", "b"]
]
```

## 一、题解和思路

### 1.1、题解

- Inverted在编程类题目中通常指**逻辑反转**（比如true 变 flase），或者**值互换**，而不是几何上的旋转或镜像。
- 给定一个包含**两种**不同值的矩阵，返回一个新矩阵，其中一种值的所有出现都与另一种值交换。
- 比如如果是["a", "b"]，那么置换的结果为["b", "a"]

### 1.2、思路

- 遍历换值

## 二、Returns

1. `invert_matrix([["a", "b"], ["a", "a"]])` should return `[["b", "a"], ["b", "b"]]`.
2. `invert_matrix([[1, 0, 1], [1, 1, 1], [0, 1, 0]])` should return `[[0, 1, 0], [0, 0, 0], [1, 0, 1]]`.
3. `invert_matrix([["apple", "banana", "banana", "apple"], ["banana", "apple", "apple", "banana"], ["banana", "banana", "banana", "apple"]])` should return `[["banana", "apple", "apple", "banana"], ["apple", "banana", "banana", "apple"], ["apple", "apple", "apple", "banana"]]`.
4. `invert_matrix([[6, 7, 7, 7, 6], [7, 6, 7, 6, 7], [7, 7, 6, 7, 7], [7, 6, 7, 6, 7], [6, 7, 7, 7, 6]])` should return `[[7, 6, 6, 6, 7], [6, 7, 6, 7, 6], [6, 6, 7, 6, 6], [6, 7, 6, 7, 6], [7, 6, 6, 6, 7]]`.
5. `invert_matrix([[1.2, 2.1, 2.1, 2.1], [2.1, 1.2, 2.1, 1.2], [1.2, 1.2, 2.1, 2.1]])` should return `[[2.1, 1.2, 1.2, 1.2], [1.2, 2.1, 1.2, 2.1], [2.1, 2.1, 1.2, 1.2]]`.

## 三、Python Solution(s)

### 3.1、常规遍历换值

```python
def invert_matrix(matrix: list) -> list:
    # 1. 先找到两个值
    values = set()
    for row in matrix:
        values.update(row)

    v1, v2 = values
    print(v1, v2) # 顺序是不确定的
    # 2. 构建新矩阵并遍历
    result = []
    for row in matrix:
        # 取出矩阵中的每个列表元素，也就是行row
        # print(row)
        new_row = []
        for cell in row:
            if cell == v1:
                new_row.append(v2)
            else:
                new_row.append(v1)
        result.append(new_row)
    print(result)
    return result
invert_matrix([["a", "b"], ["a", "a"]])
```



## 四、JavaScript Solution(s)

### 4.1、常规遍历换值

```js
function invertMatrix(matrix) {
    // 1. 找到两个值
    const values = new Set();
    matrix.forEach(row => {
        row.forEach(cell => {
            values.add(cell);
        })
    });
    console.log(values); //Set(2) { 'a', 'b' }

    const [v1, v2] = [...values];
    console.log(v1, v2);

    // 2. 构建新矩阵
    return matrix.map(row => row.map(cell => (cell === v1 ? v2 : v1)));
}

console.log(invertMatrix([["a", "b"], ["a", "a"]]));
```

