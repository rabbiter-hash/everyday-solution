# Flattened

Given an array, determine if it is flat.

- An array is flat if none of its elements are arrays.

## 一、Returns

1. `is_flat([1, 2, 3, 4])` should return `True`.
2. `is_flat([1, [2, 3], 4])` should return `False`.
3. `is_flat([1, 0, False, True, "a", "b"])` should return `True`.
4. `is_flat(["a", [0], "b", True])` should return `False`.
5.  `is_flat([1, [2, [3, [4, [5]]]], 6])` should return `False`.

## 二、题解和思路

数组元素类型的本质和判断。

- 输入一定要是数组：
  - python用` isinstance `
  - Js用`Array.isArray()`
- 如果数组中`没有任何一个元素是数组`，就符合题目要求，返回`True`
- 只要有一个元素是数组，就返回`False`

## 三、Solution(s)

### 3.1、Python

#### 3.1.1、单item类型判定

判定输入数组的每项，如果有一项是数组类型的数据，就说明不是flat。

```python
def is_flat(arr):
    # 1. 判定数据输入
    if not isinstance(arr, list):
        raise ValueError("输入必须是数组！")
    
    # 2. for循环
    for item in arr:
        if isinstance(item, list):
            return False
       
   	return True
```

#### 3.1.2、利用all函数

```python
def is_flat_all(arr):
    # 1. 数据输入判定
    if not isinstance(arr, list):
        raise ValueError("输入必须是数组！")
    
    # 2. 利用all
    return all(not isinstance(item, list) for item in arr)
```

逻辑：

- 只要有一个是list
- `not isinstance(...)` 就是False
- `all()`就会返回`False`

#### 3.1.3、利用any函数，与all对偶

```python
def is_flat_with_any(arr):
    if not isinstance(arr, list):
        raise ValueError("arr must be a list")
     
    return not any(isinstance(item, list) for item in arr)

	# any的意思，只要有一个item为list，就会返回true，所以要取反。
```

### 3.2、Javascript

#### 3.2.1、循环

```js
function isFlat(arr){
    // 1.判定输入
    if(!Array.isArray(arr) || arr.length === 0){
        throw new Error("输入必须是非空数组！");
    }
    
    // 2. 循环
    for(let i=0; i<arr.length; i++){
        if(Array.isArray(arr[i])){
            return false;
        }
    }
    
    return true;
}
```

#### 3.2.2、every函数

```js
function isFlatWithEvery(arr){
    return arr.every(item => !Array.isArray(item));
}
```

#### 3.2.3、some 函数

some函数截断。

```js
function isFlatWithSome(arr){
    return !arr.some(Array.isArray);
    // 等价于
    // return !arr.some(item => Array.isArray(item));
}
```

some的截断机制是，只要数组中有一个元素是arr，就会返回true，所以要去反。

#### 3.2.4、filter函数

filter函数根据一定规则返回一个数组

```js
function isFlatWithFilter(arr){
    return arr.filter(Array.isArray).length === 0;
    // 等价于
    // return arr.filter(item => Array.isArray(item)).length === 0;
}
```

#### 3.2.5、reduce函数

利用reduce的累加机制

```js
function isFlatWithReduce(arr){
    return arr.reduce((acc, cur) => {
        return acc && !Array.isArray(cur);
    }, true);
}
```