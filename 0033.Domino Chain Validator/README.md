# Domino Chain Validator

Given a 2D array representing a sequence of dominoes, determine whether it forms a valid chain.

- Each element in the array represents a domino and will be an array of two numbers from 1 to 6, (inclusive).
- For the chain to be valid, the second number of each domino must match the first number of the next domino.
- The first number of the first domino and the last number of the last domino don't need to match anything.

## 一、题解和思路

> 多米诺骨牌。一种古老的益智游戏，也是观赏性极佳的**连锁反应艺术**。起源于宋代，传到欧洲后演变成全球版本。

### 1.1、题解

- 二维数组，数组中的每个元素是一个由0-6组成的数组；
- 数组中的每个数组元素的右边元素要等于左边元素，
- 第一个元素的左边不用匹配，最后一个元素的右边不用匹配（The first number of the first domino and the last number of the last domino don't need to match anything.）

### 1.2、思路

- 循环遍历二维数组
- 将每个元素的右边元素和下一个的左边元素进行比较
- 二位数组中的每个元素都只有两个元素，也就是前一个元素的[1]去和下一个元素的[0]进行比较

## 二、Returns

1. `is_valid_domino_chain([[1, 3], [3, 6], [6, 5]])` should return `True`.
2. `is_valid_domino_chain([[6, 2], [3, 4], [4, 1]])` should return `False`.
3. `is_valid_domino_chain([[2, 5], [5, 6], [5, 1]])` should return `False`.
4. `is_valid_domino_chain([[4, 3], [3, 1], [1, 6], [6, 6], [6, 5], [5, 1], [1, 1], [1, 4], [4, 4], [4, 2]])` should return `True`.
5. `is_valid_domino_chain([[2, 3], [3, 3], [3, 6], [6, 1], [1, 4], [3, 5], [5, 5], [5, 4], [4, 2], [2, 2]])` should return `False`.

## 三、Python Solution(s)

### 3.1、循环遍历法

```python
def is_valid_domino_chain_with_for(dominoes):
    # 1. 判定数据的合法性
    # 1.1。 输入必须是数组
    if not isinstance(dominoes, list):
        raise TypeError("dominoes must be a list")
    # 1.2. 判定数字是否在1-6之间
    for domino in dominoes:
        if not isinstance(domino, list):
            raise TypeError("domino must be a list")
        # 检查内层数组的长度
        if(len(domino) != 2):
            raise ValueError("domino must have 2 elements")
        for d in domino:
            if not isinstance(d, int) or not (1 <= d <= 6):
                raise ValueError("domino must be an integer between 1 and 6")
    # 2. 空数组和一个元素的二维数组应该return True，因为没有违反规则
    if len(dominoes) <= 1:
        return True

    # 3. 循环
    for i in range(len(dominoes) - 1):
        if(dominoes[i][1] != dominoes[i+1][0]):
            return False

    return True

# print(is_valid_domino_chain_with_for([[1, 3], [3, 6], [6, 5]]))
```

### 3.2、循环遍历 + 手动取值

```python
def is_valid_domino_chain_mannual_var(dominoes):
    # 1. 判定数据的合法性
    # 1.1. 输入必须是数组
    if not isinstance(dominoes, list):
        raise TypeError("dominoes must be a list")
    # 1.2. 内层数组判定，长度，和值的合法性
    for domino in dominoes:
        if not isinstance(domino, list):
            raise TypeError("domino must be a list")
        # 判定内层数组的长度
        if(len(domino) != 2):
            raise ValueError("domino must have 2 elements")

        # 内层数组的元素值必须在1-6之间
        for d in domino:
            if not isinstance(d, int) or not (1 <= d <= 6):
                raise ValueError("domino must be an integer between 1 and 6")

    # 2. 特殊情况，空数组和一个元素的二维数组应该返回True，因为没有违反规则
    if len(dominoes) <= 1:
        return True

    # 3. 循环 + 手动取变量
    for i in range(len(dominoes) - 1):
        # 必须-1，以防超出边界
        current = dominoes[i]
        next = dominoes[i+1]

        right = current[1]
        left = next[0]
        if(right != left):
            return False

    return True
```

### 3.3、zip

```python
def is_valid_domino_chain_with_zip(dominoes):
    # 1. 判定数据的合法性
    # 1.1. 输入必须是数组
    if not isinstance(dominoes, list):
        raise TypeError("dominoes must be a list")
    # 1.2. 内层数组判定，长度，和值的合法性
    for domino in dominoes:
        if not isinstance(domino, list):
            raise TypeError("domino must be a list")
        # 判定内层数组的长度
        if (len(domino) != 2):
            raise ValueError("domino must have 2 elements")

        # 内层数组的元素值必须在1-6之间
        for d in domino:
            if not isinstance(d, int) or not (1 <= d <= 6):
                raise ValueError("domino must be an integer between 1 and 6")

    # 2. 特殊情况，空数组和一个元素的二维数组应该返回True，因为没有违反规则
    if len(dominoes) <= 1:
        return True

    # 3. 循环遍历 + zip
    for a, b in zip(dominoes, dominoes[1:]):
        print(a, b)
        if(a[1] != b[0]):
            return False
    return True

# is_valid_domino_chain_with_zip([[1, 3], [3, 6], [6, 5]])
```

### 3.3、all函数

```python
def is_valid_domino_chain_with_all(dominoes):
    return all(a[1] == b[0] for a, b in zip(dominoes, dominoes[1:]))
```

## 四、JavaScript Solution(s)

### 4.1、循环遍历

```js
function isValidDominoChain(dominoes){
    /*
    * @params: dominoes
    * @returns: true or false
    * @methods: use for directly
    * */
    // 1. Input check
    // 1.1. The Value of input must be an array
    if(!Array.isArray(dominoes)){
        throw new Error("Input value must be an array!")
    }
    // 1.2. Inner Array check
    for(let domino of dominoes){
        if(!Array.isArray(domino)){
            throw new Error("Inner element must be an array!");
        }
        // check the inner element's length
        if(domino.length !== 2){
            throw new Error("Inner array length must be 2")
        }
        // check the inner array's element is integer
        for(let d of domino){
            if(!Number.isInteger(d) || (d < 1 && d > 6)){
                throw new Error("Inner arrays' elements' must be integer!");
            }
        }
    }

    // 2. Use for loop to check the value
    for(let i = 0; i < dominoes.length - 1; i++){
        // The behavior -1 is a must have.
        if(dominoes[i][1] !== dominoes[i+1][0]){
            return false;
        }
    }
    return true;
}
isValidDominoChain([[1, 3], [3, 6], [6, 5]])
```

### 4.2、every函数

```js
function isValidDominoChainWithEvery(dominoes){
    return dominoes.every((domino, i) =>
        // domino是当前骨牌，而下一骨牌是dominoes[i+1]
        i === dominoes.length - 1 || domino[1] === dominoes[i+1][0]
    )
}
isValidDominoChainWithEvery([[1, 3], [3, 6], [6, 5]])

```

### 4.3、slice + every

```js
function isValidDominoChainWithSlicePlusEvery(dominoes){
    return dominoes
        .slice(0, -1)
        .every((domino, i) => domino[1] === dominoes[i+1][0]);
}
isValidDominoChainWithSlicePlusEvery([[1, 3], [3, 6], [6, 5]])
```

