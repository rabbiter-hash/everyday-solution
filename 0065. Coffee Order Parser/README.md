# Coffee Order Parser

Given a string for a coffee order, identify any menu items and return a formatted order.

Use the following menu items and prices:

|        Item         | Price |
| :-----------------: | :---: |
|    `"cold brew"`    | $4.50 |
|    `"oat latte"`    | $5.00 |
|   `"cappuccino"`    | $4.75 |
|    `"espresso"`     | $3.00 |
|  `"vanilla syrup"`  | $0.75 |
| `"caramel drizzle"` | $0.60 |
|   `"extra shot"`    | $0.50 |
|    `"oat milk"`     | $0.75 |
|      `"cream"`      | $0.75 |

Return a string with the matched items joined by `" + "`, followed by a colon and space (`": "`), and the total price.

For example, given `"I'd like an oat latte with vanilla syrup and an extra shot please."`, return `"oat latte + vanilla syrup + extra shot: $6.25"`

Items should appear in the order they appear in the menu and the total price should always have two decimal places.

## 一、题解和思路

### 1.1、题解

输入一个字符串，返回需要的菜品以及它们的总价格。

### 1.2、思路

- 将菜单和价格做成mapping
- 初始化结果存储列表和价格列表；
- 遍历菜单中的菜品和价格
- 如果当前菜品在输入中体现，就追加菜品到菜品列表，价格到总价列表；
- 返回

### 1.3、注意

需要注意处理只有一个菜品的时候返回的数值要保留两位小数。比如：3.00，很可能在处理过程中返回的是3.

## 二、Returns

1. `format_coffee_order("I'd like an oat latte with vanilla syrup and an extra shot please.")` should return `"oat latte + vanilla syrup + extra shot: $6.25"`.
2. `format_coffee_order("Give me a cappuccino with caramel drizzle, vanilla syrup, and some oat milk.")` should return `"cappuccino + vanilla syrup + caramel drizzle + oat milk: $6.85"`.
3. `format_coffee_order("Can I get a cold brew with some cream and an extra shot.")` should return `"cold brew + extra shot + cream: $5.75"`.
4. `format_coffee_order("Just an espresso please.")` should return `"espresso: $3.00"`.
5. `format_coffee_order("I'll take an oat latte with cream and an extra shot, and some vanilla syrup and caramel drizzle.")` should return `"oat latte + vanilla syrup + caramel drizzle + extra shot + cream: $7.60"`.

## 三、Python Solution(s)

### 3.1、常规解法

```python
# -*- encoding: utf-8 -*- 
# @Time: 2026/5/16 11:05
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def format_coffee_order(order):
    # 1. 先将输入转成小写
    order = order.lower()

    # 2. 将菜品和价格做成结构化数据（dict）
    mapping = {
        "cold brew": 4.50,
        "oat latte": 5.00,
        "cappuccino": 4.75,
        "espresso": 3.00,
        "vanilla syrup": 0.75,
        "caramel drizzle": 0.60,
        "extra shot": 0.50,
        "oat milk": 0.75,
        "cream": 0.75,
    }

    # 3. 初始化存储
    items = []
    total = 0

    # 4. 循环遍历
    for item, price in mapping.items():
        if item in order:
            items.append(item)
            total += price
    print(items)
    print(f"{total:.2f}")

    return " + ".join(items) + ": " + "$" + f"{total:.2f}"


format_coffee_order("I'd like an oat latte with vanilla syrup and an extra shot please.")

format_coffee_order("Just an espresso please.")

format_coffee_order("I'll take an oat latte with cream and an extra shot, and some vanilla syrup and caramel drizzle.")

```

## 四、JavaScript Solution(s)

### 4.1、常规解法

```js

function formatCoffeeOrder(order) {
    // 1. 转换成小写
    let orderStr = order.toLowerCase();

    console.log(orderStr);

    // 2. 将菜品和价格做成结构化数据
    const mapping = {
        "cold brew": 4.50,
        "oat latte": 5.00,
        "cappuccino": 4.75,
        "espresso": 3.00,
        "vanilla syrup": 0.75,
        "caramel drizzle": 0.60,
        "extra shot": 0.50,
        "oat milk": 0.75,
        "cream": 0.75,
    }

    // 3. 初始化存储
    let items = [];
    let total = 0;

    // 4. 循环
    for(let item in mapping){
        // 判定是否存在orderStr
        if(orderStr.includes(item)){
            // 说明存在，添加到数组
            items.push(item);

            // 将价格进行累加
            total += mapping[item];
        }
    }
    console.log(items);
    console.log(total);
    console.log(items.join(" + ") + ": " + "$" + total);
    console.log(items.join(" + ") + ": " + "$" + total.toFixed(2));
    return `${items.join(" + ")}: %$${total.toFixed(2)}`;
}

formatCoffeeOrder("I'd like an oat latte with vanilla syrup and an extra shot please.")
```