# Name Initials

Given a full name as a string, return their initials.

- Names to initialize are separated by a space.
- Initials should be made uppercase.
- Initials should be separated by dots.

For example, `"Tommy Millwood"` returns `"T.M."`.

## 一、题解和思路

### 1.1、题解

- 输入名字字符串，返回他们的缩写；
- 输入的名字以空格分隔；
- 返回的缩写应该全部是大写；
- 缩写的名字要用`.`分开；
- 在缩写的名字最后也要有`.`

### 1.2、思路

- 空格分割字符串，得到名字的每个单词的列表；
- 遍历列表，取每个单词的第一个元素；
- 拼接结果，每个字母后面加`.`；

## 二、Returns

1. `get_initials("Tommy Millwood")` should return `"T.M."`.
2. `get_initials("Savanna Puddlesplash")` should return `"S.P."`.
3. `get_initials("Frances Cowell Conrad")` should return `"F.C.C."`.
4. `get_initials("Dragon")` should return `"D."`.
5. `get_initials("Dorothy Vera Clump Haverstock Norris")` should return `"D.V.C.H.N."`.

## 三、Python Solution(s)

### 3.1、常规解法

```python
# -*- encoding: utf-8 -*- 
# @Time: 2026/4/17 14:17
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)


def get_initials(name):
    # 1. 判定输入是否合法
    if not isinstance(name, str):
        raise TypeError('name must be a string')

    # 2. 以空格拆分字符串
    name_words = name.split()

    # 3. 初始化存储结果
    names_initials = []
    for name_word in name_words:
        names_initials.append(name_word[0].upper())

    return ".".join(names_initials) + "."
```

### 3.2、一句话版本

```python
def get_initials_one(name):
    # 一句话代码
    return ".".join(word[0].uppper() for word in name.split("")) + "."
```



## 四、JavaScript Solution(s)

### 4.1、常规

```js

function getInitials(name){
    // 1. 判定数据是否合法
    if(typeof name !== "string"){
        throw new Error("输入必须是字符串！");
    }

    // 2. 以空格拆分字符串
    // const nameWords = name.split(" ");
    // 2. js强调用户输入，所以需要用trim()处理两边，并处理多空格问题
    const nameWords = name.trim().split(/\s+/);

    // 3. 初始化存储结果
    let nameInitials = [];

    // 4. 开始遍历，并取每个单次的首个字母的大写
    for(let i = 0; i < nameWords.length; i++){
        nameInitials.push(nameWords[i][0].toUpperCase());
    }
    // console.log(nameInitials.join(".") + ".");
    return nameInitials.join(".") + ".";
}

getInitials("Dorothy Vera Clump Haverstock Norris")


```

### 4.2、一句话版本

```js
function getInitialsSimple(name){
    return name
        .trim()
        .split(/\s+/)
        .map(word => word[0].toUpperCase())
        .join(".") + ".";
}
```

