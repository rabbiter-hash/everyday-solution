# Oldest Person

Given an array of objects, each with a `"name"` and `"age"` property, return an array containing the name of the oldest person.

If multiple people share the oldest age, return all of their names in the order they appear in the input.

## 一、题解和思路

### 1.1、题解

输入一个以对象为元素的数组，包含`name`和`age`两个字段，返回年龄最大的人的name的数组，如果有多个，就应该返回多个。

### 1.2、思路

- 初始化结果数组`oldest_names`，用来存放结果
- 定义一个`max_age`比那辆，初始值设置为`-Infinity`，Python为(`float('-inf')`)，表示目前还没有最大年龄；
- 比那里数组
  - 对每个对象，检查它的`age`：
    - 如果`age > max_age`：
      - 更新`max_age = age`
      - 清空`oldest_name`，把当前名字加入
    - 如果`age == max_age`
      - 直接把当前名字加入`oldest_names`
    - 如果`age < max_age`：
      - 什么都不做
- 最终 `oldest_names` 就是年龄最大的人名数组，顺序保持原输入顺序。

## 二、Returns

1. `get_oldest([{ "name": "Brenda", "age": 40 }])` should return `["Brenda"]`.
2. `get_oldest([{ "name": "Alice", "age": 30 }, { "name": "Bob", "age": 25 }])` should return `["Alice"]`.
3. `get_oldest([{ "name": "Allison", "age": 25 }, { "name": "Bill", "age": 30 }, { "name": "Carol", "age": 30 }])` should return `["Bill", "Carol"]`.
4. `get_oldest([{ "name": "George", "age": 50 }, { "name": "Shirley", "age": 42 }, { "name": "Beth", "age": 48 }, { "name": "Holly", "age": 50 }, { "name": "Kevin", "age": 44 }, { "name": "Frank", "age": 47 }, { "name": "Zach", "age": 50 }, { "name": "Jennifer", "age": 43 }])` should return `["George", "Holly", "Zach"]`.

## 三、Python Solution(s)

### 3.1、比较法

```python
def get_oldest_person_compare(people):
    # 1. 定义一个数组，用于存储结果
    oldest_person = []

    # 2. 定义一个负无穷大的变量，用于存储最大年龄
    max_age = float('-inf')

    # 3. 循环
    for person in people:
        # 取出name和age
        name = person['name']
        age = person['age']
        # 开始比较，如果当前发现的年龄比max_age大
        if age > max_age:
            # 更新max_age
            max_age = age
            # 清空数组
            oldest_names = [name]
        elif age == max_age:
            # 如果相等，证明有另外一个人有最大年龄
            oldest_names.append(name)
        else:
            pass
    return oldest_names

print(get_oldest_person_compare([{ "name": "George", "age": 50 }, { "name": "Shirley", "age": 42 }, { "name": "Beth", "age": 48 }, { "name": "Holly", "age": 50 }, { "name": "Kevin", "age": 44 }, { "name": "Frank", "age": 47 }, { "name": "Zach", "age": 50 }, { "name": "Jennifer", "age": 43 }]))

```

### 3.1、Pythonic

```python
def get_oldest_person_pythonic(people):
    if not people:
        return []

    # 找到最大年龄
    max_age = max(person['age'] for person in people)
    return [person['name'] for person in people if person['age'] == max_age]

print(get_oldest_person_pythonic([{ "name": "George", "age": 50 }, { "name": "Shirley", "age": 42 }, { "name": "Beth", "age": 48 }, { "name": "Holly", "age": 50 }, { "name": "Kevin", "age": 44 }, { "name": "Frank", "age": 47 }, { "name": "Zach", "age": 50 }, { "name": "Jennifer", "age": 43 }]))

```

## 四、JavaScript Solution(s)

### 4.1、比较法

```js
function getOldestPersonCompare(people){
    // 1. 定义一个空数组，用于存储结果
    let oldestNames = [];

    // 2. 定义一个最大年龄的变量，用于比较
    let maxAge = -Infinity;

    // 3. 开始循环
    for(let person of people){
        let name = person["name"];
        let age = person["age"];

        // 开始比较
        if(age > maxAge){
            // 如果年纪比最大年纪大，就要更新最大年纪的值
            maxAge = age;
            // 清空数组
            oldestNames = [name];
        } else if(age === maxAge){
            // 说明有同最大年龄的人，需要更新数组
            oldestNames.push(name);
        } else {
            console.log("不符合条件！");
        }
    }
    // 4. 返回数据
    return oldestNames;
}

console.log(getOldestPersonCompare(
    [{ "name": "George", "age": 50 }, { "name": "Shirley", "age": 42 }, { "name": "Beth", "age": 48 }, { "name": "Holly", "age": 50 }, { "name": "Kevin", "age": 44 }, { "name": "Frank", "age": 47 }, { "name": "Zach", "age": 50 }, { "name": "Jennifer", "age": 43 }]
))
```

### 4.2、Idiomatic

```js
function getOldestPersonCompare(people){
    // 1. 定义一个空数组，用于存储结果
    let oldestNames = [];

    // 2. 定义一个最大年龄的变量，用于比较
    let maxAge = -Infinity;

    // 3. 开始循环
    for(let person of people){
        let name = person["name"];
        let age = person["age"];

        // 开始比较
        if(age > maxAge){
            // 如果年纪比最大年纪大，就要更新最大年纪的值
            maxAge = age;
            // 清空数组
            oldestNames = [name];
        } else if(age === maxAge){
            // 说明有同最大年龄的人，需要更新数组
            oldestNames.push(name);
        } else {
            console.log("不符合条件！");
        }
    }
    // 4. 返回数据
    return oldestNames;
}

console.log(getOldestPersonCompare(
    [{ "name": "George", "age": 50 }, { "name": "Shirley", "age": 42 }, { "name": "Beth", "age": 48 }, { "name": "Holly", "age": 50 }, { "name": "Kevin", "age": 44 }, { "name": "Frank", "age": 47 }, { "name": "Zach", "age": 50 }, { "name": "Jennifer", "age": 43 }]
))
```



