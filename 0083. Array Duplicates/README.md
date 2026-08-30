# Array Duplicates

Given an array of integers, return an array of integers that appear more than once in the initial array, sorted in ascending order. If no values appear more than once, return an empty array.

- Only include one instance of each value in the returned array.

## 一、题解和思路

### 1.1、题解

给定一个数组，以数组形式返回该数组中重复的值，如果没有，就返回空数组；

### 1.2、思路

#### 1.2.1、暴力循环

检查每一个元素，向后扫描是否有相同的值。

时间复杂度：O(n³) - 三重循环，效率极低

#### 1.2.2、排序法

- 想对原数组进行排序
- 检查相邻两个元素是否相等

#### 1.2.3、哈希表/计数法

- 使用哈希表记录每个元素出现的次数

## 二、Returns

1. `find_duplicates([1, 2, 3, 4, 5])` should return `[]`.
2. `find_duplicates([1, 2, 3, 4, 1, 2])` should return `[1, 2]`.
3. `find_duplicates([2, 34, 0, 1, -6, 23, 5, 3, 2, 5, 67, -6, 23, 2, 43, 2, 12, 0, 2, 4, 4])` should return `[-6, 0, 2, 4, 5, 23]`.

## 三、Python Solution(s)

### 3.1、暴力枚举

```python
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
```

### 3.2、排序

```python
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
```

### 3.3、哈希表

```python
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

```

### 3.4、Pythonic

```python
def find_duplicates_pythonic(arr):
    # 初始化集合
    count = {}

    # 统计每个元素出现的次数
    for num in arr:
        count[num] = count.get(num, 0) + 1

    # 使用列表推导式找出重复元素
    return sorted([num for num, times in count.items() if times >= 2])
```

##  四、JavaScript Solution(s)

### 4.1、暴力枚举

```js
function findDuplicates(arr) {
    // 使用暴力枚舉法進行
    // 1. 初始化存儲結果
    let results = [];

    // 2. 开始循环，循环的目的是对相邻两个元素进行比较
    for(let i = 0; i < arr.length; i++){
        // 3. 内层循环出下一个元素
        for(let j = i + 1; j < arr.length; j++){
            // 判定当前循环中内外层元素是否相等
            if(arr[i] === arr[j]){
                // 检查结果数组中是否已经存在
                let alreadyExists = false;
                for(k = 0; k < results.length; k++){
                    // 如果results中有元素等于当前循环的元素，就退出循环
                    if(results[k] === arr[i]) {
                        // 说明已经存在
                        alreadyExits = true;
                        // 退出当前循环
                        break;
                    }
                }
                // 检查alreadyExists变量
                if(!alreadyExists) {
                    // 如果相等又不存在于结果数组，就加入
                    results.push(arr[i]);
                }

                // 加入还有直接退出循环
                break;
            }
        }
    }
    // 查看一下结果

    console.log(results.sort((a, b) => a - b));
    return results.sort((a, b) => a - b);
}
findDuplicates([1, 2, 3, 4, 1, 2])
```

### 4.2、排序

```js
function findDuplicatesSorted(arr) {
    // 利用排序进行相邻元素判断
    // 1. 先对原数组进行排序
    let sorted = arr.sort((a, b) => a - b);
    console.log(sorted);
    // 2. 初始化结果集
    let results = [];

    // 3. 开始循环；
    for(let i = 0; i < sorted.length; i++){
        // 比较相邻元素
        if(sorted[i] === sorted[i+1]){
            // 避免重复添加，检查是否在结果数组中
            if(results.length === 0 || results[results.length - 1] !== sorted[i]){
                results.push(arr[i]);
            }
        }
    }
    console.log(results);
    return results;
}
findDuplicatesSorted([1, 2, 3, 4, 1, 2])
```

### 4.3、哈希表

```js
function findDuplicatesHash(arr){
    // 利用哈希表记录值出现的次数
    // 1. 初始化哈希表
    let count = {};
    // 2. 初始化结果集
    let results = [];
    // 3. 第一遍遍历，计数
    for (let i = 0; i < arr.length; i++) {
        // 元素
        let num = arr[i];
        if (count[num] === undefined) {
            count[num] = 1; // 第一次出现
        } else {
            count[num]++; // 多次出现就+1
        }
    }

    // 4. 第二次遍历，找出哈希表中统计>=2的值
    for (let key in count) {
        // 打印一下元素看
        console.log(key);
        if(count[key] >= 2) {
            // 查看当前key的值的统计是否大于2，如果大于，就加入到结果集中
            console.log(typeof key);
            results.push(Number(key)); // 转为数字
        }
    }
    console.log(results);
    return results.sort((a, b) => a - b);
}

findDuplicatesHash([1, 2, 3, 4, 1, 2])
```

