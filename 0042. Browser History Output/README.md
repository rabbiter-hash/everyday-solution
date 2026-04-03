# Browser History

Given an array of browser commands, return an array with two values: the history as an array of URLs, and the index of the current page.

Valid commands are:

- `"URL"` - Where URL is a web address (`"freecodecamp.org"` for example). Navigates to the given URL, adds it to the history at the next position, and discards any forward history.
- `"Back"` - moves to the previous page in history, or stays on the current page if there isn't one.
- `"Forward"` - moves to the next page in history, or stays on the current page if there isn't one.

For example, given `["freecodecamp.org", "freecodecamp.org/learn", "Back"]`, return `[["freecodecamp.org", "freecodecamp.org/learn"], 0]`.

## 一、题解和思路

### 1.1、题解

给出一个数组的参数，参数中包括`URL`、`Back`和`Forward`，根据数组中的`Back`和`Forward`返回对应的URL数组和当前所在url的索引。

本质：

### 1.2、思路

#### 1.2.1、初始化

- 创建一个空的历史列表`history`
- 当前所以`current_index`初始化为`-1`（表示未访问过任何页面）



## 二、Returns

1. `get_browser_history(["freecodecamp.org", "freecodecamp.org/learn", "Back"])` should return `[["freecodecamp.org", "freecodecamp.org/learn"], 0]`.
2. `get_browser_history(["example.com", "example.com/about", "example.com/contact", "example.com/blog"])` should return `[["example.com", "example.com/about", "example.com/contact", "example.com/blog"], 3]`.
3. `get_browser_history(["example.com", "example.com/about", "Back", "example.com/contact", "example.com/blog", "Back", "Back", "Forward"])` should return `[["example.com", "example.com/contact", "example.com/blog"], 1]`.
4. `get_browser_history(["example.com", "example.com/about", "example.com/contact", "example.com/blog", "Back", "Back", "Forward", "freecodecamp.org"])` should return `[["example.com", "example.com/about", "example.com/contact", "freecodecamp.org"], 3]`.
5. `get_browser_history(["example.com", "example.com/about", "Back", "Back"])` should return `[["example.com", "example.com/about"], 0]`.
6. `get_browser_history(["example.com", "example.com/about", "Forward"])` should return `[["example.com", "example.com/about"], 1]`.

## 三、Python Solution(s)

## 四、JavaScript Solution(s)