# Sorted Array Swap

Given an array of integers, return a new array using the following rules:

1. Sort the integers in ascending order
2. Then swap all values whose index is a multiple of 3 with the value before it.

## 一、题解和思路

### 1.1、题解

输入一个整数数组，返回一个正序排列的数组，然后将索引为3的倍数的值与前面与其前面的值进行交换位置。

索引为3的倍数的索引为：0, 3, 6, 9....

### 1.2、思路

- 先使用sort对原数组进行正向排序
- 排序完后想办法将索引为3的倍数的值与它前面的值进行交换
- 要排除索引为0的情况，不然可能会出现：
  - undefined swap
  - 数组错误访问
  - 直接报错（JS/Python 都可能

## 二、Returns

1. `sort_and_swap([3, 1, 2, 4, 6, 5])` should return `[1, 2, 4, 3, 5, 6]`.
2. `sort_and_swap([9, 7, 5, 3, 1, 2, 4, 6, 8])` should return `[1, 2, 4, 3, 5, 7, 6, 8, 9]`.
3. `sort_and_swap([1, 2, 3, 4, 5, 6, 7, 8, 9])` should return `[1, 2, 4, 3, 5, 7, 6, 8, 9]`.
4. `sort_and_swap([12, 5, 8, 1, 3, 10, 2, 7, 6, 4, 9, 11])` should return `[1, 2, 4, 3, 5, 7, 6, 8, 10, 9, 11, 12]`.
5. `sort_and_swap([100, -50, 0, 75, -25, 50, -75, 25])` should return `[-75, -50, 0, -25, 25, 75, 50, 100]`.
6. `sort_and_swap([5, 9, 13, 77, 88, 313, -10, -65, 0, 8, 99, 101, -4, 2])` should return `[-65, -10, 0, -4, 2, 8, 5, 9, 77, 13, 88, 101, 99, 313]`.

## 三、Python Solution(s)

### 3.1、原地交换

```python
# -*- encoding: utf-8 -*- 
# @Time: 2026/4/15 13:43
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)


def sort_and_swap(arr):
    # 1. 先排序原数组
    sorted_arr = sorted(arr)
    # print(len(sorted_arr)) # 12
    # 2. 循环并且原地交换
    for i in range(len(arr)):
        # index： 0 - 11
        if i % 3 == 0 and i > 0:
            # 原地交换
            # 将当前索引i的值替换成替换成它前一个元素的值
            sorted_arr[i], sorted_arr[i - 1] = sorted_arr[i - 1], sorted_arr[i]
    return sorted_arr

sort_and_swap([12, 5, 8, 1, 3, 10, 2, 7, 6, 4, 9, 11])
```

## 四、JavaScript Solution(s)

### 4.1、原地交换

```js

function sortAndSwap(arr){
    // 1. 先排序数组
    const sortedArr = [...arr].sort((a, b) => a - b);

    // 2. 遍历原地交换
    for (let i = 0; i < sortedArr.length; i++){
        // console.log(i); // index: 0 - 11
        if(i % 3 === 0 && i > 0){
            // 将当前索引为i的值交换到它自己的前面
            // 注意这种交换写法，解构赋值，js最优雅的交换方法
            [sortedArr[i], sortedArr[i-1]] = [sortedArr[i-1], sortedArr[i]];
        }
    }
    console.log(sortedArr);
    return sortedArr;
}


sortAndSwap([12, 5, 8, 1, 3, 10, 2, 7, 6, 4, 9, 11]);
```

