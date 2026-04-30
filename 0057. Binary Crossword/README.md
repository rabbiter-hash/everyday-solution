# Binary Crossword

Given a character, determine if its 8-bit binary representation can be found in the following grid, horizontally or vertically in either direction:

```js
0 1 0 0 0 0 0 1
0 1 1 0 1 1 1 1
0 1 0 0 0 1 0 0
0 1 1 0 0 1 0 1
0 1 0 1 0 0 1 0
0 1 0 1 0 1 0 0
0 1 1 0 1 0 0 0
1 0 1 0 1 1 1 0
```

For example, `"A"` has the binary representation `01000001`, which appears in the first row from left to right.

## 一、题解和思路

### 1.1、题解

输入一个字母，计算它的`8位二进制值`，然后查找给出的二维矩阵中的行和列查找是否有完全匹配的值，方向上是从左到右从右到左以及从上到下或者从下到上，如果有就返回true，否则返回false。

### 1.2、思路

- 先建立二维矩阵
- 将字母转成`8位二进制`；
- 嵌套循环矩阵的值，看是否和转成的`8位二进制`相等，

## 二、Returns

1. `isInCrossword("I")` should return `true`.
2. `isInCrossword("D")` should return `true`.
3. `isInCrossword("0")` should return `true`.
4. `isInCrossword("u")` should return `true`.
5. `isInCrossword("Y")` should return `false`.
6. `isInCrossword("p")` should return `false`.
7. `isInCrossword("1")` should return `false`.
8. `isInCrossword("Q")` should return `false`.

## 三、Python Solution(s)

### 3.1、常规解法

```python
def is_in_crossword(char):

    # 1. 定义矩阵
    grid = [
        [0, 1, 0, 0, 0, 0, 0, 1],
        [0, 1, 1, 0, 1, 1, 1, 1],
        [0, 1, 0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 0]
    ]

    # 2. 使用format + ord取得字母的八位二进制
    target = format(ord(char), "08b")

    print(target)
    print(type(target)) # str

    # 3. 先循环二维矩阵的行
    for row in grid:
        # print(row) # list
        row_str = "".join(map(str, row))
        if row_str == target or row_str[::-1] == target:
            return True

    # 4. 循环取每一列的值
    for col in range(len(grid[0])):
        # 要先固定列的值
        # 定义列上的字符串
        col_str = ""
        for row in range(len(grid)):
            col_str += str(grid[row][col])
            # 取值
            # grid[0][0],grid[1][0],grid[2][0]....
        # 取完所有值再进行比较
        if(col_str == target or col_str[::-1] == target):
            return True
    return False
print(is_in_crossword("Q"))
```

##  四、JavaScript Solution(s)

```js

function isInCrossword(char){
    // 1. 矩阵
    const grid = [
            [0, 1, 0, 0, 0, 0, 0, 1],
            [0, 1, 1, 0, 1, 1, 1, 1],
            [0, 1, 0, 0, 0, 1, 0, 0],
            [0, 1, 1, 0, 0, 1, 0, 1],
            [0, 1, 0, 1, 0, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0],
            [1, 0, 1, 0, 1, 1, 1, 0]
    ];

    // 2. 字符八位二进制
    const target = char.charCodeAt(0).toString(2).padStart(8, "0");
    /*
        说明：
        1. charCodeAt(0)：获取字符的Unicode码点，类似python的ord
            "a".charCodeAt(0) = 97
        2. toString(2)：将数字转换成二进制字符串；
            97.toString(2) = "1100001"（注意：没有前导0）
        3. padStart(8, "0")：在字符串开头补0，确保长度至少为8位
            "1100001".padStart(8, '0') → "01100001"
     */
    console.log(target, target.length);

    // 3. 横向循环矩阵，取row跟目标对比
    for(let i = 0; i < grid.length; i++){
        // console.log(grid[i]); // array
        const row = grid[i];
        const rowStr = row.join("");
        // console.log(rowStr);
        // console.log(typeof rowStr); //string
        if(
            rowStr === target ||
            rowStr.split("").reverse().join("") === target
        ) return true;
    }

    console.log("开始纵向循环准备！");
    // 4. 纵向循环，纵向循环先要固定列的位置，然后去取行的值
    // console.log(grid);
    for(let p = 0; p < grid.length; p++){
        // 先固定列数的值，然后去取行的值
        let colStr = "";
        for(let q = 0; q < grid.length; q++){
            colStr += grid[q][p];
            // console.log(colStr);
        }
        console.log(colStr);
        // 5. 等构造出完整八位字符串再去比较
        if(
                colStr === target ||
                colStr.split("").reverse().join("") === target
            ) return true;
    }
    return false;
}

isInCrossword("abc");
```

## 五、注意纵向读取的本质

### 5.1、第0列

```0
0
0
0
0
0
0
1
```

拼接起来才是：00000001

### 5.2、第1列

```1
1
1
1
1
1
1
0
```

拼接起来：11111110

### 5.3、行和列的本质

#### 5.3.1、横向

```tex
→ → →
→ → →
→ → →
```

#### 5.3.2、纵向

```tex
↓ ↓ ↓
↓ ↓ ↓
↓ ↓ ↓
```

横向要固定行，纵向要固定列。

### 5.4、取第0列

应该是：

- col固定为0，也就是二维表格中的第一个元素；
- row：二维表格纵向数，应该是从0-7；

```tex
grid[0][0]
grid[1][0]
grid[2][0]
grid[3][0]
...
```

