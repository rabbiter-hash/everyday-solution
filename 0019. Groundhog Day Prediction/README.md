# Groundhog Day

Today is Groundhog Day, in which a groundhog predicts the weather based on whether or not it sees its shadow.

Given a value representing the groundhog's appearance, return the correct prediction:

- If the given value is the boolean `true` (the groundhog saw its shadow), return `"Looks like we'll have six more weeks of winter."`.
- If the value is the boolean `false` (the groundhog did not see its shadow), return `"It's going to be an early spring."`.
- If the value is anything else (the groundhog did not show up), return `"No prediction this year."`.

## 一、介绍

Groundhog Day（**土拨鼠日 / 土拨鼠节**）是一个**起源于北美的民俗节日**，时间在 **每年的 2 月 2 日**，主要流行于**美国和加拿大**。

**作用：**

看土拨鼠出不出洞，来“预测”春天什么时候到。

**传统说法：**

- **如果土拨鼠看到自己的影子**（通常意味着天气晴朗）
   ➜ 它会被吓到，钻回洞里
   ➜ **冬天还要再持续 6 周**

- **如果土拨鼠没看到影子**（天气阴）
   ➜ 它会留在洞外
   ➜ **春天会提前到来**

## 二、解法和思路

### 2.1、标准

**只接受 `bool` 类型的 `True / False`**

任何别的（`None`、`1`、`0`、`""`、`"true"`、对象…）
  `"No prediction this year."`

核心判断：

> appearance是否是布尔类型的值

注意：

- 不能用`if appearance is True`
- 也不能用`if appearance`

## 三、Python Solution(s)

### 3.1、常规解法（isinstance)

```python
# -*- encoding: utf-8 -*- 
# @Time: 2026/2/3 8:39
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def groundhog_day_prediction(appearance):
    # 只需要判定输入是否是bool类型的值
    if isinstance(appearance, bool):
        return (
            "Looks like we'll have six more weeks of winter." if appearance
            else "It's going to be an early spring."
        )
    return "No prediction this year."

print(groundhog_day_prediction(''))
```

### 3.2、使用type

```python
# -*- encoding: utf-8 -*- 
# @Time: 2026/2/3 8:39
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def groundhog_day_prediction(appearance):
    # 只需要判定输入是否是bool类型的值
    if type(appearance) == bool:
        return (
            "Looks like we'll have six more weeks of winter."
            if appearance
            else "It's going to be an early spring."
        )
    return "No prediction this year."

print(groundhog_day_prediction(''))
```

### 3.3、字典映射

```python
# -*- encoding: utf-8 -*- 
# @Time: 2026/2/3 8:39
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def groundhog_day_prediction(appearance):
    # 使用字段映射
    return {
        True: "Looks like we'll have six more weeks of winter.",
        False: "It's going to be an early spring.",
    }.get(appearance, "No prediction this year.")

print(groundhog_day_prediction(''))
```

### 3.4、match-case（Python 3.10+，语义最清楚）

```python
# -*- encoding: utf-8 -*- 
# @Time: 2026/2/3 8:39
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def groundhog_day_prediction(appearance):
    # case-match，python3.10后
    match appearance:
        case True:
            return "Looks like we'll have six more weeks of winter."
        case False:
            return "It's going to be an early spring."
        case _:
            return "No prediction this year."

print(groundhog_day_prediction(''))
```

## 四、JavaScript Solution(s)

### 4.1、常规判定

```js
function groundhogDayPrediction(appearance){
    // 1. boolean判定
    if(typeof appearance === "boolean"){
        return appearance
            ? "Looks like we'll have six more weeks of winter."
            : "It's going to be an early spring.";
    }
    return "No prediction this year.";
}
```

### 4.2、map映射

```js
function groundhogDayPredictionMap(appearance) {
    const map = {
        true: "Looks like we'll have six more weeks of winter.",
        false: "It's going to be an early spring."
    };
    return typeof appearance === "boolean"
        ? map[appearance] : "No prediction this year.";
}
```

### 4.3、includes

```js
function groundhogDogPredictionIncludes(appearance){
    if(![true, false].includes(appearance)){
        return "No prediction this year.";
    }
    return appearance
        ? "Looks like we'll have six more weeks of winter."
        : "It's going to be an early spring.";
}
```

