# -*- encoding: utf-8 -*- 
# @Time: 2026/5/6 17:37
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

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

def get_allergen_friendly_meals_pythonic(meals, allergens):
    allergens = set(allergens)

    return [
        meal
        for meal, allergen_meal in meals
        if not any(a in allergens for a in allergen_meal)
    ]