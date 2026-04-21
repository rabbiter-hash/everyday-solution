# Acronym Finder

Given a string representing an acronym, return the full name of the organization it belongs to from the list below:

- `"National Avocado Storage Authority"`
- `"Cats Infiltration Agency"`
- `"Fluffy Beanbag Inspectors"`
- `"Department Of Jelly"`
- `"Wild Honey Organization"`
- `"Eating Pancakes Administration"`

Each letter in the given acronym should match the first letter of each word in the organization it belongs to, in the same order.

## 一、题解和思路

### 1.1、题解

- 输入简写的大写的字符串，返回字符串的全称
- Each letter in the given acronym should match the first letter of each word
- 不能硬编码写死
- 通过计算进行匹配

### 1.2、思路

- 将所有Organizations编成数组；
- 遍历数组，并计算出每个元素的简写；
- 通过与输入进行对比，如果输入的简写与算出来的元素的简写匹配，就返回全称organization。

## 二、 Returns

1. `find_org("NASA")` should return `"National Avocado Storage Authority"`.
2. `find_org("CIA")` should return `"Cats Infiltration Agency"`.
3. `find_org("FBI")` should return `"Fluffy Beanbag Inspectors"`.
4. `find_org("DOJ")` should return `"Department Of Jelly"`.
5. `find_org("WHO")` should return `"Wild Honey Organization"`.
6. `find_org("EPA")` should return `"Eating Pancakes Administration"`.

## 三、Python Solution(s)

### 3.1、常规解法

```python
# -*- encoding: utf-8 -*- 
# @Time: 2026/4/20 15:43
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)


def find_org(acronym):
    # 1. 将所有的organizations存储成列表
    organizations = [
        "National Avocado Storage Authority",
        "Cats Infiltration Agency",
        "Fluffy Beanbag Inspectors",
        "Department Of Jelly",
        "Wild Honey Organization",
        "Eating Pancakes Administration"
    ]

    # 2. 循环遍历并拼接organizations的简写
    for org in organizations:
        # 3. 初始化拼接
        initials = ""

        # 4. 提取org中的单词并提取首字母进行拼接
        all_words = org.split(" ")

        # 5. 每次循环取每个单词的首字母大写进行拼接
        for word in all_words:
            initials += word[0].upper()
        if(initials == acronym):
            return org
    return None

find_org("NASA")
```

##  四、JavaScript Solution(s)

### 4.1、常规解法

```js

function findOrg(acronym){
    // 1. 将所有organizations存储抽成数组
    let organizations = [
        "National Avocado Storage Authority",
        "Cats Infiltration Agency",
        "Fluffy Beanbag Inspectors",
        "Department Of Jelly",
        "Wild Honey Organization",
        "Eating Pancakes Administration"
    ];

    // 2. 循环遍历
    for(let org of organizations){
        // console.log(org);
        // 3. 初始化存储字符串
        let initials = "";

        // 4. org中的单词列表
        let wordsArr = org.split(" ");
        console.log(wordsArr);
        // 5. 取每个列表中每个元素的首字母进行拼接
        for(let ch of wordsArr){
            console.log(ch);
            initials += ch[0].toUpperCase();
            if(initials === acronym){
                return org;
            }
        }
    }
    return null;
}

findOrg("NASA");
```





