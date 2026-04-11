# Rook Attack

Given two strings for the location of two rooks on a chess board, determine if they can attack each other.

A standard chessboard is 8x8, with columns labeled `A` through `H` (left to right) and rows labeled `1` through `8` (bottom to top). It looks like this:

| **A8** | **B8** | **C8** | **D8** | **E8** | **F8** | **G8** | **H8** |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| **A7** | **B7** | **C7** | **D7** | **E7** | **F7** | **G7** | **H7** |
| **A6** | **B6** | **C6** | **D6** | **E6** | **F6** | **G6** | **H6** |
| **A5** | **B5** | **C5** | **D5** | **E5** | **F5** | **G5** | **H5** |
| **A4** | **B4** | **C4** | **D4** | **E4** | **F4** | **G4** | **H4** |
| **A3** | **B3** | **C3** | **D3** | **E3** | **F3** | **G3** | **H3** |
| **A2** | **B2** | **C2** | **D2** | **E2** | **F2** | **G2** | **H2** |
| **A1** | **B1** | **C1** | **D1** | **E1** | **F1** | **G1** | **H1** |

Rooks can move as many squares as they want in a horizontal or vertical direction. So if they are on the same row or column, they can attack each other.

## 一、题解和思路

### 1.1、题解

国际象棋棋盘两个在同一条直线上的棋子可以相互攻击，也就是在行或者列上的棋子。列的数为：A-H，行的数为8-1。

### 1.2、思路

- 判定给出的两个棋子是否在同一行或者同一列
- 在同一行或者同一列，就返回True
- 否则返回false

### 1.3、步骤拆解

- 拆分坐标
  - "A1" -> 列="A"， 行="1"；
- 比较列
  - 如果列相同 -> 同一列 -> 可攻击
- 比较行
  - 如果行相同 -> 同一行 -> 可攻击

## 二、Returns

1. `rook_attack("A1", "A8")` should return `True`.
2. `rookAttack("B4", "F4")` should return `true`.
3. `rookAttack("E3", "D4")` should return `false`.
4. `rookAttack("H7", "F6")` should return `false`.

## 三、Python Solution(s)

### 3.1、常规解法

```python
def rook_attack(rook1, rook2):
    # 1. 判定数据是否合法
    if not isinstance(rook1, str) \
        or not isinstance(rook2, str) \
        or (len(rook1) != 2 or len(rook2) != 2):
        raise TypeError("The Inputs must str and all length should be 2")

    # 2. 拆解字符串
    col1, row1 = rook1[0], rook1[1]
    col2, row2 = rook2[0], rook2[1]

    return col1 == col2 or row1 == row2

```

### 3.2、一行代码

```python
def rook_attack_single(rook1, rook2):
    return rook1[0] == rook2[0] or rook1[1] == rook2[1]
```

### 3.3、zip

```python
def rook_attack_zip(rook1, rook2):
    return any(a == b for a, b in zip(rook1, rook2))
    # 相当于
    # for a, b in zip(rook1, rook2):
    #     if a == b:
    #         return True
    # return Flase
```

## 四、JavaScript Solution(s)

### 4.1、常规解法

```js
function rookAttack(rook1, rook2) {
    // 1. 首先还是做数据判定
    if(typeof rook1 !== "string" || typeof rook2 !== "string") {
        throw new TypeError("输入必须是字符串！");
    }

    if(rook1.length !== 2 || rook2.length !== 2){
        throw new Error("字符串长度必须为2！");
    }

    const col1 = rook1[0];
    const row1 = rook1[1];

    const col2 = rook[0];
    const row2 = rook2[1];

    return col1 === col2 || row1 === row2;
}
```

### 4.2、一行解法

```js
function rookAttackSingle(rook1, rook2){
    return rook1[0] === rook2[0] || rook1[1] === rook2[1];
}
```

### 4.3、解构赋值

```js
function rookAttackDeconstruction(rook1, rook2){
    const [c1, r1] = rook1;
    console.log(c1);
    console.log(r1);
    const [c2, r2] = rook2;

    return c1 === c2 || r1 === r2;
}
```

### 4.4、some函数

```js
function rookAttackSome(rook1, rook2){
    return [...roo1].some((ch, i) => ch === rook2[i]);
}
```

