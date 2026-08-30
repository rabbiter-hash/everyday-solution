# -*- encoding: utf-8 -*- 
# @Time: 2026/8/30 16:16
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: idx.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)


def find_duplicates(arr):
    # 暴力枚举
    # 初始化结果集
    results = []

    # 循环遍历
    for i in range(len(arr)):
        # 内层循环，检测当前元素后面是否有相等元素
        for j in range(i + 1, len(arr)):
            # 判定
            if(arr[i] == arr[j]):
                # 找到重复元素，检查是否已经在结果中
                if(arr[i] not in results):
                    results.append(arr[i])

                # 找到一次就退出内层循环
                break
    print(results)
    return sorted(results)
find_duplicates([1, 2, 3, 4, 5])

def find_duplicates_sort(arr):
    # 先排序，让相同元素挨在一起
    sorted_arr = sorted(arr)

    # 初始化结果集
    results = []

    # 遍历排序后的数组
    for i in range(len(sorted_arr) - 1):
        # 如果当前元素和下一个元素相同，说明是重复的
        if sorted_arr[i] == sorted_arr[i + 1]:
            # 避免重复添加：检查是否和结果中最后一个元素相同
            if not results or results[-1] != sorted_arr[i]:
                results.append(sorted_arr[i])
    return results
find_duplicates_sort([1, 2, 3, 4, 5])

def find_duplicates_set(arr):
    # 使用字典记录每个元素出现的次数
    count = {}
    results = []

    # 第一遍遍历：统计每个元素出现的次数
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    # 第二遍遍历：找出出现次数 >= 2 的元素
    for num, times in count.items():
        if times >= 2:
            results.append(num)

    return sorted(results)


def find_duplicates_pythonic(arr):
    # 初始化集合
    count = {}

    # 统计每个元素出现的次数
    for num in arr:
        count[num] = count.get(num, 0) + 1

    # 使用列表推导式找出重复元素
    return sorted([num for num, times in count.items() if times >= 2])