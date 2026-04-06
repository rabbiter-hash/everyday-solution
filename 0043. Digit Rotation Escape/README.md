# Digit Rotation Escape

Given a positive integer, determine if it, or any of its rotations, is evenly divisible by its digit count.

A rotation means to move the first digit to the end. For example, after 1 rotation, 123 becomes 231.

- Check rotation `0` (the given number) first.
- Given numbers won't contain any zeros.
- Return the first rotation number if one is found, or `"none"` if not.

## 一、题解和思路

### 1.1、题解

- 输入的必须是正整数；
- 输入的正整数中不能包含数字0；
- 判定输入不包含0的正整数和它的变体是否能整出它的位数；
- 返回第一个符合要求的数的**旋转数**，如果没有就返回`none`

### 1.2、思路

- 题目明确要求不能有0包含在数字中，所以先要处理前导0的情况；
- 将数字转成字符串，使用长度先提取数字长度的个数，d
- 生成所有旋转数：
  - 原始s
  - 旋转一次：s[1:] + s[0]
  - 旋转两次：s[2:] + s[:2]
  - 旋转k次：s[k:] + s[:k]，其中k=0....d-1
- 检查是否能被d整除
  - 将旋转后的数字转成整数`roated_num`
  - 判断`rotated_num % d == 0`
  - 如果是，直接返回这个数字，并终止循环
- 全部检查万没找到就返回none
- 时间复杂度
  - 最多检查`d`次，每次 O(d) 生成旋转 + O(1) 取模
  - 总复杂度O(d²)但 d 是数字长度，最大约 10~20，完全可以忽略不计

## 二、Returns

1. `get_rotation(123)` should return `0`.
2. `get_rotation(13579)` should return `3`.
3. `get_rotation(24681)` should return `"none"`.
4. `get_rotation(84138789345)` should return `6`.

## 三、Python Solution(s)

### 3.1、常规解法

```python
def get_rotation(n: int):
    # 1. 首先判定数字的合法性
    if not isinstance(n, int) or "0" in str(n) or n < 0:
        raise TypeError("n must be a positive integer and not contains 0")

    # 2. 将数字转成字符串并提取出长度
    str_n = str(n)
    len_n = len(str_n)

    # 3. 循环读取
    for i in range(len_n):
        # 旋转0次，就是str_n[0:] + str_n[:0]符合题意
        # 旋转1次，就是str_n[1:] + str_n[:1]
        # 边界问题，旋转range(len_n)包前不包后
        rotated_num = int(str_n[i:] + str_n[:i])
        # 判定当前被旋转的数字，是否能整除数字的长度
        if rotated_num % len_n == 0:
            return i
    return "none"
get_rotation(84138789345)
get_rotation(24681)
```

## 四、JavaScript Solution(s)

### 4.1、常规解法

```js

/* ==========================================
    第一种解法：常规解法
 ========================================== */
function getRotation(n) {
    // 1. 判定输入的合法性
    if(!Number.isInteger(n) || (n.toString()).includes("0") || n < 0){
        // 将数字n转成字符串用n.toString()
        throw new TypeError("N must be a positive integer and not contains 0");
    }

    // 2. 将数字转成字符串并提取长度
    const nStr = n.toString();
    let nLength = nStr.length;

    // 3. 开始循环
    for(let i = 0; i < nLength; i++){
        // console.log(i);
        // 旋转数字
        let rotatedNum = nStr.slice(i, nLength) + nStr.slice(0,i);
        // console.log(rotatedNum, typeof rotatedNum);
        if(rotatedNum % nLength === 0){
            // console.log(i, rotatedNum);
            return i;
        }
    }
    return "none";
}

console.log(getRotation(13579));
```

