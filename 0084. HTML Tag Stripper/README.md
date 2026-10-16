# HTML Tag Stripper

Given a string of HTML code, remove the tags and return the plain text content.

- The input string will contain only valid HTML.
- HTML tags may be nested.
- Remove the tags and any attributes.

For example, `'<a href="#">Click here</a>'` should return `"Click here"`.

## 一、题解和思路

### 1.1、题解

给出一段`HTML`代码，返回纯文本内容。

### 1.2、思路

状态机（手写扫描），每一次遍历，遇到`<`进入标签模式，遇到`>`退出标签模式，其余字符累积即可。

## 二、Returns

1. `strip_tags('<a href="#">Click here</a>')` should return `"Click here"`.
2. `strip_tags('<p class="center">Hello <b>World</b>!</p>')` should return `"Hello World!"`.
3. `strip_tags('<img src="cat.jpg" alt="Cat">')` should return an empty string (`""`).
4. `strip_tags('<main id="main"><section class="section">section</section><section class="section">section</section></main>')` should return `sectionsection`.

## 三、Python Solution(s)

### 3.1、状态机——手写扫描

```python
def strip_tags(html):
    # 1. 初始化结果集，采用列表吧，比较好拼接
    result_lis = []

    # 2. 初始化状态标识
    status = False

    # 3. 开始循环并赋予状态
    for ch in html:
        if ch == '<':
            status = True
        elif ch == '>':
            status = False
        # 当not status的时候，就追加列表
        elif not status:
            result_lis.append(ch)

    print(result_lis)
    print("".join(result_lis))
    return "".join(result_lis)
strip_tags('<a href="#">Click here</a>')
```

## 四、JavaScript Solution(s)

### 4.1、状态机——手写扫描

```js
function stripTags(html){
    // 1. 初始化结果集，直接用字符串
    let results = '';

    // 2. 初始化状态
    let status = false;

    // 3. 开始循环
    for(let ch of html){
        // 判定三种状态
        // 判定是否是html开始标签
        if(ch === "<") {
            // 更改状态值
            status = true;
        } else if(ch === ">") {
            // 如果到达了结束标签，就让状态回归false
            status = false;
        } else if(!status) {
            // 取反
            results += ch;
        }
        console.log(ch, status);
    }
    console.log(results);
    return results;
}

stripTags('<a href="#">Click here</a>')


```

