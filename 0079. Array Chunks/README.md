# Array Chunks

Given an array and a chunk size, return the array split into sub-arrays of that size.

- The last chunk may be smaller if the array doesn't divide evenly.

## 一、题解和思路

### 1.1、题解

将一个一维数组按照指定的块大小（chunk size）分割成多个子数组，最后返回一个二维数组。

### 1.2、思路

- 遍历原数组，步长为`chunk_size`
- 每次从当前位置截取`chunk_size`个元素作为一个子数组
- 将这些子数组一次添加到结果数组中

## 二、Returns

1. `chunk_array([1, 2, 3, 4, 5, 6], 3)` should return `[[1, 2, 3], [4, 5, 6]]`.
2. `chunk_array([1, "two", 3, "four", 5, "six", 7, "eight"], 2)` should return `[[1, "two"], [3, "four"], [5, "six"], [7, "eight"]]`.
3. `chunk_array([1, 2, 3, 4, 5], 3)` should return `[[1, 2, 3], [4, 5]]`.
4. `chunk_array(["a", "b", "c", "d", "e"], 1)` should return `[["a"], ["b"], ["c"], ["d"], ["e"]]`.
5. `chunk_array([1, 2, 3], 5)` should return `[[1, 2, 3]]`.

## 三、Python Solution(s)

### 3.1、常规解法

```python
def chunk_array(arr, size):
    # 1. 初始化结果集
    results = []

    # 2. 遍历
    for i in range(0, len(arr), size):
        # 左闭右开，步长为size
        results.append(arr[i:i+size])

    print(results)
    return results

chunk_array([1, 2, 3, 4, 5, 6], 3)
```

### 3.2、pythonic

```python
def chunk_array_pythonic(arr, size):
    return [arr[i:i+size] for i in range(0, len(arr), size)]
    # return list(arr[i:i+size] for i in range(0, len(arr), size))
```

## 四、JavaScript Solution(s)

### 4.1、常规解法

```js
function chunkArray(arr, size) {
    // 1. 初始化结果集
    let results = [];

    // 2. 循环遍历
    for(let i = 0; i < arr.length; i+=size){
        results.push(arr.slice(i, i+size));
    }

    console.log(results);
    return results;
}
```

### 4.2、Idiomatic

```js
function chunkArrayWhile(arr, size) {
    const result = [];
    let i = 0;
    while (i < arr.length) {
        result.push(arr.slice(i, i + size));
        i += size;
    }
    return result;
}
```

