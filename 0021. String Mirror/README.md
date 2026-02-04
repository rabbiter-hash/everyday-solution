# String Mirror

Given a string, return a new string that consists of the given string with a reversed copy of itself appended to the end of it.

## 一、Returns

1. `mirror("freeCodeCamp")` should return `"freeCodeCamppmaCedoCeerf"`.
2.  `mirror("RaceCar")` should return `"RaceCarraCecaR"`.
3. `mirror("helloworld")` should return `"helloworlddlrowolleh"`.
4.  `mirror("The quick brown fox...")` should return `"The quick brown fox......xof nworb kciuq ehT"`.

## 二、解法和思路

### 2.1、Python

1. 使用函数`reverse()`原地反转
2. 字符串切片
3. reversed()

### 2.2、JavaScript

## 三、解法

### 3.1、Python Solution(s)

#### 3.1.1、reverse()原地修改列表再拼接

```python
""" =====================================================
    *** 第一种解法：转成列表再原地翻转再拼接
===================================================== """
def mirror(s: str) -> str:
    # 1. 判定数据类型
    if not isinstance(s, str):
        raise TypeError('s is not a string')

    # 2. 拆解字符串
    str_list = list(s)
    # str_list = [item for item in s]
    # 3. 拷贝列表
    str_list_copy = str_list[:]

    # 4. 翻转拷贝列表
    str_list_copy.reverse()

    # 5. 扩展列表
    str_list.extend(str_list_copy)
    print(str_list)
    return ''.join(str_list)

mirror("freeCodeCamp")
```

#### 3.1.2、字符串切片

```python
""" =====================================================
    *** 第二种解法：使用字符串切片
===================================================== """
def mirror_with_slice(s: str) -> str:
    # 1. 判定数据
    if not isinstance(s, str):
        raise TypeError('s is not a string')

    # 2. 字符串切片
    return s + s[::-1]
```

#### 3.1.3、使用reversed()函数

```python

""" =====================================================
    *** 第三种解法：转成列表再原地翻转再拼接
===================================================== """
def mirror_with_reversed(s: str) -> str:
    if not isinstance(s, str):
        raise TypeError('s is not a string')
    # print(list(reversed(s)))
    return s + "".join(reversed(s))
mirror_with_reversed("freeCodeCamp")
```

#### 3.1.4、简化3.1.1的解法

```python
""" =====================================================
    *** 第四种解法：简化第一种方法的解法
===================================================== """
def simple_mirror(s: str) -> str:
    # 1. 判定数据类型是否合法
    if not isinstance(s, str):
        raise TypeError('s is not a string')
    # 2.
    chars = list(s)
    return "".join(chars + chars[::-1])
```

### 3.2、JavaScript Solution(s)

#### 3.2.1、对应python写法1

```js
/* ==========================================
    第一种解法：字符串->数组->字符串
 ========================================== */
function mirror(str) {
    // 1. 字符窜 -> 数组
    let arr = [];
    for(let i=0; i<str.length; i++){
        // console.log(i + "======>" + str[i]); // 主要查看边界
        arr.push(str[i]);
    }
    console.log(arr);

    // 2. 拷贝一份数组
    let reversedArr = arr.slice();
    console.log("没有反转之前： ", reversedArr);
    console.log("是否是同一个数组：", arr === reversedArr);

    // 3. 原地反转
    reversedArr.reverse();
    console.log("反转后的数组：", reversedArr);

    // 4. 拼接反转后的数组到原数组arr
    arr.push(...reversedArr);
    console.log("拼接后的数组：",arr); // 等价于python的extend

    // 5. 拼接字符串
    return arr.join("");
}

mirror("freeCodeCamp");
```

#### 3.2.2、简化1解法

```js
/* ==========================================
    第二种解法：简化方法1
 ========================================== */
function simpleMirror(str){
    // 1. 转成数组
    let arr = str.split("");
    console.log(arr);
    // 2. 反转数组
    let reversedArr = arr.slice().reverse();
    console.log(reversedArr);

    // 3. 查看数据
    console.log(arr === reversedArr);

    // 4. 拼接数组
    arr.push(...reversedArr);

    // 5. 返回
    return arr.join("");
}
simpleMirror("freeCodeCamp");
```

#### 3.2.3、split + reverse

```js
function mirrorSplitReverse(str){
    return str + str.split("").reverse().join("");
}
```

#### 3.2.4、“不可变”（不修改任何中间数组）

```js
/* ==========================================
    第四种解法： 完全不可变，不改变任何中间数组
 ========================================== */
function mirrorStand(str) {
    // 1. 用const定义数组
    const arr = str.split("");
    console.log(arr);
    // 2. 反转数组也用const
    const reversedArr = [...arr].reverse();
    console.log(reversedArr);

    // 3. 拼接
    return [...arr, ...reversedArr].join("");
}
```

#### 3.2.5、reduce

