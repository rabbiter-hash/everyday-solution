# Transposed Matrix

Given a matrix (an array of arrays), return the transposed version of it.

To transpose the matrix, swap the rows and columns. E.g: a value at index `[0, 1]` should move to index `[1, 0]`.

For example, given:

```json
[
  [1, 2, 3],
  [4, 5, 6]
]
```

Return:

```json
[
  [1, 4],
  [2, 5],
  [3, 6]
]
```

## 一、题解和思路

### 1.1、题解

输入一个二维数组，输出一个转置后的数组。

### 1.2、思路

- 得到原矩阵的行数`rows`和列数`cols`

  - rows = len(matrix)
  - cols = len(matrix[0])

- 初始化一个新矩阵`transposed`，大小为 `cols x rows`

- 遍历原矩阵

  ```python
  for i in range(rows):
      for j in range(cols):
          transposed[j][i] = matrix[i][j]
  ```

  这里的行和列是互换的。

- 返回`transposed`

## 二、Returns

- `transpose([[1, 2, 3], [4, 5, 6]])` should return `[[1, 4], [2, 5], [3, 6]]`.
- `transpose([[1, 2], [3, 4], [5, 6]])` should return `[[1, 3, 5], [2, 4, 6]]`.
- `transpose([[1, 2], [3, 4], [5, 6], [7, 8]])` should return `[[1, 3, 5, 7], [2, 4, 6, 8]]`.
- `transpose([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"]])` should return `[["a", "d", "g", "j"], ["b", "e", "h", "k"], ["c", "f", "i", "l"]]`.
- `transpose([[True, False, True, False], [False, True, False, True], [True, True, False, False], [False, False, True, True], [True, False, False, True]])` should return `[[True, False, True, False, True], [False, True, True, False, False], [True, False, False, True, False], [False, True, False, True, True]]`.

## 三、Python Solution(s)

### 3.1、常规解法

```python
def transpose(matrix):
    # 1. 空矩阵处理
    if not matrix:
        return []

    # 2. 获取矩阵的行和列，假设列的长度是一样的
    len_row = len(matrix)
    len_col = len(matrix[0])

    # 3. 初始化一个矩阵
    transposed = [[0] * len_row for _ in range(len_col)]

    print(transposed)

    # 4. 遍历
    for i in range(len_row):
        for j in range(len_col):
            transposed[j][i] = matrix[i][j]

    print(transposed)
    return transposed

transpose([
    [1, 2, 3],
    [4, 5, 6]])

```

### 3.2、Pythonic

```python
def transpose_pythonic(matrix):
    return [list(row) for row in zip(*matrix)]
```

## 四、JavaScript Solution(s)

### 4.1、常规解法

```js
function transpose(matrix){
    // 1. 空矩阵处理
    if(matrix.length === 0) return [];

    // 2. 获取矩阵的行和列，假设列的长度是一样的
    const lenRow = matrix.length;
    const lenCol = matrix[0].length;

    console.log(lenRow);
    console.log(lenCol);

    // 3. 初始化一个矩阵
    const transposeArray = Array.from({length: lenCol}, () => Array.from(lenRow));

    console.log(transposeArray);
    // 4. 开始遍历
    for(let i = 0; i < lenRow; i++){
        for(let j = 0; j < lenCol; j++){
            transposeArray[j][i] = matrix[i][j];
        }
    }
    console.log(transposeArray);
    return transposeArray;
}

transpose([[1, 2, 3], [4, 5, 6]])
```

### 4.2、Idiomatic

```js
function tranposeIdiomatic(matrix) {
    return matrix[0].map((_, colIndex) => {
        return matrix.map(row => row[colIndex]);
    });
}
```

