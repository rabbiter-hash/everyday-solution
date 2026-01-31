# Letters-Numbers

Given a string containing only letters and numbers, return a new string where a hyphen (`-`) is inserted every time the string switches from a letter to a number, or a number to a letter.

## 一、Python Solution(s)

### 1.1、返回结果示例

1. `separate_letters_and_numbers("ABC123")` should return `"ABC-123"`.
2. `separate_letters_and_numbers("Route66")` should return `"Route-66`.
3. `separate_letters_and_numbers("H3LL0W0RLD")` should return `"H-3-LL-0-W-0-RLD"`.
4. `separate_letters_and_numbers("a1b2c3d4")` should return `"a-1-b-2-c-3-d-4"`.

### 1.2、解法概述

1. 正则
2. 算法味解法

### 1.3、解法

#### 1.3.1、相邻比较 + 列表

```python
# -*- encoding: utf-8 -*- 
# @Time: 2026/1/31 11:14
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

import re
def sperate_letters_and_numbers(s: str) -> str:
    if not isinstance(s, str) and not s:
        return

    # 1. 结果数组，先将第一个存入
    result = [s[0]]
    print(result) # 打印查看结果

    # 2. 循环遍历字符串，从第二个元素开始，因为第一个已经存进了result
    for i in range(1, len(s)):
        # 每一轮比较前一个元素和当前元素
        prev = s[i - 1]
        curr = s[i]
        # 判定前一个元素是不是字母
        prev_is_letter = prev.isalpha()
        # 判断当前元素是否是字母
        curr_is_letter = curr.isalpha()
        # 如果前一个元素和当前元素互斥
        if(prev_is_letter != curr_is_letter):
            # 也就是s[0]和当前元素互斥，那么前一个元素已经在结果集里，就只要追加-
            result.append("-")

        # 注意这里的写法，不能嵌套在else中，因为result.append(curr)不是条件行为，而是每一轮都应该发生的行为
        result.append(curr)
    return "".join(result)
print(sperate_letters_and_numbers("a1b2c3d4"))
```

#### 1.3.2、相邻比较 优化

```python

def sperate_letters_and_numbers_test(s: str) -> str:
    if not isinstance(s, str) or not s:
        raise ValueError('s must be a string')

    # 2. 结果集
    result = [s[0]]

    # 3. 遍历
    for i in range(1, len(s)):
        if(s[i-1].isalpha() != s[i].isalpha()):
            result.append("-")

        result.append(s[i])
    return "".join(result)
```

#### 1.3.3、函数式 + reduce

```python
from func import 
```



## 二、JavaScript Solution(s)

### 2.1、返回结果示例

1. `separateLettersAndNumbers("ABC123")` should return `"ABC-123"`.
2. `separateLettersAndNumbers("Route66")` should return `"Route-66`.
3.  `separateLettersAndNumbers("H3LL0W0RLD")` should return `"H-3-LL-0-W-0-RLD"`.
4.  `separateLettersAndNumbers("a1b2c3d4")` should return `"a-1-b-2-c-3-d-4"`.

### 2.2、解法概述

1. 正则
2. “算法味” + 字符串直接出
3. “算法味” + 数组

### 2.3、解法

#### 2.3.1、相邻比较

##### 1、相邻比较 + 字符串

```js

function separateLettersAndNumbers(str){
    if(!str) throw new TypeError("输入必须是字符串！");

    // 1. 结果集 —— string
    let result = str[0];

    // 2. 遍历，从第二个元素开始，
    for (let i=1; i<str.length; i++){
        // 取出前一个元素和当前元素进行对比
        const prev = str[i-1];
        const curr = str[i];

        // 判定前一个元素和当前元素是否为字母
        const prev_is_letter = /[a-zA-Z]/.test(prev);
        const curr_is_letter = /[a-zA-Z]/.test(curr);

        // 判定是否为同一种元素
        if(prev_is_letter !== curr_is_letter){
            result += "-";
        }
        result += curr;
    }
    return result;
}

console.log(separateLettersAndNumbers("a1b2c3d4"));
```

##### 2、相邻比较 + 数组

```js
/* 注释 #=============================================
            *** 第二种解法：数组 +
      ============================================= # */
function separateLettersAndNumbersWithArray(str) {
    // 1. 简单判定
    if(!str) throw new TypeError("请合法输入！");

    // 2. 结果集 —— 数组
    let result = [str[0]]; // 存入首字母方便比较

    // 3. 从第二个字符开始遍历
    for(let i = 1; i < str.length; i++ ){
        // 取出前一个字符和当前字符
        const prev = str[i-1];
        const curr = str[i];

        // 字母
        const prev_is_letter = /[a-zA-Z]/.test(prev);
        const curr_is_letter = /[a-zA-Z]/.test(curr);

        // 判定
        if(prev_is_letter !== curr_is_letter){
            // 说明前一个元素和当前元素不相同类型
            result.push("-");
        }

        // 正常逻辑流，
        result.push(curr);
    }
    // 4. 返回结果字符串
    return result.join("");
}

console.log(separateLettersAndNumbersWithArray("a1b2c3d4"));
```

##### 3. 相邻比较 + isNaN

#### 2.3.2、函数是+reduce

只关心上一次的结果。

```js
function separateLettersAndNumbersWithReduce(str){
    if(!str) raise new TypeError("请输入字符串！");
    
    return [...str].reduce((acc, cur) => {
        // 注意这里的at，字符串的最后一个元素用at
        // at(-1) === acc.length - 1
        if(acc && isNaN(acc.at(-1))!==isNaN(cur)){
            acc += "-";
        }
        return acc + cur;
    }, "");
}
```

**注意**：

`at()`方法：是ES2022引入的方法，适用于：`string`，`Array`，`TypedArray`。基本用法：

```js
obj.at(index)
```



