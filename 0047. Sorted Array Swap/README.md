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

## 三、Python Solution(s)

## 四、JavaScript Solution(s)

