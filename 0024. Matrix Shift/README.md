# Matrix Shift

Given a matrix (array of arrays) of numbers and an integer, shift all values in the matrix by the given amount.

- A positive shift moves values to the right.
- A negative shift moves values to the left.

Values should wrap:

- Treat the matrix as one continuous sequence of values.
- When a value moves past the end of a row, it continues at the beginning of the next row.
- When a value moves past the last position in the matrix, it wraps to the first position.
- The same applies in reverse when shifting left.

For example, given:

```js
[
  [1, 2, 3],
  [4, 5, 6]
]
```

with a shift of `1`, move all the numbers to the right one:

```js
[
  [6, 1, 2],
  [3, 4, 5]
]
```

## 一、Returns

1. `shiftMatrix([[1, 2, 3], [4, 5, 6]], 1)` should return `[[6, 1, 2], [3, 4, 5]]`.
2.  `shiftMatrix([[1, 2, 3], [4, 5, 6]], -1)` should return `[[2, 3, 4], [5, 6, 1]]`.
3. `shiftMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5)` should return `[[5, 6, 7], [8, 9, 1], [2, 3, 4]]`.
4. `shiftMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -6)` should return `[[7, 8, 9], [1, 2, 3], [4, 5, 6]]`.
5. `shiftMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 7)` should return `[[10, 11, 12, 13], [14, 15, 16, 1], [2, 3, 4, 5], [6, 7, 8, 9]]`.
6. `shiftMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], -54)` should return `[[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 1, 2], [3, 4, 5, 6]]`.

## 二、解法、思路和坑

### 2.1. 题解

- shift为正：向右移动
- shift为负：向左移动
- 形状保持不变；
- 超出部分循环（wrap）
- **重**：Treat the matrix as one continuous sequence of values.也就是要将多维数组，拆解成一维，然后做整体shift。

### 2.2、思路

#### 2.2.1、记录原始形状

```plsql
rows = len(matrix)
cols = len(matrix[0])
```

总长度：

```plsql
n = rows * cols
```

#### 2.2.2、展开成一维数组

```plsql
[
    [1, 2, 3],
    [4, 5, 6]
]
```

变成：

```plsql
[1, 2, 3, 4, 5, 6]
```

这一步的时间复杂度是 `O(n)`

#### 2.2.3、处理shift

非常关键：

```plsql
effective_shift = shift % n
```

取模的必须性：

- shift = 1 -> 移动1
- shift = 7 -> 如果是2行3列的二维数组，长度为6，等同于移动1
- shift = -1 -> 也可以通过%统一处理。
- 避免越界

#### 2.2.4、做循环移动

右移k位的核心公式：

```plsql
new_array = arr[-k:] + arr[:-k]
```

例如：

```plsql
[1, 2, 3, 4, 5, 6]
k = 1
arr[-1:] -> [6]
arr[:-1] -> [1, 2, 3, 4, 5]
# 结果
[6, 1, 2, 3, 4, 5]
```

#### 2.2.5、还原成二维数组

按照原来的rows和cols进行切片

```plsql
[
    new_array[0: 3],
    new_array[3: 6]
]
```

得到：

```python
[
    [6, 1, 2],
    [3, 4, 5]
]
```



## 三、Solution(s)

### 3.1、Python Solution(s)

#### 3.1.1、展开 ->  移动 -> 还原

用到的函数`extend`

```python
def matrix_shift(matrix, shift):
    # 1. 判定数据合法性
    if not isinstance(matrix, list):
        raise TypeError("Matrix must be a list!")
    if not isintance(shift, int):
        raise TypeError("Shift must be an integer!")
    # 2. 获取数组的行列信息
    # 行数
    rows = len(matrix)
    # 列数
    cols = len(matrix[0])
    # 总长度
    n = rows * cols
    # 3. 展开为一维数组
    flat = []
    for row in matrix:
        flat.extend(row)
    # 4. 处理shift（防止超过长度）
    shift = shift % n # 取模可以防止越界
    # 5. 右移shift位
    if shift != 0:
        flat = flat[-shift:] + flat[:-shift]
    # 6. 还原成二维数组
    result = []
    for i in range(rows):
        start = i * cols
        end = start + cols
        result.append(flat[start:end])
    return result
```

### 3.2、JavaScript Solution(s)

#### 3.2.1、标准解法

```js
function shiftMatrix(matrix, shift){
    // 1. 判定数据输入是否合法
    if(!Array.isArray(matrix)){
        throw new Error("Matrix必须是数组！");
    }
    if(!Number.isInteger(shift)){
        throw new Error("Shift必须是整数！");
    }
    // 2. 统计数组信息
    // 行数
    const matrixRows = matrix.length;
    // 列数
    const matrixCols = matrix[0].length;
    // 总长度
    const matrixLength = matrixRows * matrixCols;
    // 3. 扁平化数组
    const flattenMatrix = matrix.flat();
    console.log(flattenMatrix);
    // 4. 处理偏移量，让它不超出边界以及能处理负数
    shift = ((shift % matrixLength) + matrixLength) % matrixLength;
    // 5. 根据偏移量返回新数组
    const shiftedFlattenArray = flattenMatrix.slice(-shift).concat(flattenMatrix.slice(0, -shift));
    console.log(shiftedFlattenArray);
    // 6. 还原成初始数组形状
    const result = [];
    for(let i = 0; i < matrixRows; i++){
        // 直接拼接
        result.push(shiftedFlattenArray.slice(i * matrixCols, (i + 1) * matrixCols));
    }
    
    return result;
}
```

需要注意的是：

> ```js
> shift = ((shift % n) + n) % n;
> ```
>
> 这一行处理shift的代码，它能支持负数。
>
> 这样写的原因：
>
> 在js中：
>
> ```js
> -2 % 6 = -2;
> ```
>
> 而python中：
>
> ```python
> -2 % 6 = 4;
> ```
>
> 