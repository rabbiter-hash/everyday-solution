# URL Query Parser

Given a URL that contains a query string, parse the query string into an object (or dictionary) of key-value pairs.

- The query string begins after the `"?"`,
- each parameter is separated by `"&"`,
- each key/value pair is separated by `"="`

For example, given `"https://example.com/search?name=Alice&age=30"`, return:

```json
{
  "name": "Alice",
  "age": "30"
}
```

All values should be returned as strings.

## 一、题解和思路

### 1.1、题解

输入一种搜索格式的URL链接地址，将搜索的参数提取为对象（字典）格式。

### 1.2、思路

#### 1.2.1、用正则

#### 1.2.2、用字符串分割方法split

- 先用`?`分割`URL`成列表
- 再取列表的第二部分用`&`再次分割成列表
- 初始化一个结果对象result
- 循环遍历第二步的列表，分别用key代替item[0]，value代替item[1]
- 用`split`分割遍历后的每个元素，让result[key] = value

## 二、Returns

1.  `parse_url_query("https://example.com/search?name=Alice&age=30")` should return `{"name": "Alice", "age": "30"}`
2.  `parse_url_query("https://freecodecamp.org/learn?skill=programming&language=python")` should return `{"skill": "programming", "language": "python"}`
3.  `parse_url_query("https://freecodecamp.org/items?category=books&sort=asc&page=2")` should return `{"category": "books", "sort": "asc", "page": "2"}`
4.  `parse_url_query("https://example.com?redirect=freecodecamp.org/learn&when=now")` should return `{"redirect": "freecodecamp.org/learn", "when": "now"}`

## 三、Python Solution(s)

### 3.1、常规解法

```python
def parse_url_query(url):
    # 1. 初始化结果
    result = {}

    # 2. 用 ? 分割取后面部分
    query = url.split("?")[1]

    # 3. 用 & 分割参数
    params = query.split("&")

    # 4. 遍历参数
    for param in params:
        key, value = param.split("=")
        result[key] = value

    return result
```

### 3.2、Pythonic

```python
def parse_url_query_pythonic(url):
    # 1. 先取到参数
    query = url.split("?")[1]
    print(query)

    return {
        key:value
        for key, value in (
            param.split("=")
            for param in query.split("&")
        )
    }
parse_url_query_pythonic("https://example.com/search?name=Alice&age=30")
```

## 四、JavaScript Solution(s)

### 4.1、常规解法

```js

function parseUrlQuery(url) {
    // 1. 初始化结果存储
    const results = {};

    // 2. 用 ? 分割取后面部分
    const query = url.split("?")[1];
    console.log(query);
    // 3. 用 & 取参数部分
    const params = query.split("&");
    console.log(params);
    for(let param of params){
        const [key, value] = param.split("=");
        results[key] = value;
    }

    return results;
}

parseUrlQuery("https://example.com/search?name=Alice&age=30")

console.log(new URL("https://example.com/search?name=Alice&age=30"));
```

