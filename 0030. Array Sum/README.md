# Array Sum

Given an array of numbers, return the sum of all the numbers.

## 一、题解和思路

### 1.1、题解

输入一个数组，计算数组中每个元素相加的和。

### 1.2、思路

- 判定数据的合法性
  - 输入必须是数组
  - 数组中的每个元素必须是数字
- 初始化计数器
- 遍历数组元素，加到计数器

## 二、Returns

- `sum_array([1, 2, 3, 4, 5])` should return `15`.
- `sum_array([42])` should return `42`.
- `sum_array([5, -2, 7, -3])` should return `7`.
- `sum_array([203, 145, -129, 6293, 523, -919, 845, 2434])` should return `9395`.
- `sum_array([0, 0])` should return `0`.

## 三、Python Solution(s)

### 3.1、遍历数组

```python
def sum_array(numbers):
    # 1. 判定数据的合法性
    if not isinstance(numbers, list):
        raise TypeError('numbers is not a list')

    # 2. 初始化计数器
    total = 0

    # 3. 遍历数组的每个元素
    for i in numbers:
        if not isinstance(i, (int, float)):
            # 如果不是数字，就跳过当前轮
            continue
        total += i
    print(total)
    return total
sum_array([1, 2, 3, 4, 5])
```

### 3.2、sum

```python
def sum_array_pythonic(numbers):
    # 将上面版本优化成
    if not isinstance(numbers, list):
        raise TypeError('numbers is not a list')
    return sum(i for i in numbers if isinstance(i, (int, float)))
```

### 3.3、functools.reduce

```python
from functools import reduce
def sum_array_with_reduce(numbers):
    # 1. 判定数据是否合法
    if not isinstance(numbers, list):
        raise TypeError('numbers is not a list')

    # 2. 直接用reduce返回
    return reduce(lambda acc, x: acc + x if isinstance(x, (int, float)) else acc, numbers, 0)
    # ====================
        # acc: 累加器
        # x： 当前元素
        # 逻辑：
            # 如果 x 是整数或浮点数 → acc + x（累加）
            # 否则 → acc 不变（跳过非数字）
    # ====================#
```

## 四、JavaScript Solution(s)

### 4.1、遍历数组

```js
function sumArray(numbers){
    // 1. 判定数据是否合法
    if(!Array.isArray(numbers)){
        throw new Error("输入必须是数组！");
    }

    // 2. 初始化计数器
    let total = 0;

    // 3. 遍历相加
    for(let i=0; i<numbers.length; i++){
        if(typeof numbers[i] !== "number"){
            // 跳过当前循环
            continue;
        }
        total += numbers[i];
    }
    console.log(total);
    return total;
}
sumArray([1, 2, 3, 4, 5]);
```

### 4.2、let...of循环

```js
function sumArrayWithForOf(numbers) {
    // 简化上方解法
    // 1. 判定是否符合要求
    if(!Array.isArray(numbers)){
        throw new Error("输入必须是数字！");
    }

    // 2. 初始化计数器
    let total = 0;

    // 3. 用for of循环
    for(const num of numbers){
        if(typeof num === "number"){
            // console.log(num);
            total += num;
        }
    }
    console.log(total);
    return total;
}
sumArrayWithForOf([1, 2, 3, 4, 5]);
```

### 4.3、使用reduce函数

```js
function sumArrayWithReduce(numbers){
    // 1. 判定输入是否合法
    if(!Array.isArray(numbers)){
        throw new Error("输入必须是数组！");
    }

    // 2. 累加器
    return numbers.reduce((acc, cur, i, oarr) => {
        return typeof cur === "number" ? acc + cur : acc;
    }, 0)
}

console.log(sumArrayWithReduce([1, 2, 3, 4, 5, 6])); // 21
```

