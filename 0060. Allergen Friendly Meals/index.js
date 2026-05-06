
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

function getAllergenFriendlyMealsIdiomatic(meals, allergens) {
    const allergensSet = new Set(allergens);

    return meals
        .filter(([meal, mealAllergens]) =>
            !mealAllergens.some(a => allerngesSet.has(a))
        )
        .map(([meal]) => meal);
}