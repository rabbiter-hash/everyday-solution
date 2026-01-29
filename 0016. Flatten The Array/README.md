# Flatten the Array

Given an array that contains nested arrays, return a new array with all values flattened into a single, one-dimensional array. Retain the original order of the items in the arrays.

## 一、Python Solution(s)

### 1.1、返回结果示例

1. `flatten([1, [2, 3], 4])` should return `[1, 2, 3, 4]`.
2.  `flatten([5, [4, [3, 2]], 1])` should return `[5, 4, 3, 2, 1]`.
3.  `flatten(["A", [[[["B"]]]], "C"])` should return `["A", "B", "C"]`.
4. `flatten([["L", "M", "N"], ["O", ["P", "Q", ["R", ["S", ["T", "U"]]]]], "V", ["W", ["X", ["Y", ["Z"]]]]])` should return `["L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]`.
5.  `flatten([["red", ["blue", ["green", ["yellow", ["purple"]]]]], "orange", ["pink", ["brown"]]])` should return `["red","blue","green","yellow","purple","orange","pink","brown"]`.

### 1.2、函数选取

数组函数`extend`。

`extend`的用法：

```python
a = ['ab', 'c']
print(a) # ['ab', 'c']
b = ['b', 'c']
print(a.extend(b)) # None
print(a) # ['ab', 'c', 'b', 'c']
for i in b:
    a.extend(i)
print(a) # ['ab', 'c', 'b', 'c', 'b', 'c']
```

### 1.3、解法

#### 1.3.1、栈

```python
# -*- encoding: utf-8 -*- 
# @Time: 2026/1/29 11:20
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def flatten(arr: list) -> list:
    # 1. 判断是否为数组
    if(not isinstance(arr, list)):
        raise TypeError('arr is not a list')

    # 2. 定义栈
    stack = arr.copy() # 拷贝数组，避免破坏原数组

    # 3. 结果存储
    result = []

    # 4. 开始循环迭代
    while(len(stack) > 0):
        # 说明是数组
        print("stack是数组，当前stack的值为：", stack)
        # 取出栈顶元素
        top = stack.pop()
        print("top的值为：", top)
        # 判定pop是否为数组，如果是，就压入栈stack
        if(isinstance(top, list)):
            # python没有展开运算，所以要循环或者extend
            for i in top:
                stack.append(i)
            print("压入top后的栈为：", stack)
        else:
            result.append(top)
    # 翻转数组
    return result[::-1]


print(flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
```

#### 1.3.2、栈+extend

只需要将上述压栈的代码修正一下：

```python
if(isinstance(top, list)):
    stack.extend(top)
```

#### 1.3.3、extend + 递归

```python
# -*- encoding: utf-8 -*- 
# @Time: 2026/1/29 11:20
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def flatten(arr: list) -> list:
    # 1. 结果容器
    result = []

    # 2. 遍历传入的数组
    for item in arr:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(flatten([["red", ["blue", ["green", ["yellow", ["purple"]]]]], "orange", ["pink", ["brown"]]]))
```

#### 1.3.4、生成器 yield + 递归

```python
# -*- encoding: utf-8 -*- 
# @Time: 2026/1/29 11:20
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def flatten(arr):
    # 1. 判定数据类型
    if not isinstance(arr, list):
        raise ValueError("Input must be a list")

    # 2. 遍历传入的数组
    for item in arr:
        if isinstance(item, list):
            # 如果item是数组，就让它再次调用生成器
            yield from flatten(item)
        else:
            yield item


print(list(flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9]])))
print(list(flatten([["red", ["blue", ["green", ["yellow", ["purple"]]]]], "orange", ["pink", ["brown"]]])))
```

#### 1.3.5、列表推导式

```python
# -*- encoding: utf-8 -*- 
# @Time: 2026/1/29 11:20
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def flatten(arr):
    # 1. 数据判定
    if not isinstance(arr, list):
        raise ValueError("arr is not a list")

    return [
        x
        for item in arr
        for x in (flatten(item) if isinstance(item, list) else [item])
    ]
    # 列表推导式


print(flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(flatten([["red", ["blue", ["green", ["yellow", ["purple"]]]]], "orange", ["pink", ["brown"]]]))
```

#### 1.3.6、递归 + yield + collections.abc

```python
# -*- encoding: utf-8 -*- 
# @Time: 2026/1/29 11:20
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

from collections.abc import Iterable
def flatten(arr):
    # 1. 数据判定
    if not isinstance(arr, list):
        raise ValueError("arr is not a list")

    # 2. 判定
    for item in arr:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            yield from flatten(item)
        else:
            yield item


print(flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(list(flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9]])))
print(flatten([["red", ["blue", ["green", ["yellow", ["purple"]]]]], "orange", ["pink", ["brown"]]]))
print(list(flatten([["red", ["blue", ["green", ["yellow", ["purple"]]]]], "orange", ["pink", ["brown"]]])))
```



## 二、JavaScript Solution(s)

### 2.1、返回结果示例

1.  `flatten([1, [2, 3], 4])` should return `[1, 2, 3, 4]`.
2. `flatten([5, [4, [3, 2]], 1])` should return `[5, 4, 3, 2, 1]`.
3. `flatten(["A", [[[["B"]]]], "C"])` should return `["A", "B", "C"]`.
4.  `flatten([["L", "M", "N"], ["O", ["P", "Q", ["R", ["S", ["T", "U"]]]]], "V", ["W", ["X", ["Y", ["Z"]]]]])` should return `["L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]`.

### 2.2、函数选取

- reduce：reduce可以扁平化数组，但是只能扁平二维数组，多维的就扁平不了；
- flat(depth)：ES2019+，depth指定层数，`Infinity`表示无限。

### 2.3、解法

#### 2.3.1、reduce递归

```js
function flatten(arr){
    // reduce只能扁平化二维，要扁平多维，需用到递归
    if(!Array.isArray(arr)) {
        throw new TypeError("请输入数组！");
    }
    return arr.reduce((acc, cur) =>
        acc.concat(Array.isArray(cur) ? flatten(cur) : cur), []);
}
console.log(flatten(["A", [[[["B"]]]], "C"])); // [ 'A', 'B', 'C' ]
console.log(flatten([["L", "M", "N"], ["O", ["P", "Q", ["R", ["S", ["T", "U"]]]]], "V", ["W", ["X", ["Y", ["Z"]]]]]));
// [
//   'L', 'M', 'N', 'O',
//   'P', 'Q', 'R', 'S',
//   'T', 'U', 'V', 'W',
//   'X', 'Y', 'Z'
// ]

console.log(flatten([["red", ["blue", ["green", ["yellow", ["purple"]]]]], "orange", ["pink", ["brown"]]]));
// [
//   'red',    'blue',
//   'green',  'yellow',
//   'purple', 'orange',
//   'pink',   'brown'
// ]
```

#### 2.3.2、flat(depth)

将`depth`的值设为`Infinity`，保证无限维数组进行扁平化。

```js
function flatten(arr){
    if(!Array.isArray(arr)) {
        throw new TypeError("请输入数组！");
    }
    // flat(Infinity)
    return arr.flat(Infinity);
}
console.log(flatten(["A", [[[["B"]]]], "C"])); // [ 'A', 'B', 'C' ]
console.log(flatten([["L", "M", "N"], ["O", ["P", "Q", ["R", ["S", ["T", "U"]]]]], "V", ["W", ["X", ["Y", ["Z"]]]]]));
// [
//   'L', 'M', 'N', 'O',
//   'P', 'Q', 'R', 'S',
//   'T', 'U', 'V', 'W',
//   'X', 'Y', 'Z'
// ]

console.log(flatten([["red", ["blue", ["green", ["yellow", ["purple"]]]]], "orange", ["pink", ["brown"]]]));
// [
//   'red',    'blue',
//   'green',  'yellow',
//   'purple', 'orange',
//   'pink',   'brown'
// ]
```

#### 2.2.3、使用栈/迭代（非递归）

```js
function flatten(arr){
    // 使用栈、迭代，
    // 优点：非递归，不会爆栈，适合超深嵌套。
    // 缺点：代码稍长，需要反转。
	if(!Array.isArray(arr)) {
        throw new TypeError("请输入数组！");
    }
    // 1. 定义栈，把初始数组展开，拷贝进栈（避免修改原数组）
    const stack = [...arr];
    // 定义结果数组
    const result = [];
    console.log("初始栈：", stack);

    // 2. 开始迭代循环，直到栈为空
    while(stack.length) {
        // 从栈顶取出一个元素（LIFO）
        const next = stack.pop();
        console.log("弹出栈顶元素：", next);

        if(Array.isArray(next)){
            // 如果是数组，把数组中的元素依次压入栈
            // 注意这里展开用 ...，把数组元素单独压入
            stack.push(...next);
            console.log("压入栈:", next, "当前栈:", stack);
        } else {
            // 如果不是数组，直接加入结果
            result.push(next);
            console.log("加入结果:", next, "当前结果:", result);
        }
    }
    // 栈是 LIFO（后进先出），所以结果需要翻转
    const finalResult = result.reverse();
    console.log("最终扁平化结果:", finalResult);

    return finalResult;
}
console.log(flatten(["A", [[[["B"]]]], "C"])); // [ 'A', 'B', 'C' ]
console.log(flatten([["L", "M", "N"], ["O", ["P", "Q", ["R", ["S", ["T", "U"]]]]], "V", ["W", ["X", ["Y", ["Z"]]]]]));
// [
//   'L', 'M', 'N', 'O',
//   'P', 'Q', 'R', 'S',
//   'T', 'U', 'V', 'W',
//   'X', 'Y', 'Z'
// ]

console.log(flatten([["red", ["blue", ["green", ["yellow", ["purple"]]]]], "orange", ["pink", ["brown"]]]));
// [
//   'red',    'blue',
//   'green',  'yellow',
//   'purple', 'orange',
//   'pink',   'brown'
// ]
```

