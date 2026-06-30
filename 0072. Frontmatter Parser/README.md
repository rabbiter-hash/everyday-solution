# Frontmatter Parser

Given a string representing a frontmatter block, parse it and return an object (JavaScript) or dictionary (Python) with the keys and values.

Frontmatter is wrapped in `---` delimiters and contains `key: value` pairs within them, one per line. For example:

```md
---
title: My Post
draft: false
views: 100
---
```

Should return:

```js
{
  title: "My Post",
  draft: false,
  views: 100
}
```

- Numbers, Booleans, and Strings should all be returned as their respective type.
- The given string will have new lines separated with the newline character (`"\n"`). The above example would be given as: `"---\ntitle: My Post\ndraft: false\nviews: 100\n---"`.

## 一、题解和思路

### 1.1、题解

给出一个类似：

```text
---
title: My Post
draft: false
views: 100
---
```

格式的字符串，实际传入的是：

```js
"---\ntitle: My Post\ndraft: false\nviews: 100\n---"
```

去掉前后`---`，按`\n`分割成每一行，再把每一行按照`:`分割成`key`和`value`形式，最终返回字典或者对象形式。

### 1.2、思路

注意value的正确数据类型。

## 二、Returns

1. `parse_frontmatter("---\ntitle: My Post\ndraft: false\nviews: 100\n---")` should return `{ title: "My Post", draft: False, views: 100 }`.
2. `parse_frontmatter("---\nid: 6a174db57256a112f932195c\ntitle: My Book\nlocale: en\nwordCount: 10000\npublished: false\n---")` should return `{ id: "6a174db57256a112f932195c", title: "My Book", locale: "en", wordCount: 10000, published: False }`.
3. `parse_frontmatter("---\nversion: 1.0.0\nurl: https://example.com\nprivate: true\n---")` should return `{ version: "1.0.0", url: "https://example.com", private: True }`.
4. `parse_frontmatter("---\nrating: 4.5\nprice: 9.99\n---")` should return `{ rating: 4.5, price: 9.99 }`.

## 三、Python Solution(s)

### 3.1、常规解法

```python
# -*- encoding: utf-8 -*- 
# @Time: 2026/6/26 10:46
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def parse_frontmatter(s):
    # 结果存储
    results = {}

    # 1. 去掉首尾，得到正确的字符串
    lines = s.split('\n')
    # 2. 去除首尾
    lines = lines[1:-1]

    # 3. 循环读取key和value
    for line in lines:
        key, value = line.split(":", 1) #按照第一个冒号分

        # 做空白处理
        value = value.strip()

        if value == "true":
            value = True
        elif value == "false":
            value = False
        else:
            # 有情况是浮点数的时候
            try:
                # 先将数字转成浮点数
                num = float(value)
                # 开始判定
                if num.is_integer():
                    value = int(value)
                else:
                    value = num
            except ValueError:
                pass

        # 将键值组成字典
        results[key] = value
    print(results)
    return results

parse_frontmatter("---\ntitle: My Post\ndraft: false\nviews: 100\n---")
```

## 四、JavaScript Solution(s)

### 4.1、常规解法

```js
function parseFrontmatter(str) {
    // 初始化结果集
    let result = {};

    // 先取出字符串中的行
    const lines = str.split("\n").slice(1, -1);
    // console.log(lines);

    // 开始循环
    for(const line of lines){
        // console.log(line);
        // 这里需要特别注意的是，需要取到第一个冒号的前后，值有可能会出现网址，那就会有两个冒号
        const firstDelimiter = line.indexOf(":", 1);

        const key = line.slice(0, firstDelimiter);
        // console.log(key);
        let value = line.slice(firstDelimiter + 1, ).trim();
        console.log(value);

        // 开始处理值的情况
        if(value === "true"){
            value = true;
        } else if(value === "false"){
            value = false;
        } else if(!Number.isNaN(Number(value))){
            // 如果 value 能够被转换成合法的数字（转换结果不是 NaN），就把它转换成 Number 类型。
            value = Number(value);
        }
        result[key] = value;
    }

    console.log(result);
    return result;
}
parseFrontmatter("---\ntitle: My Post\ndraft: false\nviews: 100\n---");
parseFrontmatter("---\nversion: 1.0.0\nurl: https://example.com\nprivate: true\n---")
```

