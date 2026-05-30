# Sum of Differences

Given an array of numbers, return the sum of the differences between each number and the one that follows it.

For example, given `[1, 3, 4]`, return `3` (2 + 1).

## 一、题解和思路

### 1.1、题解

给出一个数字数组，返回相邻两个元素的差值的和；

关键在于：`differences between each number and the one that follows it.`，这里的意思是`当前元素-后一个元素（the one that follows it）`，但是经过验证，其实是`后一个元素 - 前一个元素`

结论：这里没有要求求绝对值，而是直接用后一个元素减去前一个元素。

这个题还有一个隐藏规律：

整个式子会“望远镜消去”。中间全部抵消，最后只剩：`最后一个元素 - 第一个元素`，假设有三个元素，可以写成：

```tex
(arr[2] - arr[1]) +
(arr[1] - arr[0])
# 式子展开
arr[2] - arr[1] + arr[1] - arr[0] = arr[2] - arr[0]
```

### 1.2、思路

循环遍历输入的数组，初始化加和`total`，因为要用到后一个元素，所以在循环的时候，需要将长度`-1`。

## 二、Returns

- `sum_of_differences([1, 3, 4])` should return `3`.
- `sum_of_differences([5, -3, 3, 9, 10])` should return `5`.
- `sum_of_differences([9, 6, 15, -20, 33, 14, 25, 16, -7])` should return `-16`.
- `sum_of_differences([50, 102, -46, 82, -49, 29, 71, 902, -237, 111, -61, 75])` should return `25`.

## 三、Python Solution(s)

### 3.1、循环遍历法

```python
def sum_of_differences(arr):
    # 1. 判断数据的合法性
    if not isinstance(arr, list):
        raise TypeError('arr must be a list')

    # 2. 初始化加和
    total = 0

    # 3. 循环比那里
    for i in range(len(arr) - 1):
        # 边界问题，一定要-1，不然会出现超出边界的问题
        total += arr[i + 1] - arr[i]
    print(total)
    return total

sum_of_differences([1, 3, 4])
```

### 3.2、Pythonic（望远镜消去法）

```python
def sum_of_differences_telescoping_method(arr):
    if not isinstance(arr,list):
        raise TypeError('arr must be a list')

    if len(arr) < 2:
        return 0

    return arr[-1] - arr[0]
```

## 四、JavaScript Solution(s)

### 4.1、循环遍历

```js
function sumOfDifferences(arr){
    // 1. 判定数据的合法性
    if(!Array.isArray(arr)){
        throw new Error("Arr is must an array!");
    }

    // 2. 初始化加和
    let total = 0;

    // 3. 循环比那里
    for(let i = 0; i < arr.length - 1; i++){
        console.log(i);
        total += arr[i+1] - arr[i];
    }

    console.log(total);
    return total;
}

sumOfDifferences([1, 3, 4]);
```

### 4.2、Idiomatic（望远镜消去法）

```js
function sumOfDifferencesTelescopingMethod(arr){
    if(!Array.isArray(arr)){
        throw new Error("Arr must be an array!");
    }

    if(arr.length < 2){
        return 0;
    }

    return arr[arr.length - 1] - arr[0];
}
```