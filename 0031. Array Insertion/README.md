# Array Insertion

Given an array, a value to insert into the array, and an index to insert the value at, return a new array with the value inserted at the specified index.

## 一、题解和思路

### 1.1、题解

将给出的值（value）插入到原数组（arr）的索引（index）位置。

- 暂不考虑负索引
- 暂定为正常数组

## 1.2、思路

- 遍历数组，找到索引，通过条件填充数组；不能处理`[], 0, 0`的情况。

- 切片法（最直观）
- 利用函数原地插入

## 二、Returns

- `insert_into_array([2, 4, 8, 10], 6, 2)` should return `[2, 4, 6, 8, 10]`.
- `insert_into_array(["the", "quick", "fox"], "brown", 2)` should return `["the", "quick", "brown", "fox"]`.
-  `insert_into_array([], 0, 0)` should return `[0]`.
- `insert_into_array([0, 1, 1, 2, 3, 8, 13], 5, 5)` should return `[0, 1, 1, 2, 3, 5, 8, 13]`.

## 三、Python Solution(s)

### 3.1、循环遍历

```python
def insert_into_arr_with_for(arr, value, index):
    # 1. 判定数据的合法性
    if not isinstance(arr, list):
        raise TypeError('arr should be a list')
    if not isinstance(index, int):
        raise TypeError('index should be an integer')

    # 2. 初始化记录值
    result = []

    # 3. 遍历数组
    for i, v in enumerate(arr):
        print(i, v, sep= " | ")
        if i == index:
            # 假如到了指定的索引
            result.append(value)
        # 这里不用else，因为if只做条件判定，而下方的追加，是for循环的必要流程
        result.append(v)
    return result

print(insert_into_arr_with_for([2, 4, 8, 10], 6, 2))

```

### 3.2、切片

```python
def insert_into_arr_with_slice(arr, value, index):
    # 1. 判定数据的合法性
    if not isinstance(arr, list):
        raise TypeError('arr should be a list')
    if not isinstance(index, int):
        raise TypeError('index should be an integer')
    # 2. 利用列表切片，原则：左闭右开
    return arr[:index] + [value] + arr[index:]
print(insert_into_arr_with_slice([2, 4, 8, 10], 6, 2))
```

### 3.3、利用`insert()`函数原地插入

```python
def insert_into_arr_with_insert(arr, value, index):
    # 1. 判定数据的合法性
    if not isinstance(arr, list):
        raise TypeError('arr should be a list')
    if not isinstance(index, int):
        raise TypeError('index should be an integer')

    # 2. 原地修改数组
    arr.insert(index, value)

    # 3. 赋值给new_arr
    new_arr = arr[:]

    return new_arr
    # 也可以先复制数组，用新数组去做insert()操作
print(insert_into_arr_with_insert([2, 4, 8, 10], 6, 2))
```



## 四、JavaScript Solution(s)

### 4.1、循环遍历

```js
function insertIntoArrayWithFor(arr, value, index){
    // 1. 判定数据的合法性
    if(!Array.isArray(arr)){
        throw new Error("第一个参数必须是数组！");
    }

    if(typeof index !== "number"){
        throw new Error("index必须是整数！");
    }

    // 2. 结果集
    let result = [];

    // 3. 开始遍历
    for(let i=0; i<arr.length; i++){
        // js没有enumerate，只能定义变量
        let item = arr[i];
        console.log(item);
        // 判定i是否跟index相等
        if(i === index){
            result.push(value);
        }
        // 回到正常for流程
        result.push(item);
    }
    return result;
}
console.log(insertIntoArrayWithFor([2, 4, 8, 10], 6, 2));
```

### 4.2、数组切片

```js
function insertIntoArrayWithSlice(arr, value, index){
    // 1. 判定数据的合法性
    if(!Array.isArray(arr)){
        throw new Error("第一个参数必须是数组！");
    }

    if(typeof index !== "number"){
        throw new Error("index必须是整数！");
    }

    // 2. 切片返回，js数组相加用concat
    return arr.slice(0, index).concat([value], arr.slice(index));
}
console.log(insertIntoArrayWithSlice([2, 4, 8, 10], 6, 2));
```

### 4.3、利用`splice()`函数原地插入

```js
function insertIntoArrayWithSplice(arr, value, index){
    // 1. 判定数据的合法性
    if(!Array.isArray(arr)){
        throw new Error("第一个参数必须是数组！");
    }

    if(typeof index !== "number"){
        throw new Error("index必须是整数！");
    }

    // 2. 原地修改数组
    arr.splice(index, 0, value); // 在索引为index的地方插入值为value的元素，0表示删除0个元素

    return arr.slice(); // 返回数组的副本
    // 其实也可以先复制数组，然后用新数组去splice
}
console.log(insertIntoArrayWithSplice([2, 4, 8, 10], 6, 2));
```

