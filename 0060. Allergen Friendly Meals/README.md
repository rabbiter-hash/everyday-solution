# Allergen Friendly Meals

Given an array of meals and an array of allergens to avoid, return the names of all the meals that contain none of the given allergens.

- Each meal is in the format `[meal, allergens]`, where `meal` is the name of the meal, and `allergens` is an array of the allergens the meal contains. For example, `["pasta", ["wheat", "milk"]]`.
- Allergens to avoid will be an array of strings.

Return safe meal names in the same order given. If no meal is safe, return an empty array.

## 一、题解和思路

### 1.1、题解

输入一个二维菜单数组和一个过敏原数组，其中二维菜单数组包含菜名和过敏源数组，比较输入的过敏源数组中的元素是否在菜单过敏源数组中，如果在，证明这道菜不能吃。返回能吃的。

### 1.2、思路

检查过敏源数组和菜的过敏源数组是否有交集。

## 二、Returns



## 三、Python Solution(s)

### 3.1、set交集

```python
def get_allergen_friendly_meals(meals, allergens):
    # 1. 初始化结果集
    result = []

    # 2. 将allergens转成集合
    allergens_set = set(allergens)

    # 3. 循环
    for meal, allergen_meal in meals:
        # 4. 开始比较
        if not set(allergen_meal) & allergens_set:
            # 证明没有交集，就追加到列表result
            result.append(meal)
    return result
```

### 3.2、Pythonic

```python
def get_allergen_friendly_meals_pythonic(meals, allergens):
    allergens = set(allergens)

    return [
        meal
        for meal, allergen_meal in meals
        if not any(a in allergens for a in allergen_meal)
    ]
```

## 四、JavaScript Solution(s)

### 4.1、some + set

```js

function getAllergenFriendlyMeals(meals, allergens) {
    // 1. 转成set
    const allergenSet = new Set(allergens);
    console.log(allergenSet);
    const result = [];

    for (const [meal, mealAllergens] of meals) {
        const hasBadAllergen = mealAllergens.some(a => allergenSet.has(a));
        if (!hasBadAllergen) {
            result.push(meal);
        }
    }

    return result;
}

getAllergenFriendlyMeals([
    ["steak", ["soy"]],
    ["fried rice", []],
    ["fish tacos", ["fish", "wheat"]],
    ["chicken parmesan", ["wheat", "milk"]]],
    ["soy", "fish"])

```

### 4.2、函数式写法

```js
function getAllergenFriendlyMeals(meals, allergens) {
    const allergenSet = new Set(allergens);

    return meals
        .filter(([meal, mealAllergens]) =>
            !mealAllergens.some(a => allergenSet.has(a))
        )
        .map(([meal]) => meal);
}
```

